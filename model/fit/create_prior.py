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
import numpy as np
import pandas as pd
import bambi as bmb
from pathlib import Path
import arviz as az
import os
from imblearn.over_sampling import SMOTE

os.chdir(Path(__file__).parent.absolute())  # Change directory to ./data
DATA_PATH = Path('./data/compiled_output.csv')
POSTERIOR_PATH = Path('./data/posterior.nc')

def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["winner"] = df["winner"].astype("category")

    target_col = 'winner'
    jitter_strength = 0.05

    max_count = df[target_col].value_counts().max()
    oversampled_frames = []

    for label, group in df.groupby(target_col):
        count = len(group)
        if count < max_count:
            needed = max_count - count
            # Sample with replacement
            samples = group.sample(needed, replace=True, random_state=42).copy()

            # Add jitter to numeric columns
            for col in group.select_dtypes(include=[np.number]).columns:
                noise = np.random.normal(0, jitter_strength, size=needed)
                samples[col] += noise

            oversampled_frames.append(pd.concat([group, samples], axis=0))
        else:
            oversampled_frames.append(group)

    return pd.concat(oversampled_frames).sample(frac=1, random_state=42).reset_index(drop=True)

def build_model(data: pd.DataFrame) -> bmb.Model:
    formula = (
        "winner ~ "
        "vs_p + hs_p + vs_v + hs_v + vs_c + hs_c + "
        "pop_p + hs_p + pop_v + hs_v + pop_c + hs_c +"
        "(1|state)"
    )
    priors = {
        "Intercept": bmb.Prior("Normal", mu=0, sigma=1),

    # P terms: majority — push them toward negative to counterbalance
    "vs_p": bmb.Prior("Normal", mu=-1.5, sigma=0.5),
    "hs_p": bmb.Prior("Normal", mu=-1.5, sigma=0.5),
    "pop_p": bmb.Prior("Normal", mu=-1.5, sigma=0.5),

    # V terms: neutral, allow for modest impact
    "vs_v": bmb.Prior("Normal", mu=1.5, sigma=1),
    "hs_v": bmb.Prior("Normal", mu=1.5, sigma=1),
    "pop_v": bmb.Prior("Normal", mu=1.5, sigma=1),

    # C terms: allow large positive influence
    "vs_c": bmb.Prior("Normal", mu=2.5, sigma=1.5),
    "hs_c": bmb.Prior("Normal", mu=2.5, sigma=1.5),
    "pop_c": bmb.Prior("Normal", mu=2.5, sigma=1.5),
    }
    model = bmb.Model(formula, data, family='categorical', priors=priors, dropna=True)
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