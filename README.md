
### Overview

This is the server files for a GNGC Cyber Range project, these files include challanges hosted on the server and any server maintance files.

These files will never be pushed towards development and are only used for a long project.


### Setup
Run these commands on a Ubuntu Linux PC with internet connection
- git clone https://github.com/Fox2low/GNGC-CYBER-RANGE
- bash setup.sh
- bash start.sh

To edit settings for the challanges 
- Navigate to ~/GNGC-CYBER-RANGE/GNGC_CYBER_RANGE_SCRIPTS

To shutdown server
- stop.sh


### Task list
#### The GNGC Cyber Range - Tasklist
- [x] Github Repository Setup
- [x] Github - VS Code Intergration Setup
- [x] Maintance Scripts
    - [x] Create setup file
    - [x] Create setupcheck file
    - [x] Create startserver file
    - [x] Create setupDB file
    - [x] Create custom commands file
- [x] Full Network Connectivity
    - [x] Basic Network structure designed
    - [x] Switch / Router Setup
    - [x] Ubuntu Server setup
    - [x] Basic Kali installation installed on all clients.
- [x] Basic Network Services
    - [x] DHCP pools setup / Configured
    - [x] DNS Setup / Configured
    - [x] WSGI Server Setup / Configured
    - [x] SQL Server Setup / Configured.
- [x] Simple Challenges
    - [x] Simple Command Line Challenges

**-- Everything from this point on should be completed in Assignment 3 --**

- [ ] Advanced Challenges
    - [ ] Advanced Command Line Challenges
    - [ ] Dynamic Web Challenges
    - [ ] OINST Challenges
    - [ ] Networking Challenges
    - [ ] Programming Challenges
    - [ ] Digital Forensics Challenges
    - [ ] Cryptography Challenges

[comment]: <> (Please work on this Om)
#### GNGC Cyber Range Web Component - Tasklist
- [x] Github Repository Setup
- [x] Github - VS Code Intergration Setup
- [x] Finished tasklist on Readme file
- [x] Basic Frontned
    - [X] Website Design
    - [x] Basic HTML and CSS
    - [X] The structure of home page
- [X] Database
    - [x] Creating MariaDB database
    - [x] Creating database model in sqlalchemy
- [X] Implementing features 
    - [X] Login and signup 
    - [X] Basic home and dashboard page
    - [x] All Routes planned and done
- [x] Planning challenges
    - [x] Basic web based challanges planned out
- [ ] Implementing challenges 
    - [ ] HTML, CSS and JS challanges created and running
    - [ ] Python challanges created and running
- [ ] Cleaning and polishing
    - [ ] Cleaning up code and making it more efficient
    - [ ] Self testing to plug any leaks and protect from errors
- [ ] User Testing
    - [ ] Have a group of users test program
    - [ ] From experienced cyber users to beginners
    - [ ] Make improvements
    - [ ] Final Checks


### File Structure
- GNGC_CYBER_RANGE_SCRIPTS
    - Python scripts that hold external challanges
- GNGC_CYBER_RANGE_WEBSITE
    - Flask website
    -   All HTML pages
- Maintance_Scripts
   - Setup scripts
   - Debug scripts
   - Server Maintance scripts
