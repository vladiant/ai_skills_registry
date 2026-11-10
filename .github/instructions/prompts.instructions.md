---
applyTo: "prompts/*.md"
---

# Prompt rules

Files in `prompts/` are generated. Do not edit them by hand.

- Change the skill of the same name in `.github/skills/`, then run
  `python3 .github/scripts/sync_prompts.py` and commit both files.
- To publish another skill as a prompt, add it to `PROMPTS` in
  `.github/scripts/sync_prompts.py`, run the script, and list the prompt in
  the README.
- CI fails when a prompt differs from what the script would generate.
