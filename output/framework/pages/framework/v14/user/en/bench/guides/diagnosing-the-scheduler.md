# Diagnosing The Scheduler

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/133f9cuq27)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Diagnosing The Scheduler 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/133f9cuq27)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

If you're experiencing delays in scheduled jobs or they don't seem to run, you can run the several commands to diagnose the issue.

### bench doctor

This will output the following in order:

  * Scheduler Status per site
  * Number of Workers
  * Pending Tasks



Desirable output:

Workers online: 0 \-----None Jobs-----

### bench --site [site-name] show-pending-jobs

This will output the following in order:

  * Queue
  * Tasks within Queue



Desirable output:

\-----Pending Jobs-----

### bench purge-jobs

This will remove all pending jobs from all queues

[ Previous Page Configuring HTTPS  ](configuring-https.md) [ Next Page Using Let's Encrypt to setup HTTPS  ](lets-encrypt-ssl-setup.md)

Last updated 2 months ago 

Was this helpful?
