#!/bin/bash

echo -n 'Enter the value to hashed into md5:'

read -r x

echo "$x" | md5sum
 



