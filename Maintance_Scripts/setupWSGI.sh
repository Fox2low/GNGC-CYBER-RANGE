#!/bin/bash

flask_app_dir="$HOME/GNGC-CYBER-RANGE/GNGC_CYBER_RANGE_WEBSITE/"
domain_name="GNGC-CYBER-RANGE"
apache_virtualhost_dir="/etc/apache2/sites-available/"

sudo apt-get update
sudo apt-get install -y apache2-dev
python3 -m pip install mod_wsgi

wsgi_module_config=$(mod_wsgi-express module-config)
echo "${wsgi_module_config}" | sudo tee /etc/apache2/mods-available/wsgi.load
sudo a2enmod wsgi
sudo systemctl restart apache2

cat <<EOF > application.wsgi
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from application import app as application
EOF

mv application.wsgi "${flask_app_dir}"

cat <<EOF | sudo tee "${apache_virtualhost_dir}${domain_name}.conf"
<VirtualHost *:80>
        ServerName ${domain_name}
        SetEnv APP_ENV dev
        WSGIScriptAlias / ${flask_app_dir}application.wsgi
        <Directory ${flask_app_dir}>
                Order allow,deny
                Allow from all
        </Directory>
</VirtualHost>
EOF

sudo a2ensite ${domain_name}.conf
sudo systemctl reload apache2

echo "Apache setup for Flask app is complete. Your app should now be accessible via http://${domain_name}/"
