# Drop Ship Between Subsidiary Companies

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sjvq8th3j)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Drop Ship Between Subsidiary Companies

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sjvq8th3j)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Scenario:**

Our Business has 2 sister companies where SAS is handling clients and sales orders and BV is handling stock, purchases but also some local clients.

Using ERPNext we wish to implement the following workflow.

  1. Client contacts SAS
  2. SAS generates a Sales order
  3. SAS turns the SO into a Purchase order for BV
  4. BV receives PO > SO from SAS
  5. BV Fulfils order from Stock to end-client
  6. BV Invoices SAS
  7. SAS pays to BV
  8. SAS invoices end- client and bills



**Answer:**

You can manage this scenario by using Drop Shipping feature of ERPNext. Check following link to learn how it functions in ERPNext.

[Drop Shipping](drop-shipping-in-erpnext.md)

**Steps:**

  1. For the SAS Company, create a Sales Order for the Customer. Ensure to check "Drop Shipping" for the item.
  2. For the Company SAS, add BV as a Supplier
  3. Create a Purchase Order (PO) against a Sales Order. In PO, select BV as a Supplier. But shipping address will be the client's address.
  4. SAS will create a Purchase Invoice, as they are liable to pay to BV.
  5. Against the original Sales Order, SAS will create a Sales Invoice for Customer, and create Payment Entry later.
  6. The company BV will add SAS as their Customer. They can create a Sales Order to book income in their accounts. Make Delivery Note for the Customer. Make Sales Invoice for SAS.



[ Previous Page Change the Rate of Items in the Sales Cycle ](need-to-change-rate-of-items-during-sales-cycle.md) [ Next Page Request for Raw Materials from Sales Order  ](request-for-raw-materials-from-sales-order.md)

Last updated 1 week ago 

Was this helpful?
