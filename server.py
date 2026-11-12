import random
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("debug-my-life")

FIXES = [
    "Have you tried turning it off and on again?",
    "Root cause: not enough sleep. Patch: go to bed.",
    "Works on my machine. Ship it.",
]

@mcp.tool()
def debug_my_life(problem: str) -> str:
    """Diagnose a life problem as if it were a software bug."""
    return f"Bug report: {problem}\nSuggested fix: {random.choice(FIXES)}"

if __name__ == "__main__":
    mcp.run()
