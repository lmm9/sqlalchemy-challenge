#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:45:44 2020

@author: lmm
"""
from flask import Flask, jsonify
import os
import csv

csvpath = os.path.join('Resources', 'hawaii_measurements.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
# Dictionary of Hawaii Measurements
hawaii_measurements = csvreader

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data as json"""

#    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Return the station data as json"""

 #   return jsonify(stations)

@app.route("/api/v1.0/tobs")
def stations():
    """Return the tobs data as json"""

#    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def stations():
    """Return the <start> data as json"""

#    return jsonify(<start>)

@app.route("/api/v1.0/<start>/<end>")
def stations():
    """Return the <start>/<end> data as json"""

#    return jsonify(<start>/<end>)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Measurement Station!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)


