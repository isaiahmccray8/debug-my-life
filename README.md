# debug-my-life

A tiny MCP server for the Claude Builders Club workshop. It gives Claude one
tool, `debug_my_life`, which treats a life problem like a software bug.

## 1. Install what you need (Mac)

You need three things: git, uv and Claude Code. Run each command in the
Terminal app.

**git** (already on most Macs). Check with:

```bash
git --version
```

**uv** (installs Python and the MCP SDK for you):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Claude Code:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Now **close the terminal and open a new window**, then check both installed:

```bash
uv --version
claude --version
```

### If you see `command not found: uv` or `command not found: claude`

The install worked, but your terminal does not know where to look yet. Run
this once, then try again:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

On Windows, see the install pages for [uv](https://docs.astral.sh/uv/) and
[Claude Code](https://code.claude.com/docs/en/install.md).

## 2. Get the code

```bash
cd ~/Desktop
git clone https://github.com/isaiahmccray8/debug-my-life.git
cd debug-my-life
uv sync
```

## 3. Connect the server to Claude Code

```bash
claude mcp add debug-my-life -- uv run server.py
claude mcp list
```

`claude mcp list` should show `debug-my-life` as connected.

## 4. Start Claude Code

Stay inside the `debug-my-life` folder and run:

```bash
claude
```

The first time, it opens your browser so you can sign in with your Claude
account.

## 5. Try these

Type each one into Claude Code. Claude will ask permission before it uses the
tool. Say yes.

```
/mcp
```

Shows the servers Claude Code is connected to. You should see `debug-my-life`.

```
What tools do you have from the debug-my-life server?
```

Claude describes the tool using the description written in `server.py`.

```
Use debug_my_life: I keep procrastinating on my homework
```

```
Use debug_my_life: my group project partner never answers the group chat
```

```
Debug my life. I have a presentation today and I'm nervous.
```

This last one does not name the tool. Watch whether Claude decides to use it
on its own, based only on the tool's description.

Type `/exit` to leave Claude Code.

## How it works

Open `server.py`. Three lines do the work:

- `@mcp.tool()` turns a normal Python function into a tool Claude can call.
- The docstring is the description Claude reads to decide when to use the tool.
- `mcp.run()` starts the server and waits for Claude to talk to it.

## Make it yours

1. Add your own line to the `FIXES` list in `server.py`.
2. Type `/exit`, then run `claude` again.
3. Ask again a few times and watch for your line.

Then try adding a second function with `@mcp.tool()` above it.

## Stuck?

- `command not found: uv` or `claude`: see the fix in step 1.
- `git clone` asks for a username and password: check the link is spelled
  right. A public repo never asks you to log in.
- `destination path 'debug-my-life' already exists`: a folder with that name is
  already on your Desktop. Delete it or clone somewhere else.
- Run `claude mcp list`. Does the server show as connected?
- Are you inside the `debug-my-life` folder?
- Did you exit and reopen Claude Code after changing `server.py`?
- `No module named 'mcp.server.fastmcp'` means you are following an older
  tutorial. This repo uses version 2 of the MCP SDK, where `FastMCP` is now
  `MCPServer`.
