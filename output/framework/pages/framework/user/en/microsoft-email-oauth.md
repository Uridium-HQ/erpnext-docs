# Microsoft Office365 Email OAuth

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0u4pjdmfrc)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Microsoft Office365 Email OAuth

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0u4pjdmfrc)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

* * *

This guide helps in authenticating an outlook email account in frappe.

> Note: The user should log in as the Email Account User in their Frappe account. For example, if the email account is test@example.com, then they should log in using the user test@example.com on the site.

  1. Go to your Frappe instance and create a **New Connected App** and save it (just enter the name and save) and copy the Redirect URI for later.



![](../../../../assets/723d364fc499.png) ![](../../../../assets/ed9939b5074b.png)

  2. Login to [Microsoft Azure](https://portal.azure.com/), search for and select **Microsoft Entra ID** (formerly called **Azure Active Directory**).



![](../../../../assets/fcd00fa3191f.png)

  3. Click **Add** -> **App registration**



![](../../../../assets/c4760ee607cc.png)

  4. Enter the respective details (app name, account type), paste the previously copied redirect URI from Frappe instance and select the platform as “Web”.



![](../../../../assets/99e38fddc5be.png)

To know more about the account types, click [here](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

  5. Click on Register and you’ll be redirected to your created app. Copy your **Application ID** \- it’s the Client ID you'll need to paste into your Connected App on your Frappe instance.



![](../../../../assets/8a862cd95f18.png)

  6. Head over to **API Permission** section in your app and add Microsoft Graph permissions.



![](../../../../assets/64e0394577af.png)

  7. Select **Delegated Permissions** for `IMAP.AccessAsUserAll`, `SMTP.Send` and `offline_access`, then click "Add permissions"



![](../../../../assets/30dbb4a13d16.png) ![](../../../../assets/ec4143edc962.png) ![](../../../../assets/d608927642a1.png) ![](../../../../assets/1b3ecf778374.png)

  8. Head over to **Certificates & Secrets** to create a Client Secret



![](../../../../assets/4438a9ff2069.png)

Add description and click on add to see a newly generated client secret.

![](../../../../assets/e56f17a577df.png)

Copy over the **Value** \- paste this in the `Client Secret` field in the new Connected App on your Frappe instance.

![](../../../../assets/f971eede5972.png)

  9. Click on "Endpoints" and copy "OpenID Connect metadata document". This should be pasted into the "OpenID Configuration" field of your Frappe Connected App. After that, click "Get OpenID Configuration" on the Connected App, that will populate the endpoints.



![](../../../../assets/0c5b2d74b86d.png) ![](../../../../assets/1120882a4e9b.png) ![](../../../../assets/e10af24d4766.png)

Then, add these scopes, and save the document.

  * `https://outlook.office.com/IMAP.AccessAsUser.All`
  * `https://outlook.office.com/SMTP.Send`
  * `offline_access`


  10. Click on the “**Connect to {your connected app name}** ” button on top right which should start the Oauth flow for Microsoft.



**Make sure the email account you’re authorizing is going to be the same as the one you’re going to add in frappe.**

  11. If everything goes as planned, you’ll be redirected back to your Connected App page and should be able to see Token Cache connected to your connected app, head over to your created token cache to check if you have both refresh and access token.



![](../../../../assets/b338fc9e944b.png)

![](../../../../assets/42dd1be7a92e.gif)

  12. Head over to Email Account doctype and create a new Email Account. And select the method as Oauth and add your connected app and user which has created the token cache and set up your email account as usual.



![](../../../../assets/463f1b12cf21.png)

Please ensure IMAP/POP connections are allowed on your Microsoft account. You can find information regarding that, as well as the settings for outlook servers over here: <https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-8361e398-8af4-4e97-b147-6c6c4ac95353>

NOTE: Microsoft restricts sending from any other email address other than the one which authenticated it. For that you can check these 2 options in the email account document itself

![](../../../../assets/7f943fe79da3.png)

* * *

Please visit Microsoft’s official documentation for any Additional Info: <https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth>

* * *

### Service Principal Authentication

Email Accounts require access as a User. This disallowed the use of Shared Mailboxes dedicated to Frappe, as Full Access permissions would need to be granted to the user signing into Frappe.

This feature lets Frappe authenticate itself to e.g. Exchange Online, so it can send and receive emails from the Shared Mailbox, without having to delegate Full Access permissions to each user that accesses Frappe.

If you wish to authenticate using this method, there's a checkbox available in `Email Account`

![](../../../../assets/f24c78ad8865.png)

[ Previous Page Setting up LDAP ](https://docs.frappe.io/framework/user/en/integration/ldap-integration) [ Next Page OAuth2 ](../../oauth2.md)

Last updated 3 weeks ago 

Was this helpful?
