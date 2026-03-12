# Adding Social Login Provider

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12a3lvm5fh>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Adding Social Login Provider 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12a3lvm5fh>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

This guide discusses how to add a social login provider to frappe via pull request.

### Add your provider in `SocialLoginKey.get_social_login_provider`
[code] 
    providers["Frappe"] = {
     "provider_name": "Frappe",
     "enable_social_login": 1,
     "custom_base_url": 1,
     "icon":"/assets/frappe/images/favicon.png",
     "redirect_url": "/api/method/frappe.www.login.login_via_frappe",
     "api_endpoint": "/api/method/frappe.integrations.oauth2.openid_profile",
     "api_endpoint_args":None,
     "authorize_url": "/api/method/frappe.integrations.oauth2.authorize",
     "access_token_url": "/api/method/frappe.integrations.oauth2.get_token",
     "auth_url_data": json.dumps({
     "response_type": "code",
     "scope": "openid"
     })
    }
    
[/code]

### Add provider key in exact same type case in options of `social_login_provider` select field on `Social Login Key` DocType. e.g. `Frappe`

Once the user adds a social login provider and enables it the `Authorization Code` is sent back by the provider api server on to the redirect_url mentioned on the same server. You will have to add a whitelisted method allowing guest access in `frappe.integrations.oauth2_logins`. e.g. `login_via_office365`

There many implementations of OAuth 2.0 + OpenID Connect. Here we'll discuss two ways of accessing openid information.

#### User Creation via OpenID Profile Endpoint

example:
[code] 
    @frappe.whitelist(allow_guest=True)
    def login_via_frappe(code, state):
     login_via_oauth2("frappe", code, state, decoder=json.loads)
    
[/code]

#### User Creation via id_token

example:
[code] 
    @frappe.whitelist(allow_guest=True)
    def login_via_office365(code, state):
     login_via_oauth2_id_token("office_365", code, state, decoder=json.loads)
    
[/code]

[ Previous Page Prerequisites  ](</framework/v14/user/en/guides/app-development/generic-oauth-client>) [ Next Page Exporting Customizations to your App  ](</framework/v14/user/en/guides/app-development/exporting-customizations>)

Last updated 2 months ago 

Was this helpful?
