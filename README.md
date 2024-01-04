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
