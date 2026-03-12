# Import Large Csv File

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12efkeb47k>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Import Large Csv File 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12efkeb47k>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

To import very large CSV files, you can use the bench utility `import-csv`.

The benefit is that this is not subject to timeouts if you use the web interface.

Here is an example:

bench --site test.erpnext.com import-csv ~/Downloads/Activity_Type.csv

### Help

$ bench import-csv --help Usage: bench import-csv [OPTIONS] PATH

Import CSV using data import tool

Options: \--only-insert Do not overwrite existing records \--submit-after-import Submit document after importing it \--ignore-encoding-errors Ignore encoding errors while coverting to unicode \--help Show this message and exit.

[ Previous Page Using the Data Migration Tool  ](</framework/v14/user/en/guides/data/using-data-migration-tool>) [ Next Page Google GSuite  ](</framework/v14/user/en/guides/integration/google_gsuite>)

Last updated 2 months ago 

Was this helpful?
