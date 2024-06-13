''' Contact information: store name, phone number, email and address for each contact. Add contact:
allow users to add new contacts with their details. 
View contact list: display a list of all saved contacts with names and phone numbers. 
Search contact: implement a search function to find contacts by name and phone numbers. 
Update contact: enable users to update contact details
Delete contact: provide an option to delete a contact. 
User interface: design a user-friendly interface for easy interaction'''

contacts = []

def add_contact():
    name= input("enter contact name:")
    phone = input("enter contact phone number:")
    email = input("enter the email address:")
    contacts.append({"name":name, "phone":phone, "email":email})
    print("Contact added succesfully!")

def  view_contacts():
    if not contacts:
        print("no contacts available.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']}- {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    results = [c for c in contacts if search_term.lower() in c['name'].lower() or search_term in c['phone']]
    if results:
        print("\nSearch Results:")
        for idx, contact in enumerate(results, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
    else:
        print("No contacts found.")

def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Updating contact: {contact['name']} - {contact['phone']}")
            contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
            contact['phone'] = input("Enter new phone number (leave blank to keep current): ") or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("Contact List:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice= int(input("Enter your choice:"))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

main()
