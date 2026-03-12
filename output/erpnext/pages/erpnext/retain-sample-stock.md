# Retaining Sample Stock

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rsqv0duqe)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Retaining Sample Stock 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rsqv0duqe)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Sample stock is a batch of any Items stored for analyzing should the need arise later.**

The Item for which sample stock is stored can be raw material, packaging material, or finished product.

## 1\. Prerequisites

Before using sample retention, it is advised that you create the following first:

  * [Item](item.md)
  * [Batch](batch.md)
  * [Warehouse](warehouse.md)



## 1\. How to Set Sample Retention Warehouse in Stock Settings

It is advised to create a new Warehouse separately for retaining samples and not use it in production.

![Sample Retention Warehouse](https://docs.frappe.io/assets/33c464a0b7ba.png)

### 1.2 Enable Retain Sample in Item master

Retain Sample is based on Batch hence Has Batch No should be enabled first. Check Retain Sample and set the Maximum allowed samples for a batch.

![Retain Sample](https://docs.frappe.io/assets/9fe3fc865ab5.png)

### 1.3 Make Stock Entry

  * Whenever a [Stock Entry](stock-entry.md) is created with the purpose as Material Receipt, for items which have Retain Sample enabled, the Sample Quantity can be set during that Stock Entry. You need to select the Batch Number for the Item/Items. Sample quantity cannot be more than the Maximum sample quantity set in Item Master.



![Retain Sample](https://docs.frappe.io/assets/4640e8cd3e7d.png)

  * On submission of this Stock Entry, button 'Make Retention Stock Entry' will be available to make another Stock Entry for the transfer of sample items from the mentioned batch to the retention warehouse set in Stock Settings.



![Sample Retention Button](https://docs.frappe.io/assets/7280ed1b253f.png)

  * Clicking this button will direct you to new Stock Entry of type 'Material Transfer'. This entry is transfering your sample retention from your Target Warehouse (Stores) to the Sample Retention Warehouse. It will contain all the information, verify and click Submit.



![Retain Sample](https://docs.frappe.io/assets/79d18515b6ef.png)

### 2\. Related Topics

  1. [Warehouse](warehouse.md)



[ Previous Page Managing Batch wise Inventory  ](managing-batch-wise-inventory.md) [ Next Page Auto Creation of Material Request ](auto-creation-of-material-request.md)

Last updated 2 weeks ago 

Was this helpful?
