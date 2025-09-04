#!/bin/bash

while getopts "h:u:" opt; do
    case $opt in
    h) SERVER=$OPTARG ;;
    u) USER=$OPTARG ;;
    esac
done

docker build -t python-gpt:pi -f dockerfile .
docker save python-gpt:pi -o python-gpt.tar
scp python-gpt.tar ${USER}@${SERVER}:~/image
rm python-gpt.tar