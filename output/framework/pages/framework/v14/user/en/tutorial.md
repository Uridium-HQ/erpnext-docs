# Frappe Framework Tutorial

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/125igu5k11)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Frappe Framework Tutorial 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/125igu5k11)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

In this guide, you will learn how to create a web application from scratch using the Frappe Framework.

## Who is this for?

This guide is intended for software developers who are familiar with how web applications are built. The Frappe Framework is powered by Python, JavaScript and Redis, to name a few technologies and supports MariaDB and PostgreSQL databases. Jinja is used as the templating engine for Web Views and Print formats. Redis is used for caching, maintaing job queues and realtime updates. However, you may not need to be proficient in all these tools to get started with it.

Frappe Framework and the apps you build on it require `git` for version control and update management via Bench. It is also expected that you are familiar with basic git commands.

## What are we building?

We will build a simple **Library Management System** in which the **Librarian** can log in and manage Articles and Memberships. We will build the following models:

  1. **Article:** A Book or similar item that can be rented.
  2. **Library Member:** A user who is subscribed to a membership.
  3. **Library Transaction:** An Issue or Return of an article.
  4. **Library Membership:** A document that represents an active membership of a Library Member.
  5. **Library Settings:** Settings that define values like Loan Period and the maximum number of articles that can be issued at a time.



The Librarian will log in to an interface known as **Desk** , a rich admin interface that ships with the framework. The Desk provides many standard views like List view, Form view, Report view, etc, and many features like Role-based Permissions.

We will also create public Web Views which can be accessed by the Library Members where they can browse available Articles.

## Table of Contents

  1. [Create a Bench](tutorial/install-and-setup-bench.md)
  2. [Create an App](tutorial/create-an-app.md)
  3. [Create a Site](tutorial/create-a-site.md)
  4. [Create a DocType](tutorial/create-a-doctype.md)
  5. [DocType Features](tutorial/doctype-features.md)
  6. [Controller Methods](tutorial/controller-methods.md)
  7. [Types of DocType](tutorial/types-of-doctype.md)
  8. [Form Scripts](tutorial/form-scripts.md)
  9. [Portal Pages](tutorial/portal-pages.md)
  10. [What's Next](tutorial/whats-next.md)



[ Previous Page Installation ](installation.md) [ Next Page Install and Setup Bench  ](tutorial/install-and-setup-bench.md)

Last updated 2 months ago 

Was this helpful?
