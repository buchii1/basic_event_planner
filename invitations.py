from firebase_setup import initialize_firebase

db = initialize_firebase()

# Define collection
INVITATIONS_COLLECTION = 'invitations'

# Define subcollections
COMMENTS_SUBCOLLECTION = 'comments'
ATTENDEES_SUBCOLLECTION = 'attendees'

def add_invitation(invitation_id, event_id, user_id, status):
    """
    Add a new invitation to the Firestore database.
    params:
        invitation_id: Unique ID for the invitation.
        event_id: Unique ID for the event.
        user_id: Unique ID for the user.
        status: Status of the invitation (e.g., 'pending', 'accepted', 'declined').
    """
    doc_ref = db.collection(INVITATIONS_COLLECTION).document(invitation_id)
    doc_ref.set({
        'event_id': event_id,
        'user_id': user_id,
        'status': status
    })
    print(f'Invitation {invitation_id} added.')


def update_invitation(invitation_id, updates):
    """
    Update an existing invitation in the Firestore database.
    params:
        invitation_id: Unique ID for the invitation.
        updates: Dictionary of fields to update.
    """
    doc_ref = db.collection(INVITATIONS_COLLECTION).document(invitation_id)
    doc_ref.update(updates)
    print(f'Invitation {invitation_id} updated.')


def delete_invitation(invitation_id):
    """
    Delete an invitation from the Firestore database.
    params:
        invitation_id: Unique ID for the invitation.
    """
    doc_ref = db.collection(INVITATIONS_COLLECTION).document(invitation_id)
    doc_ref.delete()
    print(f'Invitation {invitation_id} deleted.')


def get_invitation(invitation_id):
    """
    Retrieve an invitation's data from the Firestore database.
    params: 
        invitation_id: Unique ID for the invitation.
    return: 
        Invitation data as a dictionary if found, else None.
    """
    doc_ref = db.collection(INVITATIONS_COLLECTION).document(invitation_id)
    invitation = doc_ref.get()
    if invitation.exists:
        invitation_data = invitation.to_dict()
        invitation_data['id'] = invitation_id
        print(f'Invitation data: {invitation_data}')
        return invitation_data
    else:
        print(f'No invitation found with ID {invitation_id}')
        return None


def get_invitations_by_event(event_id):
    """
    Retrieve all invitations for a specific event from the Firestore database.
    params:
        event_id: Unique ID for the event.
    return:   
        List of invitation data dictionaries.
    """
    invitations_ref = db.collection(INVITATIONS_COLLECTION).where('event_id', '==', event_id)
    invitations = [invitation.to_dict() for invitation in invitations_ref.stream()]
    for invitation in invitations:
        print(f'Invitation data: {invitation}')
    return invitations


def get_invitations_by_user(username):
    """
    Retrieve all invitations for a specific user from the Firestore database.
    params:
        username: Name of the user.
    return: 
        List of invitation data dictionaries.
    """
    invitations_ref = db.collection(INVITATIONS_COLLECTION).where('name', '==', username).stream()
    invitations = [invitation.to_dict() for invitation in invitations_ref]
    for invitation in invitations:
        print(f'Invitation data: {invitation}')
    return invitations


def add_comment_to_invitation(invitation_id, comment):
    """
    Add a comment to a specific invitation in the Firestore database.
    params:
        invitation_id: Unique ID for the invitation.
        comment: Comment to be added.
    """
    doc_ref = db.collection(INVITATIONS_COLLECTION).document(invitation_id).collection(COMMENTS_SUBCOLLECTION).document()
    doc_ref.set({'comment': comment})
    print(f'Comment added to invitation {invitation_id}.')


def get_attendees(invitation_id):
    """
    Retrieve all attendees for a specific invitation from the Firestore database.
    params:
        invitation_id: Unique ID for the invitation.
    return: 
        List of attendee data dictionaries.
    """
    attendees_ref = db.collection(INVITATIONS_COLLECTION).document(invitation_id).collection(ATTENDEES_SUBCOLLECTION).stream()
    attendees = [attendee.to_dict() for attendee in attendees_ref]
    for attendee in attendees:
        print(f'Attendee data: {attendee}')
    return attendees


def get_invitations_with_comments():
    """
    Retrieve all invitations with comments from the Firestore database.
    return: 
        List of invitation data dictionaries with comments.
    """
    query_ref = db.collection_group(COMMENTS_SUBCOLLECTION)
    invitations_with_comments = []
    for comment_doc in query_ref.stream():
        invitation_id = comment_doc.reference.parent.parent.id
        invitation_ref = db.collection(INVITATIONS_COLLECTION).document(invitation_id)
        invitation = invitation_ref.get()
        if invitation.exists:
            invitation_data = invitation.to_dict()
            invitation_data['id'] = invitation_id
            invitation_data['comments'] = [comment.to_dict() for comment in invitation_ref.collection(COMMENTS_SUBCOLLECTION).stream()]
            invitations_with_comments.append(invitation_data)
            print(f'Invitation with comments: {invitation_data}')
    return invitations_with_comments


def get_invitation_statistics():
    """
    Calculate statistics for invitations.
    return: 
        Dictionary containing invitation statistics.
    """
    total_invitations = db.collection(INVITATIONS_COLLECTION).get()
    accepted_invitations = db.collection(INVITATIONS_COLLECTION).where('status', '==', 'accepted').get()
    declined_invitations = db.collection(INVITATIONS_COLLECTION).where('status', '==', 'declined').get()
    pending_invitations = db.collection(INVITATIONS_COLLECTION).where('status', '==', 'pending').get()

    statistics = {
        'total': len(total_invitations),
        'accepted': len(accepted_invitations),
        'declined': len(declined_invitations),
        'pending': len(pending_invitations)
    }

    print(f'Invitation statistics: {statistics}')
    return statistics


def send_invitation_notifications(invitation_id):
    """
    Send notifications to users for a specific invitation.
    params:
        invitation_id: Unique ID for the invitation.
    """
    try:
        invitation_data = get_invitation(invitation_id)
        if invitation_data:
            user_id = invitation_data['user_id']
            print(f"Notification sent to user {user_id}: You've received an invitation (ID: {invitation_id}).")
    except Exception as e:
        print(f"An error occurred while sending invitation notifications: {str(e)}")


def get_all_invitations():
    """
    Retrieve all invitations from the Firestore database.
    return: 
        List of invitation data dictionaries.
    """
    invitations_ref = db.collection(INVITATIONS_COLLECTION).stream()
    invitations = []
    for invitation in invitations_ref:
        invitation_data = invitation.to_dict()
        invitation_data['id'] = invitation.id
        invitations.append(invitation_data)
    return invitations