#!/bin/bash

set_root_password() {
    sudo apt update
    echo ""
    echo "Installing ....."
    sudo apt install -y mariadb-server
    sudo service mysql start
    echo ""
    echo "Setting root password"
    echo ""
    sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'GNGC-PASS';" 2>/dev/null
    sudo mysql -e "FLUSH PRIVILEGES;" 2>/dev/null
    echo "Root password set successfully."

}

setup_default_db(){
    mysql -e "CREATE DATABASE IF NOT EXISTS gngcmain;" -u root -p"GNGC-PASS" 2>/dev/null
    echo ""
    echo "Created default user database"
}

set_root_password
setup_default_db
echo ""
