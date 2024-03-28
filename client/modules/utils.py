import io
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload


def driveUpload(file_path):
    # Define the Google Drive API scopes and service account file path
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = "capstone2024_credentials.json"
    PARENT_FOLDER_ID = "1zfnOELurwmQPXwbPWh1new3LePo60rIF"

    # Create credentials using the service account file
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_metadata = {
            'name': "1.jpg",
            'parents': [PARENT_FOLDER_ID]
        }
        
        # media = MediaFileUpload(file_path, mimetype="image/jpg")
        # pylint: disable=maybe-no-member
        file = (
            service.files()
            .create(
                body=file_metadata, 
                media_body=file_path, 
                fields="id",
                supportsAllDrives=True
            )
            .execute()
        )
        print(f'File ID: {file.get("id")}')
        return file.get("id")
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None


def driveDownload(file_id, destination_path):    
    # Define the Google Drive API scopes and service account file path
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = "capstone2024_credentials.json"

    # Create credentials using the service account file
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        id = file_id

        # pylint: disable=maybe-no-member
        request = service.files().get_media(fileId=id)
        file = io.FileIO(destination_path, mode='wb')
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}.")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None