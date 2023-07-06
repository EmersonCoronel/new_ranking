import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("backend/service_account_key.json")
firebase_admin.initialize_app(cred)

