"""

This file contains dictionaries with the past results of relevant elections
- key: postal code
- value: tuple of parties that won the state (to include ties)
"""

results_2019 = {}

results_2020 = {}  # Probably not going to worry about filling this out beacause of lack of data

results_2021 = {
    'AL': ('P',),
    'AK': ('V',),
    'AZ': ('V',),
    'AR': ('P',),
    'CA': ('P',),
    'CO': ('P',),
    'CT': ('P',),
    'DE': ('V',),
    'FL': ('C',),
    'GA': ('V',),
    'HI': ('P', 'V'),
    'ID': ('C', 'P', 'V'),
    'IL': ('P',),
    'IN': ('P',),
    'IA': ('V',),
    'KS': ('V',),
    'KY': ('V',),
    'LA': ('P',),
    'ME': ('C', 'P', 'V'),
    'MD': ('C',),
    'MA': ('V',),
    'MI': ('P',),
    'MN': ('V',),
    'MS': ('V',),
    'MO': ('V',),
    'MT': ('P',),
    'NE': ('V',),
    'NV': ('V',),
    'NH': ('P',),
    'NJ': ('V',),
    'NM': ('P',),
    'NY': ('V',),
    'NC': ('P',),
    'ND': ('P',),
    'OH': ('V',),
    'OK': ('V',),
    'OR': ('P',),
    'PA': ('P',),
    'RI': ('P',),
    'SC': ('P',),
    'SD': ('P',),
    'TN': ('V',),
    'TX': ('P',),
    'UT': ('C',),
    'VT': ('C', 'V'),
    'VA': ('P',),
    'WA': ('V',),
    'WV': ('P',),
    'WI': ('P',),
    'WY': ('V',)
}


results_2022 = {}

results_2023 = {}

results_2024 = {}

results = {
    '2019': results_2019,
    '2020': results_2020,
    '2021': results_2021,
    '2022': results_2022,
    '2023': results_2023,
    '2024': results_2024
}