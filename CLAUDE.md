@AGENTS.md

# Claude Code notes

Everything above is imported from [AGENTS.md](AGENTS.md), which is the single instruction file for
every agent working in this repo. Do not copy its content here — edit `AGENTS.md` instead.

Claude-specific only:

- **This repository holds two skills, `collect-materials` and `normalise-materials`,** under
  `skills/`, packaged as the `study-library` plugin (`.claude-plugin/plugin.json`). The three
  teaching skills live in the knowledge base next door, as the `study-kb` plugin.
- **The three agents in `.claude/agents/`** (`course-chapter-writer`, `paper-summary-writer`,
  `pdf-to-markdown`) are project agents. Run them from this checkout. They are not plugin
  components.
- An installed plugin does not load this file or `AGENTS.md`. A rule a skill depends on must be
  written in the skill.
