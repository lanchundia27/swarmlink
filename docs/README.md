# swarmlink

The goal of this project is to build a self healing mesh network for our drone swarm.
The network will work as a mobile ad-hoc network, each drone should be able to connect to the network via Xbee radios with no centralized "leader" drone. The grounstation will have a custom GUI and connect to the network via xbee.
The groundstation will be able to monitor each drone and its current state (altitude, velocity, and search algorithim) as well as send commands either to an individual agent or the entire swarm.

![]image(dataflowchar.png)