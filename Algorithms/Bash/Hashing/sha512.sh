#!/bin/bash

echo -n 'Enter the value to hashed into sha512:'

read -r x

echo "$x" | sha512sum

