Ardupilot SITL is a safe (simulated) environment to test all the code for the companion computer before the real world run on the quad copter. The system simulates ArduPilot in the your local machine. The system responds to MAVLink messages sent via UDP messages.

1. Clone the ardupilot repo from https://github.com/ArduPilot/ardupilot (either in this directory or outside)
2. Build ardupilot SITL. You have to build ardupolot to run as a simulation. There are guides with information here in ardupilot sitl install docs and the ardupilot build docs. TLDR below:
    i. Run the environment script in Tools/environment_install/install-prereqs-<your OS>.sh (for windows follow the instructions https://ardupilot.org/dev/docs/building-setup-windows11.html#building-setup-windows11) TLDR2: install WSL for windows, then follow the Ubunutu instructions to build the environment.
    ii. If everything worked out in the previous script, you should have all prerequisites installed at this point run ./waf configure --board sitl
    iii. Build ardupilot for SITL with ./waf copter.
3. We will use webots to visualize the drones. To install webots for your specific OS follow the guide: https://cyberbotics.com/doc/guide/installation-procedure.
4. run the run_ardupilot_sitl.sh, then open webots (you may have to pip install some packages to run the shell file)
