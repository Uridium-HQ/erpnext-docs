# Creating Custom Link Field

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t88tuuj1t)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Creating Custom Link Field

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t88tuuj1t)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Link fields are the ones linked to another document type. For example, Customer field is a Link Field in Sales Order. This field is linked to the Customer master.

You can insert Custom Link Field by following the steps below.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customize > Customize Form

#### Step 2: Select Form

In Customize Form, select Document Type (Quotation, Sales Order, Purchase Invoice Item etc.). Once fields are updated in the accompanying table below, open a field above the one you wish to insert your Custom Field. Then click on "Insert Above" to insert the new Custom Field.

![Select Docytpe](https://docs.frappe.io/assets/6a4ff0e2fea3.gif)

#### Step 4: Custom Field Values

To set field as Link, enter values as below.

  1. Label: Desired label that user wishes to display in the form.
  2. Type: Set as 'Link'
  3. Name: Desired name for the field
  4. Options: Enter the name of the DocType to which the field is linked



![Enter Values](https://docs.frappe.io/assets/c8c3e90aa3d5.png)

## Adding Filters to Link Field

> Note: The feature will be available from version 15 and above.

Frappe provides a user-friendly approach to apply filters on Link Fields using the Form Builder.

You'll notice an action icon on all Link Fields within a Doctype, which gives you the option to select the filters you want to apply.![1](https://docs.frappe.io/assets/8f809d905943.png)

For example, in the case of "Company", clicking on the icon will open a dialogue box where you can choose your desired filters.

![2](https://docs.frappe.io/assets/1653479123ba.png)

Once you've made your selection and clicked on apply, the filtered results will be displayed accordingly.

![3](https://docs.frappe.io/assets/f9356baeba2c.png)

If you're customizing a form and decide to change the filters, a "Reset To Default" button will appear. Clicking on this will revert the filters back to their original state. **However, it's important to note that any filters in "Customize Form" will override the default filters**

![4](https://docs.frappe.io/assets/bb30f4c0633b.png)

**Eval Support**

Users can add dynamic filters based on some value from the form.

**Use:**

`eval: doc.fieldname`

or

`eval: doc.fieldname1 + doc.fieldname2`

![Screenshot 2024-03-14 at 11.25.07 PM](https://docs.frappe.io/assets/4a244fd07660.png)

**For Child Tables:**  
2 types of filters can be added.

  * From the Child Table Row: to add these filters use `doc.child_table_field_name`
  * From Parent Document: to add these use `parent.parent_doc_fieldname`



![Screenshot 2024-03-19 at 12.28.35 PM](https://docs.frappe.io/assets/ff64a8db26e5.png)

the expression added after "eval:" is evaluated and its value is returned.
[code] 
    Note: Filters applied through frm.set_query, will take preference over filters applied via the User Interface (UI).
    
[/code]

[ Previous Page Signature Field ](https://docs.frappe.io/erpnext/electronic-signature) [ Next Page Document Versioning  ](document-versioning.md)

Last updated 1 week ago 

Was this helpful?
