CODOMAX AI & ML Internship
This repository contains my complete 14-day Artificial Intelligence and Machine Learning Internship work completed with Codomax Digital Solutions.

The internship focused on Python programming, data analysis, data visualization, machine learning, model evaluation, and building a simple exam-score prediction system.

Project Overview
The main objective of this project is to understand the complete machine-learning workflow:

Data Collection → Data Exploration → Data Cleaning → Visualization → Model Training → Prediction → Evaluation → Final Submission

The project uses the dataset:

exam_score_predictions.csv
Dataset Columns
Column	Description
id	Unique student record identifier
exam_score	Examination score of the student
Note: The id column is only an identifier and is not a meaningful academic feature. It was used here to demonstrate the machine-learning workflow. A practical prediction model should include features such as study hours, attendance, previous marks, sleep duration, and assignment performance.

14-Day Internship Roadmap
Day	Topic	Work Completed
Day 1	Environment Setup	Installed Python, VS Code, Jupyter Notebook and Git
Day 2	Python Basics	Practised variables, data types, operators, loops and functions
Day 3	NumPy	Worked with arrays, indexing and mathematical operations
Day 4	Pandas	Loaded and explored the exam-score dataset
Day 5	Data Cleaning	Checked missing values, duplicates and dataset statistics
Day 6	Data Visualization	Created scatter, bar and line charts using Matplotlib
Day 7	Machine Learning Basics	Learned supervised learning, train-test split and Linear Regression
Day 8	Model Building	Built and trained a Linear Regression model
Day 9	Prediction	Generated predictions using the trained model
Day 10	Model Evaluation	Evaluated the model using MAE, MSE and R² Score
Day 11	Prediction App	Built a simple user-input prediction program
Day 12	Project Improvement	Organized project folders and saved model outputs
Day 13	GitHub Upload	Uploaded code, dataset, screenshots and documentation
Day 14	Final Submission	Verified project files and prepared the final submission
Technologies Used
Python
NumPy
Pandas
Matplotlib
Scikit-learn
Joblib
Jupyter Notebook
Visual Studio Code
Git
GitHub
Repository Structure
CODOMAX-INTERNSHI-P/
│
├── Day-01-Environment-Setup/
├── Day-02-Python-Basics/
├── Day-03-NumPy/
├── Day-04-Pandas/
├── Day-05-Data-Cleaning/
├── Day-06-Data-Visualization/
├── Day-07-ML-Basics/
├── Day-08-Model-Building/
├── Day-09-Prediction/
├── Day-10-Model-Evaluation/
├── Day-11-Prediction-App/
├── Day-12-Project-Improvement/
├── Day-13-GitHub-Upload/
├── Day-14-Final-Submission/
│
├── data/
│   └── cleaned_exam_score_predictions.csv
│
├── models/
│   └── score_prediction_model.pkl
│
├── results/
│   └── predictions.csv
│
├── screenshots/
├── exam_score_predictions.csv
├── requirements.txt
└── README.md
Installation
Clone the repository:

git clone https://github.com/Patty2007-AIML/CODOMAX-INTERNSHI-P.git
Open the project folder:

cd CODOMAX-INTERNSHI-P
Install the required libraries:

pip install -r requirements.txt
Required Libraries
pandas
numpy
matplotlib
scikit-learn
joblib
jupyter
You can generate the requirements file using:

pip freeze > requirements.txt
How to Run
Run a Python file:

python Day_10.py
Or open Jupyter Notebook:

jupyter notebook
Machine Learning Workflow
1. Load the Dataset
import pandas as pd

df = pd.read_csv("exam_score_predictions.csv")
2. Prepare Features and Target
X = df[["id"]]
y = df["exam_score"]
3. Split the Dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
4. Train the Model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
5. Generate Predictions
predictions = model.predict(X_test)
6. Evaluate the Model
The model is evaluated using:

Mean Absolute Error
Mean Squared Error
R² Score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
Data Visualization
The project includes:

Scatter plot
Bar chart
Line chart
Only a limited sample of records is used for visualization so that the charts remain readable.

Project Outcomes
Developed basic Python programming skills
Learned NumPy and Pandas fundamentals
Cleaned and explored a dataset
Created data visualizations using Matplotlib
Understood supervised machine learning
Trained a Linear Regression model
Generated and evaluated predictions
Built a simple prediction program
Organized a professional GitHub repository
Completed the final internship submission
Limitations
The current dataset contains only id and exam_score.

Because id is not a meaningful predictive feature, the model is mainly used to demonstrate the machine-learning process. For a more accurate score-prediction system, the dataset should include:

Study hours
Attendance percentage
Previous examination marks
Assignment scores
Sleep duration
Class participation
Future Improvements
Add meaningful academic features
Compare multiple machine-learning algorithms
Create better visualizations
Build a Streamlit web application
Add model-performance graphs
Deploy the project online
Improve prediction accuracy
GitHub Repository
CODOMAX AI & ML Internship Repository

Author
Parth Angare
B.Tech Artificial Intelligence and Machine Learning Student

Acknowledgement
I would like to thank Codomax Digital Solutions for providing this structured AI and Machine Learning internship and the opportunity to gain practical experience through daily tasks and project development.

⭐ If you found this repository useful, consider giving it a star.
