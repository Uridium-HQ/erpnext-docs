# RazorPay

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12ubagq0fd)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# RazorPay 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/12ubagq0fd)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Razorpay is a popular payments solution in India which allows businesses to accept, process and disburse payments with its product suite. It gives you access to payment methods like Credit Cards, Debit Cards and Netbanking.

## Integrating Razorpay Client Checkout

Razorpay Payment

### Steps for integration

#### Include checkout script in your code

Insert the following script on your page `` The checkout script automatically fetches the razorpay checkout script and wraps their API for some syntactic sugar.

#### Create the Order controller in your backend
[code] 
    def get_razorpay_order(self):
     controller = get_payment_gateway_controller("Razorpay")
    
     payment_details = {
     "amount": 30000,
     ...
     "reference_doctype": "Conference Participant",
     "reference_docname": self.name,
     ...
     "receipt": self.name
     }
    
     return controller.create_order(**payment_details)
    
[/code]

#### Inititate the payment in client using checkout API
[code] 
    function make_payment(ticket) {
     var options = {
     "name": "",
     "description": "",
     "image": "",
     "prefill": {
     "name": "",
     "email": "",
     "contact": ""
     },
     "theme": {
     "color": ""
     },
     "doctype": "", // Mandatory
     "docname": " {
     // SCRIPT TO RUN WHEN MODAL OPENS
     }
     razorpay.on_success = () => {
     // SCRIPT TO RUN ON PAYMENT SUCCESS
     }
     razorpay.on_fail = () => {
     // SCRIPT TO RUN ON PAYMENT FAILURE
     }
     razorpay.init() // Creates the order and opens the modal
    }
    
[/code]

### Lifecycle

  1. **Create an Order in your backend**



An order is first created at the server triggered by `razorpay.init()`, for this a controller `get_razorpay_order` must be created for the doctype. The server method sets the amount to be charged and a unique receipt id for razorpay APIs to consume.

The `get_razorpay_order` internally calls the create_order controller of razorpay settings doctype. which then creates an integration request and sends POST request to `https://api.razorpay.com/v1/orders`

  1. **Process Checkout at Client**



A successful creation of the Order returns the `order_id` that is stored against the Order in integration request. This `order_id` is passed to the client which triggers the razorpay modal. After the payment, depending on the status the success or fail API method is called and the payment ID is passed to it.

  1. **Verify the payment**



Once the API method is called, The transaction details are saved in integration request. If successful the `authorize_payment` controller is called, which checks the payment status from razorpay API using the Payment ID. Once authorized, the integration request is marked as Completed, following this the payment success hook of the reference_doctype is called.

You can read more about Razorpay custom checkout in their [documentation](https://razorpay.com/docs/payment-gateway/web-integration/custom/)

[ Previous Page Query Builder  ](../api/query-builder.md) [ Next Page Google Drive  ](google_drive.md)

Last updated 2 months ago 

Was this helpful?
