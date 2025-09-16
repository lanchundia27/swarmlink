"""
Author: Luis Anchundia

Functions that define and create the JSON packet format, check constants.py for definitions.
"""

from protocol import constants
import json
from typing import Dict, Any, List

def create_routed_packet(final_dest: str, path: List[str], payload: Dict[str, any]):
    """Creates a packet to send to a specific xbee address
        
    Args:
        final_dest (str): Xbee destination address to send the payload to
        path (List[str]): list of xbee addresses to travel through 
        payload (Dict[str, any]): Command or data to be delivered
    """

    return{
        "type": constants.MSG_TYPE_ROUTED,
        "final_dest": final_dest,
        "path": path,
        "payload": payload,
    }

def create_command_packet(command_type: str, parameters: Dict[str, any]):
    """Creates a command packet to be used as a payload to send via xbee.
    
    Args:
        command_type (str): command type, check constants for types of commands
        parameters (Dict[str, any]): parameters, check constants for parameters of certain commands
    """
    return {
        "type": constants.MSG_TYPE_COMMAND,
        "command": command_type,
        "parameters": parameters
    }

def create_telemetry_packet(battery_v: float, gps_lat: float, gps_lon: float, alt: float, vehicle_state: str):
    """Creates a standard telemetry packet, this way only one request needs to be sent to update the ground station.

    Args:
        battery_v (float): battery voltage
        gps_lat (float): gps_lat
        gps_lon (float): gos lon
        alt (float): altitude
        vehicle_state (str): vehicle state, may be removed later
    """
    return {
        "type": constants.MSG_TYPE_TELEMETRY,
        "battery_v": battery_v,
        "gps_lat": gps_lat,
        "gps_lon": gps_lon,
        "altitude": alt,
        "vehicle_state": vehicle_state
    }

