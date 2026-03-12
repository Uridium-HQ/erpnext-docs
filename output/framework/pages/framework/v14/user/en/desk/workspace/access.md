# Access

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12nj29ovlt)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Access

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12nj29ovlt)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Workspaces can be restricted based on Modules and Roles.

### Modules

Users can have access to different modules and standard workspaces are visible based on access to those modules.

In the below GIF you can see when Website Module access was removed for user John Doe, he was not able to see Website Workspace. ![Module Access](https://docs.frappe.io/assets/eb58478f84b9.gif)

### Roles

Users can have access to modules but what if you still want those users to not see the standard workspace of that module. Then you can restrict access based on the roles given to that user.

Check below Example:

Jack Doe is a manager with Workspace Manager Role. He only wants user with Website Manager Role to see the Website Workspace.ence such a configuration is made as follows: ![Role Access 1](https://docs.frappe.io/assets/182a0ed4fb9c.gif)

To test this, Jane Doe is given the Website Module access and not given the Website Manager role. Due to the configuration done above, she will not be able to see Website Workspace as shown below. Where as John Doe who has Website Module access and Website Manager role, will be able to see the Website Workspace. ![Role Access 2](https://docs.frappe.io/assets/c5194434bc76.gif)

[ Previous Page Blocks ](blocks.md) [ Next Page Script Report  ](../reports/script-report.md)

Last updated 2 months ago 

Was this helpful?
