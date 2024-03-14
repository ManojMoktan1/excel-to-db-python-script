import os
from dotenv import load_dotenv


load_dotenv()

# Get credentials from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

# Excel file and sheets name
excel_file_path = "../files/Jevaia_Dental_Hub.xlsx"
sheets = [
    "patientapp_patient",
    "encounterapp_encounter",
    "encounterapp_history",
    "encounterapp_screeing",
    "treatmentapp_treatment",
    "encounterapp_refer"
]
