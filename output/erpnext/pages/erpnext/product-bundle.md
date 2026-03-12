# Product Bundle

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rsajil9kg)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Product Bundle

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rsajil9kg)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**A Product Bundle is a master where you can list existing items which are bundled together and sold as a set (or bundle).**

For instance, when you sell a smartphone, you need to ensure that the charger, cable, and sim ejector pin are delivered with it and stock levels of these items get affected. To address this scenario, you can create a Product Bundle for the main item, i.e. smartphone. Then list deliverable items i.e. smartphone + charger + cable + sim ejector pin as so-called "Child Items".

A Product Bundle can be seen as a "Bill-of-Materials" on the Sales side.

Following are the steps to set up a Product Bundle and using it in sales transactions.

To access product bundle, go to:

> Home > Selling > Items and Pricing > Product Bundle

  1. Prerequisites



* * *

Before creating and using a Product Bundle, it is advised that you create the following first:

  * [Item](item.md)


  2. How to create a Product Bundle



* * *

  1. Go to the Product Bundle list, click on Add Product Bundle.
  2. Select a Parent Item, create one if not already created. Make sure Maintain Stock unchecked when creating a Parent Item. eg: Dinner Set.
  3. Enter a price for the parent item, this will be fetched when making a transaction.
  4. You can enter a description for internal use.
  5. Enter the products to be bundled in the Items table and enter their quantities.
  6. Save.



![Screenshot 2024-08-29 at 11.41.56 AM](https://docs.frappe.io/assets/05ae22f2a72b.png)

### 2.1 Selecting Parent Item

In Product Bundle master, there are two sections. The "Parent Item" and a List of items to be shipped (Child Items).

The "Parent Item" should be seen more like a vessel or virtual item and not a physical product. The "Parent Item" must be a **non-stock item**. To create a **non-stock item** you have to unmark "Maintain Stock" in the Item Form. This is a non-stock item because there is no stock maintained for it but only for the "Child Items".

If you want to maintain stock for the Parent Item, then you must create a regular Bill of Material (BOM) and package them using Stock Entry Transactions.

### 2.2 Selecting Child Items

In the Items table, you have to list all the child items for which we maintain stock and is delivered to customer. Remember: The "Parent Item" is just virtual, so your main product (a smartphone in our example here) also has to be listed on the List of Child (or Package) Items.

  3. Features



* * *

### 3.1 Product Bundle in the Sales Transactions

When making Sales transactions (Sales Invoice, Sales Order, Delivery Note) the Parent Item will be selected in the main item table.

![Screenshot 2024-08-29 at 11.42.41 AM](https://docs.frappe.io/assets/20a1348366ca.png)

On selection of a Parent Item in the main item table, its child items will be fetched in Packing List table of the transaction. If child item is the serialized item, you will be able to specify its Serial No. in packing List table itself. On submission of the transaction, the system will reduce the stock level of child items from warehouse specified in Packing List table.

![Screenshot 2024-08-29 at 11.44.47 AM](https://docs.frappe.io/assets/189ea340ece7.png)

**Use Product Bundle to Manage Offers/Schemes:**  
This was discovered when a customer dealing into nutrition products asked for a feature to manage offers like "Buy One Get One Free".

To manage the same, he created a non-stock item which was used as Parent Item. In description of item, he entered offer details with the item's image displaying the offer. The sellable product was selected in Package Item where qty was two. Hence every time they sold one qty of Parent item under this offer, the system deducted two quantities of product from Warehouse.

### 4\. Related Topics

  1. [Item](item.md)



[ Previous Page Stock Entry ](stock-entry.md) [ Next Page Stock Reconciliation ](stock-reconciliation.md)

Last updated 2 weeks ago 

Was this helpful?
