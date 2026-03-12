# Tax Rule

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rp21oh739>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Tax Rule 

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rp21oh739>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**A Tax Rule automatically applies taxes to transactions based on preset rules.**

You can define which [Tax Template](</erpnext/setting-up-taxes.html>) must be applied on a Sales / Purchase transaction using Tax Rule. This is decided by various factors like Customer, Customer Group, Supplier, Supplier Group, Item, Item Group or a combination of these.

To access the Tax Rule list, go to:

> Home > Accounting > Taxes > Tax Rule

## 1\. Prerequisites

Before creating and using a Tax Rule, it is advised to create the following first:

  1. [Sales Taxes and Charges Template](</erpnext/sales-taxes-and-charges-template>)



Or

  1. [Purchase Taxes and Charges Template](</erpnext/purchase-taxes-and-charges-template>)



## 2\. How to create a Tax Rule

  1. Go to the Tax Rule list and click on New.
  2. Under Tax Type select whether the tax will be applied at Sales or Purchase.
  3. Select the Tax Template to be applied.
  4. Save. ![Tax Rule](/files/tax-rule.png)



You can list Items online using the Website module. Selecting 'Use for Shopping Cart' will use this Tax Rule for Shopping Cart transactions also. To know more, visit the [Shopping Cart](</erpnext/shopping-cart>) page.

> Note: It is advised to not use the Sales/Purchase Template selected here in [Item Tax Template](</erpnext/item-tax-template>), it may cause interference. If you want to use same tax rates for Tax Rule and Item Tax Template, use a different name for the Sales/Purchase Tax Templates.

## 3\. Features

### 3.1 Auto applying Tax Rule based on Customer/Supplier

Select a Customer/Supplier if tax is to be applied for a specific party. Leave it as All Customer Groups/All Supplier Groups if this Tax Rule is applicable to all Customers/Suppliers.

On selecting a Customer/Supplier their Billing and Shipping addresses will be fetched if saved in the Customer/Supplier master.

### 3.2 Auto applying Tax Rule based on Item / Item Group

On setting an Item or Item group in the Tax Rule, this Tax Rule will automatically be applied to new transactions that have the selected Item/Item Group.

### 3.3 Setting a Tax Category

Setting a Tax Category allows applying multiple Tax Rules to a transaction based on different factors. To know more, visit the [Tax Category](</erpnext/tax-category>) page.

### 3.4 Validity

Set a Start and End Date if the tax is to be applied only for a specified period. Leaving both dates blank will result in the Tax Rule to have no time limits.

### 3.5 Priority

Setting a priority number here will decide on which order a Tax Rule will be applied in case multiple Tax Rules have similar criteria. '1' is the highest priority, '2' has lesser priority and so on.

## 4\. How does Tax Rule Work?

Let us configure Tax Rule so that system automatically applies specific tax rates when a specific condition matches. For example, if the city in the billing address of customer is 'Malibu' then a 6.25% of state tax, 1% of county tax and 2.25% of district tax should be applied.

Create a Sales Taxes and Charges Template as shown below.

![City Specific To Zipcode](/files/city-specific-tax.png)

Create a Tax Rule as shown below.

![Tax Rule](/files/tax-rule.png)

Once you select a customer and a billing address of that customer with city as 'Malibu', system automatically applies the appropriate taxes.

![Tax Rule in Sales Invoice](/files/tax-rule-in-sales-invoice.gif)

### 5\. Related Topics

  1. [Pricing Rule](</erpnext/pricing-rule>)
  2. [Item Tax Template](</erpnext/item-tax-template>)
  3. [Tax Category](</erpnext/tax-category>)
  4. [Customer](</erpnext/customer>)
  5. [Supplier](</erpnext/supplier>)



[ Previous Page Finance Book ](</erpnext/finance-book>) [ Next Page Item Tax Template  ](</erpnext/item-tax-template>)

Last updated 1 week ago 

Was this helpful?
