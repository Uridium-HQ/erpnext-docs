# Desk

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0touds9384)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Desk 

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0touds9384)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe Framework comes with a rich admin interface called the Desk. It reads meta-data from DocTypes and automatically builds list views, form views, report views, etc for your DocTypes. Desk is to be used by users of the type "System User".

In this section we will discuss what views are provided by Desk and how to configure them.

  * Workspace
  * Awesomebar
  * List View
  * Form View
  * Grid View
  * Report Builder
  * Tree View
  * Calendar View
  * Gantt View
  * Kanban View
  * Desk Theme



## Workspace

When you login, you're presented with the Desk, it features a persistent sidebar with some standard items based on app modules. Each sidebar item links to a page called Workspace.

[About Workspace →](../../v14/user/en/desk/workspace.md)

![Desktop](https://docs.frappe.io/assets/8c1069121528.png)

## Awesomebar

Awesomebar helps you to navigate anywhere in the system, create new records, search in documents and even perform math operations.

![Awesomebar](https://docs.frappe.io/assets/545258ec0613.png) _Navigating ToDo using Awesomebar_

## List View

List View is generated for all DocTypes except which are Child Tables and Singles.

The List view is packed with features. Some of them are:

  1. Filters
  2. Sorting
  3. Paging
  4. Filter by tags
  5. Switch view to Report, Calendar, Gantt, Kanban, etc.



> Learn more about the [List API](../../v14/user/en/api/list.md).

## Form View

Form view is used to view the records in a Form Layout. This view has a lot of things going on. But the primary purpose of it is to view and edit records. A document can be assigned to or shared with other users and it can have arbitrary attachments and tags, all of which can be seen in the form sidebar.

![Form View](https://docs.frappe.io/assets/3c6bc21bca63.png) _Form View_

When you scroll down to the bottom of the form, you will see the form timeline. The form timeline shows emails, comments, edits and other events in a reverse chronological order.

![Form View](https://docs.frappe.io/assets/0453c15207cd.png) _Form Timeline_

> Learn more about the [Form API](../../v14/user/en/api/form.md).

## Grid View

Grid view is used as a table in the form view to insert multiple records. User can configure the columns of the grid view from the form.

![Grid View](https://docs.frappe.io/assets/267cfe97254f.gif)

## Report Builder

Report Builder is a generic tool to customize and build tabular data from a DocType. You can select columns to show, filters to apply, sort order and save this configuration by giving your report a name. You can also show Child Table data and also filter documents by their child records. You can also apply _Group By_ on a column with aggregation methods like Count, Sum and Average.

![Report Builder](https://docs.frappe.io/assets/4cf24f6d595a.gif) _Report Builder Features_

## Tree View

Frappe also supports tree structured records using the [Nested set model](https://en.wikipedia.org/wiki/Nested_set_model). If a doctype is configured to be a tree structure, it can be viewed in the Tree view.

![Tree View](https://docs.frappe.io/assets/937983c32e79.png) _Tree View_

## Calendar View

Calendar view can be configured for DocTypes with a start date and end date.

![Calendar View](https://docs.frappe.io/assets/736f18a4c76d.png) _Calendar View_

The configuration file should be named `{doctype}_calendar.js` and should exist in the doctype directory.

Here is an example configuration file for calendar view for Event doctype, which must be set in the `event_calendar.js` file.
[code] 
    frappe.views.calendar['Event'] = {
     field_map: {
     start: 'starts_on',
     end: 'ends_on',
     id: 'name',
     allDay: 'all_day',
     title: 'subject',
     status: 'event_type',
     color: 'color'
     },
     style_map: {
     Public: 'success',
     Private: 'info'
     },
     order_by: 'ends_on',
     get_events_method: 'frappe.desk.doctype.event.event.get_events'
    }
    
[/code]

## Gantt View

Gantt view uses the same configuration file as calendar, so every DocType that has a Calendar view has a Gantt view too.

In case certain settings need to be overridden for the Event DocType's Gantt view (for example the `order_by` field) the configuration can be set in the `event_calendar.js` file with the following content.
[code] 
    frappe.views.calendar['Event'] = {
     field_map: {
     start: 'starts_on',
     end: 'ends_on',
     id: 'name',
     allDay: 'all_day',
     title: 'subject',
     status: 'event_type',
     color: 'color'
     },
     gantt: { // The values set here will override the values set in the object just for Gantt View
     order_by: 'starts_on',
     }
     style_map: {
     Public: 'success',
     Private: 'info'
     },
     order_by: 'starts_on',
     get_events_method: 'frappe.desk.doctype.event.event.get_events'
    }
    
[/code]

![Gantt View](https://docs.frappe.io/assets/83828d679b10.png) _Gantt View_

## Kanban View

Kanban view can be created for any DocType that has a Select field with options. These options become the column names for the Kanban Board.

![Kanban View](https://docs.frappe.io/assets/dffa49fcda67.png)

## Dark Theme

![Dark Theme](https://docs.frappe.io/assets/83f3f5b01af2.png)

Frappe Framework has a first class support of dark theme. To switch the theme, click on your avatar on top right of the screen and click on "Toggle Theme". Once you click "Toggle Theme", you'll see following modal from which you can easily switch between available themes. To switch to dark theme select "Timeless Night".

![Desk Theme Modal](https://docs.frappe.io/assets/ee0bbe463807.png)

**Note:** You can also press CTRL + SHIFT + G to open this modal.

[ Previous Page Form Tours ](form-tours.md) [ Next Page Introduction ](desk/reports.md)

Last updated 3 weeks ago 

Was this helpful?
