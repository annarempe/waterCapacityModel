import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import r2_score


"""

	•	Using only simulations for 1980-2010 for training, predict the yields for a field for 2011-2015 using only weather* information. Repeat the same using 1990-2010, or 2000-2010. 

*Consider weather to include all of the in-season variables, as well as the value of H which reflects pre-season weather that sets the initial conditions for the season.
"""

if __name__ == '__main__':
    df = pd.read_csv('./soil/soy.sims.031416.csv')
    y = df.loc[(df['year'].between(2011, 2015)) & (df['metsite'] == 'newton_long')]
    x = y[['Junemaxt', 'Augvpd']]
    y = y['ylds']
    print(y)
    to_pred = df.loc[df['year'].between(1980, 2000)]
    print(x.shape)

    print(x.describe())
    print(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.33, random_state=7)

    model = SVR()
    model.fit(x_train, y_train)

    predictions = model.predict(x_train)
    print(r2_score(y_train, predictions))


