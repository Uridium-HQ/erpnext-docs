# Single DocType

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12l1hmpcin>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Single DocType 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12l1hmpcin>)

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



[ Previous Page Child / Table DocType ](</framework/v14/user/en/basics/doctypes/child-doctype>) [ Next Page Virtual DocTypes ](</framework/v14/user/en/basics/doctypes/virtual-doctype>)

Last updated 2 months ago 

Was this helpful?
