# Sales Cycle Integration

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rh8muv7ls>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Sales Cycle Integration

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rh8muv7ls>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Standard whitelisted methods and flows for integrating external order management system and sales cycle using REST API

### 1\. Sales Order

Frappe Framework generates [REST API](<https://frappeframework.com/docs/v14/user/en/api/rest>) for all the DocTypes out of the box. This approach can be used for creating the very first document of the sales cycle. In case you are starting with the Sales Order you can use the standard REST API POST request for generating the Order. An example is shown below, you can include custom fields and other doctype details in the body accordingly.
[code] 
    POST /api/resource/Sales Order
    
    # Body
    {
     "doctype": "Sales Order",
     "customer": "Test Customer",
     "company_address": "Test - Billing",
     "customer_address": "Test-Billing-3",
     "items": [{
     "item_code": "Mobile Display",
     "qty": 10,
     "rate": 2000,
     "delivery_date": "2022-11-06",
     "delivery_warehouse": "Stores - GTPL"
     }]
    }
    
[/code]

### 2\. Delivery Note

In case you are starting with a Delivery Note use the same method as shown above for Sales Order, just replace the doctype key value to **Delivery Note** instead of **Sales Order**. In case you want to make a Delivery Note from a Sales Order use the below endpoint. The `source_name` parameter here is the Sales Order ID.
[code] 
    POST /api/method/erpnext.selling.doctype.sales_order.sales_order.make_delivery_note
    
    # Body
    {"source_name": "SO-2022-00001"}
    
[/code]

The endpoint returns a Delivery Note JSON object as a response with all the pending items in the order to be delivered.

### 3\. Sales Invoice

Again if you are just making a Sales Invoice the best approach will be to use the standard REST API. For this please refer to the example mentioned in the Sales Order section.

For making a Sales Invoice from a Sales Order, use the endpoint mentioned below. The `source_name` parameter here is the Sales Order ID.
[code] 
    POST /api/method/erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice
    
    # Body
    {"source_name": "SO-2022-00001"}
    
[/code]

For making a Sales Invoice from a Delivery Note, use the endpoint mentioned below. The `source_name` parameter here is the Delivery Note ID.
[code] 
    POST /api/method/erpnext.stock.doctype.delivery_note.delivery_note.make_sales_invoice
    
    # Body
    {"source_name": "SO-2022-00001"}
    
    
[/code]

Both the enpoints returns a Sales Invoice JSON object with all the pending items to be billed.

### 4\. Payment against the order or invoice

For generating a Payment Entry against a Sales Order or Invoice use the below endpoint
[code] 
    POST /api/method/erpnext.accounts.doctype.payment_entry.payment_entry.get_payment_entry
    
    # Body
    {
     "dt": "Sales Invoice",
     "dn": "SI-2022-0001",
     "party_amount": 2000, # Pass if the document doesn't have an `outstanding_amount` field (optional parameter)
     "bank_account": "Bank Name - CAB", # Pass is case want to use other than the default one (optional parameter)
     "bank_amount": 2000, # Paid or received amount depending on the type of payment entry (optional parameter)
     "party_type": "Customer", # If payment entry is against party type other than Customer or Supplier (optional parameter)
     "payment_type": "Pay", # Pay or receive (optional parameter)
     
    }
    
[/code]

[ Previous Page Promotional Scheme  ](</erpnext/promotional-scheme>) [ Next Page Sales Reports ](</erpnext/sales-analytics>)

Last updated 2 weeks ago 

Was this helpful?
