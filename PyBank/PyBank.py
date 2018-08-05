
# coding: utf-8

# In[206]:


#import files
import pandas as pd
import numpy as np


# In[207]:


# read in csv file
bank_csv_path = "budget_data.csv"

# Import the data into a Pandas DataFrame
budget_df = pd.read_csv(bank_csv_path)
budget_df.head()

import locale
# locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# locale.currency( 1234.50, grouping = True )


# In[208]:


# total the number of months in data set
Total_months = budget_df.Date.count()
Total_months


# In[209]:


# total net amount P/L
Total_net = budget_df['Profit/Losses'].sum()
Total_net = locale.currency(Total_net, grouping = True )


# In[210]:


# Average change in P/L
Day_changdf = budget_df.set_index('Date').diff()
Day_changdf
Ave_changdf = Day_changdf.sum() / (Total_months - 1)
# Ave_changdf = locale.currency(Ave_changdf, grouping = True)
Ave_changdf = Ave_changdf.reset_index()
Ave_changdf = locale.currency(Ave_changdf.loc[0,0], grouping = True)
# Ave_changdf
#Ave_changdf


# In[211]:


# Greatest increase in profits
Greatest_inc = Day_changdf[Day_changdf['Profit/Losses']==Day_changdf['Profit/Losses'].max()]
Greatest_day = Greatest_inc.reset_index()
# Greatest_day
gday_final = (Greatest_day.loc[0,'Date'])

gpro_final = locale.currency((Greatest_day.loc[0, 'Profit/Losses']), grouping = True)
# gpro_final
# gpro_final2 = gpro_final.'${:, .2f}'.format(gpro_final)
# locale.currency( 1234.50, grouping = True )


# In[212]:


# greatest decrease in profit
#  
Lowest_inc = Day_changdf[Day_changdf['Profit/Losses']==Day_changdf['Profit/Losses'].min()]
Lowest_inc = Lowest_inc.reset_index()
# reset index to make easier to parse
lday_final = (Lowest_inc.loc[0,'Date'])

glow_final = locale.currency((Lowest_inc.loc[0, 'Profit/Losses']), grouping = True)
# glow_final


# In[213]:


#Print to terminal 
#Total_months
#Total_net
#Ave_changdf
#Greatest_inc

#Lowest_inc.list()



# In[217]:


# Print to csv
# 





print ("Financial Analysis ")
print ("_______________________________________________")
print(f'Total Months: {Total_months}')
print(f'Total:  {Total_net}')
print (f'Average Change: {Ave_changdf}')
print(f'Greatest Increase in Profits: {gday_final}  {gpro_final}')
print(f'Greatest Decrease in Profits: {lday_final}  {glow_final}')


# print(summary_df)

#print ("Financial Analysis")
#print ("----------------------------------------")
#print (f'Total Months: {Total_months}')
#print (f'Total:  {Total_net}')
#print (f'Average Change:  {Ave_changdf}')
#print (f'Greatest Increase in Profits:  {Greatest_inc}')
#print (f'Greatest Decrease in Profits: {Lowest_inc}') summary_df = 
with open("Pybank.txt", "w") as text_file:
    print ("Financial Analysis ", file=text_file )
    print ("_______________________________________________", file=text_file)
    print(f'Total Months: {Total_months}', file=text_file)
    print(f'Total:  {Total_net}', file=text_file)
    print (f'Average Change: {Ave_changdf}', file=text_file)
    print(f'Greatest Increase in Profits: {gday_final}  {gpro_final}', file=text_file)
    print(f'Greatest Decrease in Profits: {lday_final}  {glow_final}', file = text_file)

# with open("Output.txt", "w") as text_file:
#    print(f"Purchase Amount: {TotalAmount}", file=text_file)

