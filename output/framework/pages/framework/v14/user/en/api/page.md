# Page API

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12qmrfi77f)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Page API 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12qmrfi77f)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Every screen inside the Desk is rendered inside a `frappe.ui.Page` object.

## frappe.ui.make\\_app\\_page

Creates a new Page and attaches it to parent.
[code] 
    let page = frappe.ui.make_app_page({
     title: 'My Page',
     parent: wrapper // HTML DOM Element or jQuery object
     single_column: true // create a page without sidebar
    })
    
[/code]

![New Page](https://docs.frappe.io/assets/90efcc16e8a6.png) _New Page_

## Page methods

This section lists out the common methods available on the page instance object.

## page.set_title

Set the page title along with the document title. The document title is shown in browser tab.
[code] 
    page.set_title('My Page')
    
[/code]

![Page Title](https://docs.frappe.io/assets/590d5dcf6286.png) _Page Title_

## page.set\\_title\\_sub

Set the secondary title of the page. It is shown on the right side of the page header.
[code] 
    page.set_title_sub('Subtitle')
    
[/code]

![Page Subtitle](https://docs.frappe.io/assets/5347d8bfa25a.png) _Page Subtitle_

## page.set_indicator

Set the indicator label and color.
[code] 
    page.set_indicator('Pending', 'orange')
    
[/code]

![Page Indicator](https://docs.frappe.io/assets/3f251dadfa3b.png) _Page Indicator_

## page.clear_indicator

Clear the indicator label and color.
[code] 
    page.clear_indicator()
    
[/code]

## page.set\\_primary_action

Set the primary action button label and handler. The third argument is the icon class which will be shown in mobile view.
[code] 
    let $btn = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus')
    
[/code]

![Page Primary Action](https://docs.frappe.io/assets/b14f09e3f71c.png) _Page Primary Action_

## page.clear\\_primary_action

Clear primary action button and handler.
[code] 
    page.clear_primary_action()
    
[/code]

## page.set\\_secondary_action

Set the secondary action button label and handler. The third argument is the icon class which will be shown in mobile view.
[code] 
    let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')
    
[/code]

![Page Secondary Action](https://docs.frappe.io/assets/a7cc8ec81903.png) _Page Secondary Action_

## page.clear\\_secondary_action

Clear secondary action button and handler.
[code] 
    page.clear_secondary_action()
    
[/code]

## page.add\\_menu_item

Add menu items in the Menu dropdown.
[code] 
    // add a normal menu item
    page.add_menu_item('Send Email', () => open_email_dialog())
    
    // add a standard menu item
    page.add_menu_item('Send Email', () => open_email_dialog(), true)
    
[/code]

![Page Menu Dropdown](https://docs.frappe.io/assets/0eda3c66cef2.png) _Page Menu Dropdown_

## page.clear_menu

Remove Menu dropdown with items.
[code] 
    page.clear_menu()
    
[/code]

## page.add\\_action_item

Add menu items in the Actions dropdown.
[code] 
    // add a normal menu item
    page.add_action_item('Delete', () => delete_items())
    
[/code]

![Page Actions Dropdown](https://docs.frappe.io/assets/8b7b58e26b10.png) _Page Actions Dropdown_

## page.clear\\_actions_menu

Remove Actions dropdown with items.
[code] 
    page.clear_actions_menu()
    
[/code]

## page.add\\_inner_button

Add buttons in the inner toolbar.
[code] 
    // add a normal inner button
    page.add_inner_button('Update Posts', () => update_posts())
    
[/code]

![Page Inner Button](https://docs.frappe.io/assets/d0afd5b2b10e.png) _Page Inner Button_
[code] 
    // add a dropdown button in a group
    page.add_inner_button('New Post', () => new_post(), 'Make')
    
[/code]

![Page Inner Button Group](https://docs.frappe.io/assets/afbcfd582e33.png) _Page Inner Button Group_

### page.change\\_custom_button_type

Change a specific custom button type by label (and group).
[code] 
    // change type of ungrouped button
    page.change_inner_button_type('Update Posts', null, 'primary');
    
    // change type of a button in a group
    page.change_inner_button_type('Delete Posts', 'Actions', 'danger');
    
[/code]

## page.remove\\_inner_button

Remove buttons in the inner toolbar.
[code] 
    // remove inner button
    page.remove_inner_button('Update Posts')
    
    // remove dropdown button in a group
    page.remove_inner_button('New Posts', 'Make')
    
[/code]

## page.clear\\_inner_toolbar

Remove the inner toolbar.
[code] 
    page.remove_inner_toolbar()
    
[/code]

## page.add_field

Add a form control in the page form toolbar.
[code] 
    let field = page.add_field({
     label: 'Status',
     fieldtype: 'Select',
     fieldname: 'status',
     options: [
     'Open',
     'Closed',
     'Cancelled'
     ],
     change() {
     console.log(field.get_value());
     }
    });
    
[/code]

![Page Form Toolbar](https://docs.frappe.io/assets/0ee0334beab0.png) _Page Form Toolbar_

## page.get\\_form_values

Get all form values from the page form toolbar in an object.
[code] 
    let values = page.get_form_values()
    // { status: 'Open', priority: 'Low' }
    
[/code]

## page.clear_fields

Clear all fields from the page form toolbar.
[code] 
    page.clear_fields()
    
[/code]

[ Previous Page List  ](list.md) [ Next Page Tree  ](tree.md)

Last updated 2 months ago 

Was this helpful?
