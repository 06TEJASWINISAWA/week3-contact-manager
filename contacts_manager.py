import json
import csv
import re

# -------- PHONE VALIDATION --------
def valid_phone(phone):
    return re.fullmatch(r"\d{10}", phone)

# -------- LOAD CONTACTS --------
def load_contacts():
    try:
        with open('contacts_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("\n✅ No existing contacts file found. Starting fresh.")
        return {}

# -------- SAVE CONTACTS --------
def save_contacts(contacts):
    with open('contacts_data.json', 'w') as f:
        json.dump(contacts, f, indent=4)

# -------- ADD CONTACT --------
def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter contact name: ").strip()

    if name in contacts:
        print("⚠ Contact already exists!")
        return contacts

    # Phone validation
    while True:
        phone = input("Enter phone number: ").strip()
        if valid_phone(phone):
            break
        else:
            print("❌ Invalid phone number! Enter exactly 10 digits.")

    email = input("Enter email (optional): ").strip()
    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email if email else None,
        "address": address if address else None,
        "group": group
    }

    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")
    return contacts

# -------- SEARCH CONTACT --------
def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("\n📌 Contact Found:")
        for key, value in contacts[name].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("❌ Contact not found!")

# -------- UPDATE CONTACT --------
def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name in contacts:
        print("Leave blank to keep old value")

        phone = input("New Phone (10 digits): ").strip()
        email = input("New Email: ").strip()
        address = input("New Address: ").strip()
        group = input("New Group: ").strip()

        if phone:
            if valid_phone(phone):
                contacts[name]["phone"] = phone
            else:
                print("❌ Invalid phone number! Update skipped.")

        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address
        if group:
            contacts[name]["group"] = group

        save_contacts(contacts)
        print("✅ Contact updated successfully!")
    else:
        print("❌ Contact not found!")

# -------- DELETE CONTACT --------
def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑 Contact deleted successfully!")
    else:
        print("❌ Contact not found!")

# -------- VIEW ALL CONTACTS --------
def view_all_contacts(contacts):
    if not contacts:
        print("📭 No contacts available.")
        return

    print("\n📒 All Contacts:")
    for name, details in contacts.items():
        print(f"\nName: {name}")
        for key, value in details.items():
            print(f"  {key.capitalize()}: {value}")

# -------- EXPORT TO CSV --------
def export_to_csv(contacts):
    with open('contacts_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

        for name, details in contacts.items():
            writer.writerow([
                name,
                details["phone"],
                details["email"],
                details["address"],
                details["group"]
            ])
    print("📁 Contacts exported to contacts_export.csv")

# -------- VIEW STATISTICS --------
def view_statistics(contacts):
    total = len(contacts)
    groups = {}

    for c in contacts.values():
        grp = c["group"]
        groups[grp] = groups.get(grp, 0) + 1

    print("\n📊 Contact Statistics")
    print("Total Contacts:", total)
    for g, count in groups.items():
        print(f"{g}: {count}")

# -------- MAIN PROGRAM --------
def main():
    contacts = load_contacts()

    print("\n==========================================")
    print("        CONTACT MANAGEMENT SYSTEM         ")
    print("==========================================")

    while True:
        print("\n============================")
        print("         MAIN MENU          ")
        print("============================")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")
        print("============================")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            view_all_contacts(contacts)
        elif choice == '6':
            export_to_csv(contacts)
        elif choice == '7':
            view_statistics(contacts)
        elif choice == '8':
            print("\nThank you for using Contact Management System!")
            break
        else:
            print("⚠ Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    main()
