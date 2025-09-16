"""
Author: Luis Anchundia

controller class, all needed mavlink commands are defined here for use in computation and message processing.
"""

from pymavlink import mavutil
import pymavlink.dialects.v20.ardupilotmega as mavlink
from pymavlink.dialects.v20.ardupilotmega import (MAVLink_global_position_int_message, MAVLink_attitude_message,
                                                  MAVLink_set_position_target_global_int_message,
                                                  MAVLink_set_position_target_local_ned_message,
                                                  MAVLink_set_position_target_local_ned_message,
                                                  MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, MAV_FRAME_BODY_OFFSET_NED,
                                                  MAV_FRAME_BODY_OFFSET_NED, MAV_CMD_DO_SET_MODE, MAV_CMD_NAV_TAKEOFF,
                                                  MAV_CMD_NAV_WAYPOINT,
                                                  MAV_CMD_GUIDED_CHANGE_SPEED,
                                                  MAV_CMD_NAV_LAND)
from pymavlink.dialects.v20.common import (MAV_CMD_DO_CHANGE_SPEED)
from time import sleep
from time import perf_counter
import numpy as np
import asyncio




class Controller:

    def __init__(self, device_type: str):
        connStr = "/dev/ttyAMA0" if device_type.upper() == 'REAL' else "udp:localhost:14550"
        self.conn = mavutil.mavlink_connection(connStr)
        self.conn.wait_heartbeat()
        print("Heartbeat from system (system %u component %u)" %
              (self.conn.target_system, self.conn.target_component))

    # def __init__(self, connStr: str):
    #     self.conn = mavutil.mavlink_connection(connStr, baud=57600)
    #     self.conn.wait_heartbeat()
    #     print("Heartbeat from system (system %u component %u)" %
    #           (self.conn.target_system, self.conn.target_component))
    #
    def arm(self):
        # Set mode to guided
        self.conn.mav.command_long_send(
            self.conn.target_system,  # target_system
            self.conn.target_component,
            mavlink.MAV_CMD_DO_SET_MODE,  # command
            0,          # confirmation
            89,         # param1 (Mode)
            4,          # param2 (Custom mode)
            0,          # param3 (Custom Sub Mode)
            0,          # param4 (None)
            0,          # param5 (None)
            0,          # param6 (None)
            0)          # param7 (None)

    # Arm motor
        self.conn.arducopter_arm()
        sleep(1)

    def takeoff(self, altitude):
        self.conn.mav.command_long_send(
            self.conn.target_system,  # target_system
            self.conn.target_component,
            mavlink.MAV_CMD_NAV_TAKEOFF,  # command
            0,          # confirmation
            0,          # param1 (Min Pitch)
            0,          # param2 (None)
            0,          # param3 (None)
            0,          # param4 (Yaw Angle)
            0,          # param5 (Latitude)
            0,          # param6 (Longitude)
            altitude)   # param7 (Altitude)

    # async def move_vel(self, pos):
    #     move_vel_msg = mavlink.MAVLink_set_position_target_local_ned_message(
    #
    #     )

    def move_pos_vel(self, x, y, z, yaw_rate=0):
        # Generate a move message based on relative position received
        move_msg = mavlink.MAVLink_set_position_target_local_ned_message(
            int(perf_counter() * 1000),
            self.conn.target_system,
            self.conn.target_component,
            mavlink.MAV_FRAME_BODY_OFFSET_NED,
            0,
            0,
            0,
            0,
            x,
            y,
            z,
            0,
            0,
            0,
            0,
            yaw_rate
        )
    # Send move message
        self.conn.mav.send(move_msg)

    def land(self):
        self.conn.set_mode_rtl()

    def move_pos_rel(self, x, y, z):
        # Generate a move message based on relative position received
        move_msg = mavlink.MAVLink_set_position_target_local_ned_message(
            int(perf_counter() * 1000),
            self.conn.target_system,
            self.conn.target_component,
            mavlink.MAV_FRAME_BODY_OFFSET_NED,
            3576,
            x,
            y,
            z,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        )
        # Send move message
        self.conn.mav.send(move_msg)