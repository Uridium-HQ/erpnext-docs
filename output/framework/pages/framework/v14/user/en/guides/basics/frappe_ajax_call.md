# Frappe Ajax Call

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/127408s5rr)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Frappe Ajax Call 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/127408s5rr)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

In Frappe Framework, you can manage ajax calls via frappe.call. The frappe.call works in asynchronous manner ie. send requests and handle response via callback mechanism.

## frappe.call Structure
[code] 
    frappe.call({
     method: "",
     type: "POST",
     args: {},
     success: function(r) {},
     error: function(r) {},
     always: function(r) {},
     btn: opts.btn,
     freeze: false,
     freeze_message: "",
     async: true,
     url: "" || frappe.request.url,
    });
    
[/code]

#### Parameter description

  * `method`: dotted path to a whitelisted backend method
  * `type`: String parameter, http request type "GET", "POST", "PUT", "DELETE". Default set to "POST".
  * `args`: associative array, arguments that will pass with request.
  * `success`: Function parameter, code snippet, will after successful execution of request
  * `error`: Function parameter, code snippet, will execute after request failure
  * `always`: Function parameter, code snippet, will execute in either case
  * `btn`: Object parameter, triggering object
  * `freeze`: Boolean parameter, if set freeze the instance until it receives response
  * `freeze_message`: String parameter, message will populate to screen while screen is in freeze state.
  * `async`: Boolean parameter, default set to true. So each frappe.call is asynchronous. To make call synchronous set parameter value as false
  * `url`: String parameter, location from where hitting the request



## How to use frappe.call ?

### Calling standard API
[code] 
    frappe.call({
     method: 'frappe.client.get_value',
     args: {
     'doctype': 'Item',
     'filters': {'name': item_code},
     'fieldname': [
     'item_name',
     'web_long_description',
     'description',
     'image',
     'thumbnail'
     ]
     },
     callback: function(r) {
     if (!r.exc) {
     // code snippet
     }
     }
    });
    
[/code]

  * Param description:

  * `doctype`: name of doctype for which you want to pull information

  * `filters`: condition specifier

  * `fieldname`: you can specify fields in array that you want back in response




### Calling whitelisted methods

  * On the client side we specify the server side `method` to be called. This is a dotted path through the python modules on the server side, where the last part is the method name.


[code] 
    frappe.call({
    method: "frappe.core.doctype.user.user.get_all_roles", //dotted path to server method
    callback: function(r) {
    // code snippet
    }
    });
    
[/code]

  * The above request calls the server-side method `get_all_roles`, located in the file `$MY_BENCH/apps/frappe/frappe/core/doctype/user/user.py`:


[code] 
    @frappe.whitelist()
    def get_all_roles():
    // business logic
    return value
    
[/code]

> **Note** : any server side method that should be accessed via `frappe.call()` needs to be whitelisted, by using the decorator `@frappe.whitelist()`.

[ Previous Page Contribute Translations  ](contribute_translations.md) [ Next Page How to Enable Backup Encryption  ](how-to-enable-backup-encryption.md)

Last updated 2 months ago 

Was this helpful?
