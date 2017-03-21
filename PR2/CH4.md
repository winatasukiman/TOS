1.
..* mkdir projects
..* touch house{1..9}

2.
..* cd projects
..* mkdir house
..* cd house
..* mkdir doors
..* touch example.txt

3.
..* cp projects/house1 projects/house/
..* cp projects/house5 projects/house/

4.
..* cp -ra.usr.share.doc.initscripts*/-/projects/

5.
..* ls-lR project | less

6. rm -f projects/house[678]

7. mv projects/house{3,4} projects/house/doors/

8. rm-rf projects/house/doors

9. chmod 640 projects/house2

10. chmod -R -a -w projects
