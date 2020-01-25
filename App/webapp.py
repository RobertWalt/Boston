# Import packages
import sys
import pickle
import sys

sys.path.append('/Users/robertwalter/PycharmProjects/Boston')
from flask import Flask, jsonify, request, render_template, redirect
from model import BostonPrediction
from wtforms import Form, SelectField, FloatField, validators


class HousingPriceForm(Form):
    lot_area = FloatField('LotArea', validators=[validators.InputRequired()])
    bldg_type = SelectField('BldgType', choices=[('1Fam', '1Fam')], validators=[validators.InputRequired()])


def create_app():
    # create flask webapp
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='Boston',
    )

    model = BostonPrediction()
    model.load_model()

    @app.route('/', methods=['POST', 'GET'])
    def main():
        hpform = HousingPriceForm(request.form)
        if request.method == 'POST' and hpform.validate():
            lot_area = hpform.lot_area.data
            building_type = hpform.bldg_type.data
            prediction = model.predict(lot_area=lot_area, building_type=building_type)
            return '<h1>Predicted House Price: {} $</h1>'.format(round(prediction[0],2))
        return render_template('housing_prices.html', form=hpform)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
