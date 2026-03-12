# bench partial-restore

[ Edit ](</wiki/spaces/r3uvq1ch61/page/131224rtbu>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# bench partial-restore 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/131224rtbu>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Usage
[code] 
    bench partial-restore [OPTIONS] SQL_FILE_PATH
    
[/code]

## Description

You may want to restore only specific tables you've backed up to a site. You have likely taken partial backups using the `--only`, `--exclude` options in `bench backup`.

The `partial-restore` command may be used to restore sites using partial backups. The partial backup files may be gzip compressed or plain SQL files. In essence, you can restore anything from SQL files using this command.

## Arguments

  * `SQL_FILE_PATH` Path to the database source file. The path may be relative from the bench directory root, or the sites folder. It may also be an absolute path.



> To learn more about relative and absolute paths, on Wikipedia click [here](<https://en.wikipedia.org/wiki/Path_\(computing>)#Absolute_and_relative_paths).

## Flags

  * `-v`, `--verbose` Add verbosity



## Examples

  1. Restore with partial backups on a site.


[code] 
    bench --site {site} partial-restore -v {/path/to/sql/file}
    
[/code]

[ Previous Page bench restore  ](</framework/v14/user/en/bench/reference/restore>) [ Next Page bench version  ](</framework/v14/user/en/bench/reference/bench-version>)

Last updated 2 months ago 

Was this helpful?
