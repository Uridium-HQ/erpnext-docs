# Hooks

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12tib8not4)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Hooks 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12tib8not4)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Hooks allow you to "hook" into functionality and events of core parts of the Frappe Framework. This page documents all of the hooks provided by the framework.

> Jump to list of all available hooks in Frappe.

## How does hooks work?

Hooks are places in the core code that allow an app to override the standard implementation or extend it. Hooks are defined in **hooks.py** of your app.

Let's learn by example. Add the following hooks in your app's **hooks.py**.
[code] 
    test_string = "value"
    test_list = ["value"]
    test_dict = {
     "key": "value"
    }
    
[/code]

Now, open the python console by running the command `bench --site sitename console` and run the following lines:
[code] 
    ❯ bench --site sitename console
    Apps in this namespace:
    frappe, frappe_docs
    
    In [1]: frappe.get_hooks("test_string")
    Out[1]: ["value"]
    
    In [2]: frappe.get_hooks("test_dict")
    Out[2]: {"key": ["value"]}
    
    In [3]: frappe.get_hooks("test_list")
    Out[3]: ["value"]
    
[/code]

When you call `frappe.get_hooks`, it will convert all the values in a list. This means that if the hook is defined in multiple apps, the values will be collected from those apps. This is what enables the cascading nature of hooks.

Now, the hook value can be consumed in different ways. For example, for including JS assets using `app_include_js`, all of the values are included. But for overriding whitelisted method, the last value in the list is used.

So the implementation of the hook is totally dependent on how the author of the feature intended it to be used.

## How are conflicting hooks resolved?

Hooks are resolved using "last writer wins" strategy. Last installed app on site will have highest priority over others.

  * When the hook overrides existing behaviour like overriding a class then only overrides from last app will work.
  * When the hook extends behaviour then extensions will be applied in order of installation on the site.



> If you need to change this order you can do so by going to "Installed Applications" page and clicking on "Update Hooks Resolution Order"

## App Meta Data

These are automatically generated when you create a new app. Most of the time you don't need to change anything here.

  1. `app_name` \- slugified name of the app
  2. `app_title` \- presentable app name
  3. `app_publisher`
  4. `app_description`
  5. `app_version`
  6. `app_icon`
  7. `app_color`



## Javascript / CSS Assets

The following hooks allow you to inject static JS and CSS assets in various parts of your site.

### Desk

These hooks allow you to inject JS / CSS in `desk.html` which renders the [Desk](../desk.md).
[code] 
    # injected in desk.html
    app_include_js = "assets/js/app.min.js"
    app_include_css = "assets/js/app.min.css"
    
    # All of the above support a list of paths too
    app_include_js = ["assets/js/app1.min.js", "assets/js/app2.min.js"]
    
[/code]

### Portal

These hooks allow you to inject JS / CSS in `web.html` which renders the [Portal](../portal-pages.md).
[code] 
    # injected in the web.html
    web_include_js = "assets/js/app-web.min.js"
    web_include_css = "assets/js/app-web.min.css"
    # All of the above support a list of paths too
    web_include_js = ["assets/js/web1.min.js", "assets/js/web2.min.js"]
    
[/code]

### Web Form

These hooks allow you to add inject static JS and CSS assets in `web_form.html` which is used to render Web Forms. These will work only for Standard Web Forms.
[code] 
    webform_include_js = {"ToDo": "public/js/custom_todo.js"}
    webform_include_css = {"ToDo": "public/css/custom_todo.css"}
    
[/code]

> For user created Web Forms, you can directly write the script in the form itself.

### Page

These hooks allow you to inject JS assets in Standard Desk Pages.
[code] 
    page_js = {"page_name" : "public/js/file.js"}
    
[/code]

For e.g., Background Jobs is a standard page that is part of Core module in Frappe Framework. To add custom behaviour in that page you can add a JS file in your custom app `custom_app/public/js/custom_background_jobs.js` and add the following line in your hooks file.

**custom_app/hooks.py**
[code] 
    page_js = {"background_jobs": "public/js/custom_background_jobs.js"}
    
[/code]

## Sounds

Frappe ships with a set of audio notifications for events like a success action, document submission, error, etc. You can add your own sounds using the `sounds` hook.

**app/hooks.py**
[code] 
    sounds = [
     {"name": "ping", "src": "/assets/app/sounds/ping.mp3", "volume": 0.2}
    ]
    
[/code]

You can play your added sound using the client utility method:
[code] 
    frappe.utils.play_sound("ping")
    
[/code]

## Install Hooks

These hooks allow you to run code before and after installation of your app. For example, [ERPNext](https://github.com/frappe/erpnext) has these [defined](https://github.com/frappe/erpnext/blob/ecfa6344c02b18455637455742202c7fadf1b35d/erpnext/hooks.py).
[code] 
    # python module path
    before_install = "app.setup.install.before_install"
    after_install = "app.setup.install.after_install"
    after_sync = "app.setup.install.after_sync"
    
[/code]

**app/setup/install.py**
[code] 
    # will run before app is installed on site
    def before_install():
     pass
    
    # will run after app is installed on site
    def after_install():
     pass
    
    # will run after app fixtures are synced
    def after_sync():
     pass
    
[/code]

## Uninstall Hooks

These hooks allow you to run code before and after uninstallation of your app.

**app/hooks.py**
[code] 
    before_uninstall = "app.setup.uninstall.before_uninstall"
    after_uninstall = "app.setup.uninstall.after_uninstall"
    
[/code]

**app/setup/uninstall.py**
[code] 
    # will run before app is uninstalled from site
    def before_uninstall():
     pass
    
    # will run after app is uninstalled from site
    def after_uninstall():
     pass
    
[/code]

## Migrate Hooks

These hooks allow you to run code before and after a migration is run on your site via the command `bench --site sitename migrate`.

**app/hooks.py**
[code] 
    before_migrate = "app.migrate.before_migrate"
    after_migrate = "app.migrate.after_migrate"
    
[/code]

**app/migrate.py**
[code] 
    def after_migrate():
     # run code after site migration
     pass
    
[/code]

## Test Hooks

This hook allows you to run code before tests are run on a site. You can use this hook to add seed data to your database which will be available to your tests.

**app/hooks.py**
[code] 
    before_tests = "app.tests.before_tests"
    
[/code]

**app/migrate.py**
[code] 
    def before_tests():
     # add seed data to the database
     pass
    
[/code]

## File Hooks

These hooks allows you to change the implementation of handling user uploaded files.

**app/hooks.py**
[code] 
    before_write_file = "app.overrides.file.before_write"
    write_file = "app.overrides.file.write_file"
    delete_file_data_content = "app.overrides.file.delete_file"
    
[/code]

**app/overrides/file.py**
[code] 
    # will run before file is written to disk
    def before_write():
     pass
    
    # will override the implementation of writing file to disk
    # can be used to upload files to a CDN instead of writing
    # the file to disk
    def write_file():
     pass
    
    
    # will override the implementation of deleting file from disk
    # can be used to delete uploaded files from a CDN instead of
    # deleting file from disk
    def delete_file():
     pass
    
[/code]

## Email Hooks

These hooks allows you to change the default email module implementation of sending emails and setting default sender address.

**app/hooks.py**
[code] 
    override_email_send = "app.overrides.email.send"
    get_sender_details = "app.overrides.email.get_sender_details"
    
[/code]

By default frappe uses the currently logged in users name and id as sender details on all emails. This can be overriden with `get_sender_details` hook. And if you want to extend the email modules functionality by using a thirdy party server or app for sending emails then you can use `override_email_send` hook. This hook will send all the email information (sender, recipient, content(mime)) to a function in custom_app.

**app/overrides/email.py**
[code] 
    # will be edited as "John Doe "
    def get_sender_details():
     return "John Doe", "johndoe@gmail.com"
    
    # self - EmailQueue object refrence for updating status
    def send(self, sender, recipient, msg):
     # smtp or http request
     self.update_status("Sending")
    
[/code]

> Note: You'll have to handle the status change of email queue in your custom app depending on the webhook response you get from your mail provider/server

## Extend Bootinfo

After a successful login, the Desk is injected with a dictionary of global values called `bootinfo`. The `bootinfo` is available as a global object in Javascript as `frappe.boot`.

The `bootinfo` dict contains a lot of values including:

  * System defaults
  * Notification status
  * Permissions
  * User settings
  * Language and timezone info



You can add global values that makes sense for your app via the `extend_bootinfo` hook.
[code] 
    # python module path
    extend_bootinfo = "app.boot.boot_session"
    
[/code]

The method is called with one argument `bootinfo`, on which you can directly add/update values.

**app/boot.py**
[code] 
    def boot_session(bootinfo):
     bootinfo.my_global_key = "my_global_value"
    
[/code]

Now, you can access the value anywhere in your client side code.
[code] 
    console.log(frappe.boot.my_global_key)
    
[/code]

## Website Context

When a Portal Page is rendered, a dictionary is built with all of the possible variables that the page might need to render. This dict is also known as `context`. You can use these hooks to add or modify values in this dict.

**app/hooks.py**
[code] 
    website_context = {
     "favicon": "/assets/app/image/favicon.png"
    }
    update_website_context = "app.overrides.website_context"
    
[/code]

The `website_context` hook is a simple dict of key value pairs. Use this hook for simple value overrides.

You can use the `update_website_context` hook for more complex scenarios as it allows you to manipulate the context dict in a python method. The method is called with one argument, which is the `context` dict. You can either modify the context directly by mutating it or return a dict that will be merged with `context`.

**app/overrides.py**
[code] 
    def website_context(context):
     context.my_key = "my_value"
    
[/code]

## Website Controller Context

Frappe ships with standard web pages like `/404` and `/about`. If you want to extend the controller context for these pages you can use the `extend_website_page_controller_context` hook.

**app/hooks.py**
[code] 
    extend_website_page_controller_context = {
     "frappe.www.404": "app.pages.context_404"
    }
    
[/code]

The above hook configuration will allow you to extend the context of the 404 page so that you can add your own keys or modify existing ones.

**app/pages.py**
[code] 
    def context_404(context):
     # context of the 404 page
     context.my_key = "my_value"
    
[/code]

## Website Clear Cache

Frappe Framework caches a lot of static web pages for fast subsequent rendering. If you have created web pages that use cached values, and you want to invalidate the cache, this hook is place to do it.

**app/hooks.py**
[code] 
    website_clear_cache = "app.overrides.clear_website_cache"
    
[/code]

The method is called with one argument `path`. `path` is set when cache is being cleared for one route, and is `None` when cache is cleared for all routes. You need to handle this case if your cache is page specific.

**app/overrides.py**
[code] 
    def clear_website_cache(path=None):
     if path:
     # clear page related cache
     else:
     # clear all cache
    
[/code]

## Website Redirects

Website Redirects allow you to define redirects from one route to another. Frappe will generate a 304 Redirect response when the source URL is requested and redirect to the target URL. You can redirect plain URLs or you can use regex to match your URLs.

**app/hooks.py**
[code] 
    website_redirects = [
     {"source": "/compare", "target": "/comparison"},
     {"source": "/docs(/.*)?", "target": "https://docs.tennismart.com/\1"},
     {"source": r'/items/item\?item_name=(.*)', "target": '/items/\1', match_with_query_string=True},
    ]
    
[/code]

The above configuration will result in following redirects:

  * `/compare` to `/comparison`
  * `/docs/getting-started` to `https://docs.tennismart.com/getting-started`
  * `/docs/help` to `https://docs.tennismart.com/help`
  * `/items/item?item_name=racket` to `https://docs.tennismart.com/items/racket`



## Website Route Rules

Website Route Rules allow you to map URLs to custom controllers. This is commonly used to generate clean URLs for pages.

Let's say you want to have `/projects` route to display list of projects. This can be done by creating a `projects.html` and `projects.py` in `www` folder.

You also want to have `/project/` route to show a project page where name is the dynamic. To do this you can use the `website_route_rules` hook.

**app/hooks.py**
[code] 
    website_route_rules = [
     {"from_route": "/projects/", "to_route": "app/projects/project"},
    ]
    
[/code]

Now, you can create your controller files in `app/projects` folder.

**app/projects/project.py**
[code] 
    def get_context(context):
     project_name = frappe.form_dict.name
     project = frappe.get_doc("Project", project_name)
     context.project = project
    
[/code]

**app/projects/project.html**
[code] 
    {{ project.title }}
    ===================
    
    
    {{ project.description }}
    
    
    
[/code]

## Website 404

Frappe renders a default `/404` route when a page is not found. You can change this using the `website_catch_all` hook.

**app/hooks.py**
[code] 
    website_catch_all = "not_found"
    
[/code]

The above configuration will render `/not_found` when a 404 is occurred. It is upto you to implement the template `www/not_found.html` and controller `www/not_found.py`.

## Default Homepage

Homepage is the page which is rendered when you visit the root URL (`/`) of your site. There are multiple ways to configure what page is rendered as the default homepage.

By default, the homepage is `index`. So, frappe will try to render `index.html` from `www` folder. This can be overridden using the `homepage` hook.

**app/hooks.py**
[code] 
    homepage = "homepage"
    
[/code]

The above configuration will load the `www/homepage.html` as the default homepage.

You can also have role based homepage by using the `role_home_page` hook.

**app/hooks.py**
[code] 
    role_home_page = {
     "Customer": "orders",
     "Supplier": "bills"
    }
    
[/code]

The above configuration will make `/orders` the default homepage for users with the **Customer** role and `/bills` for users with the **Supplier** role.

You can have even more control over the logic by using the `get_website_user_home_page` hook.

**app/hooks.py**
[code] 
    get_website_user_home_page = "app.website.get_home_page"
    
[/code]

**app/website.py**
[code] 
    def get_home_page(user):
     if is_projects_user(user):
     return "projects"
     if is_partner(user):
     return "partner-dashboard"
     return "index"
    
[/code]

> If all of these hooks are defined, the `get_website_user_home_page` will have higher priority over the others, and `role_home_page` will have higher priority over `homepage`.

## Portal Sidebar

Some Portal views are shown with a sidebar with links to quickly jump to pages. These sidebar items can be customized via hooks.

**app/hooks.py**
[code] 
    portal_menu_items = [
     {"title": "Dashboard", "route": "/dashboard", "role": "Customer"},
     {"title": "Orders", "route": "/orders", "role": "Customer"},
    ]
    
[/code]

The above configuration will add two sidebar links for users with the role Customer.

![Portal Sidebar](https://docs.frappe.io/assets/f05a38a8c785.png)

These sidebar items are hardcoded in your app so they are not customizable from Desk. For e.g., if you want to hide a sidebar link temporarily you will have to make changes in your code.

There is another hook called `standard_portal_menu_items` which allows you to do that. The sidebar links set in `standard_portal_menu_items` hook will be synced with the database.

**app/hooks.py**
[code] 
    standard_portal_menu_items = [
     {"title": "Dashboard", "route": "/dashboard", "role": "Website Manager"},
     {"title": "Orders", "route": "/orders", "role": "Website Manager"},
    ]
    
[/code]

The above configuration will sync sidebar items to the Portal Settings which can later be edited by any System User.

![Portal Settings](https://docs.frappe.io/assets/f65520ab3514.png)

## Brand HTML

This hook allows you to customize the brand logo in the navbar of your website.

**app/hooks.py**
[code] 
    brand_html = '![](https://docs.frappe.io/framework/v14/user/en/python-api/tennismart.png) TennisMart'
    
[/code]

If the `brand_html` is defined, it will override the default brand html in the navbar. It is not recommended to use hooks to change your brand logo, unless you want to version control it, otherwise you can use Website Settings to change it.

## Base Template

When a web page is rendered, it extends `templates/base.html` by default. You can override the base template by overriding the `base_template` hook.

**app/hooks.py**
[code] 
    base_template = "app/templates/my_custom_base.html"
    
[/code]

You can also customize base templates based on routes. For e.g., if you want to use a different base template for all the routes that start with `docs/*` then you can use the `base_template_map` hook. The key must be a regex that matches the route. All other routes will fallback to the default base template.

**app/hooks.py**
[code] 
    base_template_map = {
     r"docs.*": "app/templates/doc_template.html"
    }
    
[/code]

## Integrations

These hooks allow you to customize behaviour of 3rd-party integrations in Frappe.

### Braintree Success Page

This hook allows you to override the default redirect URL on successful payment of Braintree transaction.

**app/hooks.py**
[code] 
    braintree_success_page = "app.integrations.braintree_success_page"
    
[/code]

The method is called with one argument `data` which has the meta data of the payment.

**app/integrations.py**
[code] 
    def braintree_success_page(data):
     # data.reference_doctype
     # data.reference_docname
     return "/thank-you"
    
[/code]

## Calendars

The calendar hook is a list of doctype names which are shown as menu items for quick navigation from the Calendar page in Desk.

**app/hooks.py**
[code] 
    calendars = ["Appointment"]
    
[/code]

![Event Menu Shortcuts](https://docs.frappe.io/assets/d31e662f3266.png)

## Clear Cache

This hook allows you to clear your app specific cache values when the global cache is being cleared by frappe.

**app/hooks.py**
[code] 
    clear_cache = "app.cache.clear_cache"
    
[/code]

You can use this hook to clear your app specific cache. The method is called without any arguments.

**app/cache.py**
[code] 
    def clear_cache():
     frappe.cache().hdel("app_specific_cache")
    
[/code]

## Default Mail Footer

If you want to set the default footer of all the emails that are sent out by Frappe, you can use the `default_mail_footer` hook.

**app/hooks.py**
[code] 
    default_mail_footer = """
     
     Sent via [TennisMart](https://tennismart.com/)
    
    """
    
[/code]

Now, all the emails will have **Sent via TennisMart** in the footer.

## Session Hooks

These hooks are triggered over the login lifecycle of a user. `on_login` is triggered immediately after a successful login, `on_session_creation` is triggered after the session is setup, `on_logout` is triggered after the user logs out.

**app/hooks.py**
[code] 
    on_login = "app.overrides.successful_login"
    on_session_creation = "app.overrides.allocate_free_credits"
    on_logout = "app.overrides.clear_user_cache"
    
[/code]

The method will be called with one argument [`login_manager`](https://github.com/frappe/frappe/blob/develop/frappe/auth.py).

**app/overrides.py**
[code] 
    def allocate_free_credits(login_manager):
     # allocate free credits to frappe.session.user
     pass
    
[/code]

## Auth Hooks

These hooks are triggered during request authentication. Custom headers, Authorization headers can be validated here, user is verified and mapped to the request using `frappe.set_user()`. Use `frappe.request` and `frappe.*` to validate request and map user.

**app/hooks.py**
[code] 
    auth_hooks = ["app.overrides.validate_custom_jwt"]
    
[/code]

The method will be called during request authentication.

**app/overrides.py**
[code] 
    def validate_custom_jwt():
     # validate jwt from header, verify signature, set user from jwt.
     pass
    
[/code]

Use this method to check for incoming request header, verify the header and map the user to the request. If header verification fails DO NOT throw error to continue with other hooks. Unverified request is treated as "Guest" request by default. You may use third party server, shared database or any alternative of choice to verify and map request and user.

## Fixtures

Fixtures are database records that are synced using JSON files when you install and update your site.

Let's say you want to create a set of categories in the database whenever you install your app. To do that, create the set of categories in your local site, and add the doctype name in the `fixtures` hook.
[code] 
    fixtures = [
     # export all records from the Category table
     "Category"
    ]
    
[/code]

Now, run the following command:
[code] 
    bench --site sitename export-fixtures
    
[/code]

This command will create a JSON file for each doctype which will contain the data to generate list of records. You can test this by creating a new site and by installing your app on that site.

You can also add conditions for exporting records.
[code] 
    fixtures = [
     # export all records from the Category table
     "Category",
     # export only those records that match the filters from the Role table
     {"dt": "Role", "filters": [["role_name", "like", "Admin%"]]},
    ]
    
[/code]

Some fields are for internal use only. They will be set and kept up-to-date by the system automatically. These will not get exported: `modified_by`, `creation`, `owner`, `idx`, `lft` and `rgt`. For child table records, the following fields will not get exported: `docstatus`, `doctype`, `modified` and `name`.

## Document Hooks

### Modify List Query

You can customize how list of records are queried for a DocType by adding custom match conditions using the `permission_query_conditions` hook. This match condition must be a valid WHERE clause fragment for an SQL query.

**app/hooks.py**
[code] 
    permission_query_conditions = {
     "ToDo": "app.permissions.todo_query",
    }
    
[/code]

The method is called with a single argument `user` which can be `None`. The method should return a string that is a valid SQL WHERE clause.

**app/permissions.py**
[code] 
    def todo_query(user):
     if not user:
     user = frappe.session.user
     # todos that belong to user or assigned by user
     return "(`tabToDo`.owner = {user} or `tabToDo`.assigned_by = {user})".format(user=frappe.db.escape(user))
    
[/code]

Now, if you use the `frappe.db.get_list` method, your WHERE clause will be appended to the query.
[code] 
    todos = frappe.db.get_list("ToDo", debug=1)
    
    # output
    '''
    select `tabToDo`.`name`
    from `tabToDo`
    where ((`tabToDo`.owner = 'john@doe.com' or `tabToDo`.assigned_by = 'john@doe.com'))
    order by `tabToDo`.`modified` DESC
    '''
    
[/code]

> This hook will only affect the result of `frappe.db.get_list` method and not `frappe.db.get_all`.

### Document Permissions

You can modify the behaviour of `doc.has_permission` document method for any DocType and add custom permission checking logic using the `has_permission` hook.

**app/hooks.py**
[code] 
    has_permission = {
     "Event": "app.permissions.event_has_permission",
    }
    
[/code]

The method will be passed the `doc`, `user` and `permission_type` as arguments. It should return `True` or a `False` value. If `None` is returned, it will fallback to default behaviour.

**app/permissions.py**
[code] 
    def event_has_permission(doc, user=None, permission_type=None):
     # when reading a document allow if event is Public
     if permission_type == "read" and doc.event_type == "Public":
     return True
    
     # when writing a document allow if event owned by user
     if permission_type == "write" and doc.owner == user:
     return True
    
     return False
    
[/code]

### Override DocType Class

You can override/extend the class for standard doctypes by using the `override_doctype_class` hook.

**app/hooks.py**
[code] 
    override_doctype_class = {
     "ToDo": "app.overrides.todo.CustomToDo"
    }
    
[/code]

**app/overrides/todo.py**
[code] 
    from frappe.desk.doctype.todo.todo import ToDo
    
    class CustomToDo(ToDo):
     def on_update(self):
     self.my_custom_code()
     super().on_update()
    
     def my_custom_code(self):
     pass
    
[/code]

> It is recommended that you extend the standard class of the doctype, otherwise you will have to implement all of the core functionality.

### Override Form Scripts

You can override/extend [Standard Form Scripts](../api/form.md) by using the `doctype_js` hook.

**app/hooks.py**
[code] 
    doctype_js = {
     "ToDo": "public/js/todo.js",
    }
    
[/code]

**app/public/js/todo.js**
[code] 
    frappe.ui.form.on("Todo", {
     refresh: function(frm) {
     frm.trigger("my_custom_code");
     },
     my_custom_code: function(frm){
     console.log(frm.doc.name)
     }
    });
    
[/code]

> The events/functions defined in `app/public/todo.js` will extend those in the standard form script of `ToDo` doctype.

### CRUD Events

You can hook into various CRUD events of any doctype using the `doc_events` hook.

**app/hooks.py**
[code] 
    doc_events = {
     "*": {
     # will run after any DocType record is inserted into database
     "after_insert": "app.crud_events.after_insert_all"
     },
     "ToDo": {
     # will run before a ToDo record is inserted into database
     "before_insert": "app.crud_events.before_insert_todo",
     }
    }
    
[/code]

The method will be passed the doc and the method name as arguments.

**app/crud_events.py**
[code] 
    def after_insert_all(doc, method=None):
     pass
    
    def before_insert_todo(doc, method=None):
     pass
    
[/code]

> See [Controller Hooks](../basics/doctypes/controllers.md) for a list of all available hooks.

### Override Whitelisted Methods

Whitelisted Methods are python methods that are accessible on a REST endpoint and consumed by a client. You can override standard whitelisted methods that are part of the core framework using the `override_whitelisted_methods` hook.

**app/hooks.py**
[code] 
    override_whitelisted_methods = {
     "frappe.client.get_count": "app.whitelisted.custom_get_count"
    }
    
[/code]

The method should have the same signature as the original method.

**app/whitelisted.py**
[code] 
    def custom_get_count(doctype, filters=None, debug=False, cache=False):
     # your custom implementation of the standard get_count method provided by frappe
     pass
    
[/code]

### Ignore Links on Delete

To ignore links to specific DocTypes when deleting documents, you can specify them in the `ignore_links_on_delete` hook like so:

**app/hooks.py**
[code] 
    ignore_links_on_delete = ["Communication", "ToDo"]
    
[/code]

### Form Timeline

The timeline section of [form view](../desk.md) of a document shows an audit trail of actions performed on that document like views, value changes, comments and related communications, etc.

Apart from these standard actions, there might arise a situation where you need to add your own custom actions. You can do this via `additional_timeline_content` hook.
[code] 
    additional_timeline_content: {
     # show in each document's timeline
     "*": ["app.timeline.all_timeline"]
     # only show in ToDo's timeline
     "ToDo": ["app.timeline.todo_timeline"]
    }
    
[/code]

The method will be passed the doctype and docname as arguments. You can perform queries and return actions related to that document as a list of dicts as shown in the example. Each dict in the list must have a `creation` value which will be used to sort the item in the timeline.
[code] 
    def todo_timeline(doctype, docname):
     # this method should return a list of dicts
     return [
     {
     # this will be used to sort the content in the timeline
     "creation": "22-05-2020 18:00:00",
     # this JS template will be rendered in the timeline
     "template": "custom_timeline_template",
     # this data will be passed to the template.
     "template_data": {"key": "value"},
     },
     ...
     ]
    
[/code]

## Scheduler Events

You can use Scheduler Events for running tasks periodically in the background using the `scheduler_events` hook.

**app/hooks.py**
[code] 
    scheduler_events = {
     "hourly": [
     # will run hourly
     "app.scheduled_tasks.update_database_usage"
     ],
    }
    
[/code]

**app/scheduled_tasks.py**
[code] 
    def update_database_usage():
     pass
    
[/code]

> After changing any scheduled events in `hooks.py`, you need to run `bench migrate` for changes to take effect.

### Available Events

  * `hourly`, `daily`, `weekly`, `monthly`



These events will trigger every hour, day, week and month respectively.

  * `hourly_long`, `daily_long`, `weekly_long`, `monthly_long`



Same as above but these jobs are run in the [long worker](../basics/directory-structure.md) suitable for long running jobs.

  * `all`



The `all` event is triggered every 60 seconds. This can be configured via the `scheduler_tick_interval` key in [`common_site_config.json`](../basics/sites.md)

  * `cron`



A valid cron string that can be parsed by [croniter](https://pypi.org/project/croniter/).

Usage Examples:
[code] 
    scheduler_events = {
     "daily": [
     "app.scheduled_tasks.manage_recurring_invoices"
     ],
     "daily_long": [
     "app.scheduled_tasks..take_backups_daily"
     ],
     "cron": {
     "15 18 * * *": [
     "app.scheduled_tasks..delete_all_barcodes_for_users"
     ],
     "*/6 * * * *": [
     "app.scheduled_tasks..collect_error_snapshots"
     ],
     "annual": [
     "app.scheduled_tasks.collect_error_snapshots"
     ]
     }
    }
    
[/code]

## Jinja Customization

Frappe provides a list of [global utility methods](../api/jinja.md) in Jinja templates. To add your own methods and filters you can use the `jinja` hook.

**app/hooks.py**
[code] 
    jinja = {
     "methods": [
     "app.jinja.methods",
     "app.utils.get_fullname"
     ],
     "filters": [
     "app.jinja.filters",
     "app.utils.format_currency"
     ]
    }
    
[/code]

**app/jinja/methods.py**
[code] 
    def sum(a, b):
     return a + b
    
    def multiply(a, b):
     return a * b
    
[/code]

> If the path is a module path, all the methods in that module will be added.

**app/utils.py**
[code] 
    def get_fullname(user):
     first_name, last_name = frappe.db.get_value("User", user, ["first_name", "last_name"])
     return first_name + " " + last_name
    
    def format_currency(value, currency):
     return currency + " " + str(value)
    
[/code]

Now, you can use these utilities in your Jinja templates like so:
[code] 
    Hi, {{ get_fullname(frappe.session.user) }}
    ============================================
    
    
    Your account balance is {{ account_balance | format_currency("INR") }}
    
    
    1 + 2 = {{ sum(1, 2) }}
    
    
    
[/code]

## Prevent Auto Cancellation of Linked Documents

To prevent documents of a specific DocType from being automatically cancelled on the cancellation of any linked documents you can use the `auto_cancel_exempted_doctypes` hook.

**app/hooks.py**
[code] 
    auto_cancel_exempted_doctypes = ["Payment Entry"]
    
[/code]

In the above example, if any document (for e.g Sales Invoice) that is linked with Payment Entry is cancelled, it will skip the auto-cancellation of the linked Payment Entry document.

## Notification configurations

The notification configuration hook is used to customize the items shown in the Notification dropdown in Desk. It can be configured by the `notification_config` hook.

**app/hooks.py**
[code] 
    notification_config = "app.notification.get_config"
    
[/code]

The method is called without any arguments.

**app/notification.py**
[code] 
    def get_config():
     return {
     "for_doctype": {
     "Issue": {"status":"Open"},
     "Issue": {"status":"Open"},
     },
     "for_module_doctypes": {
     "ToDo": "To Do",
     "Event": "Calendar",
     "Comment": "Messages"
     },
     "for_module": {
     "To Do": "frappe.core.notifications.get_things_todo",
     "Calendar": "frappe.core.notifications.get_todays_events",
     "Messages": "frappe.core.notifications.get_unread_messages"
     }
     }
    
[/code]

The above configuration has three parts:

  1. `for_doctype` part of the above configuration marks any "Issue" or "Customer Issue" as unread if its status is Open
  2. `for_module_doctypes` maps doctypes to module's unread count.
  3. `for_module` maps modules to functions to obtain its unread count. The functions are called without any argument.



## Required Apps

When building apps, you might create apps that build on top of other apps. To make sure dependent apps are installed when someone installs your app, you can use the `required_apps` hook.

**app/hooks.py**
[code] 
    required_apps = ["erpnext"]
    
[/code]

The above configuration will make sure `erpnext` is installed when someone installs your app.

## User Data Protection & Privacy

User Data Privacy features like personal data download and personal data deletion come out of the box in Frappe. What constitutes as personal data may be defined by the App publisher in the application's `hooks.py` file as `user_data_fields`.

**app/hooks.py**
[code] 
    user_data_fields = [
     {"doctype": "Access Log"},
     {"doctype": "Comment", "strict": True},
     {
     "doctype": "Contact",
     "filter_by": "email_id",
     "rename": True,
     },
     {"doctype": "Contact Email", "filter_by": "email_id"},
     {
     "doctype": "File",
     "filter_by": "attached_to_name",
     "redact_fields": ["file_name", "file_url"],
     },
     {"doctype": "Email Unsubscribe", "filter_by": "email", "partial": True},
    ]
    
[/code]

DocTypes that have user data should be mapped under this hook using the above format. Upon data deletion or download requests from users, this hook will be utilized to map over the specified DocTypes. The options available to modify documents are:

Field | Description  
---|---  
`doctype` | DocType that contains user data.  
`filter_by` | Docfield to filter the documents by. If unset, defaults to `owner`.  
`partial` | If set, all text fields are parsed and user's full name and username references will be redacted.  
`redact_fields` | Fields that have to be redacted. If unspecified, it considers partial data redaction from all text fields.  
`rename` | If document name contains user data, set this field to rename document to anonymize it.  
`strict` | If set to True, any user data will be redacted from all documents of current DocType. If unset, it defaults to False which means it only filters through documents in which user is the owner.  
  
> Note: Personal Data Download only utilizes the doctype and filter_by fields defined in `user_data_fields`

Related Topics:

  1. [Personal Data Deletion](https://docs.erpnext.com/docs/user/manual/en/setting-up/personal-data-deletion)
  2. [Personal Data Download](https://docs.erpnext.com/docs/user/manual/en/setting-up/personal-data-download)



## Signup Form Template

If you want to add additional fields to the signup form you can use this hook. Create a template file which contains the custom signup form. Pass this template to the custom signup hook.
[code] 
    signup_form_template = "school/templates/signup-form.html"
    
[/code]

> Note: If you want custom fields in signup form, it will require additional fields in the user doctype. You will have to add these fields using fixtures. Also you will have to write your own submit handler for this signup form and a function on the server side which will signup the user. This way you can also write validations for the custom fields you add.

## List of available hooks

Hook Name | Explanation  
---|---  
`additional_timeline_content` | Form Timeline  
`after_install` | Install Hooks  
`after_migrate` | Migrate Hooks  
`after_sync` | Install Hooks  
`app_include_css` | Desk Assets  
`app_include_js` | Desk Assets  
`app_logo_url` | App Meta Data  
`app_title` | App Meta Data  
`auto_cancel_exempted_doctypes` | Prevent Auto Cancellation  
`base_template_map` | Base Template  
`base_template` | Base Template  
`before_install` | Install Hooks  
`before_migrate` | Migrate Hooks  
`before_tests` | Test Hooks  
`before_write_file` | File Hooks  
`bot_parsers` | _Deprecated_  
`braintree_success_page` | Braintree Success Page  
`brand_html` | Brand HTML  
`calendars` | Calendars  
`clear_cache` | Clear Cache  
`communication_doctypes` |   
`default_mail_footer` | Default Mail Footer  
`delete_file_data_content` | File Hooks  
`doc_events` | Document CRUD Events  
`doctype_js` | Override Form Scripts  
`domains` |   
`dump_report_map` | _Deprecated_  
`extend_bootinfo` | Extend Bootinfo  
`extend_website_page_controller_context` | Website Controller Context  
`filters_config` |   
`fixtures` | Fixtures  
`get_site_info` |   
`get_translated_dict` |   
`get_website_user_home_page` | Default Homepage  
`has_permission` | Document Permissions  
`has_website_permission` |   
`home_page` | Default Homepage  
`jenv` | Jinja Customization  
`leaderboards` |   
`look_for_sidebar_json` |   
`make_email_body_message` |   
`notification_config` | Notification configuration  
`on_login` | Session Hooks  
`on_logout` | Session Hooks  
`on_session_creation` | Session Hooks  
`override_doctype_class` | Override DocType Class  
`override_doctype_dashboards` |   
`override_whitelisted_methods` | Override Whitelisted Methods  
`ignore_links_on_delete` | Ignore Links on Delete  
`permission_query_conditions` | Modify List Query  
`portal_menu_items` | Portal Sidebar  
`required_apps` | Required Apps  
`role_home_page` | Default Homepage  
`scheduler_events` | Scheduler Events  
`setup_wizard_complete` |   
`setup_wizard_exception` |   
`setup_wizard_requires` |   
`setup_wizard_stages` |   
`setup_wizard_success` |   
`signup_form_template` | Signup Form Template  
`sounds` | Sounds  
`standard_portal_menu_items` | Portal Sidebar  
`standard_queries` |   
`template_apps` |   
`translated_languages_for_website` |   
`translator_url` |   
`treeviews` | DocTypes that use TreeView as the default view (instead of ListView)  
`update_website_context` | Website Context  
`user_privacy_documents` | _Deprecated_ (Use `user_data_fields` hook)  
`user_data_fields` | User Data Protection & Privacy  
`web_include_css` | Portal Assets  
`web_include_js` | Portal Assets  
`website_catch_all` | Website 404  
`website_clear_cache` | Website Clear Cache  
`website_context` | Website Context  
`website_generators` | _Deprecated_ (Use Has Web View in DocType instead)  
`website_redirects` | Website Redirects  
`website_route_rules` | Website Route Rules  
`website_user_home_page` | _Deprecated_ (Use `homepage` hook)  
`welcome_email` |   
`write_file_keys` | _Deprecated_  
`write_file` | File Hooks  
  
[ Previous Page Search  ](search.md) [ Next Page REST API ](../api/rest.md)

Last updated 2 months ago 

Was this helpful?
