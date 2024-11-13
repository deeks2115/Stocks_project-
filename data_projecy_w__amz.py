#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 23:40:17 2023

@author: deekshitamadhalam
"""

import csv 
import matplotlib.pyplot as plt 

FILENAME = "/Users/deekshitamadhalam/Desktop/DS2000/Technology Sector List.csv"
AMZN_stock = "/Users/deekshitamadhalam/Desktop/DS2000/AMZN.csv"

def get_stocks(file):
    '''
    Parameters
    ----------
    file : csv
        contains the stock prices of 100 companies .

    Returns
    -------
    prices : list
        the prices of all the different companies.
    '''
    
    #create an empty list to add the data to so it can be "x values" 
    prices = []
    
    #read the file and only add the second column to the list because contains the price 
    with open(file, "r") as csv_file: 
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
                key = row[2]
                prices.append(key)
    #gets rid of the first value in the list which is the word "price"             
    prices = prices[1:]
    return (prices)

def amazon_stock (file):
    '''
    parameters
    -----------
    file : csv  
        contains the stock prices of amazon for each day in the year 2022 
        
    returns
    -------
    average: float 
        the average stock price for amazon  
    '''
    #empty list to add the data too 
    price = []
    with open(file, "r") as csv_file: 
        csv_reader = csv.reader(csv_file)
        
        #Reads the fourth column but only starts after the first row because the first contains  labels 
        for row in csv_reader:
            if row[4] != "High":  
                
                #gets the highest value for the day 
                key = row[4]
                
                #gets rid of the dollar sign so it is only integers 
                key = key.replace("$", '')
                
                #gets the lowest value for the day 
                key2 = row[5]
                key2 = key2.replace("$", '')
                
                #average value for the day 
                key = round((float(key) +float(key2)) / float(2),2)
                
                #add all the days in a year together 
                price.append(key)
    print(price)
    print()
    total = 0
    
    #reads through the list and adds each value to the total to then find the average of the whole year 
    for i in range(len(prices)):
        total += (float(prices[i]))
    average = total / float(len(prices))
    print(average)
    
    #draws the blue line that shows where amazon falls in this 
    for i in range(100):
        plt.scatter(i, average, color = 'blue', marker = '.', alpha = 0.5)
        
    return average 
    
def plot_stocks(price):
    axes = plt.axes()
    
    plt.title("Stock Prices of Different Companies")
    plt.xlabel("Company")
    plt.ylabel("Price of Stock")

    #to make sure that the graph is correctly positioned 
    axes.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    axes.set_yticks([0,100,200,300,400,500,600,700,800,900,1000,1100])
    
    #rPlots stock price of each company and color codes based on position in relation to amazon 
    
    for i in range(len(price)):
        colors = ['red' if float(price[i]) < float(181) else 'green']
        plt.scatter(i,float(price[i]), color = colors)
           
prices = get_stocks(FILENAME)
plot_stocks(prices)
amazon_stock(AMZN_stock)
