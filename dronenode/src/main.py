"""
Author: Luis Anchundia

Main file to handle all threads for the drone
"""

import threading
import queue
from fc_manager import Controller 
from message_router import Message_Router
from simulated_radio_manager import radio_sim

if __name__ == "__main__":
    ctrl = Controller('sim')
    radio_sim = radio_sim()
    translator = Message_Router(ctrl)
    from_radio = radio_sim.generate_arm_command()


    listen = threading.Thread(target=translator.listener_thread(from_radio))

    listen.start()
    listen.join()