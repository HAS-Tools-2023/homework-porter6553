# Forecasting Assignment 3

Week 3 forecasting homework due: 1200 September 11, 2023

##
## Grade
3/3 I know that this was a really challenging week for a lot of people. Points for effort and I think we've got the bugs sorted out now. 
##

## Weekly Description

I ran the starter code and ran into a few hiccups but ultimately was able to fix them. I found that just those simple max, min, mean, and standard deviation calculations were not enough information to do an accurate forecast. What I wanted to do was figure out a way to extract out specifically the month of september and look at those calculations for september. Unfortunately I wasn't able to get that to work. I tried a couple of things:

    for i in range(month):
        if month[i] == 8:
            print(np.mean(flow))
OR
    if month[i] == 8:
        print(np.mean(flow))

I tried a few others and just couldn't quite get it. I will keep trying this week. I forecasted a bit using what I was able to get from the code. But I also looked at weather models and past rainfall in the area. In addition, this years monsoon season has been on the drier side so I am expecting slightly lower levels than last year at least. 