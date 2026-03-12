# Dynamic Pages

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12dcuc01a2)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Dynamic Pages 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12dcuc01a2)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

You can render pages dynamically using Jinja templating language. To query data, you can update that `context` object that you pass to the template.

This can be done by adding a `.py` file with the same filename (e.g. `index.py` for `index.md`) with a `get_context` method.

### Example

If you want to show a page to see users, make a `users.html` and `users.py` file in the `www/` folder.

In `users.py`:
[code] 
    import frappe
    def get_context(context):
     context.users = frappe.get_list("User", fields=["first_name", "last_name"])
    
[/code]

In `users.html`:
[code] 
    ### List of Users
    
    
    
    {% for user in users %}
     2. {{ user.first_name }} {{ user.get("last_name", "") }}
    
    {% endfor %}
    
    
    
[/code]

[ Previous Page Table of Contents  ](table-of-contents.md) [ Next Page Portal Roles  ](portal-roles.md)

Last updated 2 months ago 

Was this helpful?
