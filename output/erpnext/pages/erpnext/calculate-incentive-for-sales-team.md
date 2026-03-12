# Calculate Incentive For Sales Team

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rhjcr8oka)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Calculate Incentive For Sales Team 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rhjcr8oka)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

You can Calculate Incentives for sales team using custom scripts.

Can be used in any Sales Transaction with **Sales Team** Table:

cur_frm.cscript.custom_validate = function(doc) { // calculate incentives for each person on the deal total_incentive = 0 $.each(wn.model.get("Sales Team", {parent:doc.name}), function(i, d) {

// calculate incentive var incentive_percent = 2; if(doc.grand_total > 400) incentive_percent = 4;

// actual incentive d.incentives = flt(doc.grand_total) * incentive_percent / 100; total_incentive += flt(d.incentives) });

doc.total_incentive = total_incentive; }

[ Previous Page Sales Person  ](sales-person.md) [ Next Page Promotional Scheme  ](promotional-scheme.md)

Last updated 2 weeks ago 

Was this helpful?
