from users import add_user, update_user, delete_user, get_user, get_all_users
from events import add_event, update_event, delete_event, get_event, get_all_events
from invitations import add_invitation, update_invitation, delete_invitation, get_invitation, \
    get_invitations_by_event, get_invitations_by_user, add_comment_to_invitation, get_attendees, \
    get_invitations_with_comments, get_invitation_statistics, send_invitation_notifications, get_all_invitations

import uuid

def list_and_select(items, item_type):
    """
    Display a list of items and prompt the user to select one by number.
    Params:
        items (list): A list of dictionaries representing items.
        item_type (str): The type of item being displayed.
    Returns:
        dict or None: The selected item from the list, or None if no selection is made.
    """
    if not items:
        print(f"No {item_type} found.")
        return None

    for index, item in enumerate(items):
        display_item = {k: v for k, v in item.items() if k != 'id'}
        print(f"{index + 1}. {display_item}")

    try:
        choice = int(input(f"Select a {item_type} by number: "))
        if 1 <= choice <= len(items):
            return items[choice - 1]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input.")
        return None
    

def display_all_users():
    """
    Display all users stored in the database.
    """
    users = get_all_users()
    if users:
        print("\nAll Users:")
        for idx, user in enumerate(users):
            print(f"{idx + 1}. Name: {user['name']}, Email: {user['email']}")
    else:
        print("No users found.")


def display_all_events():
    """
    Display all events stored in the database.
    """
    events = get_all_events()
    if events:
        print("\nAll Events:")
        for idx, event in enumerate(events):
            print(f"{idx + 1}. Name: {event['name']}, Date: {event['date']}, Location: {event['location']}")
    else:
        print("No events found.")


def main():
    """Start of the program"""
    while True:
        print("\nWelcome to the Basic Event Planner!")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Get User")
        print("5. Add Event")
        print("6. Update Event")
        print("7. Delete Event")
        print("8. Get Event")
        print("9. Add Invitation")
        print("10. Update Invitation")
        print("11. Delete Invitation")
        print("12. Get Invitation")
        print("13. Get Invitations by Event")
        print("14. Get Invitations by User")
        print("15. Add Comment to Invitation")
        print("16. Get Attendees")
        print("17. Get Invitations with Comments")
        print("18. Get Invitation Statistics")
        print("19. Send Invitation Notifications")
        print("20. View all Users")
        print("21. View all Events")
        print("22. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = str(uuid.uuid4())
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(user_id, name, email)
        elif choice == "2":
            users = get_all_users()
            selected_user = list_and_select(users, 'user')
            if selected_user:
                update_user(selected_user['id'], {'name': input("Enter new name: "), 'email': input("Enter new email: ")})
        elif choice == "3":
            users = get_all_users()
            selected_user = list_and_select(users, 'user')
            if selected_user:
                delete_user(selected_user['id'])
        elif choice == "4":
            users = get_all_users()
            selected_user = list_and_select(users, 'user')
            if selected_user:
                get_user(selected_user['id'])
        elif choice == "5":
            event_id = str(uuid.uuid4())
            name = input("Enter name: ")
            date = input("Enter date: ")
            location = input("Enter location: ")
            add_event(event_id, name, date, location)
        elif choice == "6":
            events = get_all_events()
            selected_event = list_and_select(events, 'event')
            if selected_event:
                update_event(selected_event['id'], {'name': input("Enter new name: "), 'date': input("Enter new date: "), 'location': input("Enter new location: ")})
        elif choice == "7":
            events = get_all_events()
            selected_event = list_and_select(events, 'event')
            if selected_event:
                delete_event(selected_event['id'])
        elif choice == "8":
            events = get_all_events()
            selected_event = list_and_select(events, 'event')
            if selected_event:
                get_event(selected_event['id'])
        elif choice == "9":
            invitation_id = str(uuid.uuid4())
            event_id = input("Enter event ID: ")
            user_id = input("Enter user ID: ")
            status = input("Enter status: ")
            add_invitation(invitation_id, event_id, user_id, status)
        elif choice == "10":
            invitations = get_all_invitations()
            selected_invitation = list_and_select(invitations, 'invitation')
            if selected_invitation:
                update_invitation(selected_invitation['id'], {'status': input("Enter new status: ")})
        elif choice == "11":
            invitations = get_all_invitations()
            selected_invitation = list_and_select(invitations, 'invitation')
            if selected_invitation:
                delete_invitation(selected_invitation['id'])
        elif choice == "12":
            invitations = get_all_invitations()
            selected_invitation = list_and_select(invitations, 'invitation')
            if selected_invitation:
                get_invitation(selected_invitation['id'])
        elif choice == "13":
            get_invitations_by_event(input("Enter event ID: "))
        elif choice == "14":
            get_invitations_by_user(input("Enter user name: "))
        elif choice == "15":
            invitations = get_all_invitations()
            selected_invitation = list_and_select(invitations, 'invitation')
            if selected_invitation:
                add_comment_to_invitation(selected_invitation['id'], input("Enter comment: "))
        elif choice == "16":
            invitations = get_all_invitations()
            selected_invitation = list_and_select(invitations, 'invitation')
            if selected_invitation:
                get_attendees(selected_invitation['id'])
        elif choice == "17":
            get_invitations_with_comments()
        elif choice == "18":
            get_invitation_statistics()
        elif choice == "19":
            invitations = get_all_invitations()
            selected_invitation = list_and_select(invitations, 'invitation')
            if selected_invitation:
                send_invitation_notifications(selected_invitation['id'])
        elif choice == "20":
            display_all_users()
        elif choice == "21":
            display_all_events()
        elif choice == "22":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number corresponding to the menu option.")


if __name__ == "__main__":
    main()
