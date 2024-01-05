# Real Estate
---

# Chapter 1: Architecture Overview

## 1.1 Architecture Components Interaction

Understanding the interaction between different components is crucial for Odoo development:

- The web client communicates with the server through JSON-RPC requests.
- Odoo modules define data models, views, and business logic.
- The server handles requests, processes data using the ORM, and updates the database accordingly.

## 1.2 Development Workflow

When developing for Odoo, follow these general steps:

1. **Set Up Development Environment:**
   - Install Python, PostgreSQL, and Odoo locally.
   - Create a virtual environment for your project.

2. **Create a Custom Module:**
   - Define your module structure.
   - Create models, views, and controllers as needed.

3. **Testing:**
   - Write unit tests to ensure your module works as expected.
   - Use Odoo testing tools.

4. **Deployment:**
   - Deploy your module to a development instance of Odoo for testing.
   - Once satisfied, deploy to a production environment.



# Chapter 2: Development Environment Setup

## 2.1 Prerequisites

Before you start setting up your development environment, make sure you have the following prerequisites installed on your system:

- **Python:** Odoo is primarily written in Python. Install a compatible version of Python (preferably Python 3.11 or higher).

- **PostgreSQL:** Odoo uses PostgreSQL as its database. Install and configure a PostgreSQL server (preferably PostgreSQL 15 or higher).

- **Git:** Version control is essential for collaborative development. Install Git to manage your source code.

## 2.2 Clone The Real-Estate Repository To Your Project Folder

```bash
# Clone the Real-Estate project
git clone https://github.com/razib-hossen/Real-Estate.git

# Enter the Real-Estate project folder
cd Real-Estate
```

## 2.2 Virtual Environment

It's a good practice to create a virtual environment for your Odoo project. This helps isolate your project dependencies from the system-wide Python environment.

```bash
# Create a virtual environment
python3.11 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## 2.3 Odoo Installation

Clone the Odoo source code from the official repository:

```bash
git clone https://www.github.com/odoo/odoo --depth 1 --branch 17.0 --single-branch .
```

Install the required Python dependencies using pip:

```bash
pip install -r odoo/requirements.txt
```

## 2.4 Database Setup

Create a new PostgreSQL database for your Odoo instance:

```bash
createdb odoo-test
```

## 2.5 Configuration

Copy the Odoo configuration file and customize it according to your needs:

```bash
# Create a directory 
mkdir conf

# Copy the configuration file
cp examples/local.example conf/local.conf
```

Edit `local.conf` to set the database connection parameters, addons path, and other configuration options.

## 2.6 Running Odoo

You can now run Odoo using the following command:

```bash
./odoo/odoo-bin -c conf/local.conf
```

Visit `http://localhost:8069` in your web browser to access the Odoo instance.


# Chapter 3: A New Application

In this chapter, we will guide you through the process of creating a new Odoo module called "estate." This involves setting up the necessary directory structure and creating the essential files, including the `__manifest__.py` file.

## 3.1 Editing __manifest__.py

Open the `__manifest__.py` file in a text editor and define the name of your module and its dependencies. For now, the only required dependency is the `base` module. Ensure that the `__manifest__.py` file looks like this:

```python
# /Real-Estate/estate/__manifest__.py

{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Rajib Mahmud',
    'category': 'Services',
    'description': """
    The Real Estate Advertisement module.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',

    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

```

This `__manifest__.py` file provides essential information about your module, including its name, version, summary, description, author, and dependencies.

## 3.2 Restarting the Odoo Server

Restart the Odoo server to apply the changes you made:

```bash
./odoo/odoo-bin -c conf/local.conf
```

## 3.3 Update Apps List

1. In the Odoo interface, go to **Apps**.
2. Click on **Update Apps List**.
3. Search for "estate."

Your module should appear in the list. If it doesn't, try removing the default 'Apps' filter, and it should be visible.

## 3.4 Making Your Module an 'App'

To make your module appear when the 'Apps' filter is applied, add the appropriate key to the `__manifest__.py` file. Update the file as follows:

```python
# /Real-Estate/estate/__manifest__.py

{
    ...
    'installable': True,
    'application': True,
    'auto_install': False,
}
```

The `'application': True` key designates your module as an application, making it visible under the 'Apps' filter.


# Chapter 4: Models and Basic Fields

In this chapter, we will define the Real Estate Properties model and add basic fields to the `estate.property` table. Follow the exercises to create the necessary files and implement the required model attributes.

## 4.1 Define the Real Estate Properties Model

Create the appropriate files and folders for the `estate.property` model. Based on the example in the CRM module, add a minimum definition for the `estate.property` model.

Edit the `property.py` file to include these fields:

```python
# /Real-Estate/estate/models/property.py

from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Property Name')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation',
    )
```

After making these changes, restart the server with the following command:

```bash
./odoo/odoo-bin -c conf/local.conf -u estate
```


# Chapter 5: Security - A Brief Introduction

In this chapter, we will introduce security concepts in Odoo and provide a brief exercise on adding access rights to the Real Estate Property model.

## 5.1 Understanding Access Rights

Access rights in Odoo are defined as records of the model `ir.model.access`. Each access right is associated with a model, a group (or no group for global access), and a set of permissions: create, read, write, and unlink.

For our Real Estate Property model, we will define access rights in a CSV file named `ir.model.access.csv`. This file will specify the permissions granted to a specific group (in this case, `base.group_user`).

## 5.2 Exercise: Add Access Rights

### Step 1: Create `ir.model.access.csv` File

Create the `ir.model.access.csv` file in the appropriate folder (`security` folder in this case) with the following content:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_estate_property,access_estate_property,model_estate_property,base.group_user,1,1,1,1
```

### Step 2: Reference in `__manifest__.py`

Now, reference the `ir.model.access.csv` file in the `data` section of your `__manifest__.py` file:

```python
# /Real-Estate/estate/__manifest__.py

{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Rajib Mahmud',
    'category': 'Services',
    'description': """
    The Real Estate Advertisement module.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
```

### Step 3: Restart the Server

After adding the access rights, restart the Odoo server:

```bash
./odoo/odoo-bin -c conf/local.conf
```


# Chapter 6: Finally, Some UI To Play With

In this chapter, we will enhance the Real Estate Property model by adding a state field with specific configurations.

## Exercise: Add State Field

### Step 1: Update the `estate.property` Model

Edit the `estate_property.py` file to add the state field to the `EstateProperty` model:

```python
# /Real-Estate/estate/models/property.py

from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    .........
    .........
    
    state = fields.Selection(
        [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
         ('sold', 'Sold'), ('canceled', 'Canceled')],
        string='State',
        required=True,
        default='new',
        copy=False,
    )
```

### Step 2: Restart the Server

After adding the state field, restart the Odoo server:

```bash
./odoo/odoo-bin -c conf/local.conf
```


# Chapter 7: Basic Views

In this chapter, we'll add custom views to enhance the user interface of the Real Estate Property module.

## Exercise: Add a Custom Search View

Follow a similar process to create a custom search view. Create a new XML file named `property_view.xml` in the `views` folder and define the search view.

## Exercise: Add Filter and Group By

Edit the `property_view.xml` file to add the required filter and group by functionalities:

```xml
<!-- /Real-Estate/estate/views/property_view.xml -->

<record id="view_estate_property_search" model="ir.ui.view">
    <field name="name">estate.property.search</field>
    <field name="model">estate.property</field>
    <field name="arch" type="xml">
        <search>
            <field name="name"/>
            <field name="state" filter_domain="[('state', 'in', ['new', 'offer_received'])]"/>
            <filter name="group_by_postcode" string="Group by Postcode" context="{'group_by': 'postcode'}"/>
            <!-- Add other fields as needed -->
        </search>
    </field>
</record>
```

Reference this search view in the `__manifest__.py` file under the `data` section.

### Step 4: Restart the Server

After adding the views, restart the Odoo server:

```bash
./odoo/odoo-bin -c conf/local.conf
```


# Chapter 8: Relations Between Models

In this chapter, we will establish relationships between models in the Real Estate module by adding the Real Estate Property Type, Buyer, Salesperson, Property Tag, and Property Offer tables.

## Exercise: Add the Real Estate Property Type Table

### Step 1: Create the `estate.property.type` Model

Create a new Python file named `property_type.py` inside the `models` folder:

```bash
touch /Real-Estate/estate/models/property_type.py
```

Edit `property_type.py` and define the `estate.property.type` model:

```python
# /Real-Estate/estate/models/property_type.py

from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'

    name = fields.Char(string='Property Type', required=True)
```

### Step 2: Update `__init__.py`

Make sure to import the new Python file in the `__init__.py` file:

```python
# /Real-Estate/estate/models/__init__.py

from . import estate_property
from . import property_type  # Add this line
```

### Step 3: Update `__manifest__.py`

Add the new model to the `data` section in the `__manifest__.py` file:

```python
# /Real-Estate/estate/__manifest__.py

{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Rajib Mahmud',
    'category': 'Services',
    'description': """
    The Real Estate Advertisement module.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
```

### Step 4: Create the Form and Tree Views

Create the form and tree views for the `estate.property.type` model in XML files inside the `views` folder.

`estate_property_type_form_view.xml`:

```xml
<!-- /Real-Estate/estate/views/property_type_view.xml -->

<record id="view_estate_property_type_form" model="ir.ui.view">
    <field name="name">estate.property.type.form</field>
    <field name="model">estate.property.type</field>
    <field name="arch" type="xml">
        <form>
            <group>
                <field name="name"/>
            </group>
        </form>
    </field>
</record>
```

`estate_property_type_tree_view.xml`:

```xml
<!-- /Real-Estate/estate/views/property_type_view.xml -->

<record id="view_estate_property_type_tree" model="ir.ui.view">
    <field name="name">estate.property.type.tree</field>
    <field name="model">estate.property.type</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name"/>
        </tree>
    </field>
</record>
```

### Step 5: Restart the Server

Restart the Odoo server:

```bash
./odoo/odoo-bin -c conf/local.conf
```

## Exercise: Add Buyer and Salesperson

### Step 1: Update the `estate.property` Model

Edit the `property.py` file and add the `buyer_id` and `salesperson_id` fields:

```python
# /Real-Estate/estate/models/property.py

from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    .......
    .......

    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user.id)
```

### Step 2: Update the `estate_property` Form View

Edit the `estate_property_form_view.xml` file to include the new fields:

```xml
<!-- /Real-Estate/estate/views/property_view.xml -->

<record id="view_estate_property_form" model="ir.ui.view">
    <field name="name">estate.property.form</field>
    <field name="model">estate.property</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <!-- Existing fields -->
                    <field name="name"/>
                    <field name="description"/>
                    <field name="state"/>
                    <!-- New fields -->
                    <field name="buyer_id"/>
                    <field name="salesperson_id"/>
                </group>
            </sheet>
        </form>
    </field>
</record>
```

### Step 3: Restart the Server

Restart the Odoo server:

```bash
./odoo/odoo-bin -c conf/local.conf
```

## Exercise: Add the Real Estate Property Tag Table

Follow similar steps to add the Real Estate Property Tag table:

1. Create the `estate.property.tag` model with the `name` field.
2. Update the `__init__.py` file to import the new Python file.
3. Update the `__manifest__.py` file to include the new model in the `data` section.
4. Create the form and tree views for the `estate.property.tag


# Chapter 9: Computed Fields And Onchanges

**Feature List:**

1. **Total Area Computation:**
   - Computed `total_area` in the `estate.property` model based on `living_area` and `garden_area`.

2. **Best Offer Calculation:**
   - Introduced `best_offer` in the `estate.property` model, computed from the total sum of `price` in related offers.

3. **Onchange for Garden Field:**
   - Implemented `_onchange_garden` to set/clear values for `garden_area` and `garden_orientation` based on the `garden` field.

4. **Computed Offer Validity and Deadline:**
   - Added computed fields `validity` and `deadline` in the `estate.property.offer` model.

5. **Onchange for Offer Deadline:**
   - Implemented `_onchange_deadline` to update `validity` when `deadline` changes.

6. **Onchange for Offer Validity:**
   - Added `_onchange_validity` to update `deadline` when `validity` changes.


# Chapter 10: Ready For Some Action?

**Feature List:**

1. Added buttons "Accept" and "Refuse" to the form view of the `estate.property.offer` model.
2. Implement logic in the `estate.property` model to handle the "SOLD" and "CANCEL" buttons.
3. Add logic in the `estate.property.offer` model to handle the "Accept" and "Refuse" buttons. Include logic for setting the buyer and selling price when an offer is accepted.
4. Ensure that a canceled property cannot be set as sold, and a sold property cannot be canceled.
5. Ensure that only one offer can be accepted for a given property.


# Chapter 11: Constraints

### Feature List:

1. **SQL Constraints:**
   - Property Model:
     - Ensure that the expected price is strictly positive.
     - Ensure that the selling price is positive.
   - Offer Model:
     - Ensure that the offer price is strictly positive.
   - Property Tag Model and Property Type Model:
     - Ensure that the name for both is unique.

2. **Python Constraint:**
   - Property Model:
     - Implement a constraint to ensure that the selling price cannot be lower than 90% of the expected price.
     - Take into account that the selling price is zero until an offer is validated.
     - Utilize `float_compare()` and `float_is_zero()` methods from `odoo.tools.float_utils` when working with floats.
