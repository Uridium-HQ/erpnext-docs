# How to Enable Developer Mode in Frappe

[ Edit ](</wiki/spaces/r3uvq1ch61/page/129v4kb08d>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# How to Enable Developer Mode in Frappe

[ Edit ](</wiki/spaces/r3uvq1ch61/page/129v4kb08d>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

When you are in application design mode and you want the changes in your DocTypes, Reports etc to affect the app repository, you must be in **Developer Mode**.

To enable developer mode, update the `site_config.json` file of your site in the sites folder:
[code] 
    frappe-bench/sites/{your site}/site_config.json
    
[/code]

Inside the `frappe-bench` folder, run
[code] 
    bench set-config -g developer_mode 1
    
[/code]

OR, manually, write `"developer_mode": 1` inside the `{ .. }` of `site_config.json`
[code] 
    {
      "developer_mode": 1,
      ...
    }
    
[/code]

After setting developer mode, clear the cache:
[code] 
    bench --site {your site} clear-cache
    
[/code]

Some apps might require additional dependencies to build and test in development mode. Install them using bench:
[code] 
    bench setup requirements --dev
    
[/code]

To view the full developer options, you must be logged in as the "Administrator" user. You also will need to enable the Developer icon in your desktop settings:
[code] 
    Desk -> User dropdown list -> Set Desktop Icons -> check "Developer"
    
[/code]

[ Previous Page Using Html Templates In Javascript  ](</framework/v14/user/en/guides/app-development/using-html-templates-in-javascript>) [ Next Page Fetch a Field Value from a Document into a Transaction  ](</framework/v14/user/en/guides/app-development/fetch-custom-field-value-from-master-to-all-related-transactions>)

Last updated 2 months ago 

Was this helpful?
