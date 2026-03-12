# Purchasing an Asset

[ Edit ](</wiki/spaces/24hrpr6es9/page/0s432djec8>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Purchasing an Asset

[ Edit ](</wiki/spaces/24hrpr6es9/page/0s432djec8>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**Purchasing an asset in ERPNext involves creating the asset record, optionally automating asset creation from a purchase, and following the purchase and accounting cycle.**

Assets can be purchased manually or automatically created when receiving an item in a Purchase Receipt or Purchase Invoice. This ensures accurate asset tracking and proper accounting entries.

## 1\. Prerequisites

* * *

Before purchasing a new asset, ensure the following are configured:

  * **[Asset Category](<https://docs.frappe.io/erpnext/user/manual/en/asset-category>)** is created
  * [Item](<https://docs.frappe.io/erpnext/user/manual/en/item>) is created with **‘Is Fixed Asset’** enabled
  * Optional: Enable **‘Auto Create Assets on Purchase’** in the item master if you want assets to be created automatically upon receipt



![](/files/Screenshot%202026-01-11%20at%2011.49.39%E2%80%AFPM.png) _Item Master_

## 2\. How to Purchase an Asset

* * *

  1. Follow the standard purchase cycle for the asset:


  * Create a Purchase Order (if required)
  * Receive the item via Purchase Receipt
  * Submit a Purchase Invoice


  2. Enter the asset location in the Items table of the Purchase Receipt or Purchase Invoice.
  3. On submission of the Purchase Receipt:


  * If Auto Create Assets is enabled, ERPNext will automatically create the Asset record.
  * You can then update other details manually in the Asset form.



![Auto create asset on purchase](/files/Screenshot%202025-05-21%20at%2012.04.07%E2%80%AFAM.png)

### 2.1 Accounting Entries

  1. With Capital Work in Progress (CWIP) Enabled


  * On submitting the Purchase Receipt, the CWIP account is debited instead of the asset account.
  * This represents that the asset is purchased but not yet available for use.
  * When the asset becomes available for use, CWIP is credited, and the corresponding asset account is debited.


  2. With CWIP Disabled


  * The receipt entry is posted directly to the asset accounts defined in the Asset Category.


  3. Temporary Liability Account


  * ERPNext uses **“Asset Received But Not Billed”** (a liability account) when submitting a Purchase Receipt.
  * On submitting the Purchase Invoice, this account is debited/reversed.



![](/files/Screenshot%202026-01-11%20at%2011.55.53%E2%80%AFPM.png)

## 3\. Related Topics

* * *

  1. [Purchase Receipt](<https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt>)
  2. [Purchase Invoice](<https://docs.frappe.io/erpnext/user/manual/en/purchase-invoice>)



[ Previous Page Asset Location  ](</erpnext/asset-location>) [ Next Page Asset ](</erpnext/asset>)

Last updated 2 weeks ago 

Was this helpful?
