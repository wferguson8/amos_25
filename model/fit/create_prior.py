"""
Created on Mon May 09 25:
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
import os

os.chdir(Path(__file__).parent.absolute())  # Change directory to ./data
DATA_PATH = Path('./data/compiled_output.csv')
POSTERIOR_PATH = Path('./data/posterior.nc')

def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["winner"] = df["winner"].astype("category")
    return df

def build_model(data: pd.DataFrame) -> bmb.Model:
    formula = (
        "winner ~ "
        "(vs_p * hs_p) + (vs_v * hs_v) + (vs_c * hs_c) + vs_o + "
        "(pop_p * hs_p) + (pop_v * hs_v) + (pop_c * hs_c) + pop_o"
    )
    model = bmb.Model(formula, data, family='categorical', dropna=True)
    return model

## GLOBAL BUILD MODEL
data = load_data()
model = build_model(data)

def fit_and_save_model(model: bmb.Model, save_path: Path = POSTERIOR_PATH) -> az.InferenceData:
    idata = model.fit()
    idata.to_netcdf(save_path)
    return idata

def load_posterior(path: Path = POSTERIOR_PATH) -> az.InferenceData:
    return az.from_netcdf(path)

# Run this only if the script is executed directly
if __name__ == '__main__':
    os.chdir(Path(__file__).parent.absolute())  # Change working dir to this script's folder

    posterior = fit_and_save_model(model)

    print(az.summary(posterior, hdi_prob=0.95))
    az.plot_trace(posterior)