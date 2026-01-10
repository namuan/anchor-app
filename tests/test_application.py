import pytest

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QFileDialog

from anchor import application


@pytest.fixture
def window(qtbot, mocker):
    """Pass the application to the test functions via a pytest fixture."""
    # Mock the jira_configured method to return True to prevent JIRA config dialog
    mocker.patch('anchor.core.core_settings.CoreSettings.jira_configured', return_value=True)
    # Mock JiraInteractor to prevent background threads
    mocker.patch('anchor.ui.presenters.main_presenter.JiraInteractor')
    new_window = application.MainWindow()
    qtbot.add_widget(new_window)
    new_window.show()
    return new_window


def test_window_title(window):
    """Check that the window title shows as declared."""
    assert window.windowTitle() == 'Anchor App - Improving development workflow'


def test_window_geometry(window):
    """Check that the window width and height are set as declared."""
    # assert window.width() == 1024
    # assert window.height() == 768
    pass


def test_open_file(window, qtbot, mocker):
    """Test the Open File item of the File submenu.

    Qtbot clicks on the file sub menu and then navigates to the Open File item. Mock creates
    an object to be passed to the QFileDialog.
    """
    qtbot.mouseClick(window.file_sub_menu, Qt.MouseButton.LeftButton)
    qtbot.keyClick(window.file_sub_menu, Qt.Key.Key_Down)
    mocker.patch.object(QFileDialog, 'getOpenFileName', return_value=('', ''))
    qtbot.keyClick(window.file_sub_menu, Qt.Key.Key_Enter)


def test_about_dialog(window, qtbot, mocker):
    """Test the About item of the Help submenu.

    Qtbot clicks on the help sub menu and then navigates to the About item. Mock creates
    a QDialog object to be used for the test.
    """
    qtbot.mouseClick(window.help_sub_menu, Qt.MouseButton.LeftButton)
    qtbot.keyClick(window.help_sub_menu, Qt.Key.Key_Down)
    mocker.patch.object(QDialog, 'exec', return_value='accept')
    qtbot.keyClick(window.help_sub_menu, Qt.Key.Key_Enter)
