# Inter Company Invoices

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rirajkem6>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Inter Company Invoices 

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rirajkem6>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**An Inter Company Journal Invoice is done between organizations that belong to the same group.**

Along with creating Purchase Invoices or Sales Invoices for a single company, you can create inter-linked invoices for multiple companies.

For example, you can create a Purchase Invoice for a company say 'Company ABC', and create a Sales Invoice against this Purchase Invoice for another company say 'Company XYZ' and link them together.

## How to create Inter Company Invoices

### Setting up

  1. Go to: **Accounts > Masters > Customer**.

  2. Select the Customer who you would want to choose for the inter-linked invoice.

  3. Enable the checkbox, **Is Internal Customer** shown as follows: ![](/files/image6c0597.png)

  4. Add the company which the Customer represents in the **Represents Company** field. This the company for which the Sales Invoice will be created.

  5. In the **Allowed To Transact With** table, add the company against which you will be creating a Purchase Invoice.

  6. Now, when you create a Purchase Invoice against company A (customer is from company B, the seller is company A), it'll be linked to the Sales Invoice for company A created using this Internal Customer from company B.

  7. Now, you need to follow a similar procedure for setting up a Supplier for inter-linked invoices.

  8. Go to: **Accounts > Masters > *Select the Supplier***

  9. Tick on Is Internal Supplier.

  10. In the **Represents Company** field, add the company which you added in the table **Allowed To Transact With** for the Customer.

  11. In the table **Allowed To Transact With** for the Supplier, add the company which the Customer represents. This is the company against which you are going to make an inter-linked Purchase Invoice.

  12. Here is a screenshot of the Supplier company to avoid any confusion:




![](/files/image01250f.png)

### Creating the Invoice

  1. Now, create a new Sales Invoice, fill up the fields.
  2. Remember to select the Customer who is an internal customer and company from which he's buying.
  3. Save and Submit the Invoice. Inter company invoice
  4. Before you make an _Inter Company Invoice_ you need to do the following:
  5. The selling and buying price between the companies should be in sync.
  6. Go to **Stock > Price List**, create a new Price List for inter company transactions.
  7. Tick both Selling and Buying in this new Price List.
  8. Go to **Buying > Supplier > *internal supplier***, in the currency and price list section, set the price list to the new one just created.
  9. Do the same for the internal customer, i.e., set the price list to the new one.
  10. Now, you can make an inter company Purchase or Sales Invoice.
  11. Under the **Make** button dropdown, you will find a link **Inter Company Invoice** , on clicking the link, you will be routed to a new Purchase Invoice form page.
  12. Here, the supplier and company will be auto-fetched depending on the company you selected in the Sales Invoice.



> ***Remember**: There can only be a single Internal Supplier or Customer per company.*

  1. Submit the invoice, done! Now, both the invoices are inter-linked. _Also, on canceling any of the invoices, the link will break as well._



> Note: An Inter Company invoice will only affect the accounting ledger and not the stock ledger. This is because the companies belong to the same group of companies.

You can follow the same process to create a Purchase Invoice and then an inter-linked Sales Invoice from the submitted Purchase Invoice.

### Related Topics

  1. Sales Invoice
  2. Purchase Invoice
  3. Inter Company Journal Entry



[ Previous Page Sales Return  ](</erpnext/sales-return>) [ Next Page Sales Person  ](</erpnext/sales-person>)

Last updated 2 weeks ago 

Was this helpful?
