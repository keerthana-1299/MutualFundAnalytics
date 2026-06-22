import requests
import pandas as pd

scheme_ids = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_id in scheme_ids.items():

    url = f"https://api.mfapi.in/mf/{scheme_id}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print(f"\nFetching {scheme_name}")

        nav_df = pd.DataFrame(data["data"])

        file_path = f"data/raw/{scheme_name}.csv"

        nav_df.to_csv(file_path, index=False)

        print(f"Saved {scheme_name}.csv")

    else:
        print(f"Failed to fetch {scheme_name}")