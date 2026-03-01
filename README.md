## 🎯 Project Overview
The goal of this project was to apply core Python concepts to build a real-world utility. It focuses on efficient data handling using nested dictionaries and ensures that data is preserved between sessions using JSON file operations.

### Key Features
* **Add New Contacts**: Includes real-time validation for phone numbers and email formats.
* **Search Functionality**: Supports partial name matching for quick lookups.
* **Data Persistence**: Automatically saves and loads contacts from `contacts_data.json`.
* **Contact Statistics**: Provides a breakdown of total contacts and category-wise counts.
* **Export to CSV**: Allows exporting the contact list for use in spreadsheet applications.

---


## 🛠️ Technical Details
### DATA STRUCTURE : The project utilizes a **Nested Dictionary** structure to store contact information efficiently

Core Logic
Functions: Modular code blocks for each operation (add, search, delete).

Regex (re): Used for cleaning non-digit characters from phone numbers and validating email syntax.

JSON Module: Handles the serialization of dictionary data to a physical file.
