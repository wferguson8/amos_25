"""

This file is used to compile all the versions of the polls into one master results file

"""
from typing import Dict, List
import random as r
import pandas as pd
from pathlib import Path

# local imports
from utils import (
    us_states,
    candidates,
    important_keys,
    home_states
)
from results import results

SCRATCH_DIR = Path('./scratch/')
OUTPUT_PATH = './compiled_output.csv'

columns = [
    'year',
    'state',
    'size',
    'vs_p', # Vote share perseverance
    'vs_v', # Vote share vision
    'vs_c', # Vote share compassion
    'vs_o', # Vote share other/undecided
    'hs_p', 'hs_v', 'hs_c', # Home states by candidate
    'pop_p', 'pop_v', 'pop_c', 'pop_o' # Share of population by part/unaffiliated
    'winner' # Who won the actual state
]



# Load important lists into memory you might need later
states = list(us_states.keys()) # Holds postal codes


def add_poll(file: pd.DataFrame, year: str) -> pd.DataFrame:
    """
    Adds the results of a poll into one master results file
    :param file: Dataframe representing a single poll
    :return: DataFrame of results (concat with main output)
    """

    year_cand: Dict = candidates[year]

    states_in_poll = file['State'].unique().tolist()
    results: List[Dict] = []
    for state in states_in_poll:
        if len(state) > 2:
            postal_code = us_states[state]
        else:
            postal_code = state

        # grab each value for the line in the output dataframe
        size = file[file['State'] == state]
        vs_p = round(file[file['Vote'] == year_cand['Perseverance']] / size, 2)
        vs_v = round(file[file['Vote'] == year_cand['Vision']] / size, 2)
        vs_c = round(file[file['Vote'] == year_cand['Compassion']] / size, 2)
        vs_o = 1 - sum([vs_p, vs_v, vs_c])

        hs_p = 1 if postal_code in home_states["Perseverance"] else 0
        hs_v = 1 if postal_code in home_states["Vision"] else 0
        hs_c = 1 if postal_code in home_states["Compassion"] else 0

        pop_p = round(file[file['Party'] == 'Perseverance'] / size, 2)
        pop_v = round(file[file['Party'] == 'Vision'] / size, 2)
        pop_c = round(file[file['Party'] == 'Compassion'] / size, 2)
        pop_o = 1 - sum([pop_p, pop_v, pop_c])

        winners = results[postal_code]
        tiebreak = r.choice(winners) # In the event of a tie, break it randomly for the model fitting

        items = [year, postal_code, size, vs_p, vs_v, vs_c, vs_o, hs_p, hs_v, hs_c, pop_p, pop_v, pop_c, pop_o, tiebreak]
        line = {}
        for idx, item in enumerate(columns):
            line.update({item: items[idx]})
        results.append(line)
    return pd.DataFrame(results)

def main():
    """
    Main Method

    :return: None
    """
    OUTPUT = pd.DataFrame(columns=columns)  # empty dataframe
    for file in SCRATCH_DIR.iterdir():
        if file.is_file() and file.suffix == ".csv":
            df = pd.read_csv(file)
        if file.is_file() and file.suffix == ".xlsx":
            df = pd.read_excel(file)
        year: str = file.name[0:4]
        lines = add_poll(
            file=df,
            year=year,
        )

        OUTPUT = pd.concat([OUTPUT, lines], ignore_index=True)

    # save output to file path
    OUTPUT.to_csv(OUTPUT_PATH, index=False)


if __name__ == '__main__':
    main()