# Fetching data from a linked master

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t82nlfqgb)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Fetching data from a linked master

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t82nlfqgb)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Question:** How to add terms and conditions in driver form?  
**Steps:**

  1. Go to the doctype where you want the to add the terms and conditions.
  2. Go to Menu > Customize



![](../../assets/edbd251c1bbb.png)

  1. You will see a table with a list of fields. These are the fields in your driver page.
  2. Scroll down to the section/field after which you want to add terms and conditions.
  3. Click on the small icon on the right side. This will expand the selected field.
  4. You can add a new field above on below by clicking on _Insert Above/Below_.![](../../assets/4cb00c233a70.png)
  5. Add a new field as show below:![](../../assets/0398cdedf3c2.png)For more details on adding a custom link field, refer [this link](creating-custom-link-field.md).
  6. Add a second field below this:![](../../assets/6e104d8c3a39.png)How does this work? In Fetch from, we are adding the following details: doctype.field. In the Terms and Conditions doctype, the field where we add the terms is named _terms_ and it is of type: Text Editor. For _fetch from_ to work, the data must be in the following format: link_field_name.field_to_fetch
  7. Once this is done, click on **Update** , and go back to your list. Click on Ctrl + Shift + R to reload.
  8. When you select the terms template in the driver, the system will fetch the conditions from the selected template:![](../../assets/bbaa66c2d05a.png)



[ Previous Page Fetching Data from a Document  ](https://docs.frappe.io/erpnext/fetching-data-from-a-document) [ Next Page Data Visibility in Child Tables ](customizing-data-visibility-in-child-table.md)

Last updated 1 week ago 

Was this helpful?
