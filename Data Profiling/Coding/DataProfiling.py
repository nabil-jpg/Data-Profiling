import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv(r"Data Profiling\Raw Data\bank-dataset.data", sep=";", skipinitialspace=True)

profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
profile.to_file("report.html")