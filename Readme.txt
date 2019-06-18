
1. BreastCancer_LR_Project
***************************

A sample project that contains the Training script and Deploy script

Expt1  - Experiment create in Python (ipynb) to fit Logistic Regression model
-----

Expt1/ExampleScikitLogisticRegressionModel.ipynb - Actual Training script.
Expt1/finalized_model.sav - Model dump file, which is a generated file after running the above training script
Expt1/examplescore.py - Sample Python file, which is generated file after running the above training script. For Demonstration purpose, using %writefile created this sample Predict/Deploy script that makes use of the .sav model and predict against the same.


Deploy
----------
Final Executable python script to Deploy in HSI workbench/Runtime so that REST interface is exposed for the integrating applications. 
Deploy this experiment to get the curl/ REST end points. 

Three ways/scripts of prediction 
Deploy/score.py - Python (py) based Prediction script that reads input internally (i.e. not from REST API)
Deploy/score.py.ipynb - Python (ipynb)/ Jupyter based Prediction script that reads input internally
Deploy/score_IO.py - Python (py) based prediction script that parses the input from passed REST API arguments

(Note: even above EXPT1 can as well be deployed, but we need to use examplescore.py related curl command for prediction. Which is similar to score.py above)


Created a Postman collection to test the same - BreastCancer_LR_DEMO.postman_collection.json. 
Please upload in Postman to test.
This refers to already created Project 'BreastCancer_LR_Project' in demo system using hsiuser4 user credentials.


2. BreastCancer Data
*********************

breastcancer_train.csv - ~700 records used for LR model fit training
breastcancer_test.csv - ~32 records used for validation, and confusion matrix generation etc
(by default these data sets are already present within HSI. We can use DataSources tab to add such similar data)
input.csv - sample input data that can be sent across during Prediction after Deploying in Runtime/ Workbench

(For now, the training and prediction scripts used default existing csv files that come with installation)

3. Postman Collection
**********************

Token_DEMO - Initial API to get the access token. Used hsiuser4 username and credentials
Async Score - Score.py (No args) - Async scoring api using an execution script and taking the input internally (Corresponding to score.py above)
Async Score - Score.ipynb (No args) - Async scoring api using an execution script and taking the input internally (Corresponding to score.py.ipynb above)
Async Score - Score_IO.py (No args) - Async scoring api using an execution script and taking the input from API (Corresponding to score_IO.py above)
               Input CSV (32 records) is based 64 encoded and sent in additionalParams parameter
Async Score - Score_IO.py (No args) - Async scoring api using an execution script and taking the input from API (Corresponding to score_IO.py above)
               Input CSV (2 records) is based 64 encoded and sent in additionalParams parameter
Get Status - to get the status of any of the above requests
Get result - to get the result of any of the above request execution
