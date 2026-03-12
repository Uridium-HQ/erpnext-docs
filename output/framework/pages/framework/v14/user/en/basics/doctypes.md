# Understanding DocTypes

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12jebgg68g)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Understanding DocTypes 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12jebgg68g)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

  1. Introduction
  2. [Modules](doctypes/modules.md)
  3. [DocField](doctypes/docfield.md)
  4. [Naming](doctypes/naming.md)
  5. [Controllers](doctypes/controllers.md)


  * [Controller Methods](doctypes/controllers.md)
  * [Controller Hooks](doctypes/controllers.md)


  1. [Child DocType](doctypes/child-doctype.md)
  2. [Single DocType](doctypes/single-doctype.md)
  3. [Virtual DocType](doctypes/virtual-doctype.md)
  4. [Actions and Links](doctypes/actions-and-links.md)
  5. [Customizing DocTypes](doctypes/customize.md)



## Introduction

A DocType is the core building block of any application based on the Frappe Framework. It describes the **Model** and the **View** of your data. It contains what fields are stored for your data, and how they behave with respect to each other. It contains information about how your data is named. It also enables rich **Object Relational Mapper (ORM)** pattern which we will discuss later in this guide. When you create a DocType, a JSON object is created which in turn creates a database table.

> ORM is just an easy way to read, write and update data in a database without writing explicit SQL statements.

#### Conventions

To enable rapid application development, Frappe Framework follows some standard conventions.

  1. DocType is always singular. If you want to store a list of articles in the database, you should name the doctype **Article**.
  2. Table names are prefixed with `tab`. So the table name for **Article** doctype is `tabArticle`.



The standard way to create a DocType is by typing _new doctype_ in the search bar in the **Desk**.

![ToDo DocType](https://docs.frappe.io/assets/838c76d142f0.png) _ToDo DocType_

A DocType not only stores fields, but also other information about how your data behaves in the system. We call this **Meta**. Since this meta-data is also stored in a database table, it makes it easy to change meta-data on the fly without writing much code. Learn more about Meta.

> A DocType is also a DocType. This means that we store meta-data as the part of the data.

After creating a DocType, Frappe can provide many features out-of-the-box. If you go to `/app/todo` you will be routed to the List View in the desk.

![ToDo List](https://docs.frappe.io/assets/2aa0cce35352.png) _ToDo List_

Similarly, you get a Form View at the route `/app/todo/000001`. The Form is used to create new docs and view them.

![ToDo Form](https://docs.frappe.io/assets/3c6bc21bca63.png) _ToDo Form_

[ Previous Page Sites  ](sites.md) [ Next Page Users and Permissions  ](users-and-permissions.md)

Last updated 2 months ago 

Was this helpful?
