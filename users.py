from firebase_setup import initialize_firebase

db = initialize_firebase()

# Define collection
USERS_COLLECTION = 'users'

def add_user(user_id, name, email):
    """
    Add a new user to the Firestore database.
    param(s):
        user_id: Unique ID for the user.
        name: Name of the user.
        email: Email of the user.
    """
    doc_ref = db.collection(USERS_COLLECTION).document(user_id)
    doc_ref.set({
        'name': name,
        'email': email
    })
    print(f'User {name} added.')


def update_user(user_id, updates):
    """
    Update an existing user in the Firestore database.
    param(s): 
        user_id: Unique ID for the user.
        updates: Dictionary of fields to update.
    """
    doc_ref = db.collection(USERS_COLLECTION).document(user_id)
    doc_ref.update(updates)
    print(f'User {user_id} updated.')


def delete_user(user_id):
    """
    Delete a user from the Firestore database.
    param(s): 
        user_id: Unique ID for the user.
    """
    doc_ref = db.collection(USERS_COLLECTION).document(user_id)
    doc_ref.delete()
    print(f'User {user_id} deleted.')


def get_user(user_id):
    """
    Retrieve a user's data from the Firestore database.
    param(s):
        user_id: Unique ID for the user.
    return: 
        User data as a dictionary if found, else None.
    """
    doc_ref = db.collection(USERS_COLLECTION).document(user_id)
    user = doc_ref.get()
    if user.exists:
        user_data = user.to_dict()
        user_data['id'] = user_id
        print(f'User data: {user_data}')
        return user_data
    else:
        print(f'No user found with ID {user_id}')
        return None
    
    
def get_all_users():
    """
    Retrieve all users from the Firestore database.
    return: 
        List of user data dictionaries.
    """
    users_ref = db.collection(USERS_COLLECTION).stream()
    users = []
    for user in users_ref:
        user_data = user.to_dict()
        user_data['id'] = user.id
        users.append(user_data)
    return users

