import matplotlib.pyplot as plt
import pandas as pd
import panel as pn
pn.extension()
@pn.cache
def get_data():
    return pd.read_csv("faithful.csv")

def get_faithful_hist(bins):
    faithful = get_data()
    fig, ax = plt.subplots()
    ax.hist(faithful["waiting"], bins=bins, color="orange")
    plt.close(fig) # Évite les fuites de mémoire
    return fig
bins = pn.widgets.IntSlider(name="Nombre de blocs", start=1, end=50, value=30)
faithful_hist = pn.bind(get_faithful_hist, bins=bins)
pn.template.FastListTemplate(
title="Geyser Old Faithful ￿",
sidebar=[bins],
main=[pn.pane.Matplotlib(faithful_hist)],
).servable()
