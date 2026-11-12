# debug-my-life

A tiny MCP server for the Claude Builders Club workshop. It gives Claude one
tool, `debug_my_life`, which treats a life problem like a software bug.

## What you need

- [Claude Code](https://claude.com/claude-code)
- [uv](https://docs.astral.sh/uv/) (installs Python and the MCP SDK for you)
- git

## Run it

```bash
git clone https://github.com/YOUR-USERNAME/debug-my-life.git
cd debug-my-life
uv sync
claude mcp add debug-my-life -- uv run server.py
claude mcp list
```

`claude mcp list` should show `debug-my-life` as connected. Then start Claude
Code from this folder:

```bash
claude
```

and ask:

```
Use debug_my_life: I keep procrastinating on my homework
```

## How it works

Open `server.py`. Three lines do the work:

- `@mcp.tool()` turns a normal Python function into a tool Claude can call.
- The docstring is the description Claude reads to decide when to use the tool.
- `mcp.run()` starts the server and waits for Claude to talk to it.

## Make it yours

1. Add your own line to the `FIXES` list in `server.py`.
2. Quit and reopen Claude Code.
3. Ask again and watch for your line.

Then try adding a second function with `@mcp.tool()` above it.

## Stuck?

- Run `claude mcp list`. Does the server show as connected?
- Are you inside the `debug-my-life` folder?
- Did you quit and reopen Claude Code after changing `server.py`?
- `No module named 'mcp.server.fastmcp'` means you are following an older
  tutorial. This repo uses version 2 of the MCP SDK, where `FastMCP` is now
  `MCPServer`.
