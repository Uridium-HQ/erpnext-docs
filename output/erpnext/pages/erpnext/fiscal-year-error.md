# Fixing Fiscal Year Error

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0skkor8308)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Fixing Fiscal Year Error

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0skkor8308)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

While creating any entry, system validates if dates (like Posting Date, Transaction Date etc.) belong to Fiscal Year selected. If not, system throws an error message saying:

`Date ##-##-#### not in fiscal year`

You are more likely to receive this error message if your Fiscal Year has changes, but new Fiscal Year still not set a default. To ensure new Fiscal Year is auto updated in the transactions, you should setup your master as instructed below.

#### Create New Fiscal Year

Only User with System Manager's Role Assigned has permission to create new Fiscal Year. To create new Fiscal Year, go to:

`Accounting > Accounting Masters > Fiscal Year`

Read [Fiscal Year](fiscal-year.md) to learn more.

#### Set Fiscal Year as Default

After Fiscal Year is saved, you will find option to set that Fiscal year as Default.

![Set Fiscal Year as Default](https://docs.frappe.io/assets/6a9f21400ab1.png)

Default Fiscal Year will be updated in the Global Default setting as well. You can manually update Default Fiscal Year from:

`Settings > Core > Global Default`

![Current Fiscal Year Setting in Global Defaults](https://docs.frappe.io/assets/b17ec02728b2.png)

Save Global Default, and Reload your ERPNext account. Then, default Fiscal Year will be auto-updated in your transactions.

Note: In transactions, you can manually select required Fiscal Year, from More Info section.

[ Previous Page Purchase Invoice - Account Type Error  ](purchase-invoice-account-type-error.md) [ Next Page Round off Account Validation Message ](round-off-account-validation.md)

Last updated 1 week ago 

Was this helpful?
