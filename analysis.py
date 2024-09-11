import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import seaborn.objects as so

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

columns = [
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
    "Country Name",
]
df = wdi[columns]

pds_class_plot = (
    so.Plot(
        wdi,
        x="GDP per capita (constant 2010 US$)",
        y="Mortality rate, infant (per 1,000 live births)",
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Mortality rate, infant (per 1,000 live births)")
    .theme({**style.library["seaborn-v0_8-whitegrid"]})
)


pds_class_plot.show()
