# Import packages
import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class BostonPrediction():
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def train(self):
        """
        Train RandomForestRegressor on Boston House Price.
        """

        # Read train Data
        train_dir = os.path.join(self.data_dir,'train.csv')
        train_data_df = pd.read_csv(train_dir)
        train_x_df = train_data_df[['LotArea','BldgType']]
        train_y_df = train_data_df['SalePrice']

        # Map BldgType to int
        types = list(train_x_df['BldgType'].unique())
        self.mapping = dict(zip(types, range(len(types))))
        train_x_df.replace({'BldgType': self.mapping}, inplace=True)

        # Train RandomForestRegressor
        self.reg_model = RandomForestRegressor()
        self.reg_model.fit(train_x_df, train_y_df)


    def test(self):
        """
        Test RandomForestRegressor on Boston House Price.
        """
        # Read test Data
        test_dir = os.path.join(self.data_dir, 'test.csv')
        test_data_df = pd.read_csv(test_dir)
        test_x_df = test_data_df[['LotArea','BldgType']]

        # Map BldgType to int
        test_x_df.replace({'BldgType': self.mapping}, inplace=True)

        pred_y_df = self.reg_model.predict(test_x_df)

        print(pred_y_df)
        print("finish")

    def pickle_model(self):
        pickle.dump(self.reg_model, open('App/model.pkl', 'wb'))



if __name__== "__main__":
    data_dir = 'Data'
    bp = BostonPrediction(data_dir)
    bp.train()
    bp.test()
    bp.pickle_model()