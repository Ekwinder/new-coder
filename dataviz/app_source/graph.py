from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

import parse

MY_FILE = "/home/ekwinder/Documents/projects/newcoderprojects/dataviz/data/sample_sfpd_incident_all.csv"




def visualize_days():
    """Visualize data by day of week"""
    data_file = parse.parse(MY_FILE, ",")
    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out the counter to order it correctly when plotting.
    data_list = [
                  counter["Monday"],
                  counter["Tuesday"],
                  counter["Wednesday"],
                  counter["Thursday"],
                  counter["Friday"],
                  counter["Saturday"],
                  counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot from day_list
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Days.png".  This is our graph!
    plt.savefig("Days.png")

    # Close figure
    #plt.clf()

def visualize_type():

    data_file = parse.parse(MY_FILE, ",")

    counter = Counter(item["Category"] for item in data_file)

    labels  = tuple(counter.keys())

    xlocations = np.array(range(len(labels))) + 0.5

    width = 0.5

    plt.bar(xlocations, counter.values(), width=width)

    plt.xticks(xlocations + width/2, labels, rotation=90)

    plt.subplots_adjust(bottom=0.4)

    plt.rcParams['figure.figsize'] = 12,8

    plt.savefig("Type.png")

    # Close figure
    plt.clf()


def main():
    #visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()