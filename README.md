**Predict if the applicant should be granted a loan or not.** </br></br>

**Content**</br>
A loan application is used by borrowers to apply for a loan. Through the loan application, borrowers reveal key details about their finances to the lender. The loan application is crucial to determining whether the lender will grant the request for funds or credit.</br></br>



**Problem Statement**</br>
The director of SZE bank identified that going through the loan applications to filter the people who can be granted loans or need to be rejected is a tedious and time-consuming process. He wants to automate it and increase his bank’s efficiency. After talking around a bit, your name pops up as one of the few data scientists who can make this possible within a limited time. Will you help the director out? </br>

**Objective**</br>
The idea behind this ML project is to build an ML model and web application that the bank can use to classify if a user can be granted a loan or not.</br>

**About the Data** </br>
The dataset contains information about Loan Applicants. There are 12 independent columns and 1 dependent column. This dataset includes attributes like Loan ID, gender, if the loan applicant is married or not, the level of education, applicant’s income etc. </br>

To load the training data in your jupyter notebook, use the below command:</br>

import pandas as pd</br>

loan_data  = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_train.csv" )</br>

 

**Data Description**<br></br>
Loan_ID: A unique ID assigned to every loan applicant</br>
Gender: Gender of the applicant (Male, Female)</br>
Married: The marital status of the applicant (Yes, No)</br>
Dependents: No. of people dependent on the applicant (0,1,2,3+)</br>
Education: Education level of the applicant (Graduated, Not Graduated)</br>
Self_Employed: If the applicant is self-employed or not (Yes, No)</br>
ApplicantIncome: The amount of income the applicant earns</br>
CoapplicantIncome: The amount of income the co-applicant earns</br>
LoanAmount: The amount of loan the applicant has requested for</br>
Loan_Amount_Term: The  no. of days over which the loan will be paid</br>
Credit_History: A record of a borrower's responsible repayment of debts (1- has all debts paid, 0- not paid)</br>
Property_Area : The type of location where the applicant’s property lies (Rural, Semiurban, Urban)</br>
Loan_Status: Loan granted or not (Y, N)</br>

