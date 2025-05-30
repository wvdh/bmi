from flask import Flask, request, jsonify

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

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    data = request.json
    weight = float(data['weight'])
    height = float(data['height'])
    bmi = round(weight / (height ** 2))
    interpretation = get_bmi_interpretation(bmi)

    return jsonify({"bmi": bmi, "interpretation": interpretation})

if __name__ == '__main__':
    app.run(debug=True)
