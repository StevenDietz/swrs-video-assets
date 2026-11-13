# SWRS Client Portal how-to videos

Eleven short videos, one portal process each, built from SWRS's own training videos (transcribed) and attached to Freshdesk ticket replies so clients learn to use swrsportal.com.

| Video | Length |
|---|---|
| login | 1:31 |
| reset-password | 2:18 |
| profile-mfa | 2:25 |
| reports | 2:55 |
| debtor-status | 2:30 |
| debtor-history | 1:23 |
| upload-files | 2:16 |
| new-placements | 2:43 |
| update-account | 1:43 |
| document-vault | 1:17 |
| direct-payment | 3:20 |

## Layout
- `videos/` final MP4s (v3, voice checked by transcribing each final video against its script)
- `src/` narration scripts and build code: `topics.py` (scripts and slide text), `tts.py`, `slides2.py`, `assemble.py`, `stt.py` (transcribe originals), `rt.py` (round-trip check)
- `img/` sanitized portal screenshots used on the slides (no real user or debtor data)
- `docs/` build kit, transcripts of the 18 original training videos, Freshdesk reply snippets

## Rules
- Scripts come from the transcripts, not the help pages.
- Portal passwords are NOT case-sensitive (the original video and help page are wrong).
- Support contact is only 866-837-3065, info@swrecovery.com, Mon-Fri 8 AM-5 PM CT.
- No API keys are stored here. The ElevenLabs key is read from a local file at build time.
