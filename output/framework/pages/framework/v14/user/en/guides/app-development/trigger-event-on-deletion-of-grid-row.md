# Trigger Event On Deletion Of Grid Row

[ Edit ](</wiki/spaces/r3uvq1ch61/page/128tag9a16>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Trigger Event On Deletion Of Grid Row 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/128tag9a16>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

To trigger an event when a row from a Child Table has been deleted (when user clicks on `delete` button), you need to add a handler the `fieldname_remove` event to Child Table, where fieldname is the fieldname of the Child Table in Parent Table declaration.

For example:

Assuming that your parent DocType is named `Item` has a Table Field linked to `Item Color` DocType with decloration name `color`.

In order to "catch" the delete event:
[code] 
    frappe.ui.form.on('Item Color', {
     color_remove: function(frm) {
     // You code here
     // If you console.log(frm.doc.color) you will get the remaining color list
     }
    );
    
[/code]

The same process is used to trigger the add event (when user clicks on `add row` button):
[code] 
    frappe.ui.form.on('Item Color', {
     color_remove: function(frm) {
     // You code here
     // If you console.log(frm.doc.color) you will get the remaining color list
     },
     color_add: function(frm) {}
    });
    
[/code]

Notice that the handling is be made on Child DocType Table `form.ui.on` and not on Parent Doctype so a minimal full example is:
[code] 
    frappe.ui.form.on('Item',{
     // Your client side handling for Item
    });
    
    frappe.ui.form.on('Item Color', {
     color_remove: function(frm) {
     // Deleting is triggered here
     }
    );
    
[/code]

Handlers are:

  1. fieldname_add
  2. fieldname_move
  3. fieldname_before_remove
  4. fieldname_remove



[ Previous Page Adding Custom Button To Form  ](</framework/v14/user/en/guides/app-development/adding-custom-button-to-form>) [ Next Page Dialogs Types  ](</framework/v14/user/en/guides/app-development/dialogs-types>)

Last updated 2 months ago 

Was this helpful?
