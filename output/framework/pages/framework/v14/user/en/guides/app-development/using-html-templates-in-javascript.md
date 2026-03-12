# Using Html Templates In Javascript

[ Edit ](</wiki/spaces/r3uvq1ch61/page/129l3dqjqk>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Using Html Templates In Javascript 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/129l3dqjqk>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Often while building javascript interfaces, there is a need to render DOM as an HTML template. Frappe Framework uses John Resig's Microtemplate script to render HTML templates in the Desk application.

> Note 1: In Frappe we use the Jinja-like `{% raw %}{%{% endraw %}` tags to embed code rather than the standard `<%`

> Note 2: Never use single quotes `'` inside the HTML template.

To render a template,

  1. Create a template `html` file in your app. e.g. `address_list.html`
  2. Add it to `build.json` for your app (you can include it in `frappe.min.js` or your own javascript file).
  3. To render it in your app, use `frappe.render(frappe.templates.address_list, {[context]})`



#### Example Template:

From `erpnext/public/js/templates/address_list.js`

New Address

{% for(var i=0, l=addr_list.length; i [{%= __("Edit") %}](/app/address/{%= addr_list[i].name %})

#### {%= addr_list[i].address_type %}

{% if(addr_list[i].is_primary_address) { %} {%= __("Primary") %}{% } %} {% if(addr_list[i].is_shipping_address) { %} {%= __("Shipping") %}{% } %}

{%= addr_list[i].display %}

{% } %} {% if(!addr_list.length) { %} {%= __("No address added yet.") %}

{% } %}

[ Previous Page How To Create Custom Fields During App Installation  ](</framework/v14/user/en/guides/app-development/how-to-create-custom-fields-during-app-installation>) [ Next Page How to Enable Developer Mode in Frappe ](</framework/v14/user/en/guides/app-development/how-enable-developer-mode-in-frappe>)

Last updated 2 months ago 

Was this helpful?
