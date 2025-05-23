# Claudetopia

**claudepak/** - Claude configuration manager
```bash
cd claudepak
chmod +x claudepak
./claudepak export myconfig     # Export current Claude config
./claudepak import config.json  # Import a config
./claudepak backup             # Backup current config
./claudepak list               # List available configs
```

**decision-simulator/** - AI decision simulation tool that generates personas you can chat with
```bash
cd decision-simulator
poetry env use 3.11             # Set Python environment
poetry install                  # Install dependencies
poetry run decision-simulator   # Run the simulator
```