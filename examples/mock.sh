#!/bin/sh
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
