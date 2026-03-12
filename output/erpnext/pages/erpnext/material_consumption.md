# Material consumption

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0spkqu8spt)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Material consumption 

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0spkqu8spt)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Material Consumption functionality allows you to have multiple consumption `Stock Entry` against a Work Order. To enable this, go to Manufacturing > Manufacturing Settings.

![Item Alternative](https://docs.frappe.io/assets/c4e77849c96a.png)

Once enabled, a `Material Consumption` button will be available in Work Order once started.

![Item Alternative](https://docs.frappe.io/assets/ecf49c20dfdc.png)

When button is clicked, it will do the following:

  1. It will create Stock Entry with purpose `Material Consumption for Manufacture`.



![Item Alternative](https://docs.frappe.io/assets/b930fbffd790.png)

  2. If the "Backflush Raw Materials Based On" in the Manufacturing Settings is set to `BOM`, if will propose to consume all required qty for manufacture.
  3. If the "Backflush Raw Materials Based On" in the Manufacturing Settings is set to `Material Transferred for Manufacture`, if will propose to consume all transferred qty for manufacture.
  4. Once submitted, it will update `Consumed Qty` column in the Work Order.



![Item Alternative](https://docs.frappe.io/assets/e89c819c4a29.png)

  5. In succeeding Material Consumption, it will suggest unconsumed qty.
  6. Once "Finish" button is clicked in Work Order, it will take into account consumed qty.



### Validations

  * If "Allow Multiple Material Consumption" is not set in Manufacturing Settings but "Material Consumption for Manufacture" is use in Stock Entry.



![Item Alternative](https://docs.frappe.io/assets/18ec8d3f8228.gif)

  * Cannot cancel "Material Consumption for Manufacture" for completed Work Order.



![Item Alternative](https://docs.frappe.io/assets/90b8713427a6.gif)

[ Previous Page Raw material valuation ](valuation-based-on-field-in-bom.md) [ Next Page Manufacturing without creating BOM ](manufacturing-without-creating-bom.md)

Last updated 1 week ago 

Was this helpful?
