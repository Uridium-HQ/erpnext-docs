# Discount Accounting

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rlleodnvr)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Discount Accounting

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rlleodnvr)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Discount Accounting is used to post additional ledger entries for discounts, under a separate Discount Account. This can be done for:

  1. Discounts applied on individual Items
  2. Additional Discounts applied on all the Items in an invoice



### Steps

  1. Check the _Enable Discount Accounting_ box in the _Accounts Settings_ page. ![Enable Discount Accounting checkbox](https://docs.frappe.io/assets/8aafc5d2c4bb.png)
  2. Create a Sales/Purchase Invoice as usual.
  3. To post ledger entries for discounts applied on individual Items:


  * Expand the row for that Item in the Items table
  * Enter discount in the Discount and Margin section
  * Scroll down to the Accounting Details section and enter the Discount Account ![Discount Account](https://docs.frappe.io/assets/d2ed6e3ecd37.png)


  4. To post ledger entries for Additional Discounts applied on all the Items in an invoice:


  * Go to the Additional Discount Section
  * Enter the Additional Discount Amount/Percentage and the Additional Discount Account ![Additional Discount Account](https://docs.frappe.io/assets/4b2063d86f1a.png)


  5. Save and submit the invoice to create ledger entries as shown below:


  * _For Sales Invoices:_ ![Discount Accounting for Sales Invoices](https://docs.frappe.io/assets/3b857b3749b8.png)

  * _For Purchase Invoices:_ ![Discount Accounting for Purchase Invoices](https://docs.frappe.io/assets/5a7895d69c5a.png)




### Default Discount Account

Additionally, you could enter a Default Discount Account for an Item, which will be fetched automatically while creating the Invoice. The visibility for this field is also dependant on the Enable Discount Accounting checkbox in Accounts Settings.

  1. Open the Item doc.
  2. Go to the Item Defaults table in the _Sales, Purchase, Accounting Defaults_ section.
  3. Expand the row of your choice and enter the Default Discount Account for the Item ![Default Discount Account](https://docs.frappe.io/assets/166225cc074c.png)



[ Previous Page Currency Exchange Settings ](../../../currency-exchange-settings.md) [ Next Page UnReconcile ](https://docs.frappe.io/erpnext/unreconciliation)

Last updated 2 weeks ago 

Was this helpful?
