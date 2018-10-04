=====/etc/init.d/apmonit==== 
#! /bin/sh

#
#Description=AP Monitoring Service
#


case "$1" in
  start)
        /usr/bin/python /usr/bin/apmonit.py 2>/dev/null 1>/dev/null &
        ;;
  stop)
        kill `ps x | grep apmonit | grep -v grep |grep -v init| awk '{print $1}'`
        ;;
  status)
        ps x | grep apmonit | grep -v grep | grep -v init | awk '{print $1}'
        ;;
  *)
        echo "Usage: apmonit {start|status|stop}" >&2
        exit 3
        ;;
esac
=========