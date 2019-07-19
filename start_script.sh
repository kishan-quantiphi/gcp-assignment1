#! /bin/bash
apt-get update
apt-get install -y apache2 stress
rm /var/www/html/index.html
echo "<html><body><h1>Hello People</h1><h2>This webpage in running  on intance $HOSTNAME</h2></body></html>" >> /var/www/html/index.html