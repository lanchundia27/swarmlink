"""
Creates fake xbee messages to test logic in message_router.py, use xbee_manager.py for real radio messages.

"""

from typing import Dict
from typing import Any
import pymavlink

import sys
import os
import threading
import json

project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)
from protocol import constants as const
from protocol import packet_definitions as proto



class radio_sim():
    def __init__(self):
        pass

    def generate_arm_command(self):
        arm_payload = proto.create_command_packet(const.CMD_AGENT_ARM, None)
        JSON_package = self.packet_to_json(arm_payload)
        return JSON_package
    
    def packet_to_json(self, packet: Dict[str, Any]) -> str:
    
        return json.dumps(packet)
    
    def json_to_packet(self, json_string: str) -> Dict[str, Any]:
   
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Received invalid JSON packet: {json_string}") from e


if __name__ == "__main__":
    print("yuh")