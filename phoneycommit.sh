#!/bin/sh

# Add a random number to a text file
echo "\n Original Dumbo:\n"
cat dumbo.txt
echo $RANDOM > dumbo.txt 

echo "\nNew Dumbo:\n"
cat dumbo.txt

echo "\nAdding New Dumbo:\n"
git add *

echo "\nCommit...:\n"
git commit -m "GitPrint is in full swing"

echo "\nPushing...\n\n"
git push $(cat ../gitcred.txt)
