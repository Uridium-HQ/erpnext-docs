# bench trim-database

[ Edit ](</wiki/spaces/r3uvq1ch61/page/132uqgs8m9>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench trim-database 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/132uqgs8m9>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench trim-database [OPTIONS]
    
[/code]

## Description

Deleting DocTypes from the list view may not delete their corresponding tables from the database. Migrations may leave ghost tables in your Site Database at times. This may be done for the sake of redundancy, for recovery in case your data is corrupted or lost, or simply, in cases of human error.

This command drops any tables that seem to be remnants like the above mentioned. It will attempt a partial backup of the tables before dropping them. In case, these tables were required, and were dropped errenously, you can restore them in your site's database using the [`partial-restore`](</framework/v14/user/en/bench/reference/partial-restore>) command.

## Options

  * `--format`, `-f` Set output format. Available options are JSON and Table. Defaults to Table.



## Flags

  * `--dry-run` Show what would be deleted.
  * `--no-backup` Do not backup the site prior to the trimming.



### Examples

  1. You want to figure out what data will be deleted if you run this command? Run it with the `--dry-run` flag.


[code] 
    bench --site {site} trim-database --dry-run
    
[/code]

  1. Want to build over this command and need the data to be machine parsable? Set the output `--format` to **json**.


[code] 
    bench --site {site} trim-database --format json
    
[/code]

[ Previous Page bench transform-database  ](</framework/v14/user/en/bench/reference/transform-database>) [ Next Page bench trim-tables  ](</framework/v14/user/en/bench/reference/trim-tables>)

Last updated 2 months ago 

Was this helpful?
