#!/usr/bin/env python3
"""
VoxMelt benchmark scorer — computes WER + CER for transcription outputs
against a ground-truth reference, with no external dependencies.

USAGE
-----
    python3 wer.py transcripts/

NAMING CONVENTION (in the transcripts/ folder)
----------------------------------------------
    NN_name.ref.txt            <- ground truth (what you actually said)
    NN_name.voxmelt-large.txt  <- an engine's output for the same clip
    NN_name.cloud-whisper.txt  <- another engine's output
    NN_name.otter.txt          <- etc.

The part after the LAST dot before .txt is the engine label. Every non-"ref"
file is scored against the matching NN_name.ref.txt. Output: a per-clip table
per engine, an averages summary, and results.csv.

WHAT IT DOES TO BE FAIR
-----------------------
Both reference and hypothesis go through the SAME normalization:
  - lowercased
  - punctuation stripped
  - whitespace collapsed
  - spoken numbers folded to digits ("three" -> "3", "first" -> "1")
so that "I have three" vs "I have 3" is not counted as an error. Applied
equally to every engine, so no engine is advantaged.
"""

import sys, os, csv, re
from collections import defaultdict

# ---- spoken-number folding (mirrors the app's dedup number map) ----
_NUMBER_WORDS = {
    "zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6",
    "seven":"7","eight":"8","nine":"9","ten":"10","eleven":"11","twelve":"12",
    "thirteen":"13","fourteen":"14","fifteen":"15","sixteen":"16","seventeen":"17",
    "eighteen":"18","nineteen":"19","twenty":"20","thirty":"30","forty":"40",
    "fifty":"50","sixty":"60","seventy":"70","eighty":"80","ninety":"90",
    "hundred":"100","thousand":"1000","million":"1000000","billion":"1000000000",
    "first":"1","second":"2","third":"3","fourth":"4","fifth":"5","sixth":"6",
    "seventh":"7","eighth":"8","ninth":"9","tenth":"10",
}

def normalize_words(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)          # strip punctuation
    text = re.sub(r"_", " ", text)
    toks = text.split()
    return [_NUMBER_WORDS.get(t, t) for t in toks]

def normalize_chars(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def edit_distance(a, b):
    """Levenshtein distance between two sequences -> (dist, S, D, I)."""
    n, m = len(a), len(b)
    if n == 0: return m, 0, 0, m
    if m == 0: return n, 0, n, 0
    prev = list(range(m + 1))
    # backtrace not needed for totals; count ops via a second pass DP
    # Use full matrix for op counts (sets here are small: sentences).
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i
    for j in range(m+1): dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    # backtrace for S/D/I
    i, j, S, D, I = n, m, 0, 0, 0
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + (0 if a[i-1]==b[j-1] else 1):
            if a[i-1] != b[j-1]: S += 1
            i, j = i-1, j-1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            D += 1; i -= 1
        else:
            I += 1; j -= 1
    return dp[n][m], S, D, I

def score(ref_text, hyp_text):
    r = normalize_words(ref_text); h = normalize_words(hyp_text)
    dist, S, D, I = edit_distance(r, h)
    wer = dist / len(r) if r else 0.0
    rc = list(normalize_chars(ref_text)); hc = list(normalize_chars(hyp_text))
    cdist, *_ = edit_distance(rc, hc)
    cer = cdist / len(rc) if rc else 0.0
    return {"wer": wer, "cer": cer, "ref_words": len(r), "S": S, "D": D, "I": I}

def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else "transcripts"
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}"); sys.exit(1)

    refs, hyps = {}, defaultdict(dict)   # refs[clip]=path ; hyps[engine][clip]=path
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith(".txt"): continue
        stem = fn[:-4]
        if stem.endswith(".ref"):
            refs[stem[:-4]] = os.path.join(folder, fn)
        else:
            if "." in stem:
                clip, engine = stem.rsplit(".", 1)
                hyps[engine][clip] = os.path.join(folder, fn)

    if not refs:
        print("No *.ref.txt reference files found. See BENCHMARK_PLAN.md §2."); sys.exit(1)

    def read(p):
        with open(p, encoding="utf-8") as f: return f.read()

    rows = []
    engines = sorted(hyps.keys())
    print(f"\nReferences: {len(refs)} clip(s) | Engines: {', '.join(engines) or '(none yet)'}\n")

    for engine in engines:
        results = []
        for clip in sorted(refs):
            if clip in hyps[engine]:
                s = score(read(refs[clip]), read(hyps[engine][clip]))
                results.append((clip, s))
                rows.append({"engine": engine, "clip": clip,
                             "wer_pct": round(s["wer"]*100, 2), "cer_pct": round(s["cer"]*100, 2),
                             "ref_words": s["ref_words"], "sub": s["S"], "del": s["D"], "ins": s["I"]})
        if not results: continue
        print(f"### {engine}\n")
        print("| Clip | WER | CER | Ref words | Sub | Del | Ins |")
        print("|---|---|---|---|---|---|---|")
        for clip, s in results:
            print(f"| {clip} | {s['wer']*100:.1f}% | {s['cer']*100:.1f}% | {s['ref_words']} | {s['S']} | {s['D']} | {s['I']} |")
        # micro-average (weighted by ref words) — the honest aggregate
        tw = sum(s["ref_words"] for _, s in results)
        werr = sum(s["wer"]*s["ref_words"] for _, s in results) / tw if tw else 0
        cerr = sum(s["cer"]*s["ref_words"] for _, s in results) / tw if tw else 0
        print(f"| **Overall (word-weighted)** | **{werr*100:.1f}%** | **{cerr*100:.1f}%** | **{tw}** | | | |\n")

    if rows:
        out = os.path.join(folder, "..", "results.csv")
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        print(f"Wrote {os.path.normpath(out)}")
    else:
        print("No engine output files found yet. Add NN_name.<engine>.txt files and re-run.")

if __name__ == "__main__":
    main()
