from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES_CAL = ["https://www.googleapis.com/auth/calendar.readonly"]


def calendar_events(members, time_min, time_max, max_results: int = 1000):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    userdata = list()
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("../token.json"):
        creds = Credentials.from_authorized_user_file("../token.json", SCOPES_CAL)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "../credentials.json", SCOPES_CAL
            )
            creds = flow.run_local_server(
                host="localhost",
                port=65145,
                authorization_prompt_message="Please visit this URL: {url}",
                success_message="The auth flow is complete; you may close this window.",
                open_browser=True,
            )

        # Save the credentials for the next run
        with open("../token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    for calender_id in members:
        print(calender_id)

        events_result = (
            service.events()
            .list(
                calendarId=calender_id,
                timeMin=time_min,
                timeMax=time_max,
                maxResults=max_results,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        userdata.append(events)

    return userdata

