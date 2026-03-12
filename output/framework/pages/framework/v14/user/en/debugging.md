# Debugging

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/135c8k0mgj)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Debugging 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/135c8k0mgj)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

## Server

When you run the `bench start` command during development, the log from each process of the Procfile is logged in the terminal window.
[code] 
    ▶ bench start
    14:55:17 system | redis_cache.1 started (pid=4085)
    14:55:17 system | redis_socketio.1 started (pid=4086)
    14:55:17 system | redis_queue.1 started (pid=4088)
    14:55:17 system | web.1 started (pid=4089)
    14:55:17 system | socketio.1 started (pid=4090)
    14:55:17 system | watch.1 started (pid=4094)
    14:55:17 system | worker_short.1 started (pid=4096)
    14:55:17 system | schedule.1 started (pid=4095)
    14:55:17 redis_queue.1 | 4088:C 22 May 14:55:17.257 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    14:55:17 redis_queue.1 | 4088:C 22 May 14:55:17.264 # Redis version=4.0.11, bits=64, commit=00000000, modified=0, pid=4088, just started
    14:55:17 redis_queue.1 | 4088:C 22 May 14:55:17.264 # Configuration loaded
    14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.265 * Increased maximum number of open files to 10032 (it was originally set to 4864).
    14:55:17 redis_cache.1 | 4085:C 22 May 14:55:17.262 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    14:55:17 redis_cache.1 | 4085:C 22 May 14:55:17.268 # Redis version=4.0.11, bits=64, commit=00000000, modified=0, pid=4085, just started
    14:55:17 redis_cache.1 | 4085:C 22 May 14:55:17.268 # Configuration loaded
    14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.269 * Increased maximum number of open files to 10032 (it was originally set to 4864).
    14:55:17 redis_socketio.1 | 4086:C 22 May 14:55:17.262 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    14:55:17 redis_socketio.1 | 4086:C 22 May 14:55:17.270 # Redis version=4.0.11, bits=64, commit=00000000, modified=0, pid=4086, just started
    14:55:17 redis_socketio.1 | 4086:C 22 May 14:55:17.270 # Configuration loaded
    14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.272 * Increased maximum number of open files to 10032 (it was originally set to 4864).
    14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.285 * Running mode=standalone, port=11002.
    14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.285 # Server initialized
    14:55:17 redis_queue.1 | 4088:M 22 May 14:55:17.286 * Ready to accept connections
    14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.287 * Running mode=standalone, port=13002.
    14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.292 # Server initialized
    14:55:17 redis_cache.1 | 4085:M 22 May 14:55:17.292 * Ready to accept connections
    14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.294 * Running mode=standalone, port=12002.
    14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.294 # Server initialized
    14:55:17 redis_socketio.1 | 4086:M 22 May 14:55:17.295 * Ready to accept connections
    14:55:17 system | worker_long.1 started (pid=4098)
    14:55:17 system | worker_default.1 started (pid=4100)
    14:55:18 socketio.1 | listening on *: 9002
    14:55:20 socketio.1 | { Error: connect ECONNREFUSED 0.0.0.0:8002
    14:55:20 socketio.1 | at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1191:14)
    14:55:20 socketio.1 | errno: 'ECONNREFUSED',
    14:55:20 socketio.1 | code: 'ECONNREFUSED',
    14:55:20 socketio.1 | syscall: 'connect',
    14:55:20 socketio.1 | address: '0.0.0.0',
    14:55:20 socketio.1 | port: 8002,
    14:55:20 socketio.1 | response: undefined }
    14:55:24 web.1 | * Running on http://0.0.0.0:8002/ (Press CTRL+C to quit)
    14:55:24 web.1 | * Restarting with fsevents reloader
    14:55:24 watch.1 | yarn run v1.10.1
    14:55:24 watch.1 | $ node rollup/watch.js
    14:55:25 web.1 | * Debugger is active!
    14:55:25 web.1 | * Debugger PIN: 321-355-865
    14:55:26 watch.1 |
    14:55:26 watch.1 | Rollup Watcher Started
    14:55:26 watch.1 |
    14:55:26 watch.1 | Watching...
    14:55:26 watch.1 | Rebuilding frappe-web.css
    14:55:27 watch.1 | Rebuilding frappe-web-b4.css
    14:55:27 watch.1 | Rebuilding chat.js
    14:55:28 web.1 |
    14:55:28 web.1 | test print
    
[/code]

When you write any print statements in your python code, it will show up in the `web:` process log if it is a request/response, or in one of `worker_` processes if the code runs in a background job.

> If you are a VSCode user, you can debug right in your editor by setting breakpoints in your code. Follow these [steps](https://github.com/frappe/erpnext/wiki/VSCode-Debugging-for-Frappe-Python) to set it up.

### Logging

In case you're running production, you'd need logs all the more to keep track of as much information about your Frappe environment.

Out of the box, logs are stored under the `./logs` folder in your bench. From Frappe Version 13, logs are available at site level too, under `./sites/{site}/logs`.

These site logs are created by the Frappe Application, while many of the bench level log files are generated by the processes that support your Frappe environment. Checkout `Procfile` or `supervisor.conf` in your bench for more information.

> Learn more about Frappe Logs [here](logging.md) and the Frappe Logging API from [here](api/logging.md).

### Console

To play with Python API, bench provides an iPython shell. After you run the following command, it will import frappe, initialize it and also connect to database.
[code] 
    ▶ bench --site [sitename] console
    
    In [1]: frappe.get_doc('Task', 'TASK00004')
    Out[1]: 
    
[/code]

## Client

Client side debugging is as simple as adding a `debugger` statement in your JS file. You must open your DevTools in your browser for it to pause on the statement.
[code] 
    frappe.db.get_value('Task', 'TASK00004', 'status')
     .then(values => {
     debugger
     console.log(values);
     })
    
[/code]

### Console

To play with Client API, you can open your browser's console and use the globally available `frappe` object to explore and run methods and access properties.

![Browser Console](https://docs.frappe.io/assets/e944bc7f066b.png) _Browser Console_

> Learn more about the Client API [here](api.md)

## Debugging in VS Code / Debug Adapter Protocol

![vsc debugging](https://docs.frappe.io/assets/f5a79c3d34ff.png)

Checklist for proper functioning.

  * Update `Procfile`
  * Get Visual Studio Code (duh!)
  * Install [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  * Update `launch.json`
  * Start Debugging



Caveats:

  1. Disables Auto Reload Feature (However You can achieve the same results by manual reload (⌘⇧F5))
  2. Disables Werkzeug Multithreading



**1\. Update`Procfile`**

_Caution: This modifies the behaviour of`bench start`_

Comment out a line (prepend # to it) from the `Procfile` (located in the bench directory) that looks like this.
[code] 
    web: bench serve --port 8000
    
[/code]

We will run this process from VS code instead of running it with `bench start`.

**2\. Update`launch.json`** Add a configuration to your `launch.json` in VS Code that should look something like this (This more or less does exactly what the removed line from Procfile does).
[code] 
    {
     "name": "Bench",
     "type": "python",
     "request": "launch",
     "program": "${workspaceFolder}/frappe/frappe/utils/bench_helper.py",
     "args": [
     "frappe", "serve", "--port", "8000", "--noreload", "--nothreading"
     ],
     "pythonPath": "${workspaceFolder}/../env/bin/python",
     "cwd": "${workspaceFolder}/../sites",
     "env": {
     "DEV_SERVER": "1"
     }
    }
    
[/code]

Paths mentioned in given configuration assumes that you have `apps` directory as your workspace directory (The directory you open `code` with). `workspaceFolder` is a vs code variable that points to (if it's not obvious from its name) workspace directory.

You are not forced to use `apps` as your workspace directory, however do remember to change `workspaceFolder`, `pythonPath` and `cwd` accordingly.

**3\. Execute`bench start`**

This should be kept running as usual.

**4\. Start debugging**

VS Code -> Debug Panel (⌘⇧D) -> Start Debugging or With a keyboard shortcut(⌘⇧F5).

### Explanation

**1.`program` and `args`**
[code] 
    "program": "${workspaceFolder}/frappe/frappe/utils/bench_helper.py",
    "args": ["frappe", "serve", "--port", "8000", "--noreload", "--nothreading"],
    
[/code]

Does exact same thing as `bench serve --port 8000 --noreload --nothreading` which is same as
[code] 
    cd sites
    ../env/bin/python ../apps/frappe/frappe/utils/bench_helper.py frappe serve --port 8000 --noreload --nothreading
    
[/code]

`--noreload` diasbles werkezeug's autoreload fetaure and `--nothreading` disables multithreading.

**2.`cwd`**
[code] 
    "cwd": "${workspaceFolder}/../sites",
    
[/code]

Above command must be executed from `sites` directory.

**3.`env`**
[code] 
    "env": {
     "DEV_SERVER": "1"
    }
    
[/code]

`bench start` creates an environment variable `DEV_SERVER` and set it to `1`. Socket.io doesn't work correctly without this (long story).

Running only `bench serve` doesn't set this variable so you need to explicitly set it.

**Note:**

Currently, frappe runs with `use_reloader=True` and `threaded=True`, VS Code Debugger for some reason doesn't play well with these features, [Django and Flask](https://code.visualstudio.com/docs/python/debugging) also have this problem.

[ Previous Page Desk ](hidden-features/desk.md) [ Next Page How to contribute ](how_to_contribute.md)

Last updated 2 months ago 

Was this helpful?
