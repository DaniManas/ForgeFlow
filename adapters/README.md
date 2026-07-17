# Use Forgeflow without Codex

Forgeflow’s core workflow is a Markdown instruction file, so teammates do not need Codex or a particular model.

## Any coding agent

1. Copy [core/FORGEFLOW.md](../core/FORGEFLOW.md) into the project instruction file your tool reads.
2. If your tool has no project instruction file, paste the whole file into a new chat before starting work.
3. Tell the agent:

   ```text
   Start Forgeflow in Balanced mode. I want to build: <your idea>
   ```

4. Review the suggested route. Continue only by sending the approval phrase the agent asks for.

Common project instruction file names include `AGENTS.md`, `CLAUDE.md`, and tool-specific rule files. The filename is less important than ensuring your chosen agent receives the contents of `FORGEFLOW.md` as instructions.

## Regular chat tools

Paste [core/FORGEFLOW.md](../core/FORGEFLOW.md) first. Then describe the project or feature. The workflow remains the same, although the agent may not be able to create files or run tests itself; ask it to produce the spec, plan, tasks, and review as Markdown for you to save.

## Codex

Codex users can install the optional plugin from the repository root and begin with `/forgeflow`. The plugin packages the same workflow into individually discoverable skills and adds Codex-specific model suggestions.
