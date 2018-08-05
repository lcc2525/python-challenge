
# coding: utf-8

# In[223]:


#import dependencies
import pandas as pd
import numpy as np


# In[224]:


#Import csv %%file
election_csv = "C:/users/lcc25/repos/utexas_hmwk_python/election_data.csv"
election_df = pd.read_csv(election_csv)

election_df.head()
# election_df.count()
relection_df = election_df.dropna(axis= 0)


# In[225]:


#Clean up date null votes or null candidates


# In[226]:


# Compile list candidates that recieved votes
Cand_votedf = relection_df.groupby(["Candidate"]).count().reset_index()
Cand_votedf = Cand_votedf.loc[:, 'Candidate':'Voter ID'].rename(columns={'Voter ID': 'Votes'})

#Total all votes 
Sum_ofVotesdf = Cand_votedf['Votes'].sum()
# Create table with percentage added

def cal_per(row):
    return '{:.3%}'.format((row['Votes'] / Sum_ofVotesdf) * 1)


Cand_votedf.apply(cal_per, axis=1)


# In[227]:


# Total number Votes for each candidate

Cand_votedf['% of votes'] = Cand_votedf.apply(cal_per, axis=1)
result_df = Cand_votedf.sort_values('Votes', ascending=False)
winner_df = result_df.iloc[0,0]
result_df
#new_look = Cand_votedf.sort_values('% of votes', ascending = False)
# result_df.reset_index()
# result_df.set_index('Candidate', inplace=True)
#new_look.sort(columns='Votes', axis=1, ascending=False)
#new_look.columns = new_look.iloc[0]
#new_look = new_look[0:]
#new_look
#(loc.new_look[1].to_string(index=False))
# Sum_ofVotes
#Sum_ofVotesdf['Percentage'] = (['Votes'] \ Sum_ofVotesdf)


# In[228]:


head_less = result_df.rename(columns=result_df.iloc[0]).drop(result_df.index[0])
#head_less
head_less = head_less.rename_axis(None)
head_less


# In[229]:


# percentage each candidate recieved

print ("Election Results ")
print ("_______________________________________________")
print(f'Total Votes: {Sum_ofVotesdf}')
print("_______________________________________________")
print(head_less.to_string(index=False, justify='right'))

print("_______________________________________________")
print(f'Winner:  {winner_df}')
print("_______________________________________________")


# In[238]:


with open("Election.txt", "w") as text_file:
    print ("Election Results ", file=text_file )
    print ("_______________________________________________", file=text_file)
    
    print(f'Total Votes: {Sum_ofVotesdf}', file=text_file)
    print("_______________________________________________", file=text_file)
    print(head_less.to_string(index=False, justify='right'), file=text_file)

    print("_______________________________________________", file=text_file)
    print(f'Winner:  {winner_df}', file=text_file)
    print("_______________________________________________", file=text_file)

