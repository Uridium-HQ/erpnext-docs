# Stock Entry Purpose

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0spgpcrsah)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Stock Entry Purpose 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0spgpcrsah)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Stock Entry is a stock transaction, which can be used for multiple purposes. Let's learn about each Stock Entry Purpose below.

#### 1.Purpose: Material Issue

Material Issue entry create to issue item(s) from a warehouse. On submission of Material Issue, stock of item is deducted from the Source Warehouse.

Material Issue is generally made for the low value consumable items like office stationary, product consumables etc. Also you can create Material Issue to reconcile serialized and batched item's stock.

![Material Issue](https://docs.frappe.io/assets/d8d7aa06fc0f.png)

#### 2.Purpose: Material Receipt

Material Receipt entry is created to inward stock of item(s) in a warehouse. This type of stock entry can be created for updating opening balance of serialized and batched item. Also items purchased without Purchase Order can be inwarded from Material Receipt entry.

For the stock valuation purpose, provided Item Valuation becomes a mandatory field in the Material Receipt entry.

![Material Receipt](https://docs.frappe.io/assets/39b6f7735170.png)

#### 3.Purpose: Material Transfer

Material Transfer entry is created for the inter-warehouse Material Transfer.

![Material Transfer](https://docs.frappe.io/assets/9e090f714ae2.png)

#### 4.Purpose: Material Transfer for Manufacture

In the manufacturing process, raw-materials are issued from the stores to the production department (generally WIP warehouse). This Material Transfer entry is created from Work Order. Items in this entry are fetched from the BOM of production Item, as selected in Work Order.

![Transfer for Manufacture](https://docs.frappe.io/assets/5b5dc4b7fd74.gif)

#### 5.Purpose: Manufacture

Manufacture is created from Work Order. In this entry, both raw-material item as well as production item are fetched from the BOM, selected in the Work Order. For the raw-material items, only Source Warehouse (generally WIP warehouse) is mentioned. For the production item, only target warehouse as mentioned in the Work Order is updated. On submission, stock of raw-material items are deducted from Source Warehouse, which indicates that raw-material items were consumed in the manufacturing process. Production Item is added to the Target Warehouse marking the completion of production cycle.

![Manufacture](https://docs.frappe.io/assets/487b8ed52dae.gif)

#### 6.Purpose: Repack

Repack Entry is created when items purchases in bulk is repacked under smaller packs. [Check this page to know more about Repack entry.](../../../repack-entry.md)

#### 7.Purpose: Subcontract

Subcontracting transaction involves company transfer raw-material items to the sub-contractors warehouse. This requires adding a warehouse for the sub-contractor as well. Sub-contract entry transfers stock from the companies warehouse to the sub-contractors warehouse. [Check this page to know more about Subcontracting](../../../subcontracting.md).

![Subcontract](https://docs.frappe.io/assets/68bc1d7b7535.gif)

[ Previous Page Opening Stock Balance Entry for Serialized and Batch Item  ](../../../opening-stock-balance-entry-for-serialized-and-batch-item.md) [ Next Page Repack Entry  ](../../../repack-entry.md)

Last updated 2 hours ago 

Was this helpful?
