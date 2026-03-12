# Cost Center

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rqmpa3fc4>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Cost Center 

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rqmpa3fc4>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**A Cost Center is a part of an organization where costs or income can be charged.**

In ERPNext you can use the Cost Center as a Profit Center.

Your Chart of Accounts is mainly designed to provide reports to the government and tax authorities.

Most businesses have multiple activities like different product lines, market segments, areas of business, etc that share some common overheads. They should ideally have their own structure to report whether they are profitable or not. For this purpose, there is an alternate structure called the Chart of Cost Centers.

A Cost Center acts like an [Accounting Dimension](</erpnext/accounting-dimensions>) which helps you track costing based on particular areas.

The Cost Center can be set at these levels:

  * Company
  * Item
  * Order/Invoice



The Cost Center can be linked to the following transactions:

  1. [Sales Invoice](</erpnext/sales-invoice>)
  2. [Purchase Invoice](</erpnext/purchase-invoice>)
  3. [Journal Entry](</erpnext/journal-entry>)
  4. [Payment Entry](</erpnext/payment-entry>)
  5. [Delivery Note](</erpnext/delivery-note>)



And other transactions which can be used for budgeting. You can also use Cost Center for [Budgeting](</erpnext/budget>).

## 1\. Cost Center tree

You can create a tree of Cost Centers to represent your business better. Each Income / Expense entry is also tagged against a Cost Center. If 'Allow Cost Center In Entry of Balance Sheet Account' is checked under Account Settings, the system will allow a User to tag entry in Balance Sheet Accounts against a Cost Center.

For example, if you have two types of sales:

  * Walk-in Sales
  * Online Sales



You may not have shipping expenses for your walk-in customers, and no shop- rent for your online customers. If you want to get the profitability of each of these separately, you should create the two as Cost Centers and mark all sales with either "Walk-in" or "Online" Cost Center. Mark all your purchases in the same way.

Thus when you do your analysis you get a better understanding as to which side of your business is doing better. Since ERPNext has an option to add multiple Companies, you can create Cost Centers for each Company and manage them separately.

To access the Chart of Cost Centers, go to:

> Home > Accounting > Budget and Cost Center > Chart of Cost Centers

## 2\. How to set up Chart of Cost Centers

  1. Go to the Chart of Cost Centers.
  2. Add region-wise nodes.
  3. Add other nodes as per your needs.



Selecting a different Company will display the Cost Centers for that Company.

![Cost Center](/files/chart-of-cost-center.png)

![Chart of Cost Centers](/files/company-master.png)

### 3\. Related Topics

  1. [Budgeting](</erpnext/budget>)
  2. [Sales Invoice](</erpnext/sales-invoice>)
  3. [Purchase Invoice](</erpnext/purchase-invoice>)



[ Previous Page Exchange Rate Revaluation ](</erpnext/exchange-rate-revaluation>) [ Next Page Cost Center Allocation ](</erpnext/cost_center_allocation>)

Last updated 2 weeks ago 

Was this helpful?
