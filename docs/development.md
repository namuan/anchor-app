# Development Guide

This guide is for developers who want to contribute to the Anchor App or build it from source.

## Environment Setup

### Prerequisites
- Python 3.12+
- `uv` package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/namuan/anchor-app.git
   cd anchor-app
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

## Running the Application

To run the application locally without packaging:

```bash
uv run anchor-app
# OR
uv run python anchor/application.py
```

## Project Structure

- `anchor/`: Main application package.
  - `core/`: Core business logic (Git, Jira interactors).
  - `external/`: External service connectors (Jira APIs).
  - `ui/`: User Interface components (PyQt6).
    - `generated/`: UI code generated from `.ui` files.
    - `presenters/`: MVP pattern presenters.
    - `widgets/`: Custom widgets.
  - `model/`: Data models.
- `resources/`: Raw resource files (UI definitions, icons).
- `tests/`: Unit and integration tests.

## Development Workflow

### UI Development
The UI is built using Qt Designer. The `.ui` files are located in `resources/ui/`.

To compile `.ui` files to Python code:
```bash
# See Makefile for the script
for i in `ls resources/ui/*.ui`; do FNAME=`basename $i ".ui"`; uv run pyuic6 $i > "anchor/ui/generated/$FNAME.py"; done
```

### Testing

Run the test suite using `pytest`:

```bash
uv run pytest
```

## Building and Packaging

The project uses `PyInstaller` for packaging.

### Build

```bash
uv run pyinstaller main.spec --clean
```
