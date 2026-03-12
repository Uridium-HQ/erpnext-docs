# Dialog API

[ Edit ](</wiki/spaces/1u8fslkdg6/page/0tm70j5hqm>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Dialog API

[ Edit ](</wiki/spaces/1u8fslkdg6/page/0tm70j5hqm>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe provides a group of standard, interactive and flexible dialogs that are easy to configure and use. There's also a more extensive API for [Javascript](</framework/v14/user/en/api/dialog>).

### frappe.msgprint

`frappe.msgprint(msg, title, raise_exception, as_table, as_list, indicator, primary_action, is_minimizable, wide, realtime)`

This method works only within a request / response cycle. It shows a message to the user logged in to Desk who initiated the request.

The argument list includes:

  * `msg`: The message to be displayed
  * `title`: Title of the modal
  * `as_table`: If `msg` is a list of lists, render as HTML table
  * `as_list`: If `msg` is a list, render as HTML unordered list
  * `primary_action`: Bind a primary server/client side action.
  * `raise_exception`: Exception
  * `is_wide`: Show a wide modal
  * `is_minimizable`: Allow users to minimize the modal
  * `realtime`: publish immediately using websocket instead of adding to response message log


[code] 
    frappe.msgprint(
        msg='This file does not exist',
        title='Error',
        raise_exception=FileNotFoundError
    )
      
    
    
[/code]

![frappe.msgprint](/files/dialog-api-msgprint-py.png) _frappe.msgprint_

`primary_action` can contain a `server_action` **or** `client_side` action which must contain dotted paths to the respective methods. The JavaScript function must be a globally available function. You can also pass `hide_on_success` to close the message after the action is successfully completed.
[code] 
    # msgprint with server and client side action
    frappe.msgprint(msg='This file does not exist',
        title='Error',
        raise_exception=FileNotFoundError
        primary_action={
            'label': _('Perform Action'),
            'server_action': 'dotted.path.to.server.method',
            'client_action': 'dotted.path.to.client.method',
            'hide_on_success': True,
            'args': args
        }
    )
      
    
    
[/code]

![frappe.msgprint with primary action](/files/dialog-api-msgprint-py-with-primary-action.png) _frappe.msgprint with primary action_

### frappe.throw

`frappe.throw(msg, exc, title, is_minimizable, wide, as_list, primary_action)`

This method will raise an exception as well as show a message in Desk. It is essentially a wrapper around `frappe.msgprint`.

`exc` can be passed an optional exception. By default it will raise a `ValidationError` exception.
[code] 
    frappe.throw(
        title='Error',
        msg='This file does not exist',
        exc=FileNotFoundError
    )
      
    
    
[/code]

![Throw-py](/files/dialog-api-msgprint-py.png) _frappe.throw_

[ Previous Page FullTextSearch API ](</framework/user/en/api/full-text-search>) [ Next Page Query Builder  ](</framework/user/en/api/query-builder>)

Last updated 3 weeks ago 

Was this helpful?
