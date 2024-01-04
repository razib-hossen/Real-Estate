# ERP-17: Getting started
---

# Chapter 1: Architecture Overview

Welcome to the Odoo 17 Development Getting Started Guide! This chapter provides an overview of the architecture of Odoo, offering insights into its structure and components.

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

## 2.2 Clone The ERP-17 Repository To Your Project Folder

```bash
# Clone the ERP-17 project
git clone https://github.com/razib-hossen/ERP-17.git

# Enter the ERP-17 project folder
cd ERP-17
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
./odoo/odoo-bin -c odoo.conf
```

Visit `http://localhost:8069` in your web browser to access the Odoo instance.


# Chapter 3: A New Application

In this chapter, we will guide you through the process of creating a new Odoo module called "estate." This involves setting up the necessary directory structure and creating the essential files, including the `__manifest__.py` file.

## 3.1 Editing __manifest__.py

Open the `__manifest__.py` file in a text editor and define the name of your module and its dependencies. For now, the only required dependency is the `base` module. Ensure that the `__manifest__.py` file looks like this:

```python
# /ERP-17/custom_addons/estate/__manifest__.py

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
./odoo/odoo-bin -c odoo.conf
```

## 3.3 Update Apps List

1. In the Odoo interface, go to **Apps**.
2. Click on **Update Apps List**.
3. Search for "estate."

Your module should appear in the list. If it doesn't, try removing the default 'Apps' filter, and it should be visible.

## 3.4 Making Your Module an 'App'

To make your module appear when the 'Apps' filter is applied, add the appropriate key to the `__manifest__.py` file. Update the file as follows:

```python
# /ERP-17/custom_addons/estate/__manifest__.py

{
    ...
    'installable': True,
    'application': True,
    'auto_install': False,
}
```

The `'application': True` key designates your module as an application, making it visible under the 'Apps' filter.

