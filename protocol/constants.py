"""
Author: Luis Anchundia

Application constants and definitions for sending JSON packets via xbees
Shared language between GCS and agents, maybe ground robot too
"""




# ==================== MESSAGE TYPES ====================
MSG_TYPE_ROUTED = "routed_message"
MSG_TYPE_COMMAND = "command"
MSG_TYPE_TELEMETRY = "telemetry"
MSG_TYPE_DISCOVERY_PING = "discovery_ping"
MSG_TYPE_DISCOVERY_RESPONSE = "discovery_resp"
MSG_TYPE_ACK = "acknowledgement"

#==================== COMMAND TYPES =======================
CMD_SWARM_ARM = "swarm_arm"
CMD_SWARM_DISARM = "swarm_disarm"
CMD_AGENT_ARM = "agent_arm"
CMD_AGENT_DISARM = "agent_disarm"
CMD_SWARM_TAKEOFF = "swarm_takeoff"
CMD_SWARM_LAND = "swarm_land"

# ==================== SEARCH ALGORITHM PARAMETERS ====================
# TODO

# ==================== TELEMETRY FIELDS ====================
TELEM_BATTERY_V = "battery_voltage"
TELEM_GPS_LAT = "gps_lat"
TELEM_GPS_LON = "gps_lon"
TELEM_ALTITUDE = "altitude"
TELEM_STATE = "vehicle_state"

