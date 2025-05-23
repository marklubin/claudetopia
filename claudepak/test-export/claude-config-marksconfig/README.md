# Claude Configuration Package: marksconfig

Exported on: May 22, 2025
System: Darwin (macOS)

## Overview

This is Mark's collaborative AI prototyping configuration that transforms Claude Code into a step-by-step copilot for AI experimentation and development.

## Features

- **Collaborative Workflows** - Claude asks permission at each step
- **Custom Slash Commands** - /plan, /research, /implement, etc.
- **AI Prototyping Focus** - Optimized for rapid experimentation
- **MCP Servers** - Brave Search, Spotify, CalDAV, Luma API integration
- **Python/Poetry Support** - Virtual environments and modern Python practices
- **VS Code Integration** - Seamless editor integration

## Installation

```bash
# Import this configuration using claudepak
claudepak import marksconfig.json

# Or manually:
cp claude.json ~/.claude.json
cp claude_desktop_config.json ~/Library/Application\ Support/Claude/
mkdir -p ~/.claude && cp -r commands ~/.claude/
```

## Package Contents

- `claude.json` - Claude Code configuration with collaborative workflows
- `claude_desktop_config.json` - Claude Desktop MCP server configurations  
- `commands/` - Custom slash commands (/plan, /research, etc.)
- `metadata.json` - Package information and features

## Custom Slash Commands

Type `/` in Claude Code to access:

- `/plan [task]` - Create step-by-step plans with approval
- `/research [topic]` - Guided research workflows
- `/implement [feature]` - Step-by-step implementation 
- `/review [code]` - Collaborative code review
- `/options [problem]` - Present multiple approaches
- `/verify [approach]` - Validate before proceeding

## MCP Servers Included

- **Brave Search** - Web research capabilities
- **Spotify** - Music and audio processing 
- **CalDAV** - Calendar integration
- **Luma API** - Video generation
- **Filesystem** - File operations
- **Memory** - Persistent context

## Notes

- **Restart Required** - Restart Claude Code and Claude Desktop after importing
- **API Keys** - Update any API keys specific to your environment
- **File Paths** - Adjust file paths in MCP server configurations as needed
- **Collaborative Mode** - Claude will ask permission before taking actions

## Usage

This configuration emphasizes collaborative development:

1. Claude always asks before taking actions
2. Presents options and waits for your choice
3. Works step-by-step with verification at each stage
4. Focuses on AI prototyping and experimentation workflows

Perfect for rapid AI experimentation while maintaining control over the development process.
