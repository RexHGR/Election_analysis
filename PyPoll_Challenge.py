# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""


import csv
import os


file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")


total_votes = 0
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0


winning_county = ""
winning_county_count = 0


with open(file_to_load, 'r') as election_data:

    
    file_reader = csv.reader(election_data)

    
    headers = next(file_reader)

    
    for row in file_reader:
        total_votes += 1
        
        
        candidate_name = row[2]
        
       
        if candidate_name not in candidate_options:
            
            
            candidate_options.append(candidate_name)
            
            
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        
        county_name = row[1]

        if county_name not in county_options:

            county_options.append(county_name) 

            county_votes[county_name] = 0
        county_votes[county_name] += 1


with open(file_to_save, 'w') as election_analysis_file:

    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")

    print(election_results, end="")   
    
    election_analysis_file.write(election_results)

    
 
    for county_name in county_votes:
        
        
        votes_1 = county_votes[county_name]

       
        vote_percentage_1 = float(votes_1) / float(total_votes) * 100

       
        county_results = (f"{county_name}: {vote_percentage_1:.1f}% ({votes_1:,})\n")
        print(county_results)
        election_analysis_file.write(county_results)

        
        if (votes_1 > winning_county_count):

           
            winning_county_count = votes_1
            winning_county = county_name
    
    
    winning_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    election_analysis_file.write(winning_county_summary)

   
    for candidate_name in candidate_votes:
        
        
        votes_2 = candidate_votes[candidate_name]
    
        vote_percentage_2 = float(votes_2) / float(total_votes) * 100


        candidate_results = (f"{candidate_name}: {vote_percentage_2:.1f}% ({votes_2:,})\n")
        print(candidate_results)
        election_analysis_file.write(candidate_results)

        
        if (votes_2 > winning_count) and (vote_percentage_2 > winning_percentage):
            
        
            winning_count = votes_2
            winning_percentage = vote_percentage_2
            winning_candidate = candidate_name


    winning_candidate_summary = ( 
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    election_analysis_file.write(winning_candidate_summary)