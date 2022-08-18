#!/bin/bash
# 6. Only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
