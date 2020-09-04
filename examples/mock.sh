#!/bin/sh

if [[ $6 = isp123* ]] ; then
cat << EOF
IBM Spectrum Protect
Command Line Administrative Interface - Version 8, Release 1, Level 8.0
(c) Copyright by IBM Corporation and other(s) 1990, 2019. All Rights Reserved.

Session established with server ISP123: Linux/x86_64
  Server Version 8, Release 1, Level 5.107
  Server date/time: 09/03/2020 10:06:11  Last access: 09/03/2020 10:06:00

ANS8000I Server command: 'isp123:q script toto format=raw'.
ANR1699I Resolved ISP123 to 1 server(s) - issuing command Q SCRIPT toto FORMAT=raw against server(s).
ANR1687I Output for command 'Q toto FORMAT=raw' issued against server ISP123 follows:
 BACKUP NODE N1234 /vol/tata toc=yes mode=\\\$1 wait=yes

  select name from scripts where name = 'ABORT_'
  if (RC_OK) goto endit

goto endalways

ANR1627I The previous message was repeated 1 times.
/* Endit routine to exit if ABORT_ script exist */ 
endit:
ISSUE MESSAGE I "999 This means we went to endit because the ABORT_ script exsisted" 
/* This means we went to endit because the ABORT_ script exsisted */ 
ISSUE MESSAGE I "999 House Keeping Aborted by an administrator" 

endalways:

exit
ANR1688I Output for command 'Q SCRIPT toto FORMAT=raw' issued against server ISP123 completed.
ANR1694I Server ISP123 processed command 'Q SCRIPT toto FORMAT=raw' and completed successfully.
ANR1697I Command 'Q SCRIPT toto FORMAT=raw' processed by 1 server(s):  1 successful, 0 with warnings, and 0 with errors.

ANS8002I Highest return code was 0.
EOF
fi

if [[ $6 = isp124* ]] ; then
cat << EOF
ANR1699I Resolved ISP124 to 1 server(s) - issuing command QUERY SCHEDULE TYPE=a FORMAT=detailed against server(s).
ANR1687I Output for command 'QUERY SCHEDULE TYPE=a FORMAT=detailed' issued against server ISP124 follows:
CHANGE_AAAAAAAAAAAAAAA,Change the,update admin *,5,05/16/2018 00:00:00,5 Minute(s),0,Classic,1 Hour(s),Any,,,,,No,PNL,09/11/2018 15:30:51,
N1234_FULL,,run n1234_ndmp full,5,11/15/2019 11:10:00,1 Hour(s),0,Classic,1 Day(s),Monday,,,,,No,PNL,11/15/2019 15:06:18,
ANR1688I Output for command 'QUERY SCHEDULE TYPE=a FORMAT=detailed' issued against server ISP124 completed.
ANR1694I Server ISP124 processed command 'QUERY SCHEDULE TYPE=a FORMAT=detailed' and completed successfully.
ANR1697I Command 'QUERY SCHEDULE TYPE=a FORMAT=detailed' processed by 1 server(s):  1 successful, 0 with warnings, and 0 with errors.
EOF
fi

if [[ $6 = isp125* ]] ; then
cat << EOF
ANR1687I Output for command 
N0129_CL,NetApp,NetApp Release 9.3P14 (Network Appliance),,"Version 0, release 0, level 0.0",NDMP,11/14/2019 13:45:31,294,11/07/2019 13:38:29,301,0,No,,,Yes,No,11/07/2019 13:38:29,ADMIN,NDMP,,,,,,,,,NAS,,No,1,No,No,,,,0,ANY,ANY,ClientOrServer,,,,,,,,ServerOnly,All,,UseReported,,,,,,,,,,None,None,DEFAULT,DEFAULT,DEFAULT,,,WIN:Microsoft Windows Server 2012 Standard,x64,,,Local,Default,Transitional,(?),Yes,Default interval,,,Yes,,
ANR1688I Output for command 
EOF
fi
