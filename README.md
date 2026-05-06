# make-the-receipts

A 30-minute DIY guide to building your own iMessage / WhatsApp **receipts site** with Claude Code (or Ollama, no Anthropic key required), plus a starter kit with the prompt and 4 design-reference images.

**Live:** [make-the-receipts.vercel.app](https://make-the-receipts.vercel.app)
**Kit:** [the-receipts-kit.zip](https://make-the-receipts.vercel.app/the-receipts-kit.zip) (1.5 MB)

Inspired by [Austin Lau's wedding receipts](https://x.com/helloitsaustin/status/2051792721871004002).

## What's in the kit

```
the-receipts-kit/
├── README.md       — how to use the kit
├── prompt.md       — the prompt to paste into Claude Code
└── reference/
    ├── 01-receipts.png
    ├── 02-shape.png
    ├── 03-clock.png
    └── 04-vocabulary.png
```

The reference images are screenshots of Austin's cards (cropped, all PNG metadata stripped). Claude Code reads them to match the aesthetic on the first try.

## How users get there

1. Click **Download kit**, unzip
2. Drop their `chat.db` (iMessage) or WhatsApp `.zip` into the unzipped folder
3. `claude` (or `aider --model ollama_chat/qwen2.5-coder:14b` for the local-model path)
4. Paste `prompt.md`
5. Open the generated `receipts.html`

## Open-source / no Anthropic key

The guide also walks through doing the whole thing with [Ollama](https://ollama.com) + [Aider](https://aider.chat) or [opencode](https://opencode.ai), using `qwen2.5-coder:14b` or `deepseek-coder-v2:16b`. Slower than Claude, fully offline.

## Prefer drag-drop, no terminal?

See the companion: **[chat-receipts](https://github.com/smadikanti/chat-receipts)** ([live](https://chat-receipts.vercel.app)) — same 5 cards, parsed entirely in the browser with sql.js + JSZip.

## Local dev

```bash
git clone https://github.com/smadikanti/make-the-receipts
cd make-the-receipts
python3 -m http.server 8000
# open http://localhost:8000
```

## Rebuilding the kit zip

If you edit `kit/`, regenerate the zip with:

```bash
cd kit-staging  # or any clean copy
rm -rf scripts .DS_Store
cd .. && zip -r the-receipts-kit.zip the-receipts-kit
```

The `kit/scripts/clean.py` script is what I used to crop screenshots and strip PNG metadata before publishing the references — kept in the repo for transparency.

## License

MIT — do whatever, no warranty, but keep the credit line if you can.
