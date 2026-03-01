import json
import re
import csv
from datetime import datetime

def validate_phone(phone):
    """Clean and validate phone number format (10-15 digits)."""
    digits = re.sub(r'\D', '', phone)
    return (True, digits) if 10 <= len(digits) <= 15 else (False, None)

def validate_email(email):
    """Regex to validate email format."""
    if not email: return True
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def load_contacts():
    """Load data from JSON file on startup."""
    try:
        with open('contacts_data.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    """Save contacts dictionary to JSON."""
    with open('contacts_data.json', 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    """Add a new contact with nested dictionary structure."""
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return contacts
    
    phone = input("Enter phone number: ")
    valid, clean_phone = validate_phone(phone)
    if not valid:
        print("Invalid phone number format.")
        return contacts

    email = input("Enter email (optional): ")
    group = input("Enter group (Friends/Work/Family/Other): ") or "Other"
    
    contacts[name] = {
        "phone": clean_phone,
        "email": email if email else None,
        "group": group,
        "updated_at": datetime.now().isoformat()
    }
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")
    return contacts

def search_contacts(contacts):
    """Search by name with partial matching."""
    term = input("Enter name to search: ").lower()
    results = {n: i for n, i in contacts.items() if term in n.lower()}
    if not results:
        print("No matches found.")
    else:
        for name, info in results.items():
            print(f"\nName: {name}\nPhone: {info['phone']}\nGroup: {info['group']}")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- CONTACT MANAGEMENT SYSTEM ---")
        print("1. Add Contact\n2. Search\n3. View All\n4. Exit")
        choice = input("Select (1-4): ")
        if choice == '1': contacts = add_contact(contacts)
        elif choice == '2': search_contacts(contacts)
        elif choice == '3': print(json.dumps(contacts, indent=2))
        elif choice == '4': break

if __name__ == "__main__":
    main()
