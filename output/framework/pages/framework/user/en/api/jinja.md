# Jinja API

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0tlbc050bu)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Jinja API 

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0tlbc050bu)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

These are the whitelisted methods that frappe provides to use them in Jinja Templates.

## frappe.format

`frappe.format(value, df, doc)`

Formats a raw value (stored in database) to a user presentable format. For example, convert 2019-09-08 to 08-09-2019

Usage
[code] 
    {{ frappe.format('2019-09-08', {'fieldtype': 'Date'}) }}
    
    09-08-2019
    
[/code]

## frappe.format_date

`frappe.format_date(date_string)`

Formats date into a human readable long format.

Usage
[code] 
    {{ frappe.format_date('2019-09-08') }}
    
    September 8, 2019
    
[/code]

## frappe.get_url

`frappe.get_url()`

Returns the site url

Usage
[code] 
    {{ frappe.get_url() }}
    
    https://frappe.io
    
[/code]

## frappe.get_doc

`frappe.get_doc(doctype, name)`

Returns a document by its name.

Usage
[code] 
     {% set doc = frappe.get_doc('Task', 'TASK00002') %}
     {{ doc.title }} - {{ doc.status }}
    
    
    
     Buy Eggs - Open
    
    
[/code]

## frappe.get_all

`frappe.get_all(doctype, filters, fields, order_by, start, page_length, pluck)`

Returns a list of all records of a DocType. Only returns the document `name`s if the `fields` argument is not given.

Signature
[code] 
    frappe.get_all(doctype, filters, fields, order_by, start, page_length)
    
[/code]

Usage
[code] 
     {% set tasks = frappe.get_all('Task', filters={'status': 'Open'}, fields=['title', 'due_date'], order_by='due_date asc') %}
     {% for task in tasks %}
     
    ### {{ task.title }}
    
    
    Due Date: {{ frappe.format_date(task.due_date) }}
    
    
    
     {% endfor %}
    
    
    
    
    ### Redesign Website
    
    
    Due Date: September 8, 2019
    
    
    
    
    ### Add meta tags on websites
    
    
    Due Date: September 22, 2019
    
    
    
    
    
[/code]

## frappe.get_list

`frappe.get_list(doctype, filters, fields, order_by, start, page_length)`

Similar to `frappe.get_all` but will filter records for the current session user based on permissions.

## frappe.db.get_value

`frappe.db.get_value(doctype, name, fieldname)`

Returns a single field value (or a list of values) from a document.

Usage
[code] 
    
     {% set company_abbreviation = frappe.db.get_value('Company', 'TennisMart', 'abbr') %}
     {{ company_abbreviation }}
     
    
     {% set title, description = frappe.db.get_value('Task', 'TASK00002', ['title', 'description']) %}
     ### {{ title }}
    
    
    {{ description }}
    
    
    
    
    
    
    TM
    
    
[/code]

## frappe.db.get_single_value

`frappe.db.get_single_value(doctype, fieldname)`

Returns a field value from a Single DocType.

Usage
[code] 
    
     {% set timezone = frappe.db.get_single_value('System Settings', 'time_zone') %}
     {{ timezone }}
     
    
    
    
    
     Asia/Kolkata
     
    
    
[/code]

## frappe.get_system_settings

`frappe.get_system_settings(fieldname)`

Returns a field value from System Settings.

Usage
[code] 
     {% if frappe.get_system_settings('country') == 'India' %}
     Pay via Razorpay
     {% else %}
     Pay via PayPal
     {% endif %}
    
    
    
    Pay via Razorpay
    
    
[/code]

## frappe.get_meta

`frappe.get_meta(doctype)`

Returns a doctype meta. It contains information like fields, title_field, image_field, etc.

Usage
[code] 
    
     {% set meta = frappe.get_meta('Task') %}
     Task has {{ meta.fields | len }} fields.
     {% if meta.get_field('status') %}
     It also has a Status field.
     {% endif %}
     
    
    
    
    
     Task has 18 fields. It also has a Status field.
     
    
    
[/code]

## frappe.get_fullname

`frappe.get_fullname(user_email)`

Returns the fullname of the user email passed. If user is not passed, assumes current logged in user.

Usage
[code] 
    The fullname of faris@erpnext.com is {{ frappe.get_fullname('faris@erpnext.com') }}
    The current logged in user is {{ frappe.get_fullname() }}
    
    
    
    The fullname of faris@erpnext.com is Faris Ansari
    The current logged in user is John Doe
    
    
[/code]

## frappe.render_template

`frappe.render_template(template_name, context)`

Render a jinja template string or file with context.

Usage
[code] 
    
     {{ frappe.render_template('templates/includes/footer/footer.html', {}) }}
    
     
    {{ frappe.render_template('{{ foo }}', {'foo': 'bar'}) }}
    
    
    
    
    
    
    
    
    bar
    
    
    
    
[/code]

## frappe._

`frappe._(string)` or `_(string)`

Usage
[code] 
    {{ _('This string should get translated') }}
    
    
    
    
    
    इस तार का अनुवाद होना चाहिए
    
    
    
    
[/code]

## frappe.session.user

Returns the current session user

## frappe.session.csrf_token

Returns the current session's CSRF token

## frappe.form_dict

If the template is being evaluated in a web request, `frappe.form_dict` is a dict of query parameters, else it is `None`.

## frappe.lang

Current language used by the translation function. Two letter, lowercase code.

[ Previous Page Database API ](database.md) [ Next Page Request Lifecycle  ](../python-api/routing-and-rendering.md)

Last updated 3 weeks ago 

Was this helpful?
