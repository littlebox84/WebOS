# WebOS — Browser Operating System

WebOS is a single‑file, installable Progressive Web App that delivers a desktop‑like environment inside your browser. It includes a Start menu, dock, window manager, a virtual file system, and a suite of built‑in apps (Browser, Text Editor, Terminal, Media Player, Image Viewer, Settings, Task Command). An AI Assistant app is also included for chat and safe system automations.

## Features
- Desktop UI with Start menu, dock, notifications, and clock
- Window manager: move, resize, minimize, maximize, z‑index focus
- Virtual File System persisted to localStorage
- Built‑in apps:
  - Web Navigator (browser)
  - Text Studio (text editor)
  - Terminal (toy shell)
  - Media Player and Image Viewer
  - Task Command (tasks)
  - Settings (appearance, desktop, storage, and more)
  - AI Assistant (OpenAI‑compatible chat + slash commands)
- PWA: manifest, service worker, installable, offline caching
- Dynamic particle wallpaper with themes and effects

## Quick Start (Local)
1. Clone/download this repository.
2. Start a static web server in the project directory (required for service workers/PWA):
   - Python 3
     ```bash
     python3 -m http.server 8000
     ```
   - Or any static server of your choice.
3. Open the app:
   - http://127.0.0.1:8000/webos-enhanced.html
4. Hard refresh (Ctrl/Cmd+Shift+R) after changes.

## Deploy
- Netlify: This repository includes `netlify.toml` to redirect all routes to `webos-enhanced.html` and a minimal build step.
- Any static host works. Ensure the following files are served at the site root:
  - `webos-enhanced.html`
  - `manifest.json`
  - `sw.js`

## PWA
- Static manifest: `manifest.json` (linked in `<head>` of `webos-enhanced.html`).
- Service worker: `sw.js` caches core assets and serves when offline.
- Install: Most browsers show an install prompt or a menu option to “Install App”.

## AI Assistant
The `AI Assistant` app supports OpenAI‑compatible endpoints.

- Configure in the app (Click “Connection”):
  - Base URL: e.g. `https://api.openai.com/v1` (or another compatible endpoint)
  - Model: e.g. `gpt-4o-mini`
  - API Key: Your provider key
- Settings are saved to localStorage under `webos.ai.settings.v1`.

### Slash Commands
- `/help` — List commands
- `/open <appId>` — Open an app (e.g., `browser`, `text-editor`, `terminal`, `tasks`, `settings`)
- `/openurl <url>` — Open a URL in the Browser app
- `/search <term>` — Search the virtual file system
- `/read <path>` — Read a text file (output limited to ~16 KB)
- `/write <path> <text>` — Write to a file (restricted to `/Documents` or `/Downloads`, with confirmation)
- `/append <path> <text>` — Append to a file (same restrictions)

Safety:
- Writes require an explicit confirmation modal.
- Writes are limited to `/Documents` and `/Downloads`.
- Non‑text file reads are blocked.

## Development
- Single‑file source: `webos-enhanced.html` contains HTML, CSS, and JavaScript.
- Other project files:
  - `manifest.json`: PWA metadata
  - `sw.js`: Service worker
  - `netlify.toml`: Netlify config (redirects and headers)
  - `info.prd`: Product requirements document (PRD)
- Tips
  - Use DevTools > Application > Service Workers to unregister a stale SW after major changes.
  - LocalStorage keys used:
    - `webos.fs.v1`, `webos.settings.v1`, `webos.terminal.history.v1`, `webos.media.playlist.v1`, `webos.tasks.v1`, `webos.ai.settings.v1`

## Project Structure
```
.
├─ webos-enhanced.html   # Main app (single-file WebOS)
├─ manifest.json         # PWA manifest (linked statically)
├─ sw.js                 # Service worker for offline caching
├─ netlify.toml          # Netlify redirects + headers
├─ info.prd              # PRD (requirements & current scope notes)
└─ README.md             # This file
```

## Known Limitations
- The PRD describes an expansive set of features; the current build implements a focused subset.
- Multi‑user, App Store, full multi‑desktop, and advanced DevTools are not yet implemented.

## License
Copyright © 2025. All rights reserved.
