# Architecture

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12ibno7vk2>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Architecture 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12ibno7vk2>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe Framework is a full-stack web based framework and it includes all the tools needed to deploy a site into production. Database, caching, background jobs, realtime notifications, etc are all configured when you set up a Frappe site.

Frappe framework is based on Python, so it uses the `virtualenv` to setup isolated environments for multiple Python versions. You can also use it to deploy sites with different Frappe versions.

The following diagram closely resembles the `frappe-bench` directory structure and its interface with different parts of the stack.

![Architecture](/files/architecture.png) _Architecture_

To setup a Frappe based site, you need to first install Bench. If you haven't installed it already, check out the [Installation](</framework/v14/user/en/installation>) page.

You can create a new `frappe-bench` setup by running the following command:
[code] 
    bench init frappe-bench
    
[/code]

This command will do the following:

  1. Create a directory called `frappe-bench` and `frappe-bench/sites`, `frappe-bench/apps` within it.
  2. Setup a python virtual environment under `frappe-bench/env`.
  3. Create a `frappe-bench/config` folder to store redis configuration files.
  4. Download `frappe` app and `pip install` it.
  5. Install node packages.
  6. Build JS/CSS assets.



Each `frappe-bench` setup spawns it owns web, redis and node processes.

[ Previous Page Why Frappe Framework?  ](</framework/v14/user/en/basics/why>) [ Next Page Directory structure  ](</framework/v14/user/en/basics/directory-structure>)

Last updated 2 months ago 

Was this helpful?
