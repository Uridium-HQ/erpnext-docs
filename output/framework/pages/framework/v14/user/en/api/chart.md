# Chart API

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12rulickpq>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Chart API 

[ Edit ](</wiki/spaces/r3uvq1ch61/page/12rulickpq>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe provides easy-to-use and fully configurable SVG charts. You can learn about them in the Frappe Chart's [documentation](<https://frappe.io/charts>).

## frappe.ui.RealtimeChart

`new frappe.ui.RealtimeChart(dom_element, event_name, max_label_count, data)`

Creates a new RealtimeChart instance that adds real-time data update functionality on top of the Frappe Chart API.

`dom_element`: HTML Element to be used to render the Chart. `event_name`: Socket event which will provide the data stream. `max_label_count`: Maximum number of labels allowed on the x-axis. `data`: Data for the chart to be initialized with.
[code] 
    // Empty data array
    const data = {
     datasets: [
     {
     name: "Some Data",
     values: [],
     },
     ],
    };
    
    // Realtime Chart initialization
    let chart = new frappe.ui.RealtimeChart("#chart", "test_event", 8, {
     title: "My Realtime Chart",
     data: data,
     type: "line",
     height: 250,
     colors: ["#7cd6fd", "#743ee2"]
    });
    
[/code]

Here is the sample client code to render a chart over the specified socket event.

The following python code can be executed as a cron job using [Hook](<https://frappeframework.com/docs/v14/user/en/python-api/hooks>) functionality.
[code] 
    data = {
     'label': 1,
     'points': [10]
    }
    frappe.publish_realtime('test_event', data)
    
[/code]

The `label` key specifies the label to be appended in the Chart. The `points` key specifies the array of points to be plotted. The number of values in the `points` array depends on the number of datasets.

This would produce a Chart like

![RealtimeChart](/files/realtime-chart.png)

### frappe.ui.RealtimeChart.start_updating

`frappe.ui.RealtimeChart.start_updating()`

Start listening to the specified socket event and update the RealtimeChart accordingly.
[code] 
    frappe.ui.RealtimeChart.start_updating();
    
[/code]

![RealtimeChart](/files/realtime-chart-demo.gif) _frappe.ui.RealtimeChart.start_updating_

### frappe.ui.RealtimeChart.stop_updating

`frappe.ui.RealtimeChart.stop_updating()`

Stop listening to the socket event that RealtimeChart was initialized with.
[code] 
    frappe.ui.RealtimeChart.stop_updating();
    
[/code]

### frappe.ui.RealtimeChart.update_chart

`frappe.ui.update_chart(label, data)`

Manually updates RealtimeChart by appending the label and associated data to the end of the chart.
[code] 
    frappe.ui.update_chart(2, [30]);
    
[/code]

[ Previous Page Dialog API ](</framework/v14/user/en/api/dialog>) [ Next Page Scanner API  ](</framework/v14/user/en/api/scanner>)

Last updated 2 months ago 

Was this helpful?
