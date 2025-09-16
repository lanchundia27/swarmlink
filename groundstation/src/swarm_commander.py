"""
Authors: Luis Anchundia
Main app for swarm commanding
Not fully implemented yet
"""

import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QGridLayout, QScrollArea, QWidget
from PySide6.QtCore import Qt

from SwarmGUI import swarmcommandergui, ui_form, drone_ui_form
project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)

from protocol import constants as const
from protocol import packet_definitions as proto


if __name__ == "__main__":
    swarmcommandergui.run_gui()

