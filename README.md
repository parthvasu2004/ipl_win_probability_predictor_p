🏏 **IPL Win Probability Predictor**


Predict the Winning Probability of an IPL Match in Real-Time


🔗 Repository: parthvasu2004/ipl_win_probability_predictor_p


🚀 Overview


The IPL Win Probability Predictor is a machine learning-based web application designed to estimate the probability of a team's victory in an ongoing IPL match. It leverages historical match data, machine learning models, and real-time inputs to provide accurate win predictions.


🛠️ Features


✔️ Real-Time Prediction: Calculates win probability based on match conditions.
✔️ Machine Learning Model: Uses a trained pipeline (pipe.pkl) for predictions.
✔️ Flask Web Interface: Interactive and user-friendly UI.
✔️ Data-Driven Insights: Uses past IPL match data to enhance accuracy.
✔️ Live Deployment: Hosted on Render for easy accessibility.


📂 Project Structure

ipl_win_probability_predictor_p/
│── templates/          # HTML templates for web app  
│── app.py              # Flask web application  
│── matches.csv         # Dataset containing past IPL match data  
│── pipe.pkl            # Trained ML model pipeline  
│── requirements.txt    # Python dependencies  
│── .gitignore          # Ignored files  
│── README.md           # Project documentation  


⚙️ Installation & Setup


1️⃣ Clone the Repository

git clone https://github.com/parthvasu2004/ipl_win_probability_predictor_p.git
cd ipl_win_probability_predictor_p


2️⃣ Create & Activate Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Run the Application

python app.py
Visit http://127.0.0.1:5000/ in your browser to access the web app.


🏆 Usage


1️⃣ Open the web application.
2️⃣ Enter match details (teams, overs, runs, wickets, etc.).
3️⃣ Click "Predict" to get the probability of each team's win.


🎯 Model & Training


Dataset: Uses matches.csv, which contains historical IPL match data.
Algorithm: Trained using machine learning techniques to estimate win probability.
Features Used:
Runs scored
Wickets lost
Overs played
Target score
Run rate
Match conditions


🔗 Live Deployment


The application is deployed on Render for public access. Click here: https://ip-win-probability-predictor-mhp.onrender.com


🤝 Contribution


Contributions are welcome! Feel free to fork this repository, create feature branches, and submit pull requests.


📜 License


This project is licensed under the MIT License – free to use and modify.


📬 Contact
👤 Parth Pandey
📧 parthvasu2004@gmail.com
🔗 [linkedin.com/in/parth-pandey-3442a9256](https://www.linkedin.com/in/parth-pandey-3442a9256/)
