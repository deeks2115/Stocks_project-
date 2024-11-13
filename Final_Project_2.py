#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:16:35 2023

@author: diyakadakia
"""

# import amazon dataset  
FILENAME = "/Users/diyakadakia/Downloads/data science/project/AMZN.csv"

# import csv and matplotlib 
import csv
import matplotlib.pyplot as plt  

# function to calculate the average price per year  
def calculate_average_price_per_year(file):
 
    """
        Calculate the average price of the Amazon stock per year 
        
        Parameters 
        ------
        file: file
        
            provides the list of the Amazon stock per day from 1997 to 2022
            
        Returns 
        -----
        the yearly price of the stock in a dictionary 
        
    """
    
    # define an empty dictionary 
    yearly_prices = {}

    # open and read the csv file 
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        
        # skip the header row 
        next(reader) 

        # create a for loop  
        for row in reader:
            
            # the year is the first four numbers in the first index of the file 
            year = row[0][:4]

            # for each year add the low sum and high sum and the count of days to the dictionary  
            if year not in yearly_prices:
                yearly_prices[year] = {'low_sum': 0, 'high_sum': 0, 'count': 0}


            # add the prices and counts
            yearly_prices[year]['low_sum'] += float(row[1])
            yearly_prices[year]['high_sum'] += float(row[2])
            yearly_prices[year]['count'] += 1
            
 
    # for each year in the yearly_prices dictionary 
    for year in yearly_prices: 
      
        # add the low_sum and the high_sum and divide by the count (per year) in order to find the average_price
        average_price = (yearly_prices[year]['low_sum'] + yearly_prices[year]['high_sum']) / (2 * yearly_prices[year]['count'])
        yearly_prices[year]['average_price'] = average_price
        
        # print the years and average price 
        print(f'Year: {year}, Average Price: {yearly_prices[year]["average_price"]:.2f}')
        
    # return the yearly_prices dictionary
    return yearly_prices

# function to plot the average prices 
def plot_average_prices(yearly_prices):
     
    """
        Plot the average price of the Amazon stock per year 
        
        Parameters 
        ------
        yearly_prices: yearly price dictionary 
        
            a dictonary with the average Amazon stock per year from 1997 to 2022
            
        Returns 
        -----
        nothing 
        
    """
    
    # create empty lists for the years and the average prices 
    years = []
    average_prices = []

    # create a for look for each year in the dictionary 
    for year in yearly_prices: 
        data = yearly_prices[year]
        # append the years (as integers) into the empty years list 
        years.append(int(year)) 
        # append the list of average prices into the empty average_prices list 
        average_prices.append(data["average_price"])

    # plot the data 
    plt.plot(years, average_prices, color = "darkgreen" , marker='o')
    
    # add plot features: title, xlabel and ylabel
    plt.title('Average Price of Amazon Stock per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price of Stock') 
    
    # show the graph
    plt.show()


# main function
if __name__ == "__main__": 
        
    # use the first function to find the average price per year
    result = calculate_average_price_per_year(FILENAME)
    # use the second function to plot the data 
    plot_average_prices(result)


 

        



