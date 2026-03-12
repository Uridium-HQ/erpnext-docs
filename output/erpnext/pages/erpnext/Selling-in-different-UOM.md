# Selling in Different UoM

[ Edit ](</wiki/spaces/24hrpr6es9/page/0shg3839ro>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Selling in Different UoM

[ Edit ](</wiki/spaces/24hrpr6es9/page/0shg3839ro>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

A sell price unit of measure (UOM) is the UOM with which you price items. You can have multiple sell price UOMs for any inventory item. However, when Customer places, UoM for an item could change.

For example an Item Pen is stocked in Nos, but sold in Box. Hence we will make Sales Order for Pen in Box.

**Step 1:** In the Item master, under Unit of Measure section, you can list all the possible UoM of an item, with its UoM Conversion Factor. Update UoM Conversion Factors In one Box, if you get 10 Nos. of Pen, UoM Conversion Factor would be 10.

![Item Unit of Measure](/files/Item-UOM.png)

**Setp 2:** In the Sale Order, you will find two UoM fields

  1. UoM
  2. Stock UoM



In both the fields, default UoM of an item will be fetched by default. You should edit UoM field, and select Sale UoM (Box in this case). Updating Sales UoM is mainly for the reference of the Customer. In the print format, you will see item quantity in the Sales UoM.

![Sale Order Unit of Measure](/files/Sale-Order-UOM.png)

Based on the Qty and Conversion Factor, qty will be calculated in the Stock UoM of an item. If you sell just one Box, then Qty as per stock UoM will be set as 10.

**Stock Ledger Posting**

Irrespective of the Sales UoM selected in the Sale Order, stock ledger posting will be done in the Default UoM of an item. Hence you should ensure that conversion factor is entered correctly while selling item in different UoM.

![UOM in Stock Ledger](/files/uom-in-stock-ledger.png)

[ Previous Page Setting up "Buy 1 Get 1 Free" Pricing Rule ](</erpnext/setting-up-buy-1-get-1-free-pricing-rule>) [ Next Page Change the Rate of Items in the Sales Cycle ](</erpnext/need-to-change-rate-of-items-during-sales-cycle>)

Last updated 1 week ago 

Was this helpful?
