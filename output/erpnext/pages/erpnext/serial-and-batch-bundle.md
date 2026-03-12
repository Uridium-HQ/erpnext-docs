# Serial and Batch Bundle

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rtiqm5ce0)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Serial and Batch Bundle

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rtiqm5ce0)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

> NOTE: Users must create a separate **Serial and Batch Bundle** for each stock transaction. They cannot use the same **Serial and Batch Bundle** across multiple stock transactions.
> 
> _Allow Negative Stock_ has been removed for Serial / Batch Items from version 15. From version 15 onward, users cannot make negative stock transactions for serial / batch items, even if _Allow Negative Stock_ is enabled in **Stock Settings**.

* * *

In version 15, we introduced the **Serial and Batch Bundle**. This feature is used to link Serial / Batch Nos in stock transactions.

Before version 15, the _Serial No_ field was a Small Text field, which meant one column could hold more than one serial number. Because of this design, there were a lot of data integrity issues. To solve this, we changed the _Serial No_ field from Small Text to a Link field in version 15. Since we can't add a child table inside a child table, we added a new DocType: **Serial and Batch Bundle** to pick/dispatch multiple Serial / Batch numbers.

![Serial no Configure](https://docs.frappe.io/assets/333b7db32954.png)

## How does this work?

You need to create a **Serial and Batch Bundle** and link it to stock transactions whenever you deal with Serial / Batch numbers. Users must create a separate **Serial and Batch Bundle** for each transaction, and they can't link the same **Serial and Batch Bundle** to multiple transactions.

### Auto Creation of Serial and Batch Bundle for Inward Entry

If the user wants to auto-create a **Serial and Batch Bundle** for an inward entry, they must ensure that _Serial Number Series_ is set for the serial item and that the _Automatically Create New Batch_ checkbox is enabled (with _Batch Number Series_ set) for the batch item.

#### For Serial No

![Serial no Configure](https://docs.frappe.io/assets/b09a70879ed2.png)

#### For Batch No

![Batch no Configure](https://docs.frappe.io/assets/ebdc4ecd765d.png)

After the configuration, when the user creates a **Purchase Receipt** or a **Stock Entry** with the Type "Material Receipt", the system will automatically create the inward **Serial and Batch Bundle** on submission of the record.

![Auto Serial Batch Bundle Inward](https://docs.frappe.io/assets/48461d622788.gif)

### Auto Creation of Serial and Batch Bundle for Outward Entry

If the user wants to auto-create a **Serial and Batch Bundle** for an outward entry, they must enable the checkbox _Auto Create Serial and Batch Bundle For Outward_ in **Stock Settings**. They can also set _Pick Serial / Batch Based On_ to "FIFO / LIFO / Expiry" in **Stock Settings**.

![Auto Serial Batch Bundle Outward Configure](https://docs.frappe.io/assets/478388b3e1d4.png)

After the configuration, when the user creates a **Delivery Note** or a **Stock Entry** with the Type "Material Issue", the system will automatically create the outward **Serial and Batch Bundle** on submission of the record.

![Auto Serial Batch Bundle Outward](https://docs.frappe.io/assets/32c98e528e73.gif)

### Manual Creation of Serial and Batch Bundle for Inward Entry

For the **Serial and Batch Bundle** , both **Serial No** and **Batch** records must already exist in the system. With the manual option, the user must first create the **Serial No** / **Batch** records in the system. Users can use the CSV import option to create **Serial No** / **Batch** records. The blank CSV template can be downloaded using the Serial and Batch Selector.

![create-using-csv](https://docs.frappe.io/assets/cb2a0cc36a95.png)

Complete GIF for manual creation of a **Serial and Batch Bundle** for an inward entry is as follows:

![manually-create-serial-no-inward](https://docs.frappe.io/assets/b2351de46cf4.gif)

### Manual Creation of Serial and Batch Bundle for Outward Entry

Using the Serial and Batch Selector, the user can pick the Serial / Batch Nos based on the "FIFO / LIFO / Expiry" method.

![serial-batch-selector-outward](https://docs.frappe.io/assets/a0bd051fc393.png)

Complete GIF for manual creation of a **Serial and Batch Bundle** for an outward entry is as follows:

![manually-create-serial-no-outward](https://docs.frappe.io/assets/59cb52195881.gif)

### Serial and Batch Bundle Creation Using CSV for Outward Entry

Now users can create serial and batch bundles for outward entries by importing a CSV file.

![](../../assets/56d8ebbe8c87.png)

## History of Serial Numbers

To check the history of serial numbers, see the report "Serial No Ledger".

![](../../assets/d0a0f8fd3f37.png)

## Serial / Batch Selector

This is used to select Serial Nos / Batches manually. This popup is also used to create serial nos / batches automatically if they do not exist.

![serial-batch-selector](https://docs.frappe.io/assets/2d9772cf7ba7.gif)

## Disable Serial / Batch Selector

If users don't want to use the Serial and Batch Selector (popup), they can disable it through **Stock Settings**. To disable it, go to **Stock Settings** > Serial and Batch Item (TAB) > enable _Disable Serial No And Batch Selector_ , then save.

![disable-serial-batch-selector](https://docs.frappe.io/assets/70831649e69f.png)

## Old Serial / Batch Fields

Many customers requested that we retain the old serial and batch fields to address UX issues. In response to this demand, we retained the old serial/batch fields. These fields are solely used for entering serial numbers and batches. The system will automatically create the **Serial and Batch Bundle** upon submission of the stock transaction. To enable this feature, users must navigate to **Stock Settings** and enable the _Use Serial / Batch Fields_ option (see the image below).

![use-serial-batch-fields-global](https://docs.frappe.io/assets/c9f6ee57254d.png)

After that, when the user creates a stock transaction (for example, a **Delivery Note**), the system will show the old Serial / Batch fields. For more details, see the GIF below.

![user-old-serial-batch-fieldsd](https://docs.frappe.io/assets/6753541b41dc.gif)

Users can disable the old serial / batch fields at the transaction level too.

![use-serial-batch-for-dn](https://docs.frappe.io/assets/739ca6af35a1.gif)

## Update Serial / Batch on Creation of Auto Bundle

If the user wants to automatically update the Serial No / Batch in the Serial / Batch fields when a **Serial and Batch Bundle** is created, go to **Stock Settings** and disable _Do Not Update Serial / Batch on Creation of Auto Bundle_.

![update-Serial-Batch-on-creation-of-auto-bundle](https://docs.frappe.io/assets/b15f50ca0718.png)

Case:

  1. User has enabled _Use Serial / Batch Fields_ in **Stock Settings**
  2. User wants to create the **Serial and Batch Bundle** per single batch
  3. User has set the auto-create batch in the **Item** master.
  4. On submission of the **Purchase Receipt** , the system has created the auto **Batch** and **Serial and Batch Bundle** , and set the _Batch_ and _Serial and Batch Bundle_ fields on the **Purchase Receipt** line item.
  5. Updating the value of the batch takes time. If you want to skip this step, enable _Do Not Update Serial / Batch on Creation of Auto Bundle_ in **Stock Settings**.
  6. With this, the batch column remains blank, but the **Serial and Batch Bundle** will have the value of the auto-created bundle.



## How to Use **Serial and Batch Bundle**

[https://www.youtube.com/watch?v=-VjZvRtdjDQ&t=820s](https://www.youtube.com/watch?v=-VjZvRtdjDQ&t=820s)

[ Previous Page Serial Number ](serial-no.md) [ Next Page Delivery Trip  ](delivery-trip.md)

Last updated 2 weeks ago 

Was this helpful?
