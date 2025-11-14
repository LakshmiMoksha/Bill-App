# Billing System — Flask & SQLite

A lightweight and efficient billing application built with Flask and SQLite, designed for generating itemized customer bills, storing billing records, and managing historical data.
The system provides a clean workflow for creating bills, calculating totals, and maintaining a searchable billing history with delete functionality.

---
# Tech Stack
*Backend* :Python,Flask,Jinja2 Templating

*Database*: SQLite

*Frontend*:HTML5,CSS3,Bootstrap
---

# Overview

- The application allows users to:

- Generate detailed bills with multiple items

- Automatically calculate line totals and final amounts

- Store bills securely in a local SQLite database

- View previously generated bills in a structured list

- Delete bills when needed

- Receive on-screen notifications using flash messages

This system is suitable for small shops, cafés, and businesses requiring a simple and offline-friendly billing solution.

---

# Features
*Bill Generation*

- Add items with name, unit price, and quantity

- Automatic calculation of subtotals and total bill amount

- Displays a formatted bill summary after submission

- Saves each generated bill with a timestamp

*Bill History Management*

- View all stored bills in reverse chronological order

- Each bill includes:

  - Customer name

  - Purchased items

  - Total amount

  - Date and time of creation

  - Delete bills using a secure POST operation
---

# System Functionality

- Automatic SQLite database creation on first run

- Built-in flash notifications for user feedback

- Clean and responsive templates rendered using Jinja2

- Lightweight backend suitable for local use or deployment
