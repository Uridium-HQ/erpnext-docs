# Payment Terms Template

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rocu9h2ta)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Payment Terms Template

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rocu9h2ta)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Payment Terms Template allow you to club multiple payment terms together and fetch in transactions.**

After creation, the Payment Terms Table can be set to a specific Customer/Supplier. On selecting the Customer/Supplier in a transaction, the Payment Terms Template will be fetched automatically into the transaction.

For example:

If you receive payment in the slab of 30-70, then you can define Payment Term for each slab, i.e. 30% and 70%.

In the Payment Terms Template, you can select all the Payment Terms and define a template which can be easily applied in the sales and purchase transactions.

![Payment Terms Template](https://docs.frappe.io/assets/0aa9abf96558.png)

  1. Prerequisites



* * *

Before creating and using Payment Request, it is advisable to create the following first:

  1. [Payment Terms](payment-terms.md)

  2. How to create a Payment Terms Template




* * *

A Payment Terms Template tells ERPNext how to populate the table in the 'Payment Terms Schedule' section of the sales/purchase document.

You should use it if you have a set of standard Payment Terms or for ease of use.

  1. Go to the Payment Term Template list and click on New.

  2. Enter a name for the template.

  3. Add the created Payment Terms in the table rows.

  4. Make sure that the total Invoice Portion adds up to 100.

  5. Save.

  6. Video




* * *

### 4. Term based Payment Allocation 

If 'Allocate Payment Based On Payment Terms' is enabled on a template, Payments made against the Invoice through Create->Payment will have allocation based on the Terms.

  1. Template with 'Allocate Payment Based on Payment Terms' enabled. ![Screenshot 2023-08-01 at 10.30.32 AM](https://docs.frappe.io/assets/0754759b55c6.png)
  2. Invoice made with above template. ![Screenshot 2023-08-01 at 10.32.01 AM](https://docs.frappe.io/assets/eb6fed44a5e9.png)
  3. Payment created against above invoice. ![Screenshot 2023-08-01 at 10.32.31 AM](https://docs.frappe.io/assets/16018e015450.png)



[ Previous Page Payment Terms  ](payment-terms.md) [ Next Page Payment Reconciliation ](payment-reconciliation.md)

Last updated 2 weeks ago 

Was this helpful?
