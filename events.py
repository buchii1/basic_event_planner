from firebase_setup import initialize_firebase

db = initialize_firebase()

# Define collection
EVENTS_COLLECTION = 'events'

def add_event(event_id, name, date, location):
    """
    Add a new event to the Firestore database.
    params:
        event_id: Unique ID for the event.
        name: Name of the event.
        date: Date of the event.
        location: Location of the event.
    """
    doc_ref = db.collection(EVENTS_COLLECTION).document(event_id)
    doc_ref.set({
        'name': name,
        'date': date,
        'location': location
    })
    print(f'Event {name} added.')


def update_event(event_id, updates):
    """
    Update an existing event in the Firestore database.
    params: 
        event_id: Unique ID for the event.
        updates: Dictionary of fields to update.
    """
    doc_ref = db.collection(EVENTS_COLLECTION).document(event_id)
    doc_ref.update(updates)
    print(f'Event {event_id} updated.')


def delete_event(event_id):
    """
    Delete an event from the Firestore database.
    params:
        event_id: Unique ID for the event.
    """
    doc_ref = db.collection(EVENTS_COLLECTION).document(event_id)
    doc_ref.delete()
    print(f'Event {event_id} deleted.')


def get_event(event_id):
    """
    Retrieve an event's data from the Firestore database.
    params:
        event_id: Unique ID for the event.
    return: 
        Event data as a dictionary if found, else None.
    """
    doc_ref = db.collection(EVENTS_COLLECTION).document(event_id)
    event = doc_ref.get()
    if event.exists:
        event_data = event.to_dict()
        event_data['id'] = event_id
        print(f'Event data: {event_data}')
        return event_data
    else:
        print(f'No event found with ID {event_id}')
        return None


def get_all_events():
    """
    Retrieve all events from the Firestore database.
    return: 
        List of event data dictionaries.
    """
    events_ref = db.collection(EVENTS_COLLECTION).stream()
    events = []
    for event in events_ref:
        event_data = event.to_dict()
        event_data['id'] = event.id
        events.append(event_data)
    return events