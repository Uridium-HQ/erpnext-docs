# Applying a Discount

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0so7qc34g3)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Applying a Discount 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0so7qc34g3)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

There are several ways to apply a Discount on an item in a sales transactions. This can be done in all sales and purchase transactions.

## 1\. Discount on Price List Rate of an item

You can find the Discount field in the Item table of a transaction, click on the downward arrow at the righ-hand side of a row. A Discount can be applied as a percentage or a fixed amount related to the Price List Rate of the Item.

![Discount on Price List Rate](https://docs.frappe.io/assets/da65c47e01c8.png)

The feature of Discount (%) is available in all sales and purchase transactions.

If you want to apply a discount (as a Percentage) regularly for certain quantities you'd rather use a "Pricing Rule". Read [Pricing Rule](pricing-rule.md) documentation to learn more.

## 2\. Discount on Net Total or Grand Total

In the "Additional Discount" section (of a "Sales Order" or "Sales Invoice" alike), you can apply a Discount as a fixed amount or a percentage on the total sum of the Sales.

![Additional Discount](https://docs.frappe.io/assets/e87c947c9a67.png)

### 2.1 Discount on "Net Total"

If a Discount is applied on **Net Total** , then item's Net Rate and Net Amount is calculated as per the Discount Amount. Net Rate and Amount field will be visible only if Discount is applied using this feature.

![Discount on Net Total](https://docs.frappe.io/assets/b3c4f501f92d.png)

### 2.2 Discount on "Grand Total"

If a Discount is applied based on the **Grand Total** , then with item's Net Rate, Net Amount as well as taxes are also re-calculated as per Discount Amount.

![Discount on Grand Total](https://docs.frappe.io/assets/8d5147491e66.png)

[ Previous Page Request for Raw Materials from Sales Order  ](request-for-raw-materials-from-sales-order.md) [ Next Page Amending Sales Order after Submit  ](amending-sales-order-after-submit.md)

Last updated 1 week ago 

Was this helpful?
