"""

Created on Mon May 10 25
@author: Will Ferguson
@email: will.ferguson@teenpact.com, iamwillferguson@gmail.com

This file uses the prior distribution constructed at training time, and the posterior distribution calculated
as a weighted average of modern polling data (TBD: construct this posterior) to simulate a large number of elections
and record the results (TBD: where the results are stored).

"""
from typing import Dict, Tuple, Any

import pandas as pd
from arviz import InferenceData
import os
from sqlalchemy import create_engine
from pathlib import Path
from tqdm import tqdm

# Local Imports
from model.fit.create_prior import model
from utils import electoral_college_info, state_data

posterior = Path('./data/posterior.csv')
summary = Path('./data/summary.csv')
winner_path = Path('./data/winner.csv')

def simulate_election(sample: pd.DataFrame) -> Tuple[Dict[str, int], Dict[Any, Any]]:
    """
    Given a sample from a posterior distribution, simulate the outcome of an election in 50 states.

    :param sample: A DataFrame containing the posterior distribution sampling of 50 states for a synthetic election
    :return: A dictionary containing the winners by state
    """

    predicted_totals = {
        "P": 0,
        "V": 0,
        "C": 0
    }
    predicted_by_state = {}

    data: InferenceData = model.predict(
        sample,
        kind='pps'
    )

    data: pd.DataFrame = data.to_dataframe() # convert to dataframe, should have the labels all added
    winners_by_state = data['winner']
    states = data['state']

    # Update the results based on the winner of each state
    for state, winner in zip(states, winners_by_state):
        value = electoral_college_info[state]
        predicted_totals[winner] += value
        predicted_by_state[state] = winner

    return predicted_totals, predicted_by_state


def calculate_results(totals: Dict[str, int]) -> str:
    """

    Return the winner

    :param totals: The totals for each party candidate
    :return: Str containing the party that won the election
    """
    return list(totals.keys())[list(totals.values()).index(max(totals.values()))]

def upload_results(df: pd.DataFrame, table:str) -> None:
    """
    Upload the results to the database so that the hosted API can actually access the information.

    :return: None
    """

    url = os.getenv('DB_CONNECTION')
    engine = create_engine(url)

    df.to_sql(table, engine, if_exists='replace', index=False)

def main():

    # Load the posterior distribution
    data = pd.read_csv(posterior)

    # Create dataframe you're going to use to upload the summary of results
    summary_cols = [
        'state',
        'sims_p',  # Expressed as percents at the end
        'sims_v',
        'sims_c'
    ]

    winner_db = {
        'wins_p': 0,
        'wins_v': 0,
        'wins_c': 0
    }

    summary_df = pd.DataFrame(data=state_data, columns=summary_cols)  # empty dataframe
    summary_df.set_index("state", inplace=True)

    # Simulate a whole bunch of elections (increase once testing is done completely)
    for i in tqdm(range(1000)):
        totals, by_state = simulate_election(data)
        winner = calculate_results(totals)
        winner_db[f"wins_{winner.lower()}"] += 1
        for k, v in totals.items():
            summary_df.loc[k, f"sims_{v.lower()}"] += 1

    # convert totals to percentages
    summary_df = summary_df / 1000

    # Upload results
    upload_results(summary_df, 'summary')

    summary_df.to_csv(summary)
    winner_df = pd.DataFrame(data=winner_db)

    upload_results(winner_df, 'winner')
    winner_df.to_csv(winner_path)


if __name__ == '__main__':
    main()