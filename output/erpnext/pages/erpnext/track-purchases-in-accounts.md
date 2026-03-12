# Track Purchases In Accounts

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rrjrmr4jm>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Track Purchases In Accounts

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rrjrmr4jm>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

As per the industry standards, following formula is used for driving Cost of Goods Sold:

Users can easily find the stock opening and closing balances by referring to the stock balance report, but determining the purchases is more difficult. The account Stock Received but Not Billed can help, but it doesn’t work if the user is using Purchase Invoices with ‘Update Stock’.

To address this in the ERPNext, we have Purchase Expense Account and Purchase Expense Contra Account fields in the Company and Item Defaults masters. So now, when the user books the purchase receipt and purchase invoice expense account and its contra will get debited and credited with the same amount, which means the final impact is zero, but the user will be able to see the purchase amount in P&L and Trial Balance reports.

### Company Master Configuration

Users can configure the default purchase expense and default purchase expense contra account in the company master

![](/files/purchase-expense-accounts.png)

[ Previous Page Delivery Trip  ](</erpnext/delivery-trip>) [ Next Page Landed Cost Voucher ](</erpnext/stock-transactions-landed-cost-voucher>)

Last updated 2 weeks ago 

Was this helpful?
