# Session Defaults

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rcved50nn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Session Defaults

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rcved50nn)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Session Defaults allow users to configurable default values for certain parameters during user sessions.**

Let's assume that you have a multi company setup spanning across different countries then you have to set the 'Company' , 'Country' and 'Currency' fields every time while creating new transactions. This is a very time-consuming process when you have to deal with multiple Sales Orders daily. Hence, instead of putting the value manually, the value set in the Session Defaults gets displayed automatically by default.

  1. How to Create Session Defaults



* * *

### 1.1 Set up the Session Default Settings

  1. Go to Session Default Settings. There you can see a table for Session Defaults.
  2. Click on 'Add Row'.
  3. Select the DocType for which you want to set Session Defaults.
  4. Save.



![Screenshot 2024-05-30 at 1.07.03 PM](https://docs.frappe.io/assets/8f0925e63931.png)

### 1.2 Set up the Session Default Values

  1. Click on the 'Settings' menu in the toolbar. You will find an option 'Session Defaults' there. Click on it.



![Screenshot 2024-05-30 at 1.23.34 PM](https://docs.frappe.io/assets/f2a2e2aff4ee.png) 2\. A 'Session Defaults' prompt will appear. Set the default values for the respective fields and Save.

![Screenshot 2024-05-30 at 1.09.45 PM](https://docs.frappe.io/assets/03c58b5bcc1f.png)

After saving, the default values will be set everywhere.

You can open a new Sales Order and check. The company field is set to the default Company.

![Screenshot 2024-05-30 at 1.12.02 PM](https://docs.frappe.io/assets/189ae5f4fda5.png)

The default currency is also set to INR as defined in the Session Defaults

![Screenshot 2024-05-30 at 1.13.50 PM](https://docs.frappe.io/assets/bf17990e1419.png)

Once you open any report, the default company and currency will be Cooper Hospital and INR respectviely.

![Screenshot 2024-05-30 at 1.15.45 PM](https://docs.frappe.io/assets/b8956600b470.png)

  2. Features



* * *

### 2.1 Defaults cleared on logout

The default values are set for that particular user for the ongoing session. Once logged out, these default values are cleared.

### 2.2 'Settings' button visibility

The Settings button is only visible to the System Manager or to a person having permission to access 'Session Default Settings'. This button navigates you to Session Default Settings where you can add or remove the document types for which you want to set Session Defaults.

![Screenshot 2024-05-30 at 1.21.51 PM](https://docs.frappe.io/assets/e090e8e860e8.png)

### 3\. Related Topics

  1. [Global Defaults](global-defaults.md)
  2. [System Settings](system-settings.md)



[ Previous Page Global Defaults ](global-defaults.md) [ Next Page Domain Settings ](https://docs.frappe.io/erpnext/domain-settings)

Last updated 1 week ago 

Was this helpful?
