from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

@app.route('/')
def home():
    return render_template('index.html', teams=sorted(teams), cities=sorted(cities))

@app.route('/predict', methods=['POST'])
def predict():
    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    city = request.form['city']
    target = int(request.form['target'])
    score = int(request.form['score'])
    overs = float(request.form['overs'])
    wickets = int(request.form['wickets'])

    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_left],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    return render_template('index.html', teams=sorted(teams), cities=sorted(cities), 
                           batting_team=batting_team, bowling_team=bowling_team, city=city, 
                           target=target, score=score, overs=overs, wickets=wickets, 
                           win=round(win * 100), loss=round(loss * 100), show_result=True)

if __name__ == '__main__':
    app.run(debug=True)
