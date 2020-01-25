# Import packages
import os
import pickle
from flask import Flask



class Webapp():

    def create_app(self):
        # create flask webapp
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_mapping(
            SECRET_KEY='Boston',
        )
        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        model = pickle.load(open('model.pkl', 'rb'))
