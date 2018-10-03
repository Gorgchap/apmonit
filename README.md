# apmonit
Python Flask application for checking of access points' workability (especially for CSF VSU)

This code was written for Linux Debian 9.5. Follow next steps to install the application properly:
1) Put apmonit.py into /usr/bin/, apmonit.txt into usr/local/etc/, apmonit.service into /lib/systemd/
2) systemctl daemon-reload
   systemctl enable apmonit.service
   systemctl start apmonit.service
   systemctl status apmonit.service
3) apt-get install apache2 libapache2-mod-wsgi-py3
   mkdir /var/www/FlaskApp/ /var/www/FlaskApp/FlaskApp/ /var/www/FlaskApp/FlaskApp/static/ /var/www/FlaskApp/FlaskApp/templates/
4) Put apmonit.wsgi into /var/www/FlaskApp/, __init__.py and requirements.txt into /var/www/FlaskApp/FlaskApp/
   cd /var/www/FlaskApp/FlaskApp/
   python3 -m venv venv
   source venv/bin/activate
   pip install flask flask-bootstrap
   deactivate
5) Put FlaskApp.conf into /etc/apache2/sites-enabled/
6) Add string "127.0.0.1 localhost apmonit" into /etc/hosts
7) systemctl restart apache2.service
8) If your host OS is Windows, Add string "{IP-address of Virtual Machine} apmonit" into C:\Windows\System32\drivers\etc\hosts
9) Enter in address line of your browser: http://apmonit
