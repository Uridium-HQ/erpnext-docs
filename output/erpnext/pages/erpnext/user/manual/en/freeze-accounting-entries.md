# Freeze Accounting Entries

[ Edit ](</wiki/spaces/24hrpr6es9/page/0sgl88ti3i>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Freeze Accounting Entries 

[ Edit ](</wiki/spaces/24hrpr6es9/page/0sgl88ti3i>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Introduction

After going live on ERPNext, whether it is your first ERP or accounting software or migrating from another application, then you need to ensure that recording accounting entries posting to periods earlier than your cutover date (cutover date is the first date on which ERPNext is considered the primary application for recording and processing business transactions and processes, respectively) to ensure the integrity of your data. This is controlled by the _Freeze Accounting Entries_ feature in ERPNext. Below is how to use it.

# Freezing Accounting Entries in ERPNext

To freeze accounting entries upto a certain date, follow below given steps:

  1. Go to:  
`Accounting > Accounting Msters > Accounts Settings`

  2. Set Date: set date in the **Accounts Frozen Upto** field.




![Books Closed Through](/files/books-closed-through.png)

Now, the system will not allow to make any accounting entries before set date. If at all someone tries creating entries, system will show error message as below.

![Frozen Date Error](/files/error-message-in-transaction.png)

You can still allow user with certain role to create/edit entries within accounts frozen date. You can set that Role in the Account Settings itself.

![Role Allowed To Close Books](/files/role-allowed-to-close-books.png)

[ Previous Page Freeze an Account ](</erpnext/freeze-account>) [ Next Page Common Receivable Account  ](</erpnext/common-receivable-account>)

Last updated 1 week ago 

Was this helpful?
