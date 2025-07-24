from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        fat_percent = float(request.form['fatpercent'])
        intensity = request.form['intensity']

        # Mapping intensity to calorie deficit
        deficit_map = {
            '1': 200,     # Mild
            '2': 500,     # Serious
            '3': 1000     # Extreme
        }

        if intensity not in deficit_map:
            result = {"error": "Invalid intensity level selected."}
        else:
            deficit = deficit_map[intensity]
            fat_mass_to_lose = weight * (fat_percent / 100.0)
            days = (7700 * fat_mass_to_lose) / deficit
            result = {
                "fat_mass": round(fat_mass_to_lose, 2),
                "deficit": deficit,
                "days": round(days, 1),
                "fat_percent": fat_percent
            }

    return render_template("index.html", result=result)
    
if __name__ == '__main__':
    app.run(debug=True)
