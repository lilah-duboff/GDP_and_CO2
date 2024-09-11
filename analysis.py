import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import seaborn.objects as so

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

wdi["Log GDP Per Capita"] = np.log(wdi["GDP per capita (constant 2010 US$)"])

pds_class_plot = (
    so.Plot(
        wdi,
        x="Log GDP Per Capita",
        y="Mortality rate, infant (per 1,000 live births)",
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and Infant Mortality Rate")
    .theme({**style.library["seaborn-v0_8-whitegrid"]})
)


pds_class_plot.show()
