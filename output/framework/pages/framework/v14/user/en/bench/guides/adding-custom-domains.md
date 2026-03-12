# Adding Custom Domains to your Site

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/132r2ge38h)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Adding Custom Domains to your Site 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/132r2ge38h)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

You can add **multiple custom domains** for your site, just run:

bench setup add-domain [desired-domain]

On running the command you will be asked for which site you want to set the custom domain for.

You can also setup SSL for your custom domain by using the options:

\--ssl-certificate [path-to-certificate] \--ssl-certificate-key [path-to-certificate-key]

Example:

bench setup add-domain custom.erpnext.com --ssl-certificate /etc/letsencrypt/live/erpnext.cert --ssl-certificate-key /etc/letsencrypt/live/erpnext.key

Domain configuration is stored in the respective site's site_config.json

"domains": [ { "ssl_certificate": "/etc/letsencrypt/live/erpnext.cert", "domain": "erpnext.com", "ssl_certificate_key": "/etc/letsencrypt/live/erpnext.key" } ],

**You will need to regenerate the nginx configuration by runnning`bench setup nginx` and reload the nginx service by running `sudo service nginx reload` to put your custom domain in effect**

[ Previous Page bench trim-tables  ](../reference/trim-tables.md) [ Next Page Configuring HTTPS  ](configuring-https.md)

Last updated 2 months ago 

Was this helpful?
