# Close Sales Order

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sof25ta3m)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Close Sales Order 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sof25ta3m)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

In the submitted Sales Orders, you will find **Stop** option. Stopping Sales Order will restrict user from creating Delivery Note and Sales Invoice against it.

![Close Option in Sales Order](https://docs.frappe.io/assets/56f9d4d85fa8.png)

####Scenario

An order is received for ten Wind Turbines. Sales Order is also created for ten units. Due to scarcity of stock, only seven units are delivered to the customer. Pending three units are to be delivered soon. Customer informs that they don't need to deliver pending item, as they have purchased it from other vendor.

In this case, create Delivery Note and Sales Invoice will be created only for the seven units. And the Sales Order should be set as stopped.

![Closed Sales Order](https://docs.frappe.io/assets/b4bc30f6e8a5.png)

Once Sales Order is set as stopped, you will not have pending quantities (three in this case) reflecting in Pending to Deliver and Pending to Invoice reports. To make further transactions against Stopped Sales Order, you should first Unstop it.

You will find same funtionality in the Purchase Order as well.

[ Previous Page Amending Sales Order after Submit  ](amending-sales-order-after-submit.md) [ Next Page Short Close Multiple Orders ](https://docs.frappe.io/erpnext/how-to-short-close-multiple-orders-in-erpnext)

Last updated 1 week ago 

Was this helpful?
