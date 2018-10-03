# apmonit
Python Flask application for checking of access points' workability (especially for CSF VSU)

This code was written for Linux Debian 9.5. Follow next steps to install the application properly:
1) Put apmonit.py into /usr/bin/, apmonit.txt into usr/local/etc/, apmonit.service into /lib/systemd/system/
2) systemctl daemon-reload
3) systemctl enable apmonit.service
4) systemctl start apmonit.service
5) systemctl status apmonit.service
6) apt-get install apache2 libapache2-mod-wsgi-py3 
7) mkdir /var/www/FlaskApp/ /var/www/FlaskApp/FlaskApp/ /var/www/FlaskApp/FlaskApp/static/ /var/www/FlaskApp/FlaskApp/templates/
8) Put apmonit.wsgi into /var/www/FlaskApp/, __init__.py and requirements.txt into /var/www/FlaskApp/FlaskApp/, index.html into /var/www/FlaskApp/FlaskApp/templates/
9) cd /var/www/FlaskApp/FlaskApp/
10) python3 -m venv venv
11) source venv/bin/activate
12) pip install -y flask flask-bootstrap
13) deactivate
14) useradd -M flask
15) usermod -s /bin/false flask
16) usermod -L flask
17) adduser flask www-data
18) Put FlaskApp.conf into /etc/apache2/sites-enabled/
19) Add string "127.0.0.1 localhost apmonit" into /etc/hosts
20) systemctl restart apache2.service
21) If your host OS is Windows, add string "{IP-address of Virtual Machine} apmonit" into C:\Windows\System32\drivers\etc\hosts
22) Enter in address line of your browser: http://apmonit
