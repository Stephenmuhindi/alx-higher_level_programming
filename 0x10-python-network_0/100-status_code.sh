#!/bin/bash
#script that sends a request to a URL passed 
curl -w "%{http_code}" "$1" -so /dev/null
