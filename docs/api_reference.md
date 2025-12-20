# API Reference

This document provides an overview of the key modules and classes in the Anchor App codebase.

## Core Module (`anchor.core`)

The core module contains the business logic for interacting with external systems like Git and managing the application flow.

### `git_interactor.py`
Functions for interacting with Git repositories.

- `git_info(working_dir)`: Returns the current branch name and the number of changed files.
- `is_git_dir(working_dir)`: Checks if a directory is a valid Git repository.
- `create_feature_branch(working_dir, source_branch, new_branch)`:
  - Stashes current changes.
  - Checks out the source branch.
  - Creates and switches to the new feature branch.
- `apply_stash(working_dir)`: Pops the latest stash.

### `jira_interactor.py`
#### `class JiraInteractor`
A facade for interacting with Jira asynchronously using the worker pool.

- `check_connectivity(**kwargs)`: Verifies Jira connection settings.
- `fetch_ticket_details(**kwargs)`: Retrieves details for a specific ticket.
- `fetch_all_tickets(**kwargs)`: Retrieves all tickets matching the configured query.
- `update_transition(**kwargs)`: Updates the status of a Jira ticket.

### `worker_pool.py`
Manages a thread pool for executing long-running tasks (like network requests) without freezing the UI.

## External Module (`anchor.external`)

Handles direct communication with external APIs.

### `jira_connector.py`
#### `class JiraConnector(QRunnable)`
A `QRunnable` worker that executes Jira API calls in a separate thread. It emits signals (`result`, `error`) upon completion.

### `jira_apis.py`
Contains the actual HTTP request logic for Jira REST API endpoints.

## UI Module (`anchor.ui`)

The UI is built using PyQt5 and follows a Model-View-Presenter (MVP) pattern.

### Presenters (`anchor.ui.presenters`)
Presenters handle the logic behind the views, mediating between the UI and the Core/Model layers.

- `MainPresenter`: Manages the main window logic.
- `TicketsListPresenter`: Manages the list of tickets.
- `TicketContentPresenter`: Manages the display of ticket details.
- `ConfigPresenter`: Handles configuration dialog logic.
- `FeatureBranchPresenter`: Handles the feature branch creation workflow.

### Dialogs
- `ConfigurationDialog`: Settings for Jira and general app preferences.
- `FeatureBranchDialog`: Input form for creating a new branch.
