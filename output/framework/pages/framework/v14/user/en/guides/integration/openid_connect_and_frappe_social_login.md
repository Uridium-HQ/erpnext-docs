# OpenID Connect and Frappe social login

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12ervugnkn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# OpenID Connect and Frappe social login 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12ervugnkn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## OpenID Connect

Frappe also uses Open ID connect essential standard for authenticating users. To get `id_token` with `access_token`, pass `openid` as the value for the scope parameter during authorization request.

If the scope is `openid` the JSON response with `access_token` will also include a JSON Web Token (`id_token`) signed with `HS256` and `Client Secret`. The decoded `id_token` includes the `at_hash`.

Example Bearer Token with scope `openid`
[code] 
    {
     "token_type": "Bearer",
     "id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.eyJpc3MiOiJodHRwczovL21udGVjaG5pcXVlLmNvbSIsImF0X2hhc2giOiJOQlFXbExJUy1lQ1BXd1d4Y0EwaVpnIiwiYXVkIjoiYjg3NzJhZWQ1YyIsImV4cCI6MTQ3Nzk1NTYzMywic3ViIjoiNWFjNDE2NThkZjFiZTE1MjI4M2QxYTk0YjhmYzcwNDIifQ.1GRvhk5wNoR4GWoeQfleEDgtLS5nvj9nsO4xd8QE-Uk",
     "access_token": "ZJD04ldyyvjuAngjgBrgHwxcOig4vW",
     "scope": "openid",
     "expires_in": 3600,
     "refresh_token": "2pBTDTGhjzs2EWRkcNV1N67yw0nizS"
    }
    
[/code]

## Frappe social login setup

In this example there are 2 servers,

### Primary Server

This is the main server hosting all the users. e.g. `https://frappe.io`. To setup this as the main server, go to _Setup_ > _Integrations_ > _Social Login Keys_ and enter `https://frappe.io` in the field `Frappe Server URL`. This URL repeats in all other Frappe servers who connect to this server to authenticate. Effectively, this is the main Identity Provider (IDP).

Under this server add as many `OAuth Client`(s) as required. Because we are setting up one app server, add only one `OAuth Client`

### Frappe App Server

This is the client connecting to the IDP. Go to _Setup_ > _Integrations_ > _Social Login Keys_ on this server and add appropriate values to `Frappe Client ID` and `Frappe Client Secret` (refer to client added in primary server). As mentioned before keep the `Frappe Server URL` as `https://frappe.io`

Now you will see Frappe icon on the login page. Click on this icon to login with account created in primary server (IDP) `https://frappe.io`

**Note** : If `Skip Authorization` is checked while registering a client, page to allow or deny the granting access to resource is not shown. This can be used if the apps are internal to one organization and seamless user experience is needed.

## Steps

### Part 1 : on Frappe Identity Provider (IDP)

Login to IDP ![](../../../../../../../assets/0bc5d6d9f016.png)

Add OAuth Client on IDP ![](../../../../../../../assets/3627b77a14f0.png)

Set Server URL on IDP ![](../../../../../../../assets/653e2d807e22.png)

### Part 2 : on Frappe App Server

Set `Frappe Client ID` and `Frappe Client Secret` on App server (refer the client set on IDP) ![](../../../../../../../assets/3690eb2e6a05.png)

**Note** : Frappe Server URL is the main server where identities from your organization are stored.

Login Screen on App Server (login with frappe) ![](../../../../../../../assets/fba04147efd7.png)

### Part 3 : Redirected on IDP

login with user on IDP ![](../../../../../../../assets/401e23a070f0.png)

Confirm Access on IDP ![](../../../../../../../assets/73306ea8ab72.png)

### Part 4 : Back on App Server

Logged in on app server with ID from IDP ![](../../../../../../../assets/512304074a0c.png)

[ Previous Page Token based authentication  ](how_to_setup_token_based_auth.md) [ Next Page Webhooks  ](webhooks.md)

Last updated 2 months ago 

Was this helpful?
