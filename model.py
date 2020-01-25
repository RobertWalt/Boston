# Import packages
import os, json
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class BostonPrediction:
    def preprocessing(self, data_df):
        data_df.dropna(inplace=True)
        data_df = pd.get_dummies(data_df)

        return data_df

    def train(self):
        """
        Train RandomForestRegressor on Boston House Price.
        """

        # Read train Data
        train_data_df = pd.read_csv('Data/train.csv')

        train_data_df = self.preprocessing(train_data_df[['SalePrice','LotArea','BldgType']])

        train_x_df = train_data_df.drop('SalePrice', 1)
        train_y_df = train_data_df['SalePrice']

        features_dict = {'features': list(train_x_df)}
        with open('App/model_data.json', 'w') as f:
            json.dump(features_dict, f)

        # Train RandomForestRegressor
        self.reg_model = RandomForestRegressor(oob_score=True)
        self.reg_model.fit(train_x_df, train_y_df)
        print("test")


    def test(self):
        """
        Test RandomForestRegressor on Boston House Price.
        """
        # Read test Data
        test_data_df = pd.read_csv('Data/test.csv')
        test_x_df = self.preprocessing(test_data_df[['LotArea','BldgType']])
        pred_y_df = self.reg_model.predict(test_x_df)

        print(pred_y_df)

    def predict(self, lot_area, building_type):
        # with open('App/model_data.json', 'r') as f:
        #     features_dict = json.load(f)
        # self.features = features_dict['features']

        data_df = pd.DataFrame(0, index=[0], columns=self.features)
        data_df['LotArea'] = lot_area
        bldgtype = 'BldgType_'+building_type
        data_df[bldgtype] = 1
        # data_prepro = self.preprocessing(pd.DataFrame(data_dict,index=[0]))
        # predict_x_df = self.preprocessing(data_df[['LotArea', 'BldgType']])
        # data_df.update(pd.DataFrame([data_prepro],index=[0]))




        pred_y_df = self.reg_model.predict(data_df)

        return pred_y_df

    def load_model(self):
        self.reg_model = pickle.load(open('/Users/robertwalter/PycharmProjects/Boston/App/model.pkl', 'rb'))
        with open('/Users/robertwalter/PycharmProjects/Boston/App/model_data.json', 'r') as f:
            features_dict = json.load(f)
        self.features = features_dict['features']


    def safe_model(self):
        pickle.dump(self.reg_model, open('/Users/robertwalter/PycharmProjects/Boston/App/model.pkl', 'wb'))



if __name__== "__main__":
    bp = BostonPrediction()
    #bp.train()
    #bp.test()
    #bp.safe_model()
    bp.load_model()
    bp.predict({"LotArea":"11250", "BldgType":"1Fam"})