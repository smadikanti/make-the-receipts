# Prompt for Claude Code (or any LLM CLI)

Paste everything below the `---` line into Claude Code, opened in this folder.

---

Read the chat file in this folder (`chat.db` for iMessage, or unzip the WhatsApp `.zip` and read `_chat.txt`).

For iMessage: list all chats with at least 50 messages, sorted by message count, and ask me which one to use. For WhatsApp: just use the conversation in the export.

Then build a single self-contained HTML file called `receipts.html` with **5 swipeable cards**.

## Cards

1. **The receipts** — hero stats: total messages, days, photos, videos, emojis, "I love you" count, and a sender split bar.
2. **The shape of us** — bar chart of messages per week (or per month if dataset is short), with the peak bar highlighted in orange.
3. **Around the clock** — 7 weekdays × 24 hours heatmap, shaded by volume, with the peak bucket called out.
4. **The vocabulary** — "I love you" count + top 9 emojis grid.
5. **The arc** — first message, peak day, peak month, longest unbroken streak.

## Aesthetic

Match the reference images in this folder exactly: `reference/01-receipts.png`, `reference/02-shape.png`, `reference/03-clock.png`, `reference/04-vocabulary.png`.

- Cream paper background (`#F1E9D2`)
- Sage green double scalloped border around each card
- Handwritten cursive titles (`'Snell Roundhand'`, `'Apple Chancery'`, `'Brush Script MT'`, cursive)
- Small-caps uppercase eyebrows ("BY THE NUMBERS", "MESSAGES PER WEEK")
- Monospace numbers
- Orange accent (`#D58A4A`) for the peak bar / peak callouts
- Dark page background outside the card
- Heart icon in the bottom-right of each card
- Cards swipeable with arrow keys, click zones, and touch

## Constraints

- **Single HTML file.** All data inlined as a JS object. No external CDN. No build step. No telemetry. Works offline.
- Add a `<meta http-equiv="Content-Security-Policy" content="... connect-src 'none' ...">` so the file cannot make network requests after generation.
- **"I love you" detection** — regex covering: `i love you`, `i love u`, `love you`, `love u`, `ily`, `ilu`. Add Telugu (`premistunna`, `premistunnanu`) or Hindi (`pyaar karta hoon`, `pyaar karti hoon`) variants if the chat looks like that language.
- **Emoji counting** — handle skin-tone modifiers (`U+1F3FB`–`U+1F3FF`) and ZWJ sequences correctly so 👨‍👩‍👧‍👦 counts as one emoji, not four.
- **iMessage `attributedBody`** — on iOS 16+ many messages have `text` as `NULL` and the real body in `attributedBody` (binary plist). Decode the `NSString` payload from those blobs.
- **Date math** — use UTC for the day-streak comparison so DST changes don't break the streak.

## Optional bonus card

If the dataset spans multiple months, add a 6th card called **"The vibe of each month"** — one-sentence summaries of the dominant mood per month. Keep them under 14 words each.

## Output

Just the file `receipts.html`. Don't write a separate `stats.json` — inline everything.
