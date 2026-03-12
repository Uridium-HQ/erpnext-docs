# Redirects

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12dsor0uf7>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Redirects 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12dsor0uf7>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

You can add redirects by adding the `website_redirects` hook.

### Examples
[code] 
    website_redirects = [
     # absolute location
     {"source": "/from", "target": "https://mysite/from"},
    
     # relative location
     {"source": "/from", "target": "/main"},
    
     # use regex
     {"source": "/from/(.*)", "target": "/main/\1"}
    ]
    
[/code]

[ Previous Page Generators  ](</framework/v14/user/en/guides/portal-development/generators>) [ Next Page Using the Data Migration Tool  ](</framework/v14/user/en/guides/data/using-data-migration-tool>)

Last updated 2 months ago 

Was this helpful?
