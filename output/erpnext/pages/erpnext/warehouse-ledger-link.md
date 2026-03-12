# Linking stock warehouse and accounts

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sgs0ksq67)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Linking stock warehouse and accounts

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sgs0ksq67)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

The value of stock stored in the warehouses needs to be tracked.

Each warehouse is linked to a ledger in chart of accounts through the 'Account' field in the warehouse.

![Stock Asset Ledger in Warehouse](https://docs.frappe.io/assets/41ffe84ef4e3.png)

If the Account field is empty in a warehouse, then the Account mentioned in the parent of that warehouse is considered. If an Account could not be determined by tracing the hierarchy, then the Default Inventory Account mentioned in the Company record is considered.

![Default Inventory Account in Company](https://docs.frappe.io/assets/231816628ae2.png)

When a company is created, a ledger named 'Stock In Hand' is created by default in Chart of Accounts.

**Chart of Accounts > Assets > Current Assets > Stock Assets > Stock In Hand.**

If required, you can create additional ledgers under 'Stock Assets' group.

![Stock Asset Ledger in Chart of Accounts](https://docs.frappe.io/assets/acb2fa5e9ff8.png)

[ Previous Page Stock Balance and Stock Account Balance Syncing ](stock-balance-and-stock-account-balance-not-in-sync.md) [ Next Page Allow Over Delivery/Billing  ](allow-over-delivery-billing-against-sales-order-upto-certain-limit.md)

Last updated 1 week ago 

Was this helpful?
