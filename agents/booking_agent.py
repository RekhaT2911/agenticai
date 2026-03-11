from agents.base_agent import BaseAgent
from config import RAPID_API_KEY
from datetime import datetime, timedelta
import requests
import re


class BookingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Booking Agent")
        self.api_host = "irctc1.p.rapidapi.com"
        self.headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": self.api_host
        }

        # Common city name to station code mapping
        self.city_to_code = {
            "bangalore": "SBC", "bengaluru": "SBC",
            "hyderabad": "SC", "secunderabad": "SC",
            "chennai": "MAS", "delhi": "NDLS",
            "new delhi": "NDLS", "mumbai": "CSMT",
            "kolkata": "HWH", "howrah": "HWH",
            "pune": "PUNE", "jaipur": "JP",
            "ahmedabad": "ADI", "lucknow": "LKO",
            "patna": "PNBE", "bhopal": "BPL",
            "goa": "MAO", "madgaon": "MAO",
            "vijayawada": "BZA", "visakhapatnam": "VSKP",
            "vizag": "VSKP", "tirupati": "TPTY",
            "coimbatore": "CBE", "mysore": "MYS",
            "mysuru": "MYS", "nagpur": "NGP",
            "indore": "INDB", "varanasi": "BSB",
            "agra": "AGC", "chandigarh": "CDG",
            "thiruvananthapuram": "TVC", "kochi": "ERS",
            "ernakulam": "ERS", "mangalore": "MAQ",
            "bhimavaram": "BVRM", "kakinada": "CCT",
            "rajahmundry": "RJY", "guntur": "GNT",
            "nellore": "NLR", "warangal": "WL",
            "guwahati": "GHY", "ranchi": "RNC",
            "dehradun": "DDN", "jammu": "JAT",
            "amritsar": "ASR", "jodhpur": "JU",
            "udaipur": "UDZ", "surat": "ST",
            "vadodara": "BRC", "rajkot": "RJT",
            "madurai": "MDU", "salem": "SA",
            "trichy": "TPJ", "tiruchirappalli": "TPJ",
        }

    def get_station_code(self, city_name):
        """Convert city name to station code."""
        return self.city_to_code.get(city_name.lower().strip())

    def extract_cities(self, query: str):
        pattern = r"from (.*?) to (.*?)( today| tomorrow|$)"
        match = re.search(pattern, query.lower())
        if match:
            return match.group(1).strip().title(), match.group(2).strip().title()
        return None, None

    def search_trains(self, from_code, to_code, date):
        """Call IRCTC RapidAPI to get trains between stations."""
        url = f"https://{self.api_host}/api/v3/trainBetweenStations"

        params = {
            "fromStationCode": from_code,
            "toStationCode": to_code,
            "dateOfJourney": date
        }

        try:
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=10
            )

            data = response.json()

            if data.get("status") and data.get("data"):
                return data["data"]

            return None

        except Exception:
            return None

    def handle(self, query: str):

        query_lower = query.lower()
        source, destination = self.extract_cities(query_lower)

        if not source or not destination:
            return (
                "❌ Please use this format:\n\n"
                "train ticket from <source> to <destination>\n\n"
                "Example: train ticket from bangalore to hyderabad"
            )

        from_code = self.get_station_code(source)
        to_code = self.get_station_code(destination)

        if not from_code:
            return f"❌ Could not find station code for '{source}'. Try using a major city name."

        if not to_code:
            return f"❌ Could not find station code for '{destination}'. Try using a major city name."

        if "tomorrow" in query_lower:
            travel_date = datetime.now() + timedelta(days=1)
            day_label = "Tomorrow"
        else:
            travel_date = datetime.now()
            day_label = "Today"

        date_str = travel_date.strftime("%Y-%m-%d")

        trains = self.search_trains(from_code, to_code, date_str)

        if not trains:
            return (
                f"❌ No trains found from {source} ({from_code}) to "
                f"{destination} ({to_code}) on {travel_date.strftime('%d-%m-%Y')}.\n"
                f"Try a different date or check station names."
            )

        trains = trains[:5]

        response = (
            f"### 🚆 {source} → {destination}\n"
            f"**{travel_date.strftime('%A, %d %B %Y')}** ({day_label})\n\n"
            f"| # | Train | Dep → Arr | Duration | Classes |\n"
            f"|---|-------|-----------|----------|---------|\n"
        )

        for i, train in enumerate(trains, 1):

            train_name = train.get("train_name", "N/A")
            train_number = train.get("train_number", "N/A")
            departure = train.get("from_std", "N/A")
            arrival = train.get("to_std", "N/A")
            duration = train.get("duration", "N/A")
            class_types = train.get("class_type", [])

            classes_str = ", ".join(class_types) if class_types else "N/A"

            response += (
                f"| {i} | **{train_name}** ({train_number}) "
                f"| {departure} → {arrival} | {duration} | {classes_str} |\n"
            )

        return response