# Forgeflow

Forgeflow is a Codex plugin that helps choose and run a safe engineering workflow:

- **Brainstorming** for a new or undecided product idea.
- **Grill with docs** for a focused change in an existing codebase.
- **Wayfinder** for a large, multi-session initiative with unresolved decisions.

It requires explicit approval before every transition to another skill. Forgeflow recommends the next phase, then waits for a message such as `Approve next: to-spec`.

## Attribution

This repository is a bundle and orchestration layer. The following workflow skills are **not authored by this repository or its maintainer**; they originate from [Matt Pocock's skills repository](https://github.com/mattpocock/skills):

- `grill-with-docs`
- `wayfinder`
- `to-spec`
- `to-tickets`
- `implement`
- `code-review`

The bundled `brainstorming` skill originates from [obra/superpowers](https://github.com/obra/superpowers).

Forgeflow adds the router and explicit approval gates around those skills. See [NOTICE.md](NOTICE.md) and [LICENSES](LICENSES/) for the upstream attribution and licenses.

## Install on another Mac

```bash
git clone <your-forgeflow-repository-url>
cd forgeflow-plugin
codex plugin marketplace add "$PWD"
codex plugin add forgeflow@forgeflow
```

Start a new Codex task after installing, then invoke `/forgeflow`.

## Updating

Pull the latest repository changes, then reinstall:

```bash
git pull
codex plugin add forgeflow@forgeflow
```
