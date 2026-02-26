# from agents.base_agent import BaseAgent
# from datetime import datetime, timedelta
# import re


# class BookingAgent(BaseAgent):
#     def __init__(self):
#         super().__init__("Booking Agent")

#     def extract_cities(self, query: str):
#         pattern = r"from (.*?) to (.*?)( today| tomorrow|$)"
#         match = re.search(pattern, query.lower())

#         if match:
#             source = match.group(1).strip().title()
#             destination = match.group(2).strip().title()
#             return source, destination

#         return None, None

#     def handle(self, query: str):
#         query = query.lower()

#         source, destination = self.extract_cities(query)

#         if not source or not destination:
#             return (
#                 "❌ Please use this format:\n\n"
#                 "train ticket from <source> to <destination>\n\n"
#                 "Example:\n"
#                 "train ticket from bangalore to hyderabad"
#             )

#         # 🔹 Date Handling
#         if "tomorrow" in query:
#             base_date = datetime.now() + timedelta(days=1)
#             day_label = "Tomorrow"
#         else:
#             base_date = datetime.now()
#             day_label = "Today"

#         dates = [
#             (base_date + timedelta(days=i)).strftime("%d-%m-%Y")
#             for i in range(3)
#         ]

#         # 🔹 Simulated Train Data (Realistic Structure)
#         trains = [
#             {
#                 "name": "Intercity Express",
#                 "number": "16590",
#                 "departure": "06:00",
#                 "arrival": "14:30",
#                 "duration": "8h 30m",
#                 "classes": {
#                     "SL": 350,
#                     "3A": 850,
#                     "2A": 1200
#                 }
#             },
#             {
#                 "name": "Karnataka Express",
#                 "number": "12785",
#                 "departure": "20:15",
#                 "arrival": "05:30",
#                 "duration": "9h 15m",
#                 "classes": {
#                     "SL": 450,
#                     "3A": 950,
#                     "2A": 1400,
#                     "1A": 2200
#                 }
#             },
#             {
#                 "name": "Hyderabad Express",
#                 "number": "17031",
#                 "departure": "23:00",
#                 "arrival": "07:45",
#                 "duration": "8h 45m",
#                 "classes": {
#                     "SL": 600,
#                     "3A": 1100,
#                     "2A": 1600
#                 }
#             }
#         ]

#         # 🔹 Sort trains by lowest available class price
#         trains_sorted = sorted(
#             trains,
#             key=lambda x: min(x["classes"].values())
#         )

#         # 🔹 Format Output
#         response = (
#             f"🚆 **Train Tickets from {source} to {destination}**\n"
#             f"📅 {day_label} & Next 2 Days\n\n"
#         )

#         for date in dates:
#             response += f"━━━━━━━━━━━━━━━━━━━━━━\n"
#             response += f"📆 {date}\n\n"

#             for i, train in enumerate(trains_sorted, 1):
#                 response += (
#                     f"{i}. 🚄 {train['name']} ({train['number']})\n"
#                     f"   🕒 Departure: {train['departure']}  |  Arrival: {train['arrival']}\n"
#                     f"   ⏱ Duration: {train['duration']}\n"
#                     f"   🪑 Classes:\n"
#                 )

#                 for cls, price in train["classes"].items():
#                     response += f"      • {cls} - ₹{price}\n"

#                 response += "\n"

#         response += (
#             "💡 *Trains sorted by lowest available class price.*\n\n"
#             "🔗 Book tickets here:\n"
#             "https://www.irctc.co.in"
#         )

#         return response

from agents.base_agent import BaseAgent
from datetime import datetime, timedelta
import re


class BookingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Booking Agent")

        # 🔥 Static Route-Based Train Data (Max 2 per route)
        self.route_trains = {

            # Bangalore ↔ Hyderabad
            ("Bangalore", "Hyderabad"): [
                {"name": "Kacheguda Express", "number": "16569", "departure": "21:00", "arrival": "07:30", "duration": "10h 30m", "classes": {"SL": 450, "3A": 950, "2A": 1400}},
                {"name": "Intercity Express", "number": "12785", "departure": "06:00", "arrival": "14:00", "duration": "8h", "classes": {"SL": 400, "3A": 900, "2A": 1300}}
            ],

            ("Hyderabad", "Bangalore"): [
                {"name": "Hyderabad Express", "number": "17031", "departure": "20:30", "arrival": "06:45", "duration": "10h 15m", "classes": {"SL": 500, "3A": 1000, "2A": 1500}},
                {"name": "Falaknuma Express", "number": "12704", "departure": "15:00", "arrival": "23:30", "duration": "8h 30m", "classes": {"SL": 420, "3A": 920, "2A": 1350}}
            ],

            # Bangalore ↔ Bhimavaram
            ("Bangalore", "Bhimavaram"): [
                {"name": "West Coast Express", "number": "22637", "departure": "18:00", "arrival": "06:30", "duration": "12h 30m", "classes": {"SL": 600, "3A": 1100, "2A": 1600}},
                {"name": "Bhimavaram Link Express", "number": "17256", "departure": "22:00", "arrival": "09:00", "duration": "11h", "classes": {"SL": 550, "3A": 1050, "2A": 1500}}
            ],

            ("Bhimavaram", "Bangalore"): [
                {"name": "Uday Express", "number": "17210", "departure": "19:00", "arrival": "06:00", "duration": "11h", "classes": {"SL": 580, "3A": 1080, "2A": 1550}},
                {"name": "Superfast Express", "number": "17645", "departure": "16:30", "arrival": "04:30", "duration": "12h", "classes": {"SL": 620, "3A": 1120, "2A": 1650}}
            ],

            # Bhimavaram ↔ Kakinada
            ("Bhimavaram", "Kakinada"): [
                {"name": "Passenger Express", "number": "57231", "departure": "07:00", "arrival": "10:00", "duration": "3h", "classes": {"SL": 150}},
                {"name": "Godavari Link", "number": "17240", "departure": "14:00", "arrival": "17:00", "duration": "3h", "classes": {"SL": 180}}
            ],

            ("Kakinada", "Bhimavaram"): [
                {"name": "Kakinada Passenger", "number": "57232", "departure": "11:00", "arrival": "14:00", "duration": "3h", "classes": {"SL": 150}},
                {"name": "Coastal Express", "number": "17241", "departure": "18:00", "arrival": "21:00", "duration": "3h", "classes": {"SL": 200}}
            ],

            # Bhimavaram ↔ Chennai
            ("Bhimavaram", "Chennai"): [
                {"name": "Chennai Express", "number": "17643", "departure": "17:00", "arrival": "06:00", "duration": "13h", "classes": {"SL": 650, "3A": 1200, "2A": 1800}},
                {"name": "Coromandel Link", "number": "12842", "departure": "20:00", "arrival": "09:00", "duration": "13h", "classes": {"SL": 700, "3A": 1300, "2A": 1900}}
            ],

            ("Chennai", "Bhimavaram"): [
                {"name": "Chennai Mail", "number": "17644", "departure": "15:30", "arrival": "04:30", "duration": "13h", "classes": {"SL": 600, "3A": 1150, "2A": 1750}},
                {"name": "Superfast Coastal", "number": "12843", "departure": "22:00", "arrival": "11:00", "duration": "13h", "classes": {"SL": 720, "3A": 1350, "2A": 1950}}
            ],

            # Bhimavaram ↔ Rajahmundry
            ("Bhimavaram", "Rajahmundry"): [
                {"name": "Delta Passenger", "number": "57301", "departure": "08:00", "arrival": "10:30", "duration": "2h 30m", "classes": {"SL": 120}},
                {"name": "Godavari Passenger", "number": "57302", "departure": "16:00", "arrival": "18:30", "duration": "2h 30m", "classes": {"SL": 150}}
            ],

            ("Rajahmundry", "Bhimavaram"): [
                {"name": "Rajahmundry Express", "number": "57303", "departure": "09:00", "arrival": "11:30", "duration": "2h 30m", "classes": {"SL": 120}},
                {"name": "Coastal Passenger", "number": "57304", "departure": "19:00", "arrival": "21:30", "duration": "2h 30m", "classes": {"SL": 150}}
            ],

            # Rajahmundry ↔ Chennai
            ("Rajahmundry", "Chennai"): [
                {"name": "Howrah Mail", "number": "12839", "departure": "10:00", "arrival": "22:00", "duration": "12h", "classes": {"SL": 650, "3A": 1200, "2A": 1700}},
                {"name": "Superfast Chennai", "number": "17652", "departure": "18:00", "arrival": "06:00", "duration": "12h", "classes": {"SL": 700, "3A": 1250, "2A": 1800}}
            ],

            ("Chennai", "Rajahmundry"): [
                {"name": "Chennai Express", "number": "12840", "departure": "14:00", "arrival": "02:00", "duration": "12h", "classes": {"SL": 650, "3A": 1200, "2A": 1700}},
                {"name": "Mail Express", "number": "17653", "departure": "20:00", "arrival": "08:00", "duration": "12h", "classes": {"SL": 720, "3A": 1300, "2A": 1850}}
            ],

            # Bangalore ↔ Delhi
            ("Bangalore", "Delhi"): [
                {"name": "Karnataka Express", "number": "12627", "departure": "19:20", "arrival": "06:10", "duration": "34h 50m", "classes": {"SL": 800, "3A": 1600, "2A": 2400, "1A": 4000}},
                {"name": "Rajdhani Express", "number": "22691", "departure": "20:00", "arrival": "05:00", "duration": "33h", "classes": {"3A": 2200, "2A": 3200, "1A": 5000}}
            ],

            ("Delhi", "Bangalore"): [
                {"name": "Rajdhani Express", "number": "22692", "departure": "16:30", "arrival": "03:00", "duration": "34h 30m", "classes": {"3A": 2200, "2A": 3200, "1A": 5000}},
                {"name": "Sampark Kranti", "number": "12629", "departure": "08:00", "arrival": "18:00", "duration": "34h", "classes": {"SL": 750, "3A": 1500, "2A": 2300}}
            ],
        }

    def extract_cities(self, query: str):
        pattern = r"from (.*?) to (.*?)( today| tomorrow|$)"
        match = re.search(pattern, query.lower())
        if match:
            return match.group(1).strip().title(), match.group(2).strip().title()
        return None, None

    def handle(self, query: str):
        query = query.lower()
        source, destination = self.extract_cities(query)

        if not source or not destination:
            return "❌ Please use: train ticket from <source> to <destination>"

        if "tomorrow" in query:
            base_date = datetime.now() + timedelta(days=1)
            day_label = "Tomorrow"
        else:
            base_date = datetime.now()
            day_label = "Today"

        dates = [(base_date + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(3)]

        trains = self.route_trains.get((source, destination))

        if not trains:
            return f"❌ No trains available from {source} to {destination}"

        trains_sorted = sorted(trains, key=lambda x: min(x["classes"].values()))

        response = f"🚆 **Train Tickets from {source} to {destination}**\n📅 {day_label} & Next 2 Days\n\n"

        for date in dates:
            response += f"━━━━━━━━━━━━━━━━━━━━━━\n📆 {date}\n\n"
            for train in trains_sorted:
                response += (
                    f"🚄 {train['name']} ({train['number']})\n"
                    f"🕒 Departure: {train['departure']} | Arrival: {train['arrival']}\n"
                    f"⏱ Duration: {train['duration']}\n"
                    f"🪑 Classes:\n"
                )
                for cls, price in train["classes"].items():
                    response += f" • {cls} - ₹{price}\n"
                response += "\n"

        return response