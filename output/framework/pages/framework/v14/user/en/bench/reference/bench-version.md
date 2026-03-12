# bench version

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/132pmsa1ph)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench version 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/132pmsa1ph)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench version [OPTIONS]
    
[/code]

## Description

The `version` command displays compiled info about all the apps installed in the current bench directory. You can choose your preferred output format: plain text, JSON or ASCII table. The `--format plain` option displays version information as plain text, just like `bench version`, but with additional information.
[code] 
    $ bench version --format plain
    erpnext 14.0.3 version-14 (4e88dcf)
    frappe 14.0.1 version-14 (f8ec3d7)
    
[/code]

The `--format json` option displays version information as a formatted JSON string. This is particularly useful if you're building tools over the bench CLI.
[code] 
    $ bench version --format json
    [
     {
     "app": "erpnext",
     "branch": "version-14",
     "commit": "4e88dcf",
     "version": "14.0.3"
     },
     {
     "app": "frappe",
     "branch": "version-14",
     "commit": "ef0a5e9",
     "version": "14.0.1"
     }
    ]
    
[/code]

The `--format table` option displays version information formatted as an ASCII table.
[code] 
    $ bench version --format table
    +-------------------------+------------+------------------------------+---------+
    | App | Version | Branch | Commit |
    +-------------------------+------------+------------------------------+---------+
    | erpnext | 14.0.3 | version-14 | 4e88dcf |
    | frappe | 14.0.1 | version-14 | f8ec3d7 |
    +-------------------------+------------+------------------------------+---------+
    
[/code]

## Options

  * `-f`, `--format` Choose the format for showing versions of the apps installed in the current bench. The available options are "plain", "table", "json", "legacy". This value defaults to "legacy".



## Examples

  1. Get human readable information about the installed apps on current bench, with commit messages.


[code] 
    bench version --format plain
    
[/code]

  1. Get bench version information in `JSON` format.


[code] 
    bench version -f json
    
[/code]

[ Previous Page bench partial-restore  ](partial-restore.md) [ Next Page bench transform-database  ](transform-database.md)

Last updated 2 months ago 

Was this helpful?
