# POS Invoice Consolidation

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/5cv3afh71u)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# POS Invoice Consolidation

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/5cv3afh71u)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

In the version 13 refactor of the Point of Sale, in an effort to add speed to the Point of Sale, the sales from the POS session do not affect the stock and accounting ledgers until a Closing POS Voucher is submitted for that session. It functions like so:

  1. Each transaction from the POS screen now creates an intermediate invoice (called a POS Invoice) which doesn’t update the stock and accounting ledgers to keep it as fast as possible. This is also called a “sub-ledger”. Separating the POS ledger from the General Ledger makes the system a lot more scalable.
  2. The stock and accounting entries are now created at the end of day while closing a POS session by a single sales invoice which merges all the intermediate invoices created throughout the day.
  3. This single consolidated sales invoice only creates 3-4 ledger entries. The older system would create n x 3 ledger entries where ‘n’ is the number of invoices created throughout the day.
  4. Since drastically fewer ledger entries are made, the load on the general ledger is also eased, making it faster.



### How Stock is Tracked Until a POS Session is Closed

While it is true that the Stock Ledger will disclude transactions from any active POS session, the stock levels from this "sub-ledger" update the Stock Projected Quantity Report.

> Stock > Stock Reports > Stock Projected Quantity

![Stock Projected Quantity Report](https://docs.frappe.io/assets/8ca84ab8ab0c.png)

In the above image, the "Actual Qty" column represents the value of the stock ledger. The "Reserved for POS Transactions" represents the "Actual Qty" less what quantities are currently reserved because of active POS sessions that have not yet made entries on the Stock Ledger because the sessions have not been closed. Note also that "Projected Qty" ("Active Qty" less quantities reserved for the POS, production, etc.) adds a quantity of 100 to the first line item because of an order for 100 units that has yet to be received.

Within the Point of Sale, however, quantities on order but not received will not be reflected in the "Available Qty at Warehouse" field in the Item Details view. In the instance below, as there's not enough quantity on-hand, the transaction won't be permitted. This applies to any and all open POS sessions active at any time and is applied globally (as in, the transaction from one session affects the quantities available for all other open sessions).

![Available Quanity at Warehouse](https://docs.frappe.io/assets/63ec5b642183.png)

![Item Unavailable](https://docs.frappe.io/assets/643371707beb.png)

[ Previous Page POS Workflows ](https://docs.frappe.io/erpnext/pos-workflows) [ Next Page Loyalty points redemption in POS ](loyalty-points-redemption-in-pos.md)

Last updated 2 weeks ago 

Was this helpful?
