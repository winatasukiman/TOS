1.
* cp /ext/services/tmp
* vim /tmp/services/
* /WorldWideWeb
* cwWorld Wide Web

2.
* vim /tmp/services
* /hello world
* 5dd
* G
* P

3.
* vim /tmp/services
* :g/tcp/s/WHATEVER/g

4. find /etc -name passwd 2> /dev/null

5.
* mkdir test
* cd test
* touch {one,two,three}
* find $HOME -perm -002 -type f -ls

6. find /usr/share/doc -mtime +300

7.
* mkdir /tmp/files
* find usr/share/-size +5m -size -10M -exec cp{} /tmp/files ;
* du -sh tmp/files/*

8. find/tmp/files/-type f -exec cp {} {}.mybackup;

9.
* cd usr/share/doc/kernel.doc*
* grep -rli e1000

10.
* cd /usr/share/doc/kernel-doc-* = grep -rei --color e1000
