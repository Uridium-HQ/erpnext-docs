# Setup Multitenancy

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/133plj3n4u)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Setup Multitenancy 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/133plj3n4u)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Assuming that you've already got your first site running and you've performed the [production deployment steps](setup-production.md), this section explains how to host your second site (and more). Your first site is automatically set as default site. You can change it with the command,

bench use sitename

## Port based multitenancy

You can create a new site and make run it on a different port (while the first one runs on port 80).

  * Switch off DNS based multitenancy (once)



`bench config dns_multitenant off`

  * Create a new site



`bench new-site site2name`

  * Set port



`bench set-nginx-port site2name 82`

  * Re generate nginx config



`bench setup nginx`

  * Reload nginx



`sudo service nginx reload`

## DNS based multitenancy

You can name your sites as the hostnames that would resolve to it. Thus, all the sites you add to the bench would run on the same port and will be automatically selected based on the hostname.

To make a new site under DNS based multitenancy, perform the following steps.

  * Switch on DNS based multitenancy (once)



`bench config dns_multitenant on`

  * Create a new site



`bench new-site site2name`

  * Re generate nginx config



`bench setup nginx`

  * Reload nginx



`sudo service nginx reload`

[ Previous Page Setting Limits for your Site  ](settings-limits.md) [ Next Page Setup Production  ](setup-production.md)

Last updated 2 months ago 

Was this helpful?
