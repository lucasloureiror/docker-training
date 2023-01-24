#!bin/bash
redis-server &
sleep 2
redis-cli ping
