# How To Create Custom Fields During App Installation

[ Edit ](</wiki/spaces/r3uvq1ch61/page/129hjhllpi>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# How To Create Custom Fields During App Installation 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/129hjhllpi>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Your custom app can automatically add **Custom Fields** to DocTypes outside of your app when it is installed to a new site.

To do this, add the new custom fields that your app requires, using the Frappe web application.

In your `hooks.py` file, add `"Custom Fields"`

fixtures = ["Custom Field"]

Export fixtures before you commit your app with:

$ bench --site mysite export-fixtures

This will create a new folder called `fixtures` in your app folder and a `.csv` or `.json` file will be created with the definition of the custom fields you added.

This file will be automatically imported when the app is installed in a new site or updated via `bench update`.

Note: You can also add single DocTypes like "Website Settings" as fixtures

[ Previous Page Insert A Document Via Api  ](</framework/v14/user/en/guides/app-development/insert-a-document-via-api>) [ Next Page Using Html Templates In Javascript  ](</framework/v14/user/en/guides/app-development/using-html-templates-in-javascript>)

Last updated 2 months ago 

Was this helpful?
