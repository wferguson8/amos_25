"""
Created on Mon Jul 22 14:
@author: Will Ferguson
@email: will.ferguson@teenpact.com, iamwillferguson@gmail.com

This file is used to generate the prior distribution for the Bayesian inference model.
Until the week of NatCon, the functionality will be conducted on a stub of data to ensure the
general functionality performs as expected.

Sources:

Bambi: https://pypi.org/project/bambi

"""

import pandas as pd
import bambi as bmb
from pathlib import Path
import arviz as az


DATA_PATH = Path('./data/compiled_output.csv')

# Load data as dataframe
data = pd.read_csv(DATA_PATH)

# Develop the formula
base = 'winner ~ '
state_effect = '(1|state) + '
vote_shares = '(vs_p * hs_p) + (vs_v * hs_v) + (vs_c * hs_c) + vs_o + '
pop_shares = '(pop_p * hs_p) + (pop_v * hs_v) + (pop_c * hs_c) + pop_o'
formula = base + state_effect + vote_shares + pop_shares

# initialize the model
model = bmb.Model(
    formula,
    data,
    dropna=True # Probably isn't necessary but here out of caution
)

results = model.fit()

# Inspect the model's results
az.summary(results, hdi_prob=0.95)  # Posterior means, intervals, etc.
az.plot_trace(results)              # Trace plots for diagnostics

# The model object can be used for inference later on