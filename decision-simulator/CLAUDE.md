# Project-Specific Instructions for decision-simulator

## Code Style
- DO NOT use async/await in this project
- Keep everything synchronous for simplicity

## Dependency Management
Always use Poetry for dependency management in this project. DO NOT use pip install directly.

### Examples:
- To add a dependency: `poetry add package-name`
- To add a specific version: `poetry add package-name@^1.2.3`
- To add a dev dependency: `poetry add --group dev package-name`
- To update dependencies: `poetry update`
- To install all dependencies: `poetry install`

### Common dependencies for this project:
```bash
# Add production dependencies
poetry add fast-agent
poetry add click
poetry add openai

# Add development dependencies
poetry add --group dev pytest
poetry add --group dev black
poetry add --group dev ruff
```

## Project Structure
- Use src layout: `src/decision_simulator/`
- All persona-related code goes in `src/decision_simulator/personas/`
- Database models in `src/decision_simulator/models/`
- CLI commands in `src/decision_simulator/cli/`

## Environment Variables
- OpenAI API key should be set as `OPENAI_API_KEY`
- Use python-dotenv for local development

## Testing
- Write tests for all persona creation and interaction logic
- Use pytest for testing
- Maintain test coverage above 80%