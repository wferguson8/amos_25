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

home_states_2018 = {
    "Perseverance": ["OK", "PA"],
    "Vision": ["GA", "OK"],
    "Compassion": ["CO", "IL"]
}

home_states_2019 = {
    "Perseverance": ["MO", "WA"],
    "Vision": ["GA", "NC"],
    "Compassion": ["FL"]
}

home_states_2020 = {}

home_states_2021 = {
    "Perseverance": ["NC", "IN"],
    "Vision": ["IA", "TN"],
    "Compassion": ["FL"]
}

home_states_2022 = {
    "Perseverance": ["OK", "AL"],
    "Vision": ["NC", "MO"],
    "Compassion": ["NV", "AR"]
}

home_states_2023 = {
    "Perseverance": ["OK", "TN"],
    "Vision": ["MO", "CT"],
    "Compassion": ["FL", "OR"]
}

home_states_2024 = {
    "Perseverance": ["MS", "NC"],
    "Vision": ["AL"],
    "Compassion": ["IN", "TN"]
}

# TODO: Update for hypotheticals
home_states_2025 = {
    "Perseverance": ["OK", "TN", "AZ", "NV"],
    "Vision": ["MI", "FL", "MO", "OR"],
    "Compassion": ["MO", "OR", "NC"]
}

home_states = {
    "2018": home_states_2018,
    "2019": home_states_2019,
    "2020": home_states_2020,
    "2021": home_states_2021,
    "2022": home_states_2022,
    "2023": home_states_2023,
    "2024": home_states_2024,
    "2025": home_states_2025
}

candidates_2018 = {
    "Perseverance": "Carissa Gould/Toby DeMoss",
    "Vision": "Truman Forehand/Grant Johnson",
    "Compassion": "Noah Streyle/Christa Kaufman"
}

# Candidates for each year by party
candidates_2019 = {
    "Perseverance": "Isaac Richardson/Biani Benitez",
    "Vision": "Toby Forehand/Madelyn McDonald",
    "Compassion": "Libby Robinson/Anna Adams"
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

candidates_2022 = {
    "Perseverance": "Lillian Savage/Brooks Breedlove",
    "Vision": "Corban Smith/Abbie George",
    "Compassion": "Brayden Goodrich/Daniel Goff"
}

candidates_2023 = {
    "Perseverance": "Bruce Bigler/Emma Freeland",
    "Vision": "Brad Heredia/Lila Gebhart",
    "Compassion": "Brennan Roub/Blaise Timmons"
}

candidates_2024 = {
    "Perseverance": "Naomi Strozier/Joseph Jackson",
    "Vision": "Jude Hutto/Brink Hutto",
    "Compassion": "Esther Blake/Garrett Kramer"
}

# TODO: Update this with the actual candidates to get all possible options
candidates_2025 = {
    "Perseverance": "Clark Bigler/Grace Franklin",
    "Vision": "Isaac Powers/Enrique Rodriguez",
    "Compassion": "Jed Sicilia/Chesed Vess"
}

# lookup table for results by year
candidates = {
    "2018": candidates_2018,
    "2019": candidates_2019,
    "2020": candidates_2020,
    "2021": candidates_2021,
    "2022": candidates_2022,
    "2023": candidates_2023,
    "2024": candidates_2024,
    "2025": candidates_2025
}