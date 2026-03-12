# bench set-config

[ Edit ](</wiki/spaces/r3uvq1ch61/page/13140eee38>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench set-config 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/13140eee38>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench set-config [OPTIONS] KEY VALUE
    
[/code]

## Description

Bench provides a wrapper command to insert or update values in the site config files. You can update values in your site's `site_config.json`, along with the bench directory's `common_site_config.json` through the same command.

To read more about site configuration and understanding key precedence, refer to the docs [here](</framework/v14/user/en/basics/site_config>).

## Flags

  * `-g`, `--global` Set value in the Bench's Common Site Config
  * `-p`, `--parse` Parse given value instead of string. You can use this to set dict and list values. This was `--as-dict` in earlier versions.



## Examples

  1. Enable tests for given site.


[code] 
    bench --site {site} set-config allow_tests true
    
[/code]

  1. Enable tests for all sites.


[code] 
    bench --site all set-config allow_tests true
    
[/code]

Using the above command, each site's `site_config.json` will have the key-value `"allow_tests": true`. This allows running tests on all of the sites.
[code] 
    bench set-config -g allow_tests true
    
[/code]

Using the above command, the bench's `common_site_config.json` will have the key-value `"allow_tests": true`. This will allow each site on the bench to have tests run unless they have a value defined for the sma in their `site_config.json`.

  1. Set a dict value in your site's `frappe.conf`


[code] 
    bench --site {site} set-config backup '{"includes": ["Not", "ToDo"]}' --parse
    
[/code]

You can now access the list in code as `frappe.conf.backup.get("includes")`.

[ Previous Page bench show-config ](</framework/v14/user/en/bench/reference/show-config>) [ Next Page bench restore  ](</framework/v14/user/en/bench/reference/restore>)

Last updated 2 months ago 

Was this helpful?
