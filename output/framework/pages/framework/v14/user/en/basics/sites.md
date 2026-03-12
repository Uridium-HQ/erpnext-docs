# Sites

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12jpf1jpr7)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Sites 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12jpf1jpr7)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe is a multitenant platform and each tenant is called a site. A site has its own database. Sites exist in a directory called `sites`, assumed as the current working directory when running a bench command.

## Sites Directory

The sites directory `frappe-bench/sites` is where all the sites for this bench live. It also contains some other files and directories which are explained next.

### apps.txt

This file contains a list of Frappe apps. An app should be listed here before it can be installed on a site. It is added automatically when `bench get-app` command or `bench new-app` command is run.

### common\\_site\\_config.json

Configuration common to all sites can be put in this file. Learn more about [site configuration](site_config.md).

### assets

Assets contain files that are required to be served for the client browser. These generally include *.js, *.css, and image files. This directory is auto generated using the `bench build` command. This directory is served by Nginx in production.

## Creating a new site

To create a new site, run the following command from the `frappe-bench` directory:
[code] 
    $ bench new-site mysite.local
    
    Installing frappe...
    Updating DocTypes for frappe : [========================================]
    Updating country info : [========================================]
    *** Scheduler is disabled ***
    
[/code]

The `mysite.local` directory will now be created in the `sites` directory.

## Directory Structure
[code] 
    sites/mysite.local
    ├── locks
    ├── private
    │   ├── backups
    │   └── files
    ├── public
    │   └── files
    ├── site_config.json
    └── task-logs
    
[/code]

### locks

This directory is used by the scheduler to synchronize various jobs using the [file locking concept](http://en.wikipedia.org/wiki/File_locking).

### private

This directory contains files that require authentication to access. It contains private files and backups. They can be accessed by the URL: `/private/files/private-file.png`.

### public

This directory contains publicly accessible files. They can be accessed by the URL: `/files/public-file.png`.

### site_config.json

This file contains site specific configuration.

## Site Config

A file named `site_config.json` exists in every site directory and is used to store site specific configuration. The values are available in `frappe.conf` local variable as a dict.

Example `site_config.json`:
[code] 
    {
     "db_name": "test_frappe",
     "db_password": "test_frappe",
     "admin_password": "admin",
    }
    
[/code]

To learn more about managing Site or Bench level configurations, checkout [this comprehensive document](site_config.md).

## Site Resolution

While responding to an HTTP request, a site is automatically selected based on,

  * `Host` header in the HTTP request matches a site
  * `X-Frappe-Site-Name` header in the HTTP request matches a site



It is also possible to force the development server to serve a specific site by starting it with the following command:
[code] 
    bench --site mysite.local serve
    
[/code]

## Set a site as the current site

To force a site to be used as the default site, run the following command:
[code] 
    bench use mysite.local
    
[/code]

After running this command, site specific commands can be run without the `--site` parameter.

For example, instead of running:
[code] 
    bench --site mysite.local migrate
    
[/code]

You can just run:
[code] 
    bench migrate
    
[/code]

[ Previous Page Apps  ](apps.md) [ Next Page Understanding DocTypes  ](doctypes.md)

Last updated 2 months ago 

Was this helpful?
