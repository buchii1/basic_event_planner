import firebase_admin
from firebase_admin import credentials, firestore, _apps
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()

import os

def initialize_firebase():
    """
    Initialize the Firestore database.
    return: 
        Firestore client instance
    """
    # Get path to the serviceAccount file
    service_account_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not service_account_path:
        print("Service account path not found. Please set the GOOGLE_APPLICATION_CREDENTIALS environment variable.")
        return None

    # Combine the current directory with the service account path
    current_directory = os.path.dirname(__file__)
    service_account_path = os.path.join(current_directory, service_account_path)

    # Initialize Firebase app if not already initialized
    if not _apps:
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred)
    return firestore.client()
