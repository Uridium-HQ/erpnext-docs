# Purchase Invoice - Account Type Error

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sk3juute1)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Purchase Invoice - Account Type Error 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sk3juute1)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Question:** On saving the Purchase Invoice, I am getting a validation message that Credit To Account must be a Balance Sheet account.

![Credit To Account in Purchase Invoice](https://docs.frappe.io/assets/47eae35613b5.png)

**Answer: **On submission of a Purchase Invoice, payable is updated towards the Supplier. As per the accounting standards, Payable Account is aligned under Current Liability (credit side of Balance Sheet).

The error message indicates that Account selected in the Credit To field doesn't belong to the Liability Group. Please ensure that Payable Account selected in the Purchase Invoice is located under Liability group.

[ Previous Page Closing Accounting Books in ERPNext in v15 ](https://docs.frappe.io/erpnext/closing-accounting-books-in-erpnext) [ Next Page Fixing Fiscal Year Error ](fiscal-year-error.md)

Last updated 1 week ago 

Was this helpful?
