import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Print library versions
st_version = st.__version__
joblib_version = joblib.__version__
np_version = np.__version__
pd_version = pd.__version__

print(f"Streamlit version: {st_version}")
print(f"Joblib version: {joblib_version}")
print(f"Numpy version: {np_version}")
print(f"Pandas version: {pd_version}")
