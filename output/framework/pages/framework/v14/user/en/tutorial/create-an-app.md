# Create an App

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/125jnefjs7)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Create an App

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/125jnefjs7)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Create a frappe app scaffold using the bench CLI.

## Create app

Before we start, make sure you're in a bench directory. To confirm, run `bench find .`:
[code] 
    $ bench find .
    /home/frappe/frappe-bench is a bench directory!
      
    
    
[/code]

To create our Library Management app, run the `new-app` command:
[code] 
    $ bench new-app library_management
    App Title (default: Library Management):
    App Description: Library Management System
    App Publisher: Faris Ansari
    App Email: faris@example.com
    App Icon (default 'octicon octicon-file-directory'):
    App Color (default 'grey'):
    App License (default 'MIT'):
    'library_management' created at /home/frappe/frappe-bench/apps/library_management
    
    Installing library_management
    $ ./env/bin/pip install -q -U -e ./apps/library_management
    $ bench build --app library_management
    yarn run v1.22.4
    $ FRAPPE_ENV=production node rollup/build.js --app library_management
    Production mode
    ✔ Built js/moment-bundle.min.js
    ✔ Built js/libs.min.js
    ✨  Done in 1.95s.
      
    
    
[/code]

You will be prompted with details of your app, fill them up and an app named `library_management` will be created in the `apps` folder.

To see a complete list of all icons supported in the octicons library, check out <https://primer.style/octicons/>

## App directory structure

Your app directory structure should look something like this:
[code] 
    apps/library_management
    ├── README.md
    ├── library_management
    │   ├── hooks.py
    │   ├── library_management
    │ │ └── __init__.py
    │ ├── modules.txt
    │ ├── patches.txt
    │ ├── public
    │ │ ├── css
    │ │ └── js
    │ ├── templates
    │ │ ├── __init__.py
    │ │ ├── includes
    │ │ └── pages
    │ │ └── __init__.py
    │ └── www
    └── pyproject.toml
      
    
    
[/code]

  * **library_management:** This directory will contain all the source code for your app

    * **public** : Store static files that will be served from Nginx in production
    * **templates** : Jinja templates used to render web views
    * **www** : Web pages that are served based on their directory path
    * **library_management:** Default Module bootstrapped with app
    * **modules.txt:** List of modules defined in the app
    * **patches.txt** : Patch entries for database migrations
    * **hooks.py** : Hooks used to extend or intercept standard functionality provided by the framework
    * **pyproject.toml:** Specifies how your app is built, you can optionally add 3rd party Python dependencies here which will get installed when your app is installed.



Next: [Create a Site](create-a-site.md)

[ Previous Page Install and Setup Bench  ](install-and-setup-bench.md) [ Next Page Create a Site ](create-a-site.md)

Last updated 2 months ago 

Was this helpful?
