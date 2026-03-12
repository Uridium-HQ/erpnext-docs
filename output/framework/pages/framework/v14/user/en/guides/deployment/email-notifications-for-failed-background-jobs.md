# Email Notifications For Failed Background Jobs

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12breaa2f3>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Email Notifications For Failed Background Jobs 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12breaa2f3>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe handles failure of jobs in the following way,

  1. If a job fails, (raises exception), it's logged in Scheduler Log and `logs/worker.error.log`.
  2. Keeps a lock file and would not run anymore if lock file is there.
  3. Raises LockTimeoutError in case the lock file is more than 10 minutes old.



You can configure email notification for scheduler errors. By writing a file, `sites/common_site_config.json` with content
[code] 
    {
      "celery_error_emails": {
     "ADMINS": [
     [
     "Person 1",
     "person1@example.com"
     ],
     [
     "Person2 ",
     "person2@example.com"
     ]
     ],
     "SERVER_EMAIL": "exceptions@example.com"
     }
    }
    
[/code]

One limitation is that it'll use local mailserver on port 25 to send the emails.

[ Previous Page Packages  ](</framework/v14/user/en/guides/deployment/packages>) [ Next Page How To Migrate Doctype Changes To Production  ](</framework/v14/user/en/guides/deployment/how-to-migrate-doctype-changes-to-production>)

Last updated 2 months ago 

Was this helpful?
