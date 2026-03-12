# Installation

[ Edit ](</wiki/spaces/r3uvq1ch61/page/125oc13nr4>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Installation

[ Edit ](</wiki/spaces/r3uvq1ch61/page/125oc13nr4>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

> These steps assume you want to install Bench in developer mode. If you want install in production mode, follow the [latest recommended installation methods](<https://github.com/frappe/bench#installation>).

## System Requirements

This guide assumes you are using a personal computer, VPS or a bare-metal server. You also need to be on a *nix system, so any Linux Distribution and MacOS is supported. However, we officially support only the following distributions.

  1. MacOS
  2. Debian / Ubuntu



> Learn more about the architecture [here](</framework/v14/user/en/basics/architecture>).

## Pre-requisites
[code] 
    Python 3.10+ (v14)
    Node.js 16
    Redis 6                                       (caching and realtime updates)
    MariaDB 10.6.6+ / Postgres v12 to v14         (Database backend)
    yarn 1.12+                                    (js dependency manager)
    pip 20+                                       (py dependency manager)
    wkhtmltopdf (version 0.12.5 with patched qt)  (for pdf generation)
    cron                                          (bench's scheduled jobs: automated certificate renewal, scheduled backups)
    NGINX                                         (proxying multitenant sites in production)
    
    
[/code]

### MacOS

Install command line version of Xcode tools.
[code] 
    xcode-select --install
    
    
[/code]

Install [Homebrew](<https://brew.sh/>). It makes it easy to install packages on macOS.
[code] 
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    
[/code]

Now, you can easily install the required packages by running the following command
[code] 
    brew install python@3.10 git redis mariadb@10.6 node@14
    brew install --cask wkhtmltopdf
    
    
[/code]

Now, edit the MariaDB configuration file.
[code] 
    nano /usr/local/etc/my.cnf
    
    
[/code]

For Apple silicon the path for the MariaDB config is
[code] 
    nano /opt/homebrew/etc/my.cnf
    
    
[/code]

And add this configuration
[code] 
    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server = utf8mb4
    collation-server = utf8mb4_unicode_ci
    bind-address = 127.0.0.1
    
    [mysql]
    default-character-set = utf8mb4
    
    
[/code]

Now, just restart the mysql service and you are good to go.
[code] 
    brew services restart mariadb
    
    
[/code]

**Install Yarn**

Install yarn using npm
[code] 
    npm install -g yarn
    
    
[/code]

### Debian / Ubuntu

Install `git`, `python`, and `redis`
[code] 
    sudo apt install git python-dev python-pip redis-server
    
    
[/code]

**Install MariaDB**
[code] 
    sudo apt install software-properties-common
    
    
[/code]

If you are on Ubuntu version older than 20.04, run this before installing MariaDB:
[code] 
    sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
    sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.ubuntu-tw.org/mirror/mariadb/repo/10.3/ubuntu xenial main'
    
    
[/code]

If you are on version Ubuntu 20.04, then MariaDB is available in default repo and you can directly run the below commands to install it:
[code] 
    sudo apt-get update
    sudo apt-get install mariadb-server
    
    
[/code]

During this installation you'll be prompted to set the MySQL root password. If you are not prompted, you'll have to initialize the MySQL server setup yourself. You can do that by running the command:
[code] 
    mysql_secure_installation
    
    
[/code]

> Remember: only run it if you're not prompted the password during setup.

It is really important that you remember this password, since it'll be useful later on. You'll also need the MySQL database development files.
[code] 
    apt-get install mariadb-client-10.3
    
    
[/code]

Now, edit the MariaDB configuration file.
[code] 
    nano /etc/mysql/my.cnf
    
    
[/code]

And add this configuration
[code] 
    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server = utf8mb4
    collation-server = utf8mb4_unicode_ci
    
    [mysql]
    default-character-set = utf8mb4
    
    
[/code]

Now, just restart the mysql service and you are good to go.
[code] 
    service mysql restart
    
    
[/code]

**Install Node**

We recommend installing node using [nvm](<https://github.com/creationix/nvm>)
[code] 
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
    
    
[/code]

After nvm is installed, you may have to close your terminal and open another one. Now run the following command to install node.
[code] 
    nvm install 14
    
    
[/code]

Verify the installation, by running:
[code] 
    node -v
    # output
    v14.17.2
    
    
[/code]

Finally, install `yarn` using `npm`
[code] 
    npm install -g yarn
    
    
[/code]

**Install wkhtmltopdf**
[code] 
    apt-get install xvfb libfontconfig wkhtmltopdf
    
    
[/code]

## Install Bench CLI

Install bench via pip3
[code] 
    pip3 install frappe-bench
    
    
[/code]

Confirm the bench installation by checking version
[code] 
    bench --version
    
    # output
    5.2.1
    
    
[/code]

Create your first bench folder.
[code] 
    cd ~
    bench init frappe-bench
    
    
[/code]

After the frappe-bench folder is created, change your directory to it and run this command
[code] 
    bench start
    
    
[/code]

Congratulations, you have installed bench on to your system.

[ Previous Page Prerequisites  ](</framework/v14/user/en/prerequisites>) [ Next Page Frappe Framework Tutorial  ](</framework/v14/user/en/tutorial>)

Last updated 2 months ago 

Was this helpful?
