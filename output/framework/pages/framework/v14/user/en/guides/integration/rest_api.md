# Introduction

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12f9keljnq)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Introduction 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12f9keljnq)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe ships with an HTTP API that can be classified into _Remote Procedure Calls_ (RPC), to call whitelisted methods and _Representational State Transfer_ (REST), to manipulate resources.

The base URL is `https://{your frappe instance}`. Every request shown here should be added to the end of your base URL. For example, if your instance is `demo.erpnext.com`, `GET /api/resource/User` means `GET https://demo.erpnext.com/api/resource/User`.

## RPC

A request to an endpoint `/api/method/dotted.path.to.function` will call a whitelisted python function.

For example, `GET /api/method/frappe.auth.get_logged_user` will call [this function](https://github.com/frappe/frappe/blob/28b909435320e3d6d1a3b2e7c02f286984dc39b3/frappe/auth.py) from frappe's auth module:
[code] 
    @frappe.whitelist()
    def get_logged_user():
     return frappe.session.user
    
[/code]

Response:
[code] 
    {
     "message": "Administrator"
    }
    
[/code]

## REST

All documents in Frappe are available via a RESTful API with prefix `/api/resource/`. You can perform all CRUD operations on them:

  * Create



You can create a document by sending a `POST` request to the endpoint, `/api/resource/{doctype}`.

  * Read



You can get a document by its name using the endpoint, `/api/resource/{doctype}/{name}`

  * Update



You can update a document by sending a `PUT` request to the endpoint, `/api/resource/{doctype}/{name}`. This acts like a `PATCH` HTTP request in which you do not have to send the whole document but only the parts you want to change.

  * Delete



You can delete a document by its name by sending a `DELETE` request to the endpoint, `/api/resource/{doctype}/{name}`.

[ Previous Page Using Frappe as OAuth Service ](../../using_frappe_as_oauth_service.md) [ Next Page Simple Authentication  ](rest_api/simple_authentication.md)

Last updated 2 months ago 

Was this helpful?
