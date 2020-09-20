#!/bin/bash

echo -n 'Enter the value to hashed into sha1:'

read -r x

echo "$x" | sha1sum

