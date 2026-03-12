# How To Migrate Doctype Changes To Production

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12b2ai1lgu>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# How To Migrate Doctype Changes To Production 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12b2ai1lgu>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

#### 1\. DocType / Schema Changes

If you are in `developer_mode`, the `.json` files for each **DocType** are automatically updated.

When you update in your production using `--latest` or `bench update`, these changes are updated in the site's schema too!

#### 2\. Permissions

Permissions do not get updated because the user may have changed them. To update permissions, you can add a new patch in the `patches.txt` of your app.

execute:frappe.permissions.reset_perms("[docype]")

[ Previous Page Email Notifications For Failed Background Jobs  ](</framework/v14/user/en/guides/deployment/email-notifications-for-failed-background-jobs>) [ Next Page Migrations ](</framework/v14/user/en/guides/deployment/migrations>)

Last updated 2 months ago 

Was this helpful?
