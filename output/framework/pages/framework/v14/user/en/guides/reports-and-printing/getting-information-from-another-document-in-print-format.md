# Getting Information From Another Document In Print Format

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12bjlsth83>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Getting Information From Another Document In Print Format

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12bjlsth83>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

In a print format, you can get data from another document. For example, if you have a field called `sales_order` in Sales Invoice, then you can get the sales order details using `frappe.get_doc`:
[code] 
    {% set sales_order_doc = frappe.get_doc("Sales Order", sales_order) %}
    
    {{ sales_order_doc.customer }}
    
[/code]

[ Previous Page How To Enable Social Logins  ](</framework/v14/user/en/guides/deployment/how-to-enable-social-logins>) [ Next Page Where Do I Find Standard Print Formats  ](</framework/v14/user/en/guides/reports-and-printing/where-do-i-find-standard-print-formats>)

Last updated 2 months ago 

Was this helpful?
