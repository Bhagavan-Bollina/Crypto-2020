#!/usr/bin/env bash

echo "Ready to encrypt a file"
echo "Take  me to the same folder, where a file to be encrypted is present"
echo "Enter the Exact File Name"

read -r file

#XCriminal is  decrypting it HAHAH

# gpg -d filename.gpg > filename

gpg -c "$file"

echo "The has been successfully Encrypted:-"
echo "Now I'm gonna remove the original file"

rm -rf "$file"
