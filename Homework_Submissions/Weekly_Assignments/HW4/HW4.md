# Forecasting Assignment 4

Week 4 forecasting homework due: 1200 September 18, 2023

##
## Grade
2/3  Good job on getting the forecast to run this week but you missed answering the homework questions. Note that the questions are listed at the bottom of the assignment for each week. Let me know if you have questions. 
##

## Weekly Description

This week was rather difficult to forecast for because there is actually no data available for last week. I don't really understand what is trying to be done in the week 4 numpy code. I ran it and had to fix one thing to make it run correctly. I ran into an error here:
    filename = 'streamflow_week4.txt'
    filepath = os.path.join('../data', filename)
    print(os.getcwd())
    print(filepath)

Because the original code said "filepath = os.path.join('data', filename)". So it couldn't find the correct path. Once that was fixed, it ran properly. I decided on my numbers by going back to the week 3 starter code and only using values since 2017 for this upcoming week. I then did the same for two weeks ahead.