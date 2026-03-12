# bench list-apps

[ Edit ](</wiki/spaces/r3uvq1ch61/page/131m41k1tk>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench list-apps 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/131m41k1tk>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench list-apps [OPTIONS]
    
[/code]

## Description

List all the Frappe Applications installed on the specified site. The information shown by the command is fetched from the **Installed Applications** DocType which tracks the latest version of the apps, the site was migrated to. The global default `installed_apps` is used as fallback.

Multi-site support has been added in Version 13. To see the summary for all sites, run the command with site's value as `all`.

## Options

  * `--format`, `-f` Choose the format for listing apps installed on the specified site, options being "text" and "json". Default is "json".



### Examples

  1. List apps installed on all sites.


[code] 
    bench --site all list-apps
    
[/code]

  1. List apps installed on all sites in parsable JSON format.


[code] 
    bench --site all list-apps --format json
    
[/code]

  1. List apps installed on a specific site in text format.


[code] 
    bench --site {site} list-apps --format text
    
[/code]
[code] 
    bench --site {site} list-apps -f text
    
[/code]
[code] 
    bench --site {site} list-apps
    
[/code]

[ Previous Page bench reinstall  ](</framework/v14/user/en/bench/reference/reinstall>) [ Next Page bench uninstall-app  ](</framework/v14/user/en/bench/reference/uninstall-app>)

Last updated 2 months ago 

Was this helpful?
