# Bench

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0u4nfnmtud)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Bench

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0u4nfnmtud)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Bench is a CLI tool to manage Frappe Deployments. It provides an easy interface to help you setup and manage multiple sites and apps based on Frappe Framework.

However, the term bench may mean different things depending on the context. We use the term "bench" to refer to the CLI tool and the directory interchangeably. This may get confusing a lot of times.

> "Did you update the bench?"
> 
> "Yes, migrations for the latest version were smoother this time around."
> 
> "What?! I told you to update the CLI tool!"
> 
> "Let's hope our clients like Version 13"

To avoid these type of situations, we will refer to **"Bench"** as the bench directory and **"Bench CLI"** to refer to the CLI tool.

To install the bench CLI and setup a Frappe environment, please follow the [installation instructions](../../v14/user/en/installation.md).

You may be surprised to know that a lot of the bench commands are provided by the Frappe Framework, not by the Bench CLI directly. In general, these are the commands which work on a specific site (can use the `--site` parameter). Even commands like `bench update` only provide thin wrappers around Frappe Framework commands such as `backup` and `migrate`, along with some other essential bench and system-level operations.

## References

  1. [Bench Commands](../../v14/user/en/bench/bench-commands.md)
  2. [Frappe Commands](../../v14/user/en/bench/frappe-commands.md)
  3. [Command References](../../v14/user/en/bench/reference.md)
  4. [Extending the CLI](../../v14/user/en/bench/extending-the-cli.md)



[ Previous Page OAuth2 ](../../oauth2.md) [ Next Page Bench Commands  ](bench/bench-commands.md)

Last updated 3 weeks ago 

Was this helpful?
