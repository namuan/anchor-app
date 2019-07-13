import logging

from anchor.core.core_settings import app_settings
from anchor.core.jira_interactor import JiraInteractor
from anchor.core.worker_pool import pool


class MainPresenter:
    def __init__(self, view):
        self.view = view
        self.jira_interactor = JiraInteractor()
        self.initial_load = True
        app_settings.init()
        app_settings.init_logger()
        app_settings.init_app_data()
        if app_settings.geometry():
            self.view.restoreGeometry(app_settings.geometry())
        if app_settings.window_state():
            self.view.restoreState(app_settings.window_state())

    def after_load(self):
        if not self.initial_load:
            return

        self.initial_load = False
        if not app_settings.jira_configured():
            self.view.show_jira_configuration_dialog()
        else:
            self.refresh_all_tickets()

        self.check_updates()

    def check_updates(self):
        if app_settings.load_updates_configuration():
            self.view.updater.check()

    def refresh_all_tickets(self):
        args = {
            "exclude_status": "Done",
            "on_success": self.on_all_tickets_loaded,
            "on_failure": self.on_all_tickets_failed
        }
        self.view.show_progress_dialog("Refreshing all tickets")
        self.jira_interactor.fetch_all_tickets(**args)

    def on_all_tickets_loaded(self, result):
        logging.info("All tickets loaded...Showing in List view")
        self.view.hide_progress_dialog()
        tickets = result.get('tickets')
        app_settings.app_data.add_visible_tickets(tickets)

    def on_all_tickets_failed(self, result):
        logging.error("Error fetching All tickets")
        logging.error(result)
        self.view.hide_progress_dialog()

    def save_settings(self):
        logging.info("Saving settings for Main Window")
        app_settings.save_window_state(
            geometry=self.view.saveGeometry(),
            window_state=self.view.saveState()
        )

    def shutdown(self):
        pool.shutdown()
        self.save_settings()
