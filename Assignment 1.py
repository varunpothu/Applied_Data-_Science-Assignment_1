# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:36:09 2023

@author: Varun Pothu
"""

import pandas as pds
import matplotlib.pyplot as plts

# Read data into pandas dataframe by pdss.read_csv()
data = pds.read_csv('Final-50-stocks.csv')
print(data)

#1st Graph

def line_plot(data):
    
    ''' Defining Function to create a lineplot.
    Line Graph to plot Stats of Stocks from the above dataset '''
    
    
    #Plotting the Graph with specific size
    plts.figure(figsize = (20,10))

    #Assigning the Data for - Line Graph 
    plts.plot(data["DATE"], data["WIPRO"], label = "WIPRO")
    plts.plot(data["DATE"], data["TCS"], label = "TCS")
    plts.plot(data["DATE"], data["HCLTECH"], label = "HCLTECH")
    
    
    # Plotting X & Y labels along with the title
    plts.xlabel("Year", fontsize = 16)
    plts.ylabel("Price", fontsize = 16)
    plts.title('NIFTY - 50 IT Stocks Analysis', fontsize = 16)
    
    # Slicing and Rotating X-axis
    plts.xticks(data.DATE[::80], rotation = 90)
    
    # Plotting legend
    plts.legend()
    
    # save as png
    plts.savefig("linplot.png")
    
    plts.show()
    
    
    
# Read data into pandas dataframe by pds.read_csv()
data1 = pds.read_csv('HRDataset_v14.csv')


#2nd Graph

def pie_chart(data1):
    
    ''' Defining Function to create a Pie chart.
    Pie chart to count the percentage of Departments from above dataset '''
    

    # group data by department and count the number of employees from dataset
    sum_by_dept = data1.groupby('Department')['EmpID'].nunique().sort_values\
                                                          (ascending = False)
    
    # create a list of colors for each Recruitment Source
    colors = ['cornflowerblue', 'mediumseagreen', 'tomato', 'gold', 'orange',\
              'black']

    # to explode the pie chart
    explode = [.05,.05,.08,0.08,0.08,0.05]
   
    plts.figure(figsize = (10, 6)) 
   
    # plot the data
    plts.pie(sum_by_dept.values, labels = sum_by_dept.index, \
         autopct='%1.1f%%', shadow = True, colors = colors, explode = explode)
    
     
    # Plotting the title and axis
    
    plts.title('Employee Percentage Count by Various Departments')
    plts.legend(title='Departments', bbox_to_anchor=(1, 0, 0.5, 1))
    plts.axis('equal')
    
    # save as png
    plts.savefig("Piechart.png")
    plts.show()
 


#3rd graph    
  
def histogram(data1):
    
    ''' Defining Function to create a histogram.
    Histogram to plot Distribution of Salaries from above dataset '''
    
    #Plotting the Graph with specific size
    plts.figure(figsize = (10,6))
    
    # ploting the data
    plts.hist(data1['Salary'], edgecolor = 'black')
    
    # Plotting X & Y labels along with the title
    plts.title('Distribution of Salaries', fontsize = 16)
    plts.xlabel('Salary', fontsize = 14)
    plts.ylabel('Count', fontsize = 14)
    
    # save as png
    plts.savefig("histogram.png")
    plts.show()
    

# call the plots functions to generate individual plots
line_plot(data)
pie_chart(data1)
histogram(data1)
