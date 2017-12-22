#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')  # To run this program on bash, add this line.
import numpy as np
import matplotlib.pyplot as plt
import mpld3



N = 100
scatter_list = []


def main():
    figure_on_browser, ax_of_browser_subplot = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
    x_even_list = []
    y_even_list = []
    even_labels = []

    x_odd_list = []
    y_odd_list = []
    odd_labels = []

    little_values = []
    little_labels = []


    for x in range(1, 20):
        if x < 10 :
            little_values.append(x)
            little_labels.append("this is (" + str(x) + "," + ")" )
            continue

        if x % 2 == 0:  # even number case
            x_even_list.append(x)
            y_even_list.append(x)
            even_labels.append("this is (" + str(x) + "," + ")" )
        else:  # odd number case
            x_odd_list.append(x)
            y_odd_list.append(x)
            odd_labels.append("this is (" + str(x) + "," + ")" )

    even_scatters = ax_of_browser_subplot.scatter(x_even_list,
                                                   y_even_list,
                                                   c='b',
                                                    marker='>',
                                                   s=1000 * np.random.random(size=N),
                                                   alpha=0.3,
                                                   cmap=plt.cm.jet)

    odd_scatters = ax_of_browser_subplot.scatter(x_odd_list,
                                                    y_odd_list,
                                                    c='r',
                                                    s=1000 * np.random.random(size=N),
                                                    alpha=0.3,
                                                    cmap=plt.cm.jet)

    little_pointers, = ax_of_browser_subplot.plot(little_values,
                               little_values,
                               '-o',
                               ms=7,
                               lw=1,
                               alpha=0.7,
                               mfc='red')

    # print(type(what) )

    ax_of_browser_subplot.grid(color='white', linestyle='solid')  # set grid on the subplot
    ax_of_browser_subplot.set_title("Scatter Plot (with tooltips!)", size=20)  # set title of subplot
    # Generate tooltip in combination with label list according to scatter list
    tooltip_even = mpld3.plugins.PointLabelTooltip(even_scatters,
                                              labels=even_labels)

    tooltip_odd = mpld3.plugins.PointLabelTooltip(odd_scatters,
                                                   labels=odd_labels)

    tooltip_little = mpld3.plugins.PointLabelTooltip(little_pointers,
                                                  labels=little_labels)

    # Apply hover action
    mpld3.plugins.connect(figure_on_browser, tooltip_even)
    mpld3.plugins.connect(figure_on_browser, tooltip_odd)
    mpld3.plugins.connect(figure_on_browser, tooltip_little)

    # open plot chart in browser
    # save plot chart as html file
    mpld3.save_html(figure_on_browser, "html_result.html")

if __name__ == '__main__':
    main()
