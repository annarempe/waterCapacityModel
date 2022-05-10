import pandas as pd
import numpy as np

"""

	•	Using only simulations for 1980-2010 for training, predict the yields for a field for 2011-2015 using only weather* information. Repeat the same using 1990-2010, or 2000-2010. 

*Consider weather to include all of the in-season variables, as well as the value of H which reflects pre-season weather that sets the initial conditions for the season.
"""

if __name__ == '__main__':
    df = pd.read_csv('./soil/soy.sims.031416.csv')
    to_pred = df.loc[(df['year'].between(2011, 2015)) & (df['metsite'] == 'newton_long')]
    to_pred = to_pred['ylds']
    print(to_pred)
    df = df.loc[df['year'].between(1980, 2000)]


    print(df)


