# Realtime (socket.io)

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12s8ipa5k9)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Realtime (socket.io)

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12s8ipa5k9)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe ships with an API for realtime events based on [socket.io](https://socket.io/). Since socket.io needs a Node server to run, we run a Node process in parallel to the main web server.

## frappe.realtime.on

To listen to realtime events on the client (browser), you can use the `frappe.realtime.on` method:
[code] 
    frappe.realtime.on('event_name', (data) => {
     console.log(data)
    })
    
[/code]

## frappe.realtime.off

Stop listening to an event you have subscribed to:
[code] 
    frappe.realtime.off('event_name')
    
[/code]

## frappe.publish_realtime

To publish a realtime event from the server, you can use the `frappe.publish_realtime` method:
[code] 
    frappe.publish_realtime('event_name', data={'key': 'value'})
    
[/code]

## frappe.publish_progress

You can use this method to show a progress bar in a dialog:
[code] 
    frappe.publish_progress(25, title='Some title', description='Some description')
    
[/code]

![frappe publish realtime](https://docs.frappe.io/assets/f1336f0d91fa.png)

[ Previous Page Form Tours  ](../form-tours.md) [ Next Page Background Jobs ](background_jobs.md)

Last updated 2 months ago 

Was this helpful?
