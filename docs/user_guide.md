# User Guide

## Overview
Anchor App is a desktop application designed to streamline your development workflow by integrating Jira and Git. This guide will help you configure and use the application effectively.

## Getting Started

### Initial Configuration
When you first launch Anchor App, you need to configure your Jira server and preferences.

1. **Open Configuration**: Click the "Configure" button (gear icon) in the toolbar.
2. **Jira Settings**:
   - Enter your Jira Server URL.
   - Provide your credentials (username and password/API token).
   - Test the connection to ensure it works.

### Managing Jira Tickets

#### Viewing Tickets
- The main dashboard displays a list of your Jira tickets.
- Click the "Refresh" button to fetch the latest updates from Jira.
- Select a ticket from the list to view its details in the right pane.

#### Ticket Actions
- **View Details**: See the description, comments, and status of the selected ticket.
- **Update Status**: Change the workflow state of a ticket (e.g., from "In Progress" to "Done") using the available transition buttons.

### Git Integration

Anchor App helps you manage your local Git repositories in the context of your Jira tickets.

#### Feature Branch Workflow
You can create a new feature branch directly from a Jira ticket.

1. **Select a Ticket**: Choose the Jira ticket you are working on.
2. **Create Branch**: Click the "Create Feature Branch" button (or similar action).
3. **Configure Branch**:
   - Select the repository directory.
   - Choose the source branch (e.g., `master` or `develop`).
   - The new branch name is often automatically suggested based on the ticket ID and title.
4. **Execution**:
   - The app will stash any current changes in your working directory.
   - It will checkout the source branch.
   - It will create and switch to the new feature branch.
   - It will attempt to apply the stashed changes (pop stash).

#### Git Statistics
- The app provides a quick view of your current repository status, including the active branch and the number of changed files.

## Troubleshooting

- **Connection Issues**: Ensure your Jira server is accessible and your credentials are correct. If using 2FA or SSO, you might need an API token instead of a password.
- **Git Errors**: Make sure the selected directory is a valid Git repository. If the "Create Feature Branch" fails, check if you have uncommitted changes that might conflict even after stashing.
