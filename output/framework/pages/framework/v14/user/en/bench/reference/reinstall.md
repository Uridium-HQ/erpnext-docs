# bench reinstall

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/131lf0u7q7)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench reinstall 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/131lf0u7q7)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench reinstall [OPTIONS]
    
[/code]

## Description

Reinstall a site with the current apps. This will wipe all site data and start afresh. This is considered a destructive operation, hence, contains an interactive confirmation prompt by default.

> Note: This feature only exists for **MariaDB** sites currently. In the future, they may be extended for **PostgreSQL** support as well.

## Options

  * `--admin-password` Administrator Password for reinstalled site
  * `--mariadb-root-username` Root username for MariaDB
  * `--mariadb-root-password` Root password for MariaDB



## Flags

  * `--yes` Skip confirmation for reinstall



## Examples

  1. Reinstall a site skipping the prompts for:


  * Confirmation for operation
  * MariaDB Root Password
  * Administrator Password


[code] 
    bench reinstall {site} --yes
    --mariadb-root-password {db-pass}
    --admin-password {admin-pass}
    
[/code]

  1. Reinstall a site using an alternative user with _DBMS SUPER_ privileges.


[code] 
    bench reinstall
    --mariadb-root-username {db-user}
    --mariadb-root-password {db-pass}
    
[/code]

[ Previous Page bench backup  ](backup.md) [ Next Page bench list-apps  ](list-apps.md)

Last updated 2 months ago 

Was this helpful?
