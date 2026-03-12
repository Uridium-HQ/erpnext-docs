# Bank Transaction

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rq5i41c92)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Bank Transaction

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0rq5i41c92)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

The **Bank Transaction** form shows bank transactions imported into ERPNext, typically from bank statements or integrations.

## 1\. Prerequisites

Before using **Bank Transaction** , it is advised that you create the following first:

  1. **[Bank](bank.md)**
  2. **[Bank Account](bank-account.md)**



## 2\. How to use Bank Transaction

A **Bank Transaction** is typically not created manually. It can be imported or created using:

  1. **[Bank Statement Import](bank-reconciliation.md)** — import from CSV or XLSX files
  2. **[Data Import](https://docs.frappe.io/erpnext/user/manual/en/data-import)** — standard data import tool
  3. Bank integration apps (e.g., Plaid or other third-party integrations)



Once imported, **Bank Transactions** can be reconciled with vouchers using the **[Bank Reconciliation Tool](bank-reconciliation.md)**.

## 3\. Fields

### 3.1 Basic Information

  * _Date_ : The date of the bank transaction.
  * _Status_ : The current status of the transaction:
    * Pending
    * Settled
    * Unreconciled
    * Reconciled
    * Cancelled
  * _Bank Account_ : The **Bank Account** from which the transaction was made.
  * _Company_ : The **Company** associated with the bank account (auto-fetched from _Bank Account_).



### 3.2 Transaction Amount

  * _Deposit_ : The amount deposited (credited to your account).
  * _Withdrawal_ : The amount withdrawn (debited from your account).
  * _Currency_ : The currency in which the transaction was made.



### 3.3 Description and Reference

  * _Description_ : A description from the bank statement.
  * _Reference Number_ : A cheque number or other reference.
  * _Transaction ID_ : A unique identifier from the bank (read-only).
  * _Transaction Type_ : The type of transaction as reported by the bank.



### 3.4 Payment Entries

The _Payment Entries_ table links the bank transaction to vouchers in ERPNext for reconciliation:

  * _Payment Document_ : The document type against which the transaction was reconciled, such as **Sales Invoice** , **Purchase Invoice** , **Payment Entry** , **Journal Entry** , or **Expense Claim**.
  * _Payment Entry_ : The specific document linked to this transaction.
  * _Allocated Amount_ : The amount allocated from this bank transaction to the payment entry.
  * _Clearance Date_ : The date when the payment was cleared (shown after submission).



### 3.5 Allocation Summary

  * _Allocated Amount_ : The total amount that has been allocated to payment entries (read-only).
  * _Unallocated Amount_ : The remaining amount that has not been allocated (read-only).



### 3.6 Payment From / To (Party Information)

  * _Party Type_ : The type of party (e.g., Customer, Supplier, Employee).
  * _Party_ : The specific party linked to this transaction.



The following fields contain party information as provided by the bank statement:

  * _Party Name/Account Holder (Bank Statement)_ : The party name from the bank statement.
  * _Party Account No. (Bank Statement)_ : The party's account number from the bank statement.
  * _Party IBAN (Bank Statement)_ : The party's IBAN from the bank statement.



> Party information from the bank statement can be used for automatic party matching when enabled in **Accounts Settings**.

### 3.7 Extended Bank Statement (Fee Handling)

These fields handle bank fees that may be included in or excluded from the transaction amount:

  * _Included Fee_ : A fee that is already included within the _Withdrawal_ amount. For example, if a withdrawal of 100 includes a 5 fee, the net payment is 95.
  * _Excluded Fee_ : A fee that was charged separately from the transaction. On save, this is automatically converted to an _Included Fee_ by adjusting the transaction amount.



> **Note:** Excluded fees adjust the transaction amount: they reduce _Deposit_ or increase _Withdrawal_.

[ Previous Page UnReconcile ](https://docs.frappe.io/erpnext/unreconciliation) [ Next Page Include Tax or Charge in Valuation or Total? ](../../../difference-in-total-and-valuation-in-tax-and-charges.md)

Last updated 2 weeks ago 

Was this helpful?
