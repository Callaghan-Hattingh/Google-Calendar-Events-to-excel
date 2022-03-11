import os
from dotenv import load_dotenv
from app.google_calendar_events import calendar_events
from app.save_data import data_to_df


load_dotenv()


if __name__ == "__main__":
    # You could also replace the os.getenv("EMAIL_1") with "example@business.com"
    users = [
        os.getenv("EMAIL_1"),
        os.getenv("EMAIL_2"),
    ]

    timemin = "2022-02-01T00:00:00+02:00"
    timemax = "2022-02-28T23:59:00+02:00"

    resp = calendar_events(users, timemin, timemax)
    df = data_to_df(resp)
    df.to_excel(r'Data.xlsx', index=False)


