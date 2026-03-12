# Setting Up Dropbox Backups

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0s6vo4r0vn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Setting Up Dropbox Backups

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0s6vo4r0vn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

We always recommend customers to maintain backup of their data in ERPNext. The database backup is downloaded in the form of an SQL file. If needed, this SQL file of backup can be restored in the another ERPNext account as well.

You can automate database backup download of your ERPNext account into your Dropbox account.

> Note: If you are Frappe Cloud user, onsite and offsite backups are automatically created for you: <https://frappecloud.com/docs/sites/backups> > >

To setup Dropbox Backup, > Home > Integrations > Dropbox Settings

#### Step 1: Login to Dropbox Developer area

<https://www.dropbox.com/developers/apps>

#### Step 2: Create a new Dropbox app

![Create new](https://docs.frappe.io/assets/a60b901276b3.png)

#### Step 3: Fill in the details for your new app

![Choose Dropbox API and type as APP Folder](https://docs.frappe.io/assets/2fa963872827.png) ![Setup APP Name](https://docs.frappe.io/assets/850f1a4460a1.png)

![https://support.frappe.io/files/nBdh7wu.png](https://docs.frappe.io/assets/e5a49ffe5aee.png)

#### Step 4: Insert your custom domain Redirect URI

`https://{yourwebsite.com}/api/method/frappe.integrations.doctype.dropbox_settings.dropbox_settings.dropbox_auth_finish` ![Set Redirect URL](https://docs.frappe.io/assets/ea5db36292cc.png)

#### Step 5: In a new window, open the Dropbox Settings page in your ERPnext installation

#### Step 6: Set backup frequency and email

Set the frequency to download your site backups to your Dropbox account. ![set frequency](https://docs.frappe.io/assets/2015949c2d6d.png)

#### Step 7: Input Keys from your Dropbox App window

From your Dropbox App page, enter the app key and (unhidden) app secret into the ERPnext Dropbox settings page.

Alternatively, you can enter it manually in `sites/{sitename}/site_config.json` as follows,
[code] 
           {
     "db_name": "demo",
     "db_password": "DZ1Idd55xJ9qvkHvUH",
     "dropbox_access_key": "ACCESSKEY",
     "dropbox_secret_key": "SECRECTKEY"
    }
    
        
    
[/code]

#### Step 8: Click Save before continuing

#### Step 9: After saving, click "Allow Dropbox Access"

The Dropbox login page will open in the new tab. This might require you to allow pop-up for your ERPNext account.

#### Step 11: Allow Dropbox Access

On successful login, you will find a confirmation message as following. Click on "Allow" to let your ERPNext account have access to your Dropbox account. ![Allow](https://docs.frappe.io/assets/259b07dafc1e.png)

#### Step 12: Confirm Backups Work

From the ERPnext Dropbox page, click `Take Backup Now` and then go to you Dropbox files view. You should see a new folder in Dropbox named `Apps` and inside of it your {New App} folder. Inside of it should be backup folders for both files and database. So for an app named `erpnext`, following are the folder locations:
[code] 
    Database files: /Apps/erpnext/database
    Public files: /Apps/erpnext/files
    Private files: /Apps/erpnext/private/files
      
    
    
[/code]

> **Note** : If the compressed backup size exceeds 1GB (Gigabyte), the system will upload the latest available backup to Dropbox instead of generating a new backup file.

[ Previous Page Google Contacts Integration  ](https://docs.frappe.io/erpnext/google_contacts) [ Next Page Google Maps Integration  ](https://docs.frappe.io/erpnext/google_maps)

Last updated 1 week ago 

Was this helpful?
