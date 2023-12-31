#!/bin/bash

set_permissions() {
    echo ""
    echo "Making files executeable"
    echo ""
    chmod +x setup.sh
    chmod +x start.sh
    chmod +x stop.sh
    echo "Changing permissions for files"    
    echo ""
    chmod 700 Maintance_Scripts
    chmod 700 GNGC_CYBER_RANGE_WEBSITE
    chmod 700 GNGC_CYBER_RANGE_SCRIPTS
    chmod 700 setup.bat
    chmod 700 setup.sh
    chmod 700 setupcheck.sh
    chmod 700 start.sh
    chmod 700 stop.sh
    echo "Permissions set!"
}

end_message() {
    echo ""
    echo "If there was an error, then it's recommended to restart the script and agree to update installers."
    echo ""
}

update_installers() {
    echo "Updating Installers..."
    sudo apt update
    python -m pip install --upgrade pip --no-warn-script-location
    echo ""
}

install_python_dependencies() {
    echo "Installing Python dependencies..."
    sudo python3 -m pip install flask --break-system-packages
    sudo python3 -m pip install flask_login --break-system-packages
    sudo python3 -m pip install bcrypt --break-system-packages
    sudo python3 -m pip install sqlalchemy --break-system-packages
    sudo python3 -m pip install re --break-system-packages
    sudo python3 -m pip install validate_email --break-system-packages
    sudo python3 -m pip install mysqlclient --break-system-packages
    sudo python3 -m pip install pymysql --break-system-packages
    sudo python3 -m pip install validate_email --break-system-packages
    sudo python3 -m pip install python-dotenv --break-system-packages
    sudo python3 -m pip cache purge --break-system-packages

}


install_other_dependencies() {
    echo "Installing other dependencies..."
    echo ""
    echo "Installing and configuing database"
    echo ""
    sudo apt install mariadb-server
    echo ""
    sudo ./Maintance_Scripts/setupDB.sh
    sudo apt-get install -y iputils-ping
    sudo apt install python3
    sudo apt install python3-pip
    echo ""
    sudo ./Maintance_Scripts/setupWSGI.sh
}

read -p "Do you want to install other dependencies? (Y/N): " other_choice
if [[ "$other_choice" =~ ^[Yy]$ ]]; then
    install_other_dependencies
    end_message
fi

read -p "Do you want to update apt and pip? (Recommended) (Y/N): " python_choice
if [[ "$python_choice" =~ ^[Yy]$ ]]; then
    update_installers
fi

read -p "Do you want to install Python dependencies? (Y/N): " python_choice
if [[ "$python_choice" =~ ^[Yy]$ ]]; then
    install_python_dependencies
    end_message
fi

cd ~/GNGC-CYBER-RANGE/

set_permissions

echo ""
echo "Setting up custom commands"
echo ""
source ./Maintance_Scripts/setupAlias.sh

echo "Done!"
