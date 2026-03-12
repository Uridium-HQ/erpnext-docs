# Adding Module Icons On Desktop

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12apsb77hl>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Adding Module Icons On Desktop 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12apsb77hl>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

> Frappe version 12

To create an icon for your app, you have to edit your app's `config/desktop.py`. In this file you can add a `get_data` method returns a dictionary with the module icon parameters.

You can also create a dropdown list of actions available on this module and actions available on the page when you click on this module. To achieve this, create a file `config/MODULE_NAME.py` (replace `MODULE_NAME` with the name of one of your app's modules).

## Example App Library Management

`config/desktop.py`:
[code] 
    def get_data():
     return [
     {
     "module_name": "Library Management",
     "category": "Modules",
     "label": _("Library Management"),
     "color": "#589494",
     "icon": "octicon octicon-book",
     "type": "module",
     "description": "Library management"
     }
     ]
    
[/code]

`config/library_management.py`:
[code] 
    def get_data():
     return [
     {
     "label": _("Library Management"),
     "icon": "octicon octicon-book",
     "items": [
     {
     "type": "doctype",
     "name": "Article",
     "label": _("Article"),
     "description": _("Manage Books"),
     "onboard": 1,
     },
     {
     "type": "doctype",
     "name": "Library Member",
     "label": _("Library Member"),
     "description": _("Manage Members"),
     # Not displayed on dropdown list action but on page after click on module
     "onboard": 0,
     }
     ]
     }
     ]
    
[/code]

Note: Module views are visible based on permissions.

[ Previous Page Fetch a Field Value from a Document into a Transaction  ](</framework/v14/user/en/guides/app-development/fetch-custom-field-value-from-master-to-all-related-transactions>) [ Next Page Single Type Doctype  ](</framework/v14/user/en/guides/app-development/single-type-doctype>)

Last updated 2 months ago 

Was this helpful?
