# Managing Batch wise Inventory

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rsmucv15c)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Managing Batch wise Inventory 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rsmucv15c)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Set of items which has same properties and attributes can be group in a single Batch. For example, pharmaceuticals items are batch, so that it's manufacturing and expiry date can be tracked together.

To maintain batches against an Item you need to mention 'Has Batch No' as yes in the Item Master.

![Batch Item](https://docs.frappe.io/assets/69a8829cb709.png)

You can create a new Batch from:

`Stock > Documents > Batch > New`

Read [Stock batch](../../../batch.md) to learn more.

For the Batch item, updating Batch No. in the stock transactions (Purchase Receipt & Delivery Note) is mandatory.

#### Purchase Receipt

When creating Purchase Receipt, you should create new Batch, or select one of the existing Batch master. One Batch can be associated with one Batch Item.

![Batch in Purchase Receipt](https://docs.frappe.io/assets/fd5fc9df3486.png)

#### Delivery Note

Define Batch in Delivery Note Item table. If Batch item is added under Product Bundle, you can update it's Batch No. in the Packing List table as well.

![Batch in Delivery Note](https://docs.frappe.io/assets/835148bcaf88.png)

#### Batch-wise Stock Balance Report

To check batch-wise stock balance report, go to:

Stock > Standard Reports > Batch-wise Balance History

![Batchwise Stock Balance](https://docs.frappe.io/assets/176d65e59e18.png)

[ Previous Page Inventory Dimension ](../../../inventory_dimension.md) [ Next Page Retaining Sample Stock  ](../../../retain-sample-stock.md)

Last updated 2 weeks ago 

Was this helpful?
