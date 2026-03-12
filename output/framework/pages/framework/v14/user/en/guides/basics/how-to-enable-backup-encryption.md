# How to Enable Backup Encryption

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/127hu0jhkp)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# How to Enable Backup Encryption 

[ Edit ](https://docs.frappe.io/wiki/spaces/r3uvq1ch61/page/127hu0jhkp)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Files created during the backup process can be encrypted using an **Auto-generated key** by checking the **Encrypt Backup** option and the data can be saved under the default or provided location.

## System Requirements

For MacOS, ensure that [gnupg](https://formulae.brew.sh/formula/gnupg) is installed in the system. Use the following command to install gnupg:
[code] 
    brew install gnupg
    
[/code]

Most Linux distributions already have GnuPG installed, and the current version will likely use GnuPG 2.0 by default.

## Encrypt Backup option

  1. Under Settings tab go to `System settings`.

  2. Inside the `Backups` section check the `Encrypt Backup` checkbox.




![Encrypt Backup option\(Enabled\)](https://docs.frappe.io/assets/e0822295b9ce.png)

The system uses an auto-generated key supplied by the **Site config**. If no such key is found, **a new key is generated**. Any Administrator can later look it from the `https://{site}/app/backups` page.

It encrypts the public and private files as well as the partial backup files.

## Backup Encryption Status

  1. Encrypted backups are stored at the same location as the general backups `./sites/{site}/private/backups`.

  2. Encrypted backups can be downloaded from the `https://{site}/app/backups`

  3. Encrypted backups are differentiated using the `key icon`.




![Encrypt Backup option\(Enabled\)](https://docs.frappe.io/files/backup-page.png)

## Backup Encryption Key

  1. To get the backup encryption key go to the `./sites/{site}/private/backups`.

  2. Click on the `Get Encrpytion key` and verify your password.




![Encrypt Backup option\(Enabled\)](https://docs.frappe.io/assets/5bf2c857809f.png)

Copy the key to restore the encrypted backup files.

## Restoring the Encrypted backup files

  1. The `bench restore SQL_FILE_PATH` can be used to restore the files without `--backup-encryption-key` as it is automatically picked from the Site Config.

  2. In case of an unsuccessful restoration due to a wrong key `--backup-encryption-key` can be used to provide the key to restore the files.

  3. Usage:



  * For full backup files


[code] 
    bench --site {site} restore --backup-encryption-key {key} [OPTIONS]
    
[/code]

  * For partial backup files


[code] 
    bench --site {site} partial-restore --backup-encryption-key {key} [OPTIONS]
    
[/code]

[ Previous Page Frappe Ajax Call  ](frappe_ajax_call.md) [ Next Page Sites  ](sites.md)

Last updated 2 months ago 

Was this helpful?
