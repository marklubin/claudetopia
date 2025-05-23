# claudepak

A command-line tool for managing Claude Code configurations. Export, import, and share Claude configurations including MCP servers, custom commands, and settings.

## Features

- 📦 **Export** complete Claude configurations as portable packages
- 📥 **Import** configurations from packages 
- 🔄 **Backup** current configuration before changes
- 📋 **List** available configuration packages
- 🛡️ **Safe** - automatically backs up existing configs before import

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/claudepak.git
cd claudepak

# Make executable
chmod +x claudepak

# Add to PATH (optional)
ln -s $(pwd)/claudepak /usr/local/bin/claudepak
```

## Usage

### Export Configuration
```bash
# Export your current Claude setup
./claudepak export myconfig

# Creates: myconfig.json
```

### Import Configuration  
```bash
# Import someone else's configuration
./claudepak import someconfig.json

# Automatically backs up your existing config first
```

### Backup Current Config
```bash
# Create timestamped backup
./claudepak backup

# Creates: backup-20250522-143045.json
```

### List Available Configs
```bash
# Show all .json config files in current directory
./claudepak list
```

## What Gets Exported

Each configuration package includes:

- **`.claude.json`** - Claude Code configuration (behavior, MCP servers, etc.)
- **`claude_desktop_config.json`** - Claude Desktop MCP server configurations
- **`commands/`** - Custom slash commands for Claude Code
- **`metadata.json`** - Package information and export details
- **`README.md`** - Installation instructions

## Package Format

Packages are compressed tar.gz files containing:

```
claude-config-myconfig/
├── claude.json                    # Claude Code config
├── claude_desktop_config.json     # Claude Desktop MCP servers  
├── commands/                      # Custom slash commands
│   ├── plan.md
│   ├── research.md
│   └── ...
├── metadata.json                  # Package metadata
└── README.md                      # Installation guide
```

## Safety Features

- 🔒 **Automatic backups** - Existing configs are backed up before import
- ✅ **Validation** - Checks package format before import
- 📊 **Metadata** - Tracks when/where/how packages were created
- 🔍 **Verification** - Shows package contents before import

## Examples

```bash
# Share your optimized AI research setup
./claudepak export ai-research-setup

# Import a team configuration  
./claudepak import team-standard.json

# Create backup before experimenting
./claudepak backup
./claudepak import experimental-config.json

# List all available configs
./claudepak list
```

## Requirements

- macOS or Linux
- Claude Code installed
- `jq` for JSON processing (optional, for prettier output)
- `tar` and `gzip` (standard on most systems)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Version History

- **v1.0.0** - Initial release with export/import functionality
