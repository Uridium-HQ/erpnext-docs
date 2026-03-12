# Prerequisites

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12a3vt5mfk)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Prerequisites 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12a3vt5mfk)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

  * [Connected App](connected-app.md)



**Connected App** stores the client ID and secret, scopes and endpoints of the platform you're integrating with.

## Getting started

> This example uses Google, but you can use any service supporting OAuth 2.0.

Your integration will most probably need a settings doctype (for example, "Google Settings"). Here you create a link field to **Connected App**. A System Manager can later create a **Connected App** , enter the client credentials and link it to your integration. You will know which **Connected App** belongs to your integration via your settings DocType.
[code] 
    google_settings = frappe.get_single('Google Settings')
    connected_app_name = google_settings.get('connected_app')
    
    connected_app = frappe.get_doc('Connected App', connected_app_name)
    
[/code]

Now you have an instance of your **Connected App** , containing the credentials and endpoint URIs. If a user didn't connect yet, they can open the **Connected App** and click the "Connect to ..." button on the top right. Alternatively, you can get the authorization URI and use it for your own custom button or redirect:
[code] 
    authorization_uri = connected_app.initiate_web_application_flow() # optional
    
[/code]

Once the user is authorized, you can get an authenticated session like this:
[code] 
    session = connected_app.get_oauth2_session()
    
[/code]

> If the user is not authenticated at this time, they will be redirected to the authentication page.

Now you can retrieve any allowed resource from the target platform:
[code] 
    session.get('https://www.googleapis.com/oauth2/v2/userinfo')
    
[/code]

If the access token is expired, the session will automatically try to refresh it.

[ Previous Page Single Type Doctype  ](single-type-doctype.md) [ Next Page Adding Social Login Provider  ](adding-social-login-provider.md)

Last updated 2 months ago 

Was this helpful?
