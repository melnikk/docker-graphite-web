#!/bin/sh

# Set Time Zone 
cp /usr/share/zoneinfo/$TZ /etc/localtime
echo $TZ > /etc/TZ

# Start Services
exec /usr/bin/supervisord -c /etc/supervisor/supervisord.conf 
