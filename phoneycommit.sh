#!/bin/sh

# Add a random number to a text file
echo $RANDOM > dumbo.txt 
git add *
git commit -m "GitPrint is in full swing"
git push $(cat ../gitcred.txt)
