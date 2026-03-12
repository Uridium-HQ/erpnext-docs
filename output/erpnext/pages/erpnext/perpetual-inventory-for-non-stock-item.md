# Perpetual Inventory for Non-stock Item

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sifn9reop)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Perpetual Inventory for Non-stock Item

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sifn9reop)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Question:**

We have enabled Perpetual Inventory in the Company master. Still, in some Purchase Invoice, posting if done in the Expense Account.

**Answer:** As per the perpetual inventory, when item is a stock item, then only it's value is booked under Stock-in-hand at the time of Purchase. In this case, the posting in the GL Entry for Purchase Invoice will be as follows.

|  |   
---|---|---  
**Account** | **Debit** | **Credit**  
Creditors |  | 100  
Stock Received but not Billed | 90 |   
Tax | 10 |   
|  |   
  
Perpetual Inventory doesn't apply on the non-stock item, and expense is booked for them as soon as Purchase Invoice is submitted. The posting in General Ledger for in this scenario will look like:

|  |   
---|---|---  
**Account** | **Debit** | **Credit**  
Creditors |  | 100  
COGS / Other Expense Account | 90 |   
Tax | 10 |   
|  |   
  
[ Previous Page Serialised Item Valuation Rate calculation ](how-is-valuation-rate-of-serialised-item-calculated-in-erpnext.md) [ Next Page Material Transfer from Delivery Note and Purchase Receipt  ](material-transfer-from-delivery-note.md)

Last updated 1 week ago 

Was this helpful?
