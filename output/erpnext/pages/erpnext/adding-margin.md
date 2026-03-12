# Adding Margin

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t4rtvjc8u)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Adding Margin 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t4rtvjc8u)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

User Can apply the margin on Quotation Item and Sales Order Item using following two options. 1)Price Rule: With the help of this method user can apply the margin on Quotation and Sales Order based on condition. You can find the section margin on pricing rule where a user has to select the type of margin whether it is Percentage or Amount and Rate or Amount. The system will apply the margin on quotation item and sales order item if pricing rule is enabled.

To setup Pricing Rule, go to:

`Selling > Setup > Pricing Rule` or `Accounts > Setup > Pricing Rule`

####Adding Margin in Pricing Rule

![Adding Margin in Pricing Rule](https://docs.frappe.io/assets/eb1a3ab231f1.png)

Total Margin is calculated as follows: `Rate = Price List Rate + Margin Rate`

So, In order to apply the Margin you need to add the Price List for the Item

To add Price List, go to:

`Selling > Setup > Item Price` or `Stock > Setup > Item Price`

####Adding Item Price

![Adding Margin in Pricing Rule](https://docs.frappe.io/assets/d6231d593629.png)

  2. Apply margin direct on Item: If user wants to apply the margin without pricing rule, they can use this option. In Quotation Item and Sales Order Item, user can select the margin type and rate or amount. The system will calculate the margin and apply it on price list rate to calculate the rate of the product.



To add margin directly on Quotation or Sales Order, go to:

`Selling > Document > Quotation`

add item and scroll down to section where you can find the Margin Type

####Adding Margin in Quotation

![Adding Margin in Quotation](https://docs.frappe.io/assets/28d5bc8a734a.png)

[ Previous Page Sales Return Management  ](sales-return-use-cases.md) [ Next Page Introduction to Stock Module ](stock.md)

Last updated 1 week ago 

Was this helpful?
