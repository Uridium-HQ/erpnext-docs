# Users and Permissions

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12jnbqep3c>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Users and Permissions 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12jnbqep3c>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe comes with a user authentication system. It handles user accounts, role based permissions and cookie based user sessions.

User authentication system in Frappe comes with a lot of features out of the box:

  1. User
  2. Role
  3. DocType Permissions
  4. Permission Level
  5. Role Permission Manager
  6. User Permissions
  7. Restricting Views and Forms
  8. Password Hashing
  9. Password strength checking
  10. Throttling of login attempts
  11. Third party authentication like OAuth, Google, Facebook, etc



## User and Role

A User record represents an authenticated user who can perform authorized actions in the system. A User can have multiple roles assigned to it. A Role describes what actions a User can perform on a DocType.

![User Roles](/files/user-roles.png) _User Roles_

For example, the role **Blogger** has read, write and create permission on the doctype **Blog Post** , but only read permission on **Blog Category**.

![Role Blogger](/files/role-blogger.png) _Role Blogger_

## DocType Permissions

DocTypes can have a default set of Roles applied when you install your app. To configure roles for a DocType you must add them in the Permissions table in DocType.

![DocType Permissions](/files/doctype-permissions.png) _DocType Permissions_

If you expand the row, you will see many more options that can be configured. ![DocType Permissions Row](/files/doctype-permissions-detail.png) _DocType Permissions_

Here is a list of them with their explanation:

Option | Explanation  
---|---  
Level | Permission Level assigned to this role  
If the user is owner | The restrictions will apply only if the user is the one who created that document  
Read | Allow read access to the document  
Write | Allow edit access to the document  
Create | Allow create access to the document  
Delete | Allow user to delete the document  
Submit | Allow user to submit the document  
Cancel | Allow user to cancel the document  
Amend | Allow user to amend the document  
Report | Allow user to view the report view  
Export | Allow user to export records in Excel/CSV  
Import | Allow user to import records using the Data Import Tool  
Set User Permissions | Allow user to apply user permissions for other users  
Share | Allow user to share the document with other users  
Print | Allow user to print the document or generate PDF  
Email | Allow user to send emails for that document  
  
## Permission Level

Permission Levels can be used to group fields in a document and apply separate roles to each level. By default all fields have permlevel set as 0.

![Permission Level](/files/permission-level.png) _Permission Level_

## Role Permissions Manager

Role Permissions Manager is a user tool to manage role permissions. The default set of permissions show up here and can be overridden.

![Role Permissions Manager](/files/role-permissions-manager.gif)

## User Permissions

User Permissions are another set of rules that can be applied per user basis. It can be used to restrict documents which contain a specific value for a Link field.

For example, to restrict the User John such that he can only view **Blog Post** s that were created by him, i.e, Blogger **John**. A user permission record with the following values should be created.

![User Permissions Example](/files/user-permissions-example-1.png) _User Permission Record_

After creating the user permission configuration, when the User logs in to see the Blog Post list, he will have a restricted view of blog posts that were created by him.

![Restricted Blog Post List](/files/user-permissions-example-2.png) _Restricted Blog Post List_

## Restricting Views and Forms

Frappe Framework allows you to configure what modules, doctypes and views are visible to the user. To configure which modules are shown to a user go to the **Allow Modules** section of the User form.

![Allow Modules in User](/files/allow-modules-in-user.png)

To hide a doctype from a User, remove the read permission from a Role using the Role Permissions Manager.

To control permissions for Pages and Reports, use the **Role Permission for Page and Report** tool.

![Role Permission for Page and Report](/files/role-permission-for-page-and-report.png)

## Password Hashing

Frappe handles password hashing out of the box. They are encrypted and saved in a separate database table named `__Auth`.
[code] 
    MariaDB [_baa0f26509a564b6]> select * from __Auth;
    +---------+------------------+-----------+-----------------------------------------------
    | doctype | name | fieldname | password
    +---------+------------------+-----------+-----------------------------------------------
    | User | Administrator | password | $pbkdf2-sha256$29000$Xss5pxSC8F5rDSHEOEdo7Q$in
    | User | test@erpnext.com | password | $pbkdf2-sha256$29000$y7mXMoZQau09RwiBsLaWsg$h.
    +---------+------------------+-----------+-----------------------------------------------
    
[/code]

## Password Policy

Frappe also supports password strength checking. It can be enabled from **System Settings** in the Security section. The Minimum Password Score field validates how strong the password should be.

![Password Policy](/files/password-policy.png) _Password Policy_

## Login Attempts

Frappe allows you to configure how many consecutive login attempts should be allowed before locking the account for a set time period.

![Login Attempts](/files/login-attempts.png)

## Third Party Authentication

Frappe supports third party login providers. To setup a login provider you need to setup a **Social Login Key**. Learn more about it [here](</framework/v14/user/en/guides/integration/social_login_key>).

[ Previous Page Understanding DocTypes  ](</framework/v14/user/en/basics/doctypes>) [ Next Page Asset Bundling  ](</framework/v14/user/en/basics/asset-bundling>)

Last updated 2 months ago 

Was this helpful?
