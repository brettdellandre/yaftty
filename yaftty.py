#!/usr/bin/python3

# yaftty.py: Orchistration Core to Migrate Data From Isilon to VAST
# determine dry run, estimate, seed, delta, or cleanup

import sys

PROTOCOL="nfsv3" # Can be "nfsv3"; The following are not yet implimented "nfsv41", "smb" or "s3"
ONEFS_LOGIN_IP="empty" 
ONEFS_USERNAME="root"
ONEFS_PASSWORD="a"
ONEFS_ACCESS_ZONE="System"
VMS_LOGIN_IP="empty"
VMS_USERNAME="admin"
VMS_PASSWORD="123456"
VMS_VIP_POOL="main"
SOURCE_PATH="/ifs/data"
SOURCE_NFS_EXPORT="/ifs/data/"
#SOURCE_SMB_SHARE="ifs" # Not yet implimented
DESTINATION_PATH="/data/"
DESTINATION_NFS_EXPORT="/ifs/data"
#DESTINATION_SMB_SHARE="ifs" # Not yet implimented
FPSYNC_TMP_DIR="/tmp/yaftty/fpsync"
FPSYNC_THREADS_PER_NODE="8"
LOGGING="warn" # Other options: "error", "info", "debug" or "none"
