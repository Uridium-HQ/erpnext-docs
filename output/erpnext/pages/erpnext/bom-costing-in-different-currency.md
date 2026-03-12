# BOM Costing in different Currency

[ Edit ](</wiki/spaces/24hrpr6es9/page/0s1jqqcl82>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# BOM Costing in different Currency 

[ Edit ](</wiki/spaces/24hrpr6es9/page/0s1jqqcl82>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

User can change the Currency in the BOM _before_ submitting. The system calculates the costing based on the Price List currency. You can check the manufacturing cost in a particular Currency by changing the Currency in the BOM.

Consider that you import plastic as a raw material from Japan and the Sales Invoices are in the Yen currency. Your company Currency is INR but you want the BOM costing to be done in Yen. On setting 'Rate Of Materials Based On' to 'Price List' the raw materials used in the BOM will also have rates set in Yen. These rates are fetched from the Price List you create for Japan. In this case, it is a buying Price List called 'Import Japan'.

![BOM in different Currency](/files/bom-currency.png)

If you select 'Rate Of Materials Based On' to 'Valuation Rate' or 'Last Purchase Rate', the prices will be fetched from the Item master or the Sales Invoice respectively. In case of Item master, you'll need to enter the Valuation Rate in **your** Currency. In the BOM, Valuation Rate will be converted to the Currency set in the BOM.

![BOM in different Currency](/files/bom-currency-1.png)

[ Previous Page Issued Items Against Work Order ](</erpnext/consumed-materials-in-production>) [ Next Page Managing Multi-level BOM ](</erpnext/managing-multi-level-bom>)

Last updated 2 weeks ago 

Was this helpful?
