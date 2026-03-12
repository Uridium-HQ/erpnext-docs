# Bench

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12vsbc4u9g)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Bench 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12vsbc4u9g)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Bench is a CLI tool to manage Frappe Deployments. It provides an easy interface to help you setup and manage multiple sites and apps based on Frappe Framework.

However, the term bench may mean different things depending on the context. We use the term "bench" to refer to the CLI tool and the directory interchangeably. This may get confusing a lot of times.

A: "Did you update the bench?" B: "Yes, migrations for the latest version were smoother this time around." A: "What?! I told you to update the CLI tool!" B: "Let's hope our clients like Version 13"

To avoid these type of situations, we will refer to **"Bench"** as the bench directory and **"Bench CLI"** to refer to the CLI tool.

> To install the bench CLI and setup a Frappe environment, follow [Installation](installation.md).

This may not be known to a lot of people but half the bench commands we're used to, exist in the Frappe Framework and not in bench directly. Those commands generally are the `--site` commands. Even commands like `update` provide easy wrappers around and invoke multiple Frappe commands such as `backup` and `migrate` along with some other essential bench and system-level operations.

## References

  1. [Bench Commands](bench/bench-commands.md)
  2. [Frappe Commands](bench/frappe-commands.md)
  3. [Command References](bench/reference.md)
  4. [Extending the CLI](bench/extending-the-cli.md)



[ Previous Page Video Tutorials for Frappe Framework  ](videos.md) [ Next Page Bench Commands  ](bench/bench-commands.md)

Last updated 2 months ago 

Was this helpful?
