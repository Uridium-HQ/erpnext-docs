# bench show-config

[ Edit ](</wiki/spaces/r3uvq1ch61/page/1313np7o21>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench show-config

[ Edit ](</wiki/spaces/r3uvq1ch61/page/1313np7o21>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench show-config [OPTIONS]
    
[/code]

## Description

The applied configuration for your sites gets applied as a combination of the bench directory's `common_site_config.json` and the site's own `site_config.json`. Bench provides an interface to view the applied `frappe.conf` values for your sites. You may choose to access this information in tabular or JSON formats.

To read more about site configuration and understanding key precedence, refer to the docs [here](</framework/v14/user/en/basics/site_config>).

## Flags

  * `-f`, `--format` Choose the format for listing apps installed on the specified site, options being "text" and "json". Default is "text".



## Examples

  1. Show site config for all sites in JSON format.


[code] 
    bench --site all show-config -f json
    
[/code]

  2. Show the site config in tabular form.


[code] 
    bench --site {site} show-config --format text
    
[/code]
[code] 
    bench --site {site} show-config -f text
    
[/code]
[code] 
    bench --site {site} show-config
    
[/code]

[ Previous Page bench uninstall-app  ](</framework/v14/user/en/bench/reference/uninstall-app>) [ Next Page bench set-config  ](</framework/v14/user/en/bench/reference/set-config>)

Last updated 2 months ago 

Was this helpful?
