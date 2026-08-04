# SWRS Video Factory — Production Standards (v2)

Canonical build recipe for every episode. Established after EP-001–005; **EP-006 onward
must follow this spec**, and earlier episodes are retrofitted opportunistically.
Conforms to PRODUCTION_HANDOFF.md v1.0 and brand/BRAND.md.

## Episode structure (~23s nominal, flexible)

| Slot | Duration | Content |
|---|---|---|
| Scene 1 | hook line + 0.75s | Unexpected hook + relatable frustration (hook VO at t=0.3s) |
| Scene 2 | second line + 0.5s | Escalation or "SWRS simplifies" beat |
| Scene 3 | closer + tail | SWRS simplifies + clear CTA (closer may carry onto the card) |
| Brand card | 3.5s | Navy end card: tagline + CTA + **logo reveal** |

- **Client rule (2026-08-04): episodes CAN run over 23 seconds.** The 23s figure is a
  nominal target, not a cap — when the script needs room, extend the timeline rather
  than compressing reads or slow-motioning scenes past ~0.7x. Max length 30s; the AV-SYNC
  rule (cuts land when their lines end) always holds; hook lands inside the first 3 seconds.
- Scene clips: request kling durations that roughly match the retimed scene length
  (5/8/10s) so retiming stays near 1.0x.
- **VO durations must be measured (ffprobe) before assembly** — lines that collide get
  re-recorded shorter, never sped up. (EP-004 lesson: first takes ran 7s/17s and collided.)

## Generation pipeline

1. **Keyframes** — `nano_banana_pro`, 16:9, one per scene, with each character's locked
   `canonical_reference` job_id passed as `medias` role `image`. Never generate a recurring
   character without their reference.
2. **Animation** — `kling3_0_turbo` image-to-video, `start_image` = keyframe job_id,
   durations 5/5/8.
3. **Voiceover** — `seed_audio`, preset voice **Arthur** (`30fc8796-ceb6-4a66-b3a7-4a145ef7f346`).
   Email is always written as `info at S-W Recovery dot com` in TTS text ("take 1" standard).
4. **Assembly** — ffmpeg in the Higgsfield sandbox (see recipe below).

## Assembly recipe (sandbox)

Sandbox is ephemeral (~10s after a call returns): **downloads → render → verify → PUT
uploads must run in ONE sandbox_exec call** (background:true is unreliable; use a single
foreground call, `timeout_seconds` 115, parallel `curl ... &` + `wait`, presets
veryfast/ultrafast).

- **Typography: Fira Sans Bold** (brand standard) — fetch at build time:
  `curl -fsSL https://github.com/google/fonts/raw/main/ofl/firasans/FiraSans-Bold.ttf -o FiraSans-Bold.ttf`
  Use for all captions and brand-card text. (DejaVuSans was the pre-v2 stand-in.)
- Canvas 1280x720 @30fps master; brand card generated with lavfi color=0x070731.
- Captions: `drawtext` textfiles, `box=1:boxcolor=0x070731@0.6:boxborderw=16`, fontsize 38,
  hook captions lower-third (y=560), narration captions top (y=70). Caption every VO line.
- **Logo (client rule): only in the last scene.** White logo media
  `38707f0b-0ba6-407b-90c4-c8800ab7b661` as `-loop 1` input (NEVER without -loop 1 — a
  still input's lone frame fades to transparent), scale 520px, alpha fade-in st=18.2 d=0.8,
  top-center y=80 with soft shadow (lutrgb black + boxblur 12, offset +3/+3).
- **Audio — DUCKING mix**: scene SFX (concat of clip audio) at 1.0x, ducked to 0.22x during
  each measured VO window (+0.25s tail); VO 1.25x (hooks 1.3x); `amix normalize=0`.
- **SFX kit (v2)** — synthesized in-sandbox with sox, license-free, mixed at low level:
  - `whoosh.wav` (0.6s, filtered noise fade) → scene transitions at t=5.0 and t=10.0
  - `pop.wav` (0.12s sine tick) → checkmark/success beat in scene 3
  - **The logo reveal is SILENT** — a synthesized chime was tried on EP-006 and cut per
    client feedback ("weird bell... sounds off"). No SFX on or after the brand card.
  ```
  sox -n -r 48000 -c 2 whoosh.wav synth 0.6 whitenoise fade h 0 0.6 0.45 lowpass 2400 gain -4
  sox -n -r 48000 -c 2 pop.wav synth 0.12 sine 620 fade h 0.005 0.12 0.09 gain -3
  ```
- **Loudness (v2)**: final audio chain ends `alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=11`
  (−14 LUFS social/YouTube target) so every episode plays at the same perceived level.
- Formats: master 16:9 1280x720 → 1:1 1080x1080 and 9:16 1080x1920 (navy pad).
  (Native vertical framing is deferred to the finishing pass.)

## Revision cuts get FRESH media ids (hard rule, 2026-08-04)

**NEVER overwrite delivered media in place.** The delivery CDN (d2ol7oe51mr4n9.cloudfront.net)
caches a served object at the edge for many hours (observed: 9+ hours, `x-cache: Hit`,
query strings ignored, no invalidation available, media_confirm does not flush it). Re-PUTting
to the same presigned slot updates the origin but viewers keep getting the old cut — this
silently swallowed a full day of revisions on 2026-08-04. Every revision cut is uploaded to
NEW media ids; the episode package and the client's links are updated to the new URLs.

## Real on-screen assets (client rule, 2026-08-04)

**EVERY visible computer, laptop, or monitor screen in EVERY scene must display the REAL
SWRS Client Portal — never an AI-invented interface, and never a generic icon/animation as
the screen's content.** (Client rule strengthened 2026-08-04: "this overlay of the real
portal needs to be on any computer screen throughout the campaign." Originally the rule
covered only screens depicting the portal.) Floating holographic icons — envelopes,
checkmarks, notification banners — hovering ABOVE or BESIDE a device are fine; the screen
itself shows the portal. Standard method (proven on EP-003 scene 1): pass the portal
screenshot as an additional `medias` role `image` reference on the keyframe generation
alongside the character references, prompting "the laptop screen displays EXACTLY the
client portal dashboard from the reference image, reproduced faithfully."

- Canonical portal set-piece: media `089434d8-d720-468d-a82c-a246f3c2e5e5`
  (live screenshot of https://www.swrsportal.com/ — SWRS wordmark, "Secure access to
  real-time recovery reporting.", Client Portal Login card, News & Updates row).
- Re-capture in the sandbox (`npx playwright screenshot`) if the live site's design changes.
- The same applies to any other real SWRS property shown on screen (swrecovery.com, email
  templates): screenshot the real thing, reference it, never invent it.

## Verification (every build, before upload)

- `ffprobe` duration == the planned total (scene durations + 3.5s card), exactly.
- **Logo placement check**: extract frames, count near-white pixels (RGB all >225) in the
  crop (300,50)–(980,210): t=17s must be LOW (scene, no logo), t=20s HIGH (card + logo).
  Never ship a cut without this check (EP-003 lesson: a transparent logo rendered "successfully").
- All three PUT uploads return HTTP 200 → then `media_confirm`.

## Deliverables per episode

- `episode_package.json` — system of record: barrier, engine mapping, all job_ids/media_ids,
  VO lines + placements, scene table, superseded-cut history.
- Final MP4s: 16:9 (email/YouTube), 1:1 (LinkedIn), 9:16 (Reels/TikTok) at 1080p.
- **Email thumbnails (v2 standard)**: hook frame + centered play button
  (navy 175-alpha circle, white ring + triangle), 1200x675 and 600x338 JPG, recorded
  under `email_assets` in the package.
- Commit + push to the repo after every episode.

## Deferred to the post-sign-off finishing pass (all 12 episodes at once)

1. Native 9:16 / 1:1 scene renders (or AI reframe) instead of padding.
2. Licensed music bed — one brand track reused across the series.
3. Premium render tier + 4K master archive (upscale_video).
4. Optional custom cloned brand narrator voice.

## Standing rules

- The frustration always belongs to the situation, never to SWRS. Never sarcastic; clients
  never look foolish.
- Recurring characters only from `characters/character_manifest.json` with locked references.
- CTA everywhere: **Email your placements to info@swrecovery.com.**
