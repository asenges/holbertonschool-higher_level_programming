#!/bin/bash
# 7. cURL a JSON file
curl -X POST -sH 'Content-Type:application/json' -d @"$2" "$1"
