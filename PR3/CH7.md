1.
 * mkdir bin
 * cd bin
 * vim myownscript
 * #!/bin/bash
 * echo "Today is $(DATE)"
 * echo "You are in $(pwd) and your host is $(hostname)"
 * chmod 755 myownscript
2.
#!/bin/bash

ONE=$1

TWO=$2

THREE=$3

echo "There are $# parameters that include: $@"

echo "The first is $ONE, the second is $TWO, the third is $THREE"

3.
#!/bin/bash

read -p "What street?" mystreet

read -p "What Town?" mytown

echo "The Street I grew up in was $mystreet and the town was $mytown"
4.
#!/bin/bash
read -p "whats your favourite OS?mac,windows,linux?" oss
if [$oss = windows] ;then

echo "Windows is Nice"

elif [$oss = mac] ; then

echo "What's a Mac?"

elif [$oss = lin] ; then

echo "yea linux"

else

echo "Is that an OS?"

fi

5.
#!/bin/bash

for ANIMALS in moose cow goose sow ; do

echo "I have a $ANIMALS"
done
