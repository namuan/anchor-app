# Anchor App

**Improving development workflow by integrating Jira and Git.**

Anchor App is a desktop productivity tool designed to streamline your daily development tasks. It brings your Jira tickets and Git workflow together in a simple, unified interface, allowing you to manage tasks and context switch efficiently.

## Key Features

- **Jira Integration**:
  - View and manage your Jira tickets directly from the desktop.
  - Quick access to ticket details, comments, and status.
  - Update ticket transitions (e.g., move to "In Progress" or "Done") without opening the browser.
- **Git Integration**:
  - View the status of your local repositories (current branch, changed files).
  - **Automated Feature Branching**: Create a new Git branch based on a Jira ticket with a single click. The app automatically stashes your changes, switches to the source branch, and creates the new feature branch for you.
- **Productivity**:
  - Clean, focused UI to reduce distractions.
  - Offline support (cached data).
  - Cross-platform support (macOS, Windows, Linux).

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- [**User Guide**](docs/user_guide.md): How to configure and use the application.
- [**Development Guide**](docs/development.md): How to set up the development environment, run tests, and build the app.
- [**API Reference**](docs/api_reference.md): Overview of the code structure and key modules.

## Quick Start

### Prerequisites
- Python 3.3+
- Git installed and available in your PATH.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/namuan/anchor-app.git
   cd anchor-app
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the application:
   ```bash
   uv run anchor-app
   ```

## Development

To run the tests:

```bash
uv sync
uv run pytest
```

For more details on contributing and building the application, please refer to the [Development Guide](docs/development.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
