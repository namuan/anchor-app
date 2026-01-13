import tempfile
from pathlib import Path
from unittest import TestCase

from PyQt6.QtCore import QSettings


class TestJQLConfiguration(TestCase):
    """Test JQL configuration save and load functionality."""

    def setUp(self):
        """Create a temporary settings file for testing."""
        self.temp_dir = tempfile.mkdtemp()
        self.settings_file = Path(self.temp_dir) / "test_settings.ini"
        self.settings = QSettings(str(self.settings_file), QSettings.Format.IniFormat)

    def test_save_and_load_jql(self):
        """Test that JQL can be saved and loaded from settings."""
        # Test data
        test_jql = 'project = TEST AND status = "In Progress"'
        
        # Save JQL to settings
        self.settings.setValue('jql', test_jql)
        self.settings.sync()
        
        # Load JQL from settings
        loaded_jql = self.settings.value('jql', '')
        
        # Assert
        self.assertEqual(test_jql, loaded_jql)

    def test_load_jql_with_default(self):
        """Test that default JQL is returned when no value is set."""
        default_jql = 'project = FRN AND status IN (New, Ready, "In Progress") AND type IN (Story, Bug)'
        
        # Load JQL from settings (should return default)
        loaded_jql = self.settings.value('jql', default_jql)
        
        # Assert
        self.assertEqual(default_jql, loaded_jql)

    def test_save_complete_configuration(self):
        """Test saving all configuration values including JQL."""
        # Test data
        test_server = 'https://jira.example.com'
        test_username = 'testuser'
        test_password = 'testpass'
        test_jql = 'project = MYPROJECT'
        
        # Save configuration
        self.settings.setValue('server', test_server)
        self.settings.setValue('username', test_username)
        self.settings.setValue('password', test_password)
        self.settings.setValue('jql', test_jql)
        self.settings.sync()
        
        # Load configuration
        loaded_server = self.settings.value('server', '')
        loaded_username = self.settings.value('username', '')
        loaded_password = self.settings.value('password', '')
        loaded_jql = self.settings.value('jql', '')
        
        # Assert
        self.assertEqual(test_server, loaded_server)
        self.assertEqual(test_username, loaded_username)
        self.assertEqual(test_password, loaded_password)
        self.assertEqual(test_jql, loaded_jql)
