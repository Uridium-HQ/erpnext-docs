# Insert A Document Via Api

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/1298i9k0oq)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Insert A Document Via Api 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/1298i9k0oq)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

You can insert documents via a script using the `frappe.get_doc` method

### Examples:

#### 1\. Insert a ToDo

todo = frappe.get_doc({"doctype":"ToDo", "description": "test"}) todo.insert()

* * *

#### 2\. Insert without the user's permissions being checked:

todo = frappe.get_doc({"doctype":"ToDo", "description": "test"}) todo.insert(ignore_permissions = True)

* * *

#### 3\. Submit after inserting

todo = frappe.get_doc({"doctype":"ToDo", "description": "test"}) todo.insert(ignore_permissions=True) todo.submit()

* * *

#### 4\. Insert a document on saving of another document

class MyType(Document): def on_update(self): todo = frappe.get_doc({"doctype":"ToDo", "description": "test"}) todo.insert()

* * *

#### 5\. Insert a document with child tables:

sales_order = frappe.get_doc({ "doctype": "Sales Order", "company": "_Test Company", "customer": "_Test Customer", "delivery_date": "2013-02-23", "sales_order_details": [ { "item_code": "_Test Item Home Desktop 100", "qty": 10.0, "rate": 100.0, "warehouse": "_Test Warehouse - _TC" } ] }) sales_order.insert()

[ Previous Page Custom Module Icon  ](custom-module-icon.md) [ Next Page How To Create Custom Fields During App Installation  ](how-to-create-custom-fields-during-app-installation.md)

Last updated 2 months ago 

Was this helpful?
