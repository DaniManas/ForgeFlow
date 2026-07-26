# Set up Forgeflow in any agent

Install Forgeflow **once per project** instead of pasting instructions into every new chat. The setup copies the portable [Forgeflow core](../core/FORGEFLOW.md) into the persistent instruction format used by your chosen agent.

## Quick setup

Clone this repository, then run one command from its root. Replace `/path/to/your-project` with the project folder you want to configure.

```bash
python3 scripts/forgeflow-init.py <agent> --project /path/to/your-project
```

On Windows, use `py` or `python` instead of `python3` if that is how Python is installed:

```powershell
py scripts/forgeflow-init.py <agent> --project C:\path\to\your-project
```

Supported agents:

| Agent | Command | File created in the target project |
| --- | --- | --- |
| Claude Code | `python3 scripts/forgeflow-init.py claude --project /path/to/project` | `.claude/rules/forgeflow.md` |
| Cursor | `python3 scripts/forgeflow-init.py cursor --project /path/to/project` | `.cursor/rules/forgeflow.mdc` |
| Windsurf / Devin Desktop | `python3 scripts/forgeflow-init.py windsurf --project /path/to/project` | `.devin/rules/forgeflow.md` |
| GitHub Copilot | `python3 scripts/forgeflow-init.py copilot --project /path/to/project` | `.github/instructions/forgeflow.instructions.md` |
| An agent that reads `AGENTS.md` | `python3 scripts/forgeflow-init.py agents --project /path/to/project` | `AGENTS.md` |

The command never overwrites an existing instruction file. If it reports that a file already exists, add Forgeflow’s instructions to that file deliberately instead of replacing your project rules.

After setup, open a **new session** in that project and say:

```text
Start Forgeflow in Balanced mode. I want to build: <your idea>
```

The agent should propose a route and wait for your approval. When it asks, reply naturally with `approve`, `go ahead`, `continue`, or a clear `yes`. Your reply approves only the stage it just named.

Forgeflow remains dormant for normal work in the project. It activates only when you explicitly start or resume Forgeflow.

## Why these files?

- **Claude Code:** project rules in `.claude/rules/` persist across sessions and can be version-controlled. Claude also supports project `CLAUDE.md` files and importing shared instruction files. [Official docs](https://code.claude.com/docs/en/memory)
- **Cursor:** project rules live in `.cursor/rules/` as `.mdc` files. [Official docs](https://docs.cursor.com/context/rules)
- **Windsurf / Devin Desktop:** `.devin/rules/` is the preferred workspace-rule location; `.windsurf/rules/` remains a fallback. [Official docs](https://docs.devin.ai/desktop/cascade/memories)
- **GitHub Copilot:** repository and path-specific instructions live under `.github/`; the initializer uses a project-wide instruction file. [Official docs](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- **AGENTS.md:** useful for agents that support the emerging shared convention. Claude Code and Copilot can also work alongside it.

## Regular chat tools

For a chat tool with no project or persistent-instruction feature, paste [FORGEFLOW.md](../core/FORGEFLOW.md) once at the beginning of a conversation. Ask it to output specs, plans, tasks, and reviews as Markdown if it cannot create files or run tests.

## Codex

Codex users can install the optional plugin from the repository root and begin with `/forgeflow`. The plugin packages the same workflow into individually discoverable skills and adds Codex-specific model suggestions.
