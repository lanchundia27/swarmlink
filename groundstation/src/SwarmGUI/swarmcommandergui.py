# This Python file uses the following encoding: utf-8
"""
Author: Luis Anchundia
GUI for swarm commander    
"""

# Important:
# You need to run the following command to generate the ui_form.py file whenver you edit the .ui in Qt designer
#     pyside6-uic form.ui -o ui_form.py


import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QGridLayout, QScrollArea, QWidget, QLabel, QMessageBox, QPushButton, QDialog
from PySide6.QtCore import Qt

from .ui_form import Ui_SwarmCommanderGUI
from .drone_ui_form import Ui_GroupBox

# Main window class, sets up the central widget and connects actions
class SwarmCommanderGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SwarmCommanderGUI()
        self.ui.setupUi(self)
        self.drone_counter = 0
        self.drone_container = {}
        self.connect_actions()

        # Scroll area set up
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.container = QWidget()
        self.grid_layout = QGridLayout(self.container)
        self.grid_layout.setAlignment(Qt.AlignTop)
        
        self.scroll_area.setWidget(self.container)
        
        self.setCentralWidget(self.scroll_area)

    # Connects all actions to the buttons defined in swarmcommandergui.ui
    def connect_actions(self):
        self.ui.actionAdd_agent.triggered.connect(self.add_agent_button)
        self.ui.actionRemove_agent.triggered.connect(self.show_delete_dialog)

    # Adds an agent widget to the main window
    def add_agent_button(self):
        self.drone_counter += 1
        if(self.drone_counter not in self.drone_container.keys()):
            drone_widget = DroneNodeWidget(self.drone_counter)
            drone_widget.setFixedSize(400, 400)  # Square size
            # Format the grid layout
            row = (self.drone_counter - 1) // 3
            col = (self.drone_counter - 1) % 3
            self.grid_layout.addWidget(drone_widget, row, col)
            self.drone_container[self.drone_counter] = drone_widget
        

    # Removes a specific agent from the window
    def remove_agent(self, drone_id):
        if drone_id in self.drone_container:
            widget = self.drone_container[drone_id]
            self.grid_layout.removeWidget(widget)
            widget.deleteLater()
            del self.drone_container[drone_id]
            self.drone_counter -= 1
            self.reorganize_grid
        

    # Reogranizes the widgets on the main window
    def reorganize_grid(self):
        layout = self.ui.centralwidget.layout()
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
        
        drone_ids = sorted(self.drone_container.keys())
        for i, drone_id in enumerate(drone_ids):
            widget = self.drone_container[drone_id]
            row = i // 3
            col = i % 3
            layout.addWidget(widget, row, col)

        self.drone_counter = max(drone_ids) if drone_ids else 0

    # Shows a dialog option to select which agent to remove
    def show_delete_dialog(self):
        if not self.drone_container:
            QMessageBox.information(self, "No Drones", "There are no drones to delete.")
            return
        # Dialog set up
        dialog = QDialog(self)
        dialog.setWindowTitle("Delete Drone")
        dialog.setModal(True)
        layout = QVBoxLayout(dialog)
        
        label = QLabel("Select drone to delete:")
        label.setStyleSheet("""
        QLabel {
            color: #39FF14;
            border: 2px solid white;
            border-radius: 5px;
            padding: 5px;
            background-color: black;
            font-weight: bold;
        }
        """)
        layout.addWidget(label)
        
        # Add a button for each drone
        for drone_id in sorted(self.drone_container.keys()):
            btn = QPushButton(f"Delete Drone {drone_id}")
            btn.clicked.connect(lambda checked, id=drone_id: self.delete_drone_and_close(id, dialog))
            btn.setStyleSheet("""
            QPushButton {
                color: #39FF14;
                border: 2px solid white;
                border-radius: 5px;
                padding: 5px;
                background-color: #222222;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 2px solid #CCCCCC;
            }
            QPushButton:pressed {
                background-color: #111111;
                border: 2px solid #999999;
            }
        """)
            layout.addWidget(btn)
        
        # Cancel button
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(dialog.reject)
        layout.addWidget(cancel_btn)
        
        dialog.exec_()
    
    # Calls remove agent and closes the dialog option
    def delete_drone_and_close(self, drone_id, dialog):
        self.remove_agent(drone_id)
        dialog.accept()

# Drone widget class
    """
        TODO: Add mavlink functionality for sim, add radio functionality for real meshing

            For mavlink, each button/label should connect to the mavlink command as follows:

                Label - Connected: Display connected if a heartbeat is detected, else display searching for heartbeat
                Label - Battery status: Display the current battery amp
                Label - GPS Status: display the gps lock for the drone (true or false?)
                Label - Flightmode: display the current flightmode of the drone

                Button - 


    """
class DroneNodeWidget(QGroupBox, Ui_GroupBox):
    def __init__(self, drone_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.drone_id = drone_id
        self.setTitle(f"Drone {drone_id}")
                


def run_gui(): 
    app = QApplication(sys.argv)
    widget = SwarmCommanderGUI()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_gui()
