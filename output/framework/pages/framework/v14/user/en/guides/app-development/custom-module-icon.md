# Custom Module Icon

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/129o7l2c51)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Custom Module Icon 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/129o7l2c51)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

If you want to create a custom icon for your module, you will have to create an SVG file for your module and set the path to this file in the `desktop/config.py` of your app.

This icon is loaded via AJAX first time, then it will be rendered.

Example:

from frappe import _

def get_data(): return { "Frappe Apps": { "color": "orange", "icon": "assets/frappe/images/frappe.svg", "label": _("Frappe.io Portal"), "type": "module" } }

> PS: A great place to buy SVG icons for a low cost is the awesome [Noun Project](http://thenounproject.com/)

[ Previous Page Set up a new Connected App  ](connected-app.md) [ Next Page Insert A Document Via Api  ](insert-a-document-via-api.md)

Last updated 2 months ago 

Was this helpful?
