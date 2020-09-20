#!/bin/bash

echo -n 'Enter the value to hashed into sha256:'

read -r x

echo "$x" | sha256sum

