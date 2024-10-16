from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    fiber_type = request.form['fiber_type']
    distance = request.form['distance']
    optical_source = request.form['optical_source']
    optical_detector = request.form['optical_detector']

    # Validate distance input
    try:
        distance = float(distance)
        if distance <= 0:
            raise ValueError("Distance must be positive.")
    except ValueError as e:
        return f"Input Error: {str(e)}", 400  # Return a bad request error

    # Example calculation of signal strength
    signal_strength = calculate_signal_strength(fiber_type, distance, optical_source, optical_detector)

    # Render results page with the computed signal strength
    return render_template('result.html', signal_strength=signal_strength)

def calculate_signal_strength(fiber_type, distance, optical_source, optical_detector):
    # Placeholder logic for calculating signal strength based on parameters
    # You can replace this with your actual calculation logic
    if fiber_type == "Single-Mode":
        strength = 20 - (0.2 * distance)  # Example formula
    else:
        strength = 15 - (0.5 * distance)  # Example formula for multi-mode

    return max(strength, 0)  # Ensure signal strength is non-negative

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)