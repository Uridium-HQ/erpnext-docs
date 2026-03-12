# Opening Balance in Accounts

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rmcrbi0ic>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Opening Balance in Accounts 

[ Edit ](</wiki/spaces/24hrpr6es9/page/0rmcrbi0ic>)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

**The opening balance is the balance that is brought forward at the beginning of an accounting period from the end of a previous accounting period or when starting out.**

This also applies when starting a new Company and would like your offline balances to be updated in ERPNext.

## 1\. Introduction

If you are a new company, you will have minimal opening balances to be imported. However, if you are migrating from a legacy accounting system like Tally or a Fox Pro based software you will have considerable data to be imported as opening balance.

We recommend that you start using ERPNext for accounting from a new financial year, but you could start midway too. To set up your accounts, you will need the following for the “day” you start using accounting in ERPNext:

### 1.1 Assets

  1. Stock assets (stock in hand).
  2. Fixed assets like furnitures, computers, etc.
  3. Accounts Receivables (AR) i.e. unpaid invoices which you have sent to your Customers.
  4. Current assets like bank balances, cash in hand, deposits, etc.



### 1.2 Liabilities

  1. Capital accounts like your shareholder’s (or owner’s) capital
  2. Current liabilities like loans, salary payables etc
  3. Accounts Payables(AP) i.e. unpaid invoices which your suppliers have sent you



If you were using another accounting software before, you should **close** financial statements in that software first. The closing balance of the accounts should be updated as an opening balance in the ERPNext. Before starting to update opening balance, ensure that your [Chart of Accounts](</erpnext/chart-of-accounts>) has all the Accounts required.

Opening entries can be created using the Opening Invoice Creation Tool in ERPNext.

> Opening entry is only for Balance Sheet accounts and not for Profit and Loss Accounts.

## 2\. Opening Balance of Assets

### 2.1 Update Fixed Assets

To import all the existing fixed assets first create the asset record and then create a Journal Entry to update the General Ledger.

**Step 1. Create Asset Records**

> To know about Assets in detail, [visit this page](</erpnext/asset>).

Create Asset record for each asset that your company owns which is not fully depreciated.

To create a new Asset:

  1. Create an [Item](</erpnext/item>) with 'Is fixed Asset' enabled.
  2. Go to **Assets > Assets > New**.
  3. Enter Asset Name.
  4. Enter Item Code.
  5. Enter Location.
  6. Enter the Purchase Date.
  7. Enter Gross Amount.
  8. Tick **Is Existing Asset.**
  9. Save.



![Opening Stock Balance](/files/asset-opening-balance.png)

**Step 2. Create Journal Entry to Update the Ledgers**

When you create an Asset with 'Is Existing Asset' checkbox ticked, the General Ledger is not updated. You will have to update the value via a Journal Entry.

To create a new Journal Entry:

  1. Go to: **Accounting > Masters and Accounts > Journal Entry > New.**
  2. Enter Posting Date.
  3. Select the appropriate fixed asset ledgers in Account column and enter the value in Debit column.
  4. Select 'Temporary Opening' ledger in Account column and enter the balancing amount in Credit column.
  5. Set 'Is Opening' to Yes.



![Journal Entry Fixed Asset Opening](/files/journal-entry-fixed-asset.png)

### 2.2 Update Stock Assets

Read [Opening Stock](</erpnext/opening-stock>) to understand how to set this up

### 2.3 Update Accounts Receivable

**Accounts Receivables is the balance amount your Customer owes you towards the Sales Invoices you have already sent to them.**

You can import the accounts receivables details using the [Opening Invoice Creation Tool](</erpnext/opening-invoice-creation-tool>).

After importing, Sales Invoices will be created. You can post Payment Entry against these invoices as and when you receive payment from your customer.

### 2.4 Update Current Assets

Before importing current assets, make sure that you have created the required ledgers under **Chart of Accounts > Assets > Current Assets** group.

To import details of current assets:

  1. Go to: **Accounting > Company and Accounts > Journal Entry > New**.
  2. Enter Posting Date.
  3. Select the appropriate current asset ledger in the Account column and enter the value in Debit.
  4. Select 'Temporary Opening' ledger in Account and enter the balancing amount in Credit.
  5. Set 'Is Opening' to Yes.



> To know about Journal Enter in detail, [visit this page](</erpnext/journal-entry>).

![Opening Balance Current Assets](/files/opening-balance-current-assets.png)

## 3\. Opening Balance of Liabilities

### 3.1 Update Capital Accounts

Before importing capital accounts, make sure that you have created the required ledgers under **Chart of Accounts > Liabilities > Capital Accounts** group.

To import details of capital accounts:

  1. Go to: **Accounting > Masters and Accounts > Journal Entry > New**.
  2. Enter Posting Date.
  3. Select the appropriate capital account ledgers in Account column and enter the value in Credit column.
  4. Select 'Temporary Opening' ledger in Account and enter the balancing amount in Debit column.
  5. Set 'Is Opening' to Yes.



![Opening Entry Capital Accounts](/files/opening-balance-capital-accounts.png)

### 3.2 Update Current Liabilities

Before importing current liabilities, make sure that you have created the required ledgers under **Chart of Accounts > Liabilities > Current Liabilities** group.

To import details of current liabilities:

  1. Go to: **Accounting > Masters and Accounts > Journal Entry > New**.
  2. Enter Posting Date.
  3. Select the appropriate current liability ledgers in the Account column and enter the value in the Credit column.
  4. Select 'Temporary Opening' ledger in Account and enter the balancing amount in Debit column.
  5. Set 'Is Opening' to Yes.



![Opening Balance Current Liabilities](/files/opening-balance-current-liabilities.png)

### 3.3 Update Accounts Payable

**Accounts Payables is the balance amount you owe your Suppliers towards the invoices they have already sent you.**

You can import the accounts payables details using the [Opening Invoice Creation Tool](</erpnext/opening-invoice-creation-tool>).

After importing, Purchase Invoices will be created. You can post Payment Entry against these invoices as and when you make the payment.

## 4\. Verify the Opening Balance

Once all assets and liabilities have been imported, the balance of **Temporary Opening** ledger should be zero.

[ Previous Page Opening Invoice Creation Tool  ](</erpnext/opening-invoice-creation-tool>) [ Next Page Setting Up Taxes  ](</erpnext/setting-up-taxes>)

Last updated 1 week ago 

Was this helpful?
