from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap 
import pandas as pd 
import numpy as np 

import pandas_datareader.data as web
import matplotlib.pyplot as plt

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	Ticker=request.form['Ticker']
	try:
		df = web.DataReader(Ticker, 'yahoo')
		print(df)
	except:
		return 'Invalid Ticker!'
	df.reset_index(inplace=True)
	df = df[['Date', 'Adj Close']]
	VaR = 'Hello World'
	df = df.set_index('Date')
	return render_template('generic.html', prices=df, VaR=VaR)

if __name__ == '__main__':
	app.run(debug=True)