from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    try:
        age = int(data.get('age', 0))
        income = float(data.get('income', 0))
        insurance_type = data.get('insuranceType', '').lower()
        health_condition = data.get('healthCondition', '').lower()
        coverage = float(data.get('coverage', 0))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input data."}), 400

    base_rate = 0.02  # Default base rate
    if insurance_type == "medical":
        base_rate += 0.01
        if health_condition == "poor":
            base_rate += 0.03
    elif insurance_type == "term":
        base_rate += 0.015
    elif insurance_type == "vehicle":
        base_rate += 0.012
    elif insurance_type == "business":
        base_rate += 0.018

    age_factor = max(0, (age - 18)) * 0.001
    total_rate = base_rate + age_factor

    estimated_premium = coverage * total_rate / 1000

    return jsonify({"premium": round(estimated_premium, 2)})

if __name__ == '__main__':
    # Avoid using debug mode to prevent issues with _multiprocessing in some environments
    app.run(debug=False)
