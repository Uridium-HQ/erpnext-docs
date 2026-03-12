# Adding Pages

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12cqpiee94>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Adding Pages 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12cqpiee94>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

To add pages, just add `.html` or `.md` files in the `www` folder. The pages must only have the content, not the `and` tags.

You can also write markdown pages

### Index

The first file in a folder must be called `index.md` or `index.html`

Either file must be present for the system to make this a valid folder to build pages.

### Markdown

# This is a title

This is some page content a [link](</link/to/page>)

### Adding Links

Links urls to pages can be given without the `.html` extension for example `/home/link`

### Title

The first `block if present will be the page title if not specified in a special tag. If no` or title is specified, the file name will be the title.

### Adding CSS

You can also add a `.css` file with the same filename (e.g. `index.css` for `index.md`) that will be rendered with the page.

### Special Tags

  1. `` will make the page render in Jinja
  2. `` will add a custom title
  3. `` will not add breadcrumbs in the page
  4. # `` will enable caching (if you have used Jinja templating)




[ Previous Page Ordering  ](</framework/v14/user/en/guides/portal-development/ordering>) [ Next Page Table of Contents  ](</framework/v14/user/en/guides/portal-development/table-of-contents>)

Last updated 2 months ago 

Was this helpful?
