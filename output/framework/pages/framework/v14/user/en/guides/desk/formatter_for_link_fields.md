# Formatter For Link Fields

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12hkmlg709)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Formatter For Link Fields 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12hkmlg709)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

In case where a code and a name is maintained for an entity, (for example for Employee there may be an Employee Code and Employee Name) and we want to show both the ID and name in a link field, we can make a formatter.

#### Example:

frappe.form.link_formatters['Employee'] = function(value, doc) { if(doc.employee_name && doc.employee_name !== value) { return value + ': ' + doc.employee_name; } else { return value; } }

Notes:

  1. Both the primary key (`name) and the descriptive name (e.g. `employee_name`) must be present in the document. The descriptive name field could be hidden
  2. This needs to be loaded before the document is loaded and can be re-used for all forms. You can also add it in `build.json`



[ Previous Page Desk Customization  ](../desk.md) [ Next Page Making Charts  ](making_charts.md)

Last updated 2 months ago 

Was this helpful?
