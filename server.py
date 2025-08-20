from fastmcp import FastMCP, TextContent

# Create server instance
mcp = FastMCP("resume-server")

# Define a simple tool
@mcp.tool()
def read_resume(name: str) -> TextContent:
    """Reads and returns resume text for a given name."""
    return TextContent(f"Here is the resume content for {name} (to be replaced with actual parsing).")

# Run server
if __name__ == "__main__":
    mcp.run()
