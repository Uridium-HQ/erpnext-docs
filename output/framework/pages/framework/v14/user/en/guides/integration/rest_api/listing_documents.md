# Listing documents

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12ghf1ff30)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Listing documents 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12ghf1ff30)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

To list documents, make a GET request to `/api/resource/{doctype}`.

GET **/api/resource/Person**

> All listings are returned paginated by 20 items. To change the page size, you can pass the query parameter `limit_page_length`. To request succesive pages, pass `limit_start`.

The response is returned as JSON Object and the listing is an array in with the key `data`.

Response:
[code] 
    {
     "data": [
     {
     "name": "000000012"
     },
     {
     "name": "000000008"
     }
     ]
    }
    
[/code]

By default, only the `name` field is included in the listing. To add more fields, you can pass the `fields` parameter with your GET request. `fields` has to be a JSON array containing the fieldnames.

GET **/api/resource/Person/?fields=["name","first_name"]**

Response:
[code] 
    {
     "data": [
     {
     "first_name": "Jane",
     "name": "000000012"
     },
     {
     "first_name": "John",
     "name": "000000008"
     }
     ]
    }
    
[/code]

You can filter the listing using SQL-conditions by passing the query parameter `filters`. `filters` has to be a JSON array containing one or multiple filters. Each condition is an array of the format, [{doctype}, {field}, {operator}, {operand}].

For example, get the name (id) of all persons with firstname "Jane":

GET **/api/resource/Person?filters=[["Person","first_name","=","Jane"]]**

Response:
[code] 
     { "data": [ { "name": "000000012" } ] }
    
[/code]

Authors: Rushabh Mehta (rushabh@erpnext.com), Raffael Meyer (raffael@alyf.de)

[ Previous Page OAuth 2  ](oauth-2.md) [ Next Page Manipulating DocTypes  ](manipulating_documents.md)

Last updated 2 months ago 

Was this helpful?
