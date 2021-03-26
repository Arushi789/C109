import statistics
import csv
import pandas as pd 
import plotly.figure_factory as ff


df= pd.read_csv("data.csv")
height_list=df["Height"].to_list()
weight_list=df["Weight"].to_list()

#find the mean for height and weight
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

#find the median 
height_median= statistics.median(height_list)
weight_median= statistics.median(weight_list)

#find the mode 
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

#find StdDev
print("The mean, median and mode of the height is {}, {} and {} respectively.".format(height_mean,height_median,height_mode))
print("The mean, median and mode of the weight is {}, {} and {} respectively.".format(weight_mean,weight_median,weight_mode))

#standard deviation
height_stddev= statistics.stdev(height_list)
height_firstStddev_start,height_firstStddev_end= height_mean-height_stddev,height_mean + height_stddev
height_secondStddev_start,height_secondStddev_end= height_mean-(height_stddev*2),height_mean + (height_stddev*2)
height_thirdStddev_start,height_thirdStddev_end= height_mean-(height_stddev*3),height_mean + (height_stddev*3)

weight_stddev= statistics.stdev(weight_list)
weight_firstStddev_start,weight_firstStddev_end= weight_mean-weight_stddev,weight_mean + weight_stddev
weight_secondStddev_start,weight_secondStddev_end=weight_mean-(weight_stddev*2),weight_mean + (weight_stddev*2)
weight_thirdStddev_start,weight_thirdStddev_end= weight_mean-(weight_stddev*3),weight_mean + (weight_stddev*3)

fig= ff.create_distplot([height_list],["Height"],show_hist=False)
fig.show()