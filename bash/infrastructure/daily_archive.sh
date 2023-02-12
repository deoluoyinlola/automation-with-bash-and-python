"""The DESTINATION variable appends the full pathname for the archived file.
The CONFIG_ FILE variable points to the archive configuration file containing 
the directories to be archived. These both can be easily changed to alternate 
directories and files if needed."""

#!/bin/bash
#
# Daily_Archive - Archive designated files & directories ######################################################## #
# Gather Current Date
#
DATE=$(date +%y%m%d)
#
# Set Archive File Name
#
FILE=archive$DATE.tar.gz
#
# Set Configuration and Destination File
#
CONFIG_FILE=/archive/Files_To_Backup DESTINATION=/archive/$FILE
#
######### Main Script #########################
#
# Check Backup Config file exists
#

# If it doesn't exist, issue error & exit script.
"$CONFIG_FILE does not exist."
"Backup not completed due to missing Configuration File"
-f $CONFIG_FILE ] # Make sure the config file still exists. # If it exists, do nothing but continue on.
fi
#
# Build the names of all the files to backup
#
FILE_NO=1 # Start on Line 1 of Config File.
exec < $CONFIG_FILE # Redirect Std Input to name of Config File #


FILE_NO=$[$FILE_NO + 1] # Increase Line/File number by one.
read FILE_NAME # Read next record. done
#
#######################################
#
# Backup the files and Compress Archive
#
