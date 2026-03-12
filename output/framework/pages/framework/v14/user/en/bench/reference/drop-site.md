# bench drop-site

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/1308s3u2hc)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench drop-site 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/1308s3u2hc)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench drop-site [OPTIONS] SITE
    
[/code]

## Description

Drop an existing site. In this operation, the database is dropped and the respective site's folder is moved from `./sites` to `./archived_sites` _(unless specified otherwise)_ on your Bench. A full site backup is taken prior to this.

## Options

  * `--db-root-username` Username for a DBMS user with drop database privileges. Defaults to _root_
  * `--db-root-password` Password for the DBMS user
  * `--archived-sites-path` Specify the path to move the site's folder in



## Flags

  * `--no-backup` Skip backup prior to site drop
  * `--force` Force drop-site even if an error is encountered



### Examples

  1. Skip the interactive prompt by passing the root password.


[code] 
    bench drop-site {site} --db-root-password {db-root-pass}
    
[/code]

  1. Skip taking a backup before site deletion.


[code] 
    bench drop-site {site} --no-backup
    
[/code]

  1. Move the site's folder in a different folder instead of the standard `./archived_sites`.


[code] 
    bench drop-site {site} --archived-sites-path {path/to/archive}
    
[/code]

[ Previous Page bench new-site  ](new-site.md) [ Next Page bench migrate  ](migrate.md)

Last updated 2 months ago 

Was this helpful?
