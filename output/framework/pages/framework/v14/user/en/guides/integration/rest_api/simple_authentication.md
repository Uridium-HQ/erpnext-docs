# Simple Authentication

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12fpojl01l)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Simple Authentication 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12fpojl01l)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## POST /api/method/login

Content-Type: application/x-www-form-urlencoded

Params (in body):

  * usr (string)



Username

  * pwd (string)



Password

Example:
[code] 
    curl -X POST https://{your frappe instance}/api/method/login \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -d '{"usr":"Administrator","pwd":"admin"}'
    
[/code]

Returns:

  * HTTP Code: 200
  * application/json:


[code] 
     {
     "home_page": "/desk",
     "full_name": "Administrator",
     "message": "Logged in"
     }
    
[/code]

  * Cookie: `sid` (send this to authenticate future requests). [Expires in three days](https://github.com/frappe/frappe/blob/e551153ea0a5fb905f2d9508143a9d25ec74aa43/frappe/auth.py).


[code] 
     sid=05d8d46aaebff1c87a90f570a3ff1c0f570a3ff1c87a90f56bacd4;
     path=/;
     domain=.{your frappe instance};
     Expires=Sat, 29 Sep 2018 00:59:54 GMT;
    
[/code]

Error:

  * HTTP Code: 401
  * text/html: Wrong password or username.



## GET /api/method/logout

Example:
[code] 
     curl -X GET https://{your frappe instance}/api/method/logout
    
[/code]

Returns:

  * HTTP Code: 200
  * application/json: `{}`



## GET /api/method/frappe.auth.get\\_logged\\_user

Get the ID of the currently authenticated user.

Example:
[code] 
     curl -X GET https://{your frappe instance}/api/method/frappe.auth.get_logged_user
    
[/code]

Returns:

  * HTTP Code: 200
  * application/json:


[code] 
     {
     "message": "Administrator"
     }
    
[/code]

Author: Raffael Meyer (raffael@alyf.de)

[ Previous Page Introduction  ](../rest_api.md) [ Next Page Token Based Authentication ](token_based_authentication.md)

Last updated 2 months ago 

Was this helpful?
