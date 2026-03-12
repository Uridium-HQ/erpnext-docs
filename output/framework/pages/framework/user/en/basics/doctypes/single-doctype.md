# Single DocType

[ Edit ](</wiki/spaces/1u8fslkdg6/page/0tk9suc90i>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Single DocType 

[ Edit ](</wiki/spaces/1u8fslkdg6/page/0tk9suc90i>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

A Single DocType is a DocType that has only one instance in the database. It is useful for persisting things like _System Settings_ , which don't make sense to have multiple records.

![Single DocType](/files/single-doctype.png)
[code] 
    >>> settings = frappe.get_doc('System Settings')
    >>> settings.notification_frequency
    'Daily'
    
[/code]

### Schema

Single DocTypes are stored in the `tabSingles` table in the database, with each property having its own record.

Columns:

  * `doctype`
  * `field`
  * `value`



[ Previous Page Child / Table DocType ](</framework/user/en/basics/doctypes/child-doctype>) [ Next Page Virtual DocTypes ](</framework/user/en/basics/doctypes/virtual-doctype>)

Last updated 3 weeks ago 

Was this helpful?
