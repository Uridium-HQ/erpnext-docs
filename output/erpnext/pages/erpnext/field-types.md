# Field Types

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t78bjp255)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

# Field Types

[ Edit ](https://docs.frappe.io/wiki/spaces/24hrpr6es9/page/0t78bjp255)

Open in ChatGPT  Ask ChatGPT about this page Open in Claude  Ask Claude about this page

The following are the types of fields you can define while creating new ones, or while amending standard ones.

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](creating-custom-link-field.md).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](dynamic-link-fields.md) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here.

![Check Field TYpe](../../assets/42a7022022f2.png)

#### Select

Select will be a drop-down field. You can add multiple results in the Option field, separated by row.

![Select Field Type](../../assets/d45e967f923c.png)

#### Table

A table will be a kind of Link field which renders another DocType within the current form. For example, the Item Table in the Sales Order is a Table field, which is linked to Sales Order Item DocType.

![Table Field Type](../../assets/5f1eae8c45b9.png)

#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

![Attach Field Type](../../assets/3386d3b620b4.png)

#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

![Field Type Image](../../assets/d8520dae5e80.png)

#### Text Editor

Text Editor is a text field. It has text-formatting options. In ERPNext, this field is generally used for defining Terms and Conditions.

![Field Type Text Editor](../../assets/8436a1fde0c9.png)

#### Date

This field will enable you to enter the Date in this field.

![Field Type Date](../../assets/c7a53f4eb951.png)

#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

![Field Type Date and Time](../../assets/9b9c89dbb8ff.png)

#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Oce you do that, the Barcode would automatically get generated against the number.

![Field Type Barcode](../../assets/632ee7d8463d.png)

#### Button

This kind of field will be an action button, like Save, Submit, etc.

![Field Type Button](../../assets/ef024050360f.png)

#### Code

If the Field Type is selected as code, you will be able to enter a Code to the field.

![Field Type Code](../../assets/7578813e45f3.png)

#### Color

You will have the option of specifying the color for this Form.

![Field Type Colour](../../assets/1c78b3ff3ce7.png)

#### Column Break

Since ERPNext has multiple column layouts, using Column Breaks, you can divide a set of fields into a maximum of two columns.

![Field Type Column Break](../../assets/0e6400b50ed3.png)

#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

![Field Type Currency](../../assets/c922a3d3adbc.png)

#### Data

The data field will be a simple text field. It allows you to enter a value of up to 140 characters, making this the most generic field type. To enable validations for Email, Name, or Phone Number inputs, set options to "Email", "Name", "Phone" in Settings > DocType.

![Field Type Data](../../assets/559ba56bdd89.png)

#### Float

Float field carries numeric value, up to nine decimal places. Precision for the float field is set via [Set Precision](set-precision.md)

> Setup > Settings > System Settings

The setting will be applicable on all the float field.

![Field Type Float](../../assets/87db1fd3f5e1.png)

#### Geolocation

Use Geolocation field to store GeoJSON [feature_collection](https://tools.ietf.org/html/rfc7946). Stores polygons, lines, and points. Internally it uses the following custom properties for identifying a circle.

Read [Geolocation field](geolocation-field.md) for more understanding.

![Field Type Geolocation](../../assets/4d6fabab14f3.png)

#### HTML

You can select the field to be an HTML field when you want the data to be entered in HTML format.

![Field Type HTML](../../assets/039c74a59cde.png)

#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

![Field Type Image](../../assets/8cdb77484862.png)

#### Int (Integer)

The integer field holds numeric value, without decimal place.

![Field Type Integer](../../assets/fc708884ea94.png)

#### Small Text

Small Text field carries text content and has more character limit than the Data field.

![Field Type Small Text](../../assets/e5ef0fb01b9e.png)

#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

![Field Type Long Text](../../assets/265e335fe08a.png)

#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

![Field Type Text](../../assets/9df731d98060.png)

#### Markdown Editor

This field will allow you to add the text in Markup language.

![Field Type Markdown Editor](../../assets/884289e88b17.png)

#### Password

The password field will have decoded value in it.

![Field Type Password](../../assets/dc594d16d2f6.png)

#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

![Field Type Percent](../../assets/8b72a44b77ef.png)

#### Rating

You can define the field as a Rate field which in the background will be calculated as Rating.

![Field Type Rating](../../assets/2e97e9aaf6e5.png)

#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

![Field Type Read Only](../../assets/5517b31ffc9e.png)

#### Section Break

Section Break is used to divide the form into multiple sections.

![Field Type Section Break](../../assets/06444cfed20e.png)

#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field.

![Screenshot 2024-08-28 at 3.01.56 PM](../../assets/8326a757c905.png)

#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.

![Field Type Table MultiSelect](../../assets/a90d033311a8.png)

#### Time

This is a Time field where you can define the Time in the field.

![Field Type Time](../../assets/b371b29be376.png)

#### Duration

You can use the Duration field if you want to define a timespan.

![Field Type Duration](../../assets/3b7116d7babf.png)

If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form.

![Field Type Duration Options](../../assets/a3e0de4f33c5.png)

This is how the duration field looks after the above changes.

![Field Type Duration](../../assets/e2b0307a40f7.png)

[ Previous Page Document Naming Rule ](document-naming.md) [ Next Page Geolocation Field ](geolocation-field.md)

Last updated 1 week ago 

Was this helpful?
