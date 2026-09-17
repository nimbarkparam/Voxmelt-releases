# Put your audio here

Drop 16-bit WAV files in this folder, one per clip, and write what was actually
said into `../transcripts/<same-base-name>.ref.txt`.

```
benchmark/clips/01_clean.wav
benchmark/transcripts/01_clean.ref.txt
```

Any sample rate and channel count works - the runners downmix to mono and
resample to 16 kHz, exactly as our own run did.

**Our five source clips are not published.** They are recordings of the founder's
voice, so the audio stays private while the method does not. The reference
transcripts in `../transcripts/` are published, so you can see precisely how hard
the material was: clean speech, code and identifiers, fast natural speech with
filler, domain jargon, and speech over background noise.

For a neutral public corpus, LibriSpeech `test-clean` works with the same
commands and needs no changes to any runner.
