"""

This file contains some important info that will make converting the data into a usable format a bit easier.

"""

# A dictionary of state/postal code pairings
us_states = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}

# A dictionary of keys (renamed) that are important to calculate for each poll
important_keys = {
    "State",
    "Party",
    "Vote"
}

home_states_2019 = {}

home_states_2020 = {}

home_states_2021 = {
    "Perseverance": ["NC", "IN"],
    "Vision": ["IA", "TN"],
    "Compassion": ["FL"]
}

home_states_2022 = {}

home_states_2023 = {}

home_states_2024 = {}

home_states = {
    "2019": home_states_2019,
    "2020": home_states_2020,
    "2021": home_states_2021,
    "2022": home_states_2022,
    "2023": home_states_2023,
    "2024": home_states_2024
}

# Candidates for each year by party
candidates_2019 = {
}

# Likely no meaningful data from 2020 due to pandemic
candidates_2020 = {
    "Perseverance": "Jake Myers/Katie Patterson",
    "Vision": "Stephen Deloglos/Briley Glisson",
    "Compassion": "Will Ferguson/Hannah Freeland"
}

candidates_2021 = {
    "Perseverance": "Luke Wilson/Noah Diaz",
    "Vision": "Elise Hof/Brock Freeland",
    "Compassion": "Ethan Wright/Lauren Wagner"
}

candidates_2022 = {}

candidates_2023 = {}

candidates_2024 = {}

# lookup table for results by year
candidates = {
    "2019": candidates_2019,
    "2020": candidates_2020,
    "2021": candidates_2021,
    "2022": candidates_2022,
    "2023": candidates_2023,
    "2024": candidates_2024,
}