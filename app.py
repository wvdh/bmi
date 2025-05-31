
from flask import Flask, request, render_template

app = Flask(__name__)

def get_bmi_interpretation(bmi):
	if bmi <= 18.4:
		return 'You are underweight.'
	elif bmi <= 24.9:
		return 'Your weight is normal.'
	elif bmi <= 29.9:
		return 'You are slightly overweight.'
	elif bmi <= 34.9:
		return 'You are severely overweight.'
	elif bmi <= 39.9:
		return 'You are obese.'
	else:
		return 'You are severely obese.'

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		weight = float(request.form['weight'])
		height = float(request.form['height'])
		bmi = round(weight / (height ** 2), 2)
		interpretation = get_bmi_interpretation(bmi)
		return render_template('result.html', bmi=bmi, interpretation=interpretation)
	return render_template('index.html')


import os

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)