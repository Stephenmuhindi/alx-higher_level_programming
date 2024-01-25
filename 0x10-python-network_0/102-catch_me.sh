#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me
curl -sL -d "user_id=98&message=You%20got%20me!" "0.0.0.0:5000/catch_me" -H "Origin:HolbertonSchool" -X PUT 
