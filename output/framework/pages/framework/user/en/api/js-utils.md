# Common Utilities API

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0tnqna64k0)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Common Utilities API 

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0tnqna64k0)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## frappe.get_route

`frappe.get_route()`

Returns the current route as an array.
[code] 
    frappe.get_route()
    // ["List", "Task", "List"]
    
[/code]

## frappe.set_route

`frappe.set_route(route)`

Changes the current route to `route`.
[code] 
    // route in parts
    frappe.set_route('List', 'Task', 'List')
    
    // route as array
    frappe.set_route(['List', 'Task', 'Gantt'])
    
    // route as string
    frappe.set_route('List/Event/Calendar')
    
    // route with options
    frappe.set_route(['List', 'Task', 'Task'], { status: 'Open' })
    
[/code]

## frappe.format

`frappe.format(value, df, options, doc)`

Format a raw value into user presentable format.
[code] 
    frappe.format('2019-09-08', { fieldtype: 'Date' })
    // "09-08-2019"
    
    frappe.format('2399', { fieldtype: 'Currency', options: 'currency' }, { inline: true })
    // "2,399.00"
    
[/code]

## frappe.provide

`frappe.provide(namespace)`

Creates a namespace attached to the window object if it doesn't exist.
[code] 
    frappe.provide('frappe.ui.form');
    
    // has the same effect as
    window.frappe = {}
    window.frappe.ui = {}
    window.frappe.ui.form = {}
    
[/code]

## frappe.require

`frappe.require(asset_path, callback)`

Load a JS or CSS asset asynchronously. It is used for libraries that are not used often.
[code] 
    // load a single asset
    frappe.require('/assets/frappe/chat.js', () => {
     // chat.js is loaded
    })
    
    // load multiple assets
    frappe.require(['/assets/frappe/chat.js', '/assets/frappe/chat.css'], () => {
     // chat.js and chat.css are loaded
    })
    
[/code]

[ Previous Page Tree  ](tree.md) [ Next Page Dialog API ](dialog.md)

Last updated 3 weeks ago 

Was this helpful?
