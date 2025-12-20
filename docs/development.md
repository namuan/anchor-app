# Development Guide

This guide is for developers who want to contribute to the Anchor App or build it from source.

## Environment Setup

### Prerequisites
- Python 3.3+ (Recommended: Python 3.6 or 3.7)
- `pip` package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/namuan/anchor-app.git
   cd anchor-app
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally without packaging:

```bash
python -m anchor.application
# OR
export PYTHONPATH=$PYTHONPATH:.
python anchor/application.py
```

## Project Structure

- `anchor/`: Main application package.
  - `core/`: Core business logic (Git, Jira interactors).
  - `external/`: External service connectors (Jira APIs).
  - `ui/`: User Interface components (PyQt5).
    - `generated/`: UI code generated from `.ui` files.
    - `presenters/`: MVP pattern presenters.
    - `widgets/`: Custom widgets.
  - `model/`: Data models.
- `resources/`: Raw resource files (UI definitions, icons).
- `tests/`: Unit and integration tests.
- `packaging/`: Resources for packaging the app.

## Development Workflow

### UI Development
The UI is built using Qt Designer. The `.ui` files are located in `resources/ui/`.

To compile `.ui` files to Python code:
```bash
# See HowTo.md for the script
for i in `ls resources/ui/*.ui`; do FNAME=`basename $i ".ui"`; pyuic5 $i > "anchor/ui/generated/$FNAME.py"; done
```

To compile resources (`.qrc`):
```bash
pyrcc5 -compress 9 -o anchor/resources_rc.py anchor/resources.qrc
```

### Testing

Run the test suite using `pytest`:

```bash
pytest
```

## Building and Packaging

The project uses `py2app` (macOS) and `py2exe` (Windows) for packaging.

### macOS
```bash
python setup.py py2app
```

### Windows
```bash
python setup.py py2exe
```

See `HowTo.md` for Docker-based build instructions using PyInstaller.
