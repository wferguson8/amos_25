"""

This file contains dictionaries with the past results of relevant elections
- key: postal code
- value: tuple of parties that won the state (to include ties)
"""
results_2018 = {
    'AL': ('P',),
    'AK': ('P',),
    'AZ': ('P',),
    'AR': ('P',),
    'CO': ('C',),
    'CT': ('P',),
    'DE': ('V',),
    'FL': ('P',),
    'GA': ('V',),
    'HI': ('P',),
    'IL': ('C',),
    'IN': ('V',),
    'IA': ('C',),
    'KY': ('V',),
    'LA': ('V',),
    'ME': ('P',),
    'MD': ('P',),
    'MA': ('P',),
    'MI': ('C', 'V'),  # Forehand/Streyle tie
    'MS': ('P',),
    'MT': ('P',),
    'NE': ('C',),
    'NH': ('V',),
    'NY': ('P', 'V'),  # Forehand/Gould tie
    'NC': ('P',),
    'OH': ('C',),
    'OK': ('P',),
    'OR': ('V',),
    'PA': ('P',),
    'RI': ('P', 'V'),  # Forehand/Gould tie
    'SC': ('V',),
    'SD': ('C',),
    'TN': ('P',),
    'TX': ('V',),
    'VA': ('P',),
    'WA': ('P',),
    'WI': ('C',),
    'WY': ('C',)
}

results_2019 = {
    'AZ': ('P',),
    'MT': ('P',),
    'WY': ('P',),
    'MN': ('P',),
    'ME': ('P',),
    'MS': ('V',),
    'OH': ('V',),
    'MI': ('V',),
    'RI': ('V',),
    'MA': ('V',),
    'GA': ('V',),
    'FL': ('C',),
    'MO': ('P',),
    'WA': ('P',),
    'NC': ('V',),
}

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


results_2022 = {
    'AL': ('C',),    # Alabama: Goodrich 45
    'AK': ('V',),    # Alaska: Smith 7
    'AZ': ('C',),    # Arizona: Goodrich 19
    'AR': ('C',),    # Arkansas: Goodrich 14
    'CA': ('V',),    # California: Smith 9
    'CO': ('V',),    # Colorado: Smith 10
    'CT': ('V',),    # Connecticut: Smith 11
    'DE': ('C',),    # Delaware: Goodrich 5
    'FL': ('V',),    # Florida: Smith 76
    'GA': ('V',),    # Georgia: Smith 52
    'HI': ('V',),    # Hawaii: Smith 6
    'ID': ('V',),    # Idaho: Smith 6
    'IL': ('V',),    # Illinois: Smith 14
    'IN': ('P',),    # Indiana: Savage 13
    'IA': ('P',),    # Iowa: Savage 17
    'KS': ('V',),    # Kansas: Smith 7
    'KY': ('C', 'P', 'V'),  # Kentucky: Three-way tie 3-3-3
    'LA': ('V',),    # Louisiana: Smith 22
    'ME': ('V',),    # Maine: Smith 3
    'MD': ('P',),    # Maryland: Savage 14
    'MA': ('V',),    # Massachusetts: Smith 3
    'MI': ('V',),    # Michigan: Smith 20
    'MN': ('V',),    # Minnesota: Smith 4
    'MS': ('V',),    # Mississippi: Smith 44
    'MO': ('V',),    # Missouri: Smith 86
    'MT': ('C',),    # Montana: Goodrich 11
    'NE': ('C',),    # Nebraska: Goodrich 10
    'NV': ('C',),    # Nevada: Goodrich 31
    'NH': ('V',),    # New Hampshire: Smith 1
    'NJ': ('V',),    # New Jersey: Smith 1
    'NM': ('C',),    # New Mexico: Goodrich 6
    'NY': ('C',),    # New York: Goodrich 13
    'NC': ('V',),    # North Carolina: Smith 42
    'ND': ('V',),    # North Dakota: Smith 8
    'OH': ('V',),    # Ohio: Smith 9
    'OK': ('P',),    # Oklahoma: Savage 52
    'OR': ('C', 'V'),# Oregon: Goodrich 6 vs Smith 6 (tie)
    'PA': ('C',),    # Pennsylvania: Goodrich 12
    'RI': ('P',),    # Rhode Island: Savage 1
    'SC': ('C',),    # South Carolina: Goodrich 11
    'SD': ('C',),    # South Dakota: Goodrich 9
    'TN': ('V',),    # Tennessee: Smith 33
    'TX': ('V',),    # Texas: Smith 77
    'UT': ('V',),    # Utah: Smith 3
    'VT': ('V',),    # Vermont: Smith 1
    'VA': ('V',),    # Virginia: Smith 15
    'WA': ('V',),    # Washington: Smith 5
    'WV': ('V',),    # West Virginia: Smith 7
    'WI': ('C',),    # Wisconsin: Goodrich 10
    'WY': ('V',)     # Wyoming: Smith 3
}

results_2023 = {
    'OK': ('P',),
    'ID': ('P',),
    'AK': ('P', 'V'),
    'KS': ('C',),
    'TN': ('P',),
    'NJ': ('C',),
    'NH': ('V',),
    'NY': ('P',),
    'MA': ('V',),
    'ME': ('V',),
    'CT': ('V',),
    'DE': ('P', 'V'),
    'IL': ('V',),
    'NM': ('V',),
    'OR': ('C',),
    'UT': ('C',),
    'HI': ('P',),
    'MO': ('P',),
    'FL': ('P',),
    'WV': ('C', 'P'),
    'AZ': ('C',),
    'CA': ('V',),
    'SD': ('V',),
    'OH': ('V',),
    'MN': ('V',),
    'WI': ('V',),
    'WY': ('V',),
    'NV': ('V',),
    'MS': ('P',),
    'TX': ('V',),
    'CO': ('P',),
    'MD': ('P',),
    'MI': ('P',),
    'VA': ('P',),
    'AL': ('P',),
    'WA': ('P',),
    'MT': ('P',),
    'NE': ('P',),
    'NC': ('P',),
    'ND': ('P',),
    'IN': ('P',),
    'IA': ('P',),
    'GA': ('P',),
    'PA': ('P',),
    'KY': ('P',),
    'LA': ('P',),
    'AR': ('P',),
    'SC': ('P',)
}


results_2024 = {
    'TX': ('P',),
    'GA': ('P',),
    'MO': ('P',),
    'CT': ('P',),
    'DE': ('V',),
    'RI': ('C', 'P', 'V'),
    'MA': ('C', 'P', 'V'),
    'ME': ('C', 'P'),
    'NH': ('C',),
    'NJ': ('C',),
    'PA': ('C', 'P'),
    'NY': ('P',),
    'VT': ('C',),
    'OK': ('C',),
    'AZ': ('V',),
    'NM': ('V',),
    'AL': ('V',),
    'FL': ('P',),
    'WV': ('P',),
    'NC': ('P',),
    'MS': ('P',),
    'TN': ('C',),
    'WA': ('C',),
    'ID': ('P', 'V'),
    'IN': ('C',),
    'AR': ('V',),
    'LA': ('P', 'V'),
    'MD': ('P',),
    'IA': ('V',),
    'MT': ('V',),
    'WY': ('V',),
    'NE': ('C',),
    'ND': ('C',),
    'UT': ('P',),
    'KS': ('P',),
    'OR': ('C',),
    'AK': ('P',),
    'SD': ('P',),
    'CA': ('P',),
    'HI': ('P',),
    'IL': ('P',),
    'KY': ('P',),
    'MI': ('P',),
    'MN': ('P',),
    'NV': ('P',),
    'OH': ('P',),
    'SC': ('P',),
    'VA': ('P',),
    'WI': ('P',),
    'CO': ('P',)
}

results = {
    '2018': results_2018,
    '2019': results_2019,
    '2020': results_2020,
    '2021': results_2021,
    '2022': results_2022,
    '2023': results_2023,
    '2024': results_2024
}