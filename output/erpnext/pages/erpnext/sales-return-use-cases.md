# Sales Return Management

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sphk7028q)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Sales Return Management 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sphk7028q)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

In an event of Sales Return, the following adjustment pertaining to stock and accounting can be handled in multiple ways. Let's check what stock and accounts posting would be posted based on the Sales Return adjustment.

### Return Without Payment

If a customer request for the returns even before processing a payment, then you can simply:

  1. Cancel the Sales Invoice.
  2. Create a Sales Return against a Delivery Note



If your statutory laws don't allow you to cancel the Sales Invoice, you can create a Credit Note against a Sales Invoice as well.

### Paid Sales Invoice - Adjustment via Credit Note

This is a scenario where the customer purchased an item from you for which Sales Invoice as submitted, and also paid.

  1. Create a Credit Note against a Sales Invoice.
  2. In the Sales Invoice, check field "Is Paid". Ensure that Payment Account / Mode of Payment is selected in the relevant table.
  3. If you wish to also return items via Sales Invoice itself, check field "Update Stock".
  4. Save and Submit Credit Note.



![Create sales return](https://docs.frappe.io/assets/60b4f2db5ece.png)

As per this entry, the sold items will be accepted back in your Warehouse. Also, the payment received from the Customer will be reversed.

After the Credit Note creation, the Outstanding Balance of Sales Invoice will turn negative. This will give you scope to adjust this Sales Invoice (with a negative balance) to adjust against the future outstanding Sales Invoice.

### Unpaid Sales Invoice - Credit Note

In the case of Sales Return where the customer didn't process any payment, you can simply create a Credit Note. On creation of Credit Note, Outstanding of the Sales Invoice will become negative.

For the Adjustment of stock, you can create a Sales Return against Delivery Note or in the Credit Note itself, check field "Update Stock".

[ Previous Page Sales Persons in the Sales Transactions  ](sales-persons-in-the-sales-transactions.md) [ Next Page Adding Margin  ](adding-margin.md)

Last updated 1 week ago 

Was this helpful?
