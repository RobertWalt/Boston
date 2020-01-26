# Import packages
import io
from flask import Flask, request, render_template, redirect, Response, url_for
from model import BostonPrediction
from wtforms import Form, SelectField, FloatField, validators
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


class predict(Form):
    lot_area = FloatField('lot_area_f', validators=[validators.InputRequired()])
    bldg_type = SelectField('bldg_type', choices=[('1Fam','One family house'), ('2fmCon','Two family Condor'),
                                                 ('Duplex','Duplex building'),
                                                 ('TwnhsE','Townhouse')], validators = [validators.InputRequired()])

# Create flask webapp.
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='1234',
)
# Loads model.
model = BostonPrediction()
model.load_model()

@app.route('/', methods=['POST', 'GET'])
def main():
    hpform = predict(request.form)
    if request.method == 'POST' and hpform.validate():
        lot_area = hpform.lot_area.data
        building_type = hpform.bldg_type.data
        prediction = model.predict(lot_area_f=lot_area, building_type_str=building_type)
        return '<h2>Predicted House Price: {} $</h2>'.format(round(prediction[0],2))
    # elif request.form['submit_button'] == 'Plot':
    #     return redirect(url_for('plot_png'))
    return render_template('predict.html', form=hpform)


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    model = BostonPrediction()
    model.load_model()
    fig = model.partial_dep_plot()
    return fig


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
