# bench migrate

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/130rmmpdhn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench migrate 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/130rmmpdhn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench migrate [OPTIONS]
    
[/code]

## Description

The migrate command updates the site's state to the current available apps. It performs a range of tasks, in order:

  * Run `before_migrate` Hooks
  * Run Application Patches
  * Synchronize Database Schema and Background Jobs
  * Synchronize Fixtures
  * Synchronize Dashboards, Desktop Icons and Web Pages
  * Updates Translations
  * Rebuild Search Index for all routes
  * Run `after_migrate` Hooks



This operation also updates the `touched_tables.json` file for the respective file and updates the App Versions in the "Installed Applications" DocType.

## Flags

  * `--skip-failing` Skip patches that fail to run
  * `--skip-search-index` Skip search indexing for web documents



## Examples

  1. Run migrations on an existing site.


[code] 
    bench --site {site} migrate
    
[/code]

  1. Run migrations skipping rebuilding search index for web documents


[code] 
    bench --site {site} migrate --skip-search-index
    
[/code]

  2. Run migrations skipping any failing patches.


[code] 
    bench --site {site} migrate --skip-failing
    
[/code]

> Note: Skipping failing patches is not recommended for production use

[ Previous Page bench drop-site  ](drop-site.md) [ Next Page bench backup  ](backup.md)

Last updated 2 months ago 

Was this helpful?
