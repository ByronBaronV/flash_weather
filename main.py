from flask import Flask, render_template

app = Flask(__name__)


# Sample weather data - in a real app, this would come from an API
weather_data = {
    'temperature': 22,
    'condition': 'Sunny',
    'humidity': 45,
    'wind_speed': 15
}
#Lenni estuvo aquiiiii
@app.route('/')
def index():
    return render_template('weather.html',
                           weather=weather_data)

# DEMO AREA
if __name__ == '__main__':
    app.run(debug=True)

