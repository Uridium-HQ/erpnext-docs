# bench uninstall-app

[ Edit ](</wiki/spaces/r3uvq1ch61/page/131pfcoj76>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench uninstall-app 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/131pfcoj76>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench uninstall-app [OPTIONS] APP
    
[/code]

## Description

Remove Application and linked doctypes, modules from the site. Executing the vanilla command will check if the app exists on site before attempting to delete its modules and doctypes. The application may not be necessarily installed on the bench to run the `uninstall-app` command.

## Flags

  * `-y`, `--yes` To bypass confirmation prompt for uninstalling the app
  * `--dry-run` List all doctypes that will be deleted
  * `--no-backup` Do not backup the site
  * `--force` Force remove the app from site



## Examples

  1. Perform a dry run to see what would happen on running it on a particular site.


[code] 
    bench --site {site} uninstall-app {app} --dry-run
    
[/code]

  1. Don't take a backup before the application uninstall operation.


[code] 
    bench --site {site} uninstall-app {app} --no-backup
    
[/code]

  1. Use force to uninstall application from site.


[code] 
    bench --site {site} uninstall-app {app} --force
    
[/code]

  2. Skip the interactive prompt for confirmation of uninstall.


[code] 
    bench --site {site} uninstall-app {app} --yes
    
[/code]

[ Previous Page bench list-apps  ](</framework/v14/user/en/bench/reference/list-apps>) [ Next Page bench show-config ](</framework/v14/user/en/bench/reference/show-config>)

Last updated 2 months ago 

Was this helpful?
