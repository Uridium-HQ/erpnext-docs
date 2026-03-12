# Production Scrap Management

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sqfj1kqfg)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Production Scrap Management 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0sqfj1kqfg)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Scrap means waste that either has no economic value or only the value of its basic material content recoverable through recycling.

Scrap is generally availed at the end of the manufacture process. Also you can find some products that are damaged or that are unusable due to expiry or for some other reason, which needs to be scraped.

In ERPNext, at the end of manufacturing process, scrap items are accounted in the scrap warehouses.

## Scrap in Bill of Materials

You can update estimated scrap quantity of an item in the BOM, Scrap table. If required, you can reselect a raw-material item as scrap.

![Scrap in BOM](https://docs.frappe.io/assets/8421e68b24c6.png)

## Scrap in Manufacture Entry

When production is completed, Finish / Manufacture Entry is created against a Production Order. In this entry, scrap item is fetched in the Item table, with only Target Warehouse updated for it. Ensure that Valuation Rate is updated for this item for the accounts posting purposes.

![Scrap in Manufacture Entry](https://docs.frappe.io/assets/261bf9c1910b.gif)

> Scrap from the BOM will only work if Manufacture Entry is created based on BOM, and not based on Material Transfer. This is configurable from Manufacturing Settings.

![Manufacturing Settings](https://docs.frappe.io/assets/caae9b4f92d2.png)

[ Previous Page Customer Provided Items  ](customer-provided-items.md) [ Next Page Manufacturing Settings ](manufacturing-settings.md)

Last updated 1 week ago 

Was this helpful?
