# Drop Ship

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rinakirpk)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Drop Ship

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rinakirpk)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Drop shipping** is a supply chain management method in which the retailer does not keep goods in stock but instead transfers the customer orders and shipment details to either the manufacturer, another retailer, or a wholesaler, who then ships the goods directly to the customer.

Drop shipping may also occur when a small retailer (that typically sells in small quantities to the general public) receives a single large order for a product. The retailer may arrange for the goods to be shipped directly to the customer from the manufacturer or distributor. Drop shipping is common with expensive products. No inventory is maintained by the retailer in any case, simply acting as a _middleman_. In this article, we will see how ERPNext provides a seamless drop-shipping experience.

Consider a business dealing with Computer Monitors. Now, the retailer has received an order from a customer, ABC Inc. for 1000 DELL 24Inch Monitors.

## **Drop Shipping In Action:**

### **Item Configuration**

  * Setup Item with mandatory information keeping Maintain Stock disabled since there will be no stocking of this Item.
  * Next, **enable** "Delivered By Supplier (Drop Ship)
  * Set the Supplier with whom the Purchase Order will be raised for this orders fulfillment.



![](../../assets/833803702412.png)

### **Sales Cycle:**

  * Create Sales Order with Customer, Item, Qty, Rate, Taxes and so on.



![](../../assets/9c91e8a95f8d.png)

### **Order Fulfillment:**

  * From the Sales Order Document itself, you can create the Purchase Order for this shipment, track delivery, and bill the customer accordingly.



![](../../assets/39254f09d21e.gif)

[ Previous Page Blanket Order ](blanket-order.md) [ Next Page Credit Limit  ](credit-limit.md)

Last updated 2 weeks ago 

Was this helpful?
