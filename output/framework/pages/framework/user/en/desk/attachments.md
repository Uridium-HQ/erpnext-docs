# Attachments

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0tovb5ngom)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Attachments

[ Edit ](https://docs.frappe.io/wiki/spaces/1u8fslkdg6/page/0tovb5ngom)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

Frappe allows attachment of files to documents. Users with **Read** permissions on a particular document will also be able to access the files attached to it. Users can also access the File Manager from the sidebar.

![attachments-sidebar](https://docs.frappe.io/assets/6ef704e8497d.png)

## How to Attach a New File

There are several ways to attach a file to a document.

### Select File

![attach-from-disk](https://docs.frappe.io/assets/580e2733674b.gif)

### Drag and Drop

![2023-08-28 13.28.01](https://docs.frappe.io/assets/1a9d6da9ae8c.gif)

### Uploaded File

Attach a file a that was previously uploaded, to a different document.

![2023-08-28 13.33.07](https://docs.frappe.io/assets/802c652a533d.gif)

### Web Link

If you use a separate server for files or use online services like Dropbox or Docs, you can attach a file by providing a link to it.

![2023-08-28 13.34.48](https://docs.frappe.io/assets/46fea73f357e.gif)

### Camera

Attach Images by taking a photo using your device's camera.

![Camera](https://docs.frappe.io/assets/651847491069.gif)

## File Manager

All the attached files are listed in the File Manager. You can access these by navigating here:

**Home > Tools > Files**

![Screenshot 2023-07-31 at 8.01.55 PM](https://docs.frappe.io/assets/fcbfecb7f977.png)

## Import Zip

You can also bulk import multiple files at once using the Import Zip feature.

  1. Go to **File List > Menu > Import Zip**.
  2. Upload a zip file.
  3. After the zip file is uploaded, it's contents will be extracted and each file will be created as a new File record.



![Importing files from zip](https://docs.frappe.io/assets/005c3f70cd68.gif)

> Note: Hidden files (files starting with `.`) are not extracted when importing from a zip file.

## Export as Zip

You can also bulk export multiple files at once using the Export as Zip feature.

  1. Go to **File List**.
  2. Select multiple files.
  3. Click on Actions > Export as zip.
  4. After the zip file is downloaded, you can import it in another site using Import Zip feature or send it across via email.



![Export files as zip](https://docs.frappe.io/assets/e55e974c1caf.png)

## Cropping Images

You can crop `.jpeg` and `.png` images by clicking on the crop icon.

![Cropping images on upload](https://docs.frappe.io/assets/b9d793aa2b55.gif)

## Optimizing Images

Images can be optimized to reduce their file size. Currently optimizing an image does the following:

  1. Resizes it to fit a max-width of 1920px and a max-height of 1080px, while preserving the aspect ratio
  2. Uses optimal encoder settings
  3. Reduces the quality to 85%



**Toggle optimization during upload**

![Toggle image optimization](https://docs.frappe.io/assets/f63850d37a68.gif)

**Optimize an already uploaded image**

![Optimize saved image](https://docs.frappe.io/assets/a1e5c24d2d2e.gif)

## Limits

A limit of 10MB is applicable on file size per attachment by default. For self-hosted users, this can be changed by setting `max_file_size` in your site's configuration file.

### Attachments per Document

You can limit how many files can be attached to a specific document.

#### Step 1: Navigate to Customize Form

> Home > Customization > Customize Form

#### Step 2: Select Document Type

Select the document type for which you'd like to set this limit.

![Select Document Type](https://docs.frappe.io/assets/241c3779c81f.png)

#### Step 3: Set Limit

Set the value of **Max Attachments** to the maximum number of attachments allowed for this document type.

![Set Limit](https://docs.frappe.io/assets/4fe6ce79762f.png)

Once you're satisfied with the changes, click the **Update** button. That's it! The maximum number of attachments per document will now be validated every time a new attachment is added to a document of this type.

[ Previous Page Printing ](printing.md) [ Next Page Scripting  ](scripting.md)

Last updated 3 weeks ago 

Was this helpful?
