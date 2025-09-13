#!/usr/bin/env bash
#
# Startup script for ArduPilot SITL
#

if [ -z "$1" ]; then
    echo "Usage: $0 <project_dir> [ardupilot_path]"
    echo "Please provide path to your project folder"
    exit 1
fi

projDir=$1

# Use custom ardupilot path if provided, otherwise use default
if [ -z "$2" ]; then
    ardupilot="${projDir}/SoftwareTools/ardupilot/Tools/autotest"
else
    ardupilot="$2/Tools/autotest"  # Assuming you provide the root ardupilot path
fi

toolsDir="${projDir}/SoftwareTools"
pythonEnv="${projDir}/env"

if [ -d ${pythonEnv} ]; then
    echo "Python Environment already exists."
else
    python3 -m venv ${pythonEnv}
fi

source ${pythonEnv}/bin/activate

# Startup script
python3 ${ardupilot}/sim_vehicle.py -v ArduCopter -w --model webots-python --add-param-file=${projDir}/Webots_Ardupilot/params/iris.parm
