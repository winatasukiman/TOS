1. ps -f|less
2. ps -ef --sort=user|less
3. ps -eo 'pid,user,group,nice,vsz,rss,comm'|less
4. top
 * P
 * M
5. gedit &
6.
 * gedit &
 * kill -SIGTOP 21578
7.
 * killall -SIGCONT gedit
8.
 * yum install xorg=xll-apps
 * xeyes &
 * xeyes &
 * killall xeyes &
9.
 * nice -n 7 21578
10.
 * ps -ep 'pid,user,nice,comm'|grep gedit
