"""
Author: Luis Anchundia

Parses incoming radio messages and processes data. Functions are defined to read each type of message/command and also 
See protocol/constants.py for message definitions.

"""
import sys
import os
import threading
import json
from typing import Dict
from typing import Any
from fc_manager import Controller


project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)

from protocol import constants as const
from protocol import packet_definitions as proto


class Message_Router():
    def __init__(self, ctrl: Controller):
        self.lock = threading.Lock()
        self.ctrl = ctrl

    def listener_thread(self, json_string: str):
        with self.lock:
            packet = self.json_to_packet(json_string)
            if(packet["type"] == const.MSG_TYPE_COMMAND):
                if packet["command"] == const.CMD_AGENT_ARM:
                    self.ctrl.arm()
                    return print("AGENT ARMING")




    def packet_to_json(self, packet: Dict[str, Any]) -> str:
        return json.dumps(packet)
    


    def json_to_packet(self, json_string: str) -> Dict[str, Any]:
   
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Received invalid JSON packet: {json_string}") from e

