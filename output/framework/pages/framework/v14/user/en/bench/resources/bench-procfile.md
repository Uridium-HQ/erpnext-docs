# Bench Procfile

[ Edit ](</wiki/spaces/r3uvq1ch61/page/134td1mg87>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Bench Procfile 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/134td1mg87>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

`bench start` uses [honcho](<http://honcho.readthedocs.org>) to manage multiple processes in **developer mode**.

### Processes

The various process that are needed to run frappe are:

  1. `bench start` \- the web server
  2. `redis_cache` for caching (general)
  3. `redis_queue` for managing queue for background workers
  4. `redis_socketio` as a message broker for real-time updates / updates from background workers
  5. `web` for the frappe web server.
  6. `socketio` for real-time messaging.
  7. `schedule` to trigger periodic tasks
  8. `worker_*` redis workers to handle async jobs



Optionally if you are developing for frappe you can add:

`bench watch` to automatically build the desk javascript app.

### Sample

redis_cache: redis-server config/redis_cache.conf redis_socketio: redis-server config/redis_socketio.conf redis_queue: redis-server config/redis_queue.conf web: bench serve --port 8000 socketio: /usr/bin/node apps/frappe/socketio.js watch: bench watch schedule: bench schedule worker_short: bench worker --queue short worker_long: bench worker --queue long worker_default: bench worker --queue default

[ Previous Page Bench Commands Cheatsheet  ](</framework/v14/user/en/bench/resources/bench-commands-cheatsheet>) [ Next Page Database Migrations  ](</framework/v14/user/en/database-migrations>)

Last updated 2 months ago 

Was this helpful?
