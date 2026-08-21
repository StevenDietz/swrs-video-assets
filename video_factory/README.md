# SWRS Video Factory

A repeatable system for producing short, character-driven onboarding/activation videos
that reduce the **placement gap** — the ~30% of signed clients who don't place their first
accounts within 60 days.

**Core promise:** *Getting your accounts to SWRS is easier than you think.*

## What's here

| Path | What it is |
|---|---|
| `characters/character_manifest.json` | **System of record** for the SWRS Character Universe — ~50 characters across 9 groups, each with role, personality, catchphrase, props, and continuity rules. Every episode reads from this. |
| `episodes/` | Per-episode packages (storyboard + scene prompts + generated assets). *(added as episodes are produced)* |

## The Character Universe → content engine

The universe isn't decoration; it's a production engine. Episodes are assembled from a
fixed formula:

```
Obstacle (the problem)  ->  Persona (who feels it)  ->  Hero / AI Guide (the easy fix)  ->  Success character (payoff + CTA)
```

- **Comic Obstacles** (Invoice Monster, Password Goblin, Late Fee Dragon…) = episode premises
- **Client Personas / Industry Specialists** (Frank, Harvey, Patty, Healthcare Hannah…) = audience segments
- **Heroes & AI Guides** (Victor, Penny, Max, Clarity AI…) = recurring leads that deliver the fix
- **Success Characters** (Cash Flow Hero, Victory Bell, Happy Customer…) = the closing payoff

Example matrix (obstacle × persona → episode):

| Obstacle | Persona | Episode |
|---|---|---|
| Password Goblin | any procrastinator (Victor) | **The Login Curse** — place by email, skip the portal |
| Invoice Monster | Frank the Franchise Owner | Aging receivables grow teeth after 90 days |
| Coffee Cup Carl | Patty the Property Manager | Stop putting it off — one upload |
| Late Fee Dragon | Harvey HVAC | Waiting costs you money |

## Continuity — the one hard rule

Characters are **assets**. To ship a consistent series, each character is locked to **one
canonical reference image** (`canonical_reference` in the manifest) and every future frame
is generated against it. Never change hair, eye color, body type, or signature clothing;
always use the SWRS cool-blue palette (navy `#070B97`, blue `#0446F1`, sky `#0495F1`).

## How it connects to the rest of the system

Finished episodes feed the **client activation drip** (behavior-triggered email sequence
that auto-stops the moment a client records their first placement). See the connection
blueprint in the `SWRS_Video_Factory_Connections` kit: Claude (storyboards/prompts) →
generation (image/voice/video) → review/approval → asset registry → Nutshell CRM trigger →
activation email → analytics.
