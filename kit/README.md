# the receipts — starter kit

Drop your chat file in this folder, open Claude Code (or any LLM CLI), and paste the prompt below.

## What's in here

- `README.md` — this file
- `prompt.md` — the prompt to paste into Claude Code
- `reference/` — design reference images from [Austin Lau's wedding receipts](https://x.com/helloitsaustin/status/2051792721871004002). The model uses these to match the aesthetic.

## How to use

1. Put your chat file in this folder:
   - **iMessage:** `cp ~/Library/Messages/chat.db ./chat.db` (Mac, with Full Disk Access enabled for Terminal)
   - **WhatsApp:** drop the exported `.zip` here
2. Open Claude Code in this folder:
   ```bash
   claude
   ```
3. Paste the contents of `prompt.md`.
4. Wait 1–2 minutes. You'll get a single `receipts.html`.
5. Open it:
   ```bash
   open receipts.html      # macOS
   start receipts.html     # Windows
   xdg-open receipts.html  # Linux
   ```

## Open-source path (no Anthropic key)

Same idea with a local model:
```bash
ollama pull qwen2.5-coder:14b
pip install aider-chat
aider --model ollama_chat/qwen2.5-coder:14b
```
Then paste `prompt.md`.

## Privacy

Everything runs on your machine. Claude Code only sends what you type plus the code it writes — not your raw chat. The Ollama path is fully offline.
