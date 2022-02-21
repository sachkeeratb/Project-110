import plotly.figure_factory as pff
import plotly.express as pe
import plotly.graph_objects as go
import random
import statistics
import csv
import pandas as pd

df = pd.read_csv('medium_data.csv')
data_list = df["reading_time"].to_list()

population_mean = statistics.mean(data_list)
print(population_mean)

population_sdev = statistics.stdev(data_list)
print(population_sdev)

figure = pff.create_distplot([data_list],["Reading Time"], show_hist=False)
figure.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1],mode="lines",name="Mean"))
figure.add_trace(go.Scatter(x=[population_sdev,population_sdev],y=[0,1],mode="lines",name="Standard Deviation"))
figure.show()

def random_set_mean(counter): 
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data_list))
        value = data_list[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_figure(mean_list):
    df = mean_list
    figure = pff.create_distplot([df],["Responses"],show_hist=False)
    figure.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_mean(30)
        mean_list.append(set_of_means)
    show_figure(mean_list)

setup()