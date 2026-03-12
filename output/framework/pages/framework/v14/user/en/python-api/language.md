# Language Resolution

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12tvf985h9)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Language Resolution 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12tvf985h9)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Here, let's take a look into how language in Frappe is resolved, and how you may be able to use them in your Frappe apps or scripts.

The language for your session depends on the value of `frappe.lang`. This is resolved in the following order:

  1. Form Dict > _lang
  2. Cookie > preferred\_language \_[Guest User only]_
  3. Request Header > Accept-Language _[Guest User only]_
  4. User document > language
  5. System Settings > language



## Form Dict: _lang

The Form Dict's `_lang` parameter has the highest priority. Setting this will update all translatable components in given request. Frappe uses this mechanism in certain places to handle Email Templates and Print views.

## Cookie: preferred_language

Although, it may not be practical to pass a `?_lang=ru` in every request. If you want persistent yet temporary language setting, you can set the `preferred_language` key in cookies. Frappe utilizes this for the website language switcher. This method may be used to persist language based on the client.

> Only considered for Guest Users. Ignored for logged in users.

## Request Header: Accept-Language

Another relatively cleaner, and standard way to manage languages is using the `Accept-Language` header. If the previous two methods aren't set, Frappe starts resolving this header's values, which have an ordered set of a range of acceptable languages by the client. You can check out [the Mozilla Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language) on this topic for more clarity perhaps.

> Only considered for Guest Users. Ignored for logged in users.

## User & System Settings

The User document has a `language` field that sets the session language for said user. This setting persists across devices, clients. This allows a particular user to view the website, and Desk in a language of their choice. Say for instance, a user sets their language as "Russian" on a "French" site, when they login, the site would be translated to Russian automatically.

The `language` field in the System Settings sets the language for the entire site. It has the lowest priority and is the fallback language for all sessions.

[ Previous Page Request Lifecycle  ](routing-and-rendering.md) [ Next Page Utility Functions  ](../api/utils.md)

Last updated 2 months ago 

Was this helpful?
