# Server Calls (AJAX)

[ Edit ](</wiki/spaces/1u8fslkdg6/page/0tosgbbgp8>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Server Calls (AJAX) 

[ Edit ](</wiki/spaces/1u8fslkdg6/page/0tosgbbgp8>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## frappe.call

`frappe.call(method, args)`

Makes an AJAX request to the server, where the `method` which is the dotted path to a whitelisted Python method, is executed and it's return value is sent as the response.
[code] 
    // call with no parameters
    frappe.call('ping')
     .then(r => {
     console.log(r)
     // {message: "pong"}
     })
    
    // call with a single parameter
    frappe.call('frappe.core.doctype.user.user.get_role_profile', {
     role_profile: 'Test'
    }).then(r => {
     console.log(r.message)
    })
    
    // call with all options
    frappe.call({
     method: 'frappe.core.doctype.user.user.get_role_profile',
     args: {
     role_profile: 'Test'
     },
     // disable the button until the request is completed
     btn: $('.primary-action'),
     // freeze the screen until the request is completed
     freeze: true,
     callback: (r) => {
     // on success
     },
     error: (r) => {
     // on error
     }
    })
    
[/code]

## frappe.db.get_doc

`frappe.db.get_doc(doctype, name, filters)`

Returns the Document object of `doctype` and `name`. If `name` is not provided, gets the first document matched by `filters`.
[code] 
    // get doc by name
    frappe.db.get_doc('Task', 'TASK00002')
     .then(doc => {
     console.log(doc)
     })
    
    // get doc by filters
    frappe.db.get_doc('Task', null, { status: 'Open' })
     .then(doc => {
     console.log(doc)
     })
    
[/code]

## frappe.db.get_list

`frappe.db.get_list(doctype, { fields, filters })`

Returns a list of records of `doctype` with `fields` and `filters`.
[code] 
    frappe.db.get_list('Task', {
     fields: ['subject', 'description'],
     filters: {
     status: 'Open'
     }
    }).then(records => {
     console.log(records);
    })
    
[/code]

## frappe.db.get_value

`frappe.db.get_value(doctype, name, fieldname)`

Returns a document's field value or a list of values.
[code] 
    // single value
    frappe.db.get_value('Task', 'TASK00004', 'status')
     .then(r => {
     console.log(r.message.status) // Open
     })
    
    // multiple values
    frappe.db.get_value('Task', 'TASK00004', ['status', 'subject'])
     .then(r => {
     let values = r.message;
     console.log(values.status, values.subject)
     })
    
    // using filters
    frappe.db.get_value('Task', {status: 'Open'}, 'subject')
     .then(r => {
     let values = r.message;
     console.log(values.subject)
     })
    
[/code]

## frappe.db.get_single_value

`frappe.db.get_single_value(doctype, field)`

Returns a field value from a Single DocType.
[code] 
    frappe.db.get_single_value('System Settings', 'time_zone')
     .then(time_zone => {
     console.log(time_zone);
     })
    
[/code]

## frappe.db.set_value

`frappe.db.set_value(doctype, docname, fieldname, value, callback)`

Sets a document's property using `frappe.get_doc` and `doc.save` on server.
[code] 
    // update a field's value
    frappe.db.set_value('Task', 'TASK00004', 'status', 'Open')
     .then(r => {
     let doc = r.message;
     console.log(doc);
     })
    
    // update multiple fields
    frappe.db.set_value('Task', 'TASK00004', {
     status: 'Working',
     priority: 'Medium'
    }).then(r => {
     let doc = r.message;
     console.log(doc);
    })
    
[/code]

## frappe.db.insert

`frappe.db.insert(doc)`

Insert a new document.
[code] 
    frappe.db.insert({
     doctype: 'Task',
     subject: 'New Task'
    }).then(doc => {
     console.log(doc);
    })
    
[/code]

## frappe.db.count

`frappe.db.count(doctype, filters)`

Returns number of records for a given `doctype` and `filters`.
[code] 
    // total number of Task records
    frappe.db.count('Task')
     .then(count => {
     console.log(count)
     })
    
    // total number of Open Tasks
    frappe.db.count('Task', { status: 'Open' })
     .then(count => {
     console.log(count)
     })
    
[/code]

## frappe.db.delete_doc

`frappe.db.delete_doc(doctype, name)`

Delete a document identified by `doctype` and `name`.
[code] 
    frappe.db.delete_doc('Task', 'TASK00004')
    
[/code]

## frappe.db.exists

`frappe.db.exists(doctype, name)`

Returns true if a document record exists.
[code] 
    frappe.db.exists('Task', 'TASK00004')
     .then(exists => {
     console.log(exists) // true
     })
    
[/code]

[ Previous Page Scanner API  ](</framework/user/en/api/scanner>) [ Next Page Logging ](</framework/user/en/api/logging>)

Last updated 3 weeks ago 

Was this helpful?
