import pandas as pd
import random

# Insert excel columns as per the exchanger excel file here
exchanger_name = 'Full Name in English (as on your Passport):'
exchanger_nEmail = 'NUS email address (exxxxxxx@u.nus.edu):'
exchanger_pEmail = 'Personal email address:'
exchanger_telehandle = 'Telegram Handle (do not include the @):'
exchanger_hCountry = 'Home Country:'
exchanger_hUniversity = 'Home University (in English):'
exchanger_major = 'Major of study (if any):'
exchanger_faculty = 'Faculty of study at NUS:'
exchanger_year = 'Year of study at home university (as of Aug 2024)'
exchanger_match_faculty = 'Would you want to be matched with a buddy from the same faculty?'
exchanger_interest = 'Share with us your interests! (Top 3)'
exchanger_gender = 'Gender:'
exchanger_match_gender = 'Would you want to be matched with a buddy of the same gender?'
exchanger_comment = '(Optional) If you have any other comments or preferences regarding the matching, please let us know below!'

# Insert excel columns as per the buddy excel file here
buddy_name = 'Full Name (as on your student card):'
buddy_nEmail = 'NUS email address (exxxxxxx@u.nus.edu):'
buddy_pEmail = 'Personal email address:'
buddy_telehandle = 'Telegram Handle (do not include the @):'
buddy_major = 'Major:'
buddy_year = 'Year and semester of study (as of AY24/25 Sem 1):'
buddy_faculty = 'Faculty:'
buddy_match_faculty = 'Would you like to be matched with exchangers from the same faculty?'
buddy_gender = 'Gender:'
buddy_match_gender = 'Would you like to be matched with exchanger of the same gender? (If applicable)'
buddy_interest = 'Share with us your interests! (Top 3)'
buddy_comment = '(Optional) If you have any other comments or preferences regarding the matching, please let us know below!'

# This code block is to encapsulate the information of an exchanger


class Exchanger:

    def __init__(self, name, nEmail, pEmail, telehandle, hCountry, hUniversity,
                 major, year, faculty, match_faculty,
                 gender, match_gender, interest, comment):
        self.name = name
        self.nEmail = nEmail
        self.pEmail = pEmail
        self.telehandle = telehandle
        self.hCountry = hCountry
        self.hUniversity = hUniversity
        self.major = major
        self.year = year
        self.faculty = faculty
        self.match_faculty = match_faculty
        self.interest = interest
        self.gender = gender
        self.match_gender = match_gender
        self.comment = comment

    # Adjust the scores accordingly to optimise the significance of each preference
    def matching_score(self, buddy):
        score = 0
        # This ensures that buddies that already have an exchanger are less likely to be matched again
        # Ensuring fairness in distribution of exchangers to buddies
        if buddy.has_exchanger():
            score -= 3

        # If either has a preference for gender, and it matches, add 1 to the score
        # Else we add 0.5 to the score, as it is easier to match with someone who does not have a preference
        if self.match_gender or buddy.match_gender:
            if self.gender == buddy.gender:
                score += 1
        else:
            score += 0.5

        # Same logic as above, but has a higher weightage of 5
        if self.match_faculty or buddy.match_faculty:
            matched = False
            for faculty in buddy.faculty:
                if faculty in self.faculty:
                    matched = True
                    break
            if matched:
                score += 5
            else:
                score -= 5
        else:
            score += 0.5

        # For eacb similar interests, add 1 to the score
        for interest in self.interest:
            if interest in buddy.interest:
                score += 1

        return score


# This code block is to encapsulate the information of a buddy
class Buddy:

    def __init__(self, name, nEmail, pEmail, tele, major, year, faculty, match_faculty,
                 gender, match_gender, interest, comment):
        self.name = name
        self.nEmail = nEmail
        self.pEmail = pEmail
        self.tele = tele
        self.major = major
        self.year = year
        self.faculty = faculty
        self.match_faculty = match_faculty
        self.gender = gender
        self.match_gender = match_gender
        self.interest = interest
        self.comment = comment
        self.odds = random.randint(0, 9)
        self.buddies = []

    # Check if the buddy has reached the limit of exchangers
    # Adjust the limit accordingly, 1 means buddy can have up to 2 exchangers
    # 2 means buddy can have up to 3 exchangers and so on
    def is_full(self):
        # Change the number below to adjust the odds up to 9.
        if self.odds < 8:
            # 80% of buddies have 2 or less exchanger
            return len(self.buddies) > 1
        else:
            # 20% of buddies have 3 exchanger
            return len(self.buddies) > 2

    def has_exchanger(self):
        return len(self.buddies) > 0

    def add_exchanger(self, exchanger):
        if self.is_full():
            return False
        self.buddies.append(exchanger)
        return True


matchings = []

# Ensure that the name of the CSV files are correct
exchangers_data = pd.read_csv("AY24_25 Sem1 Exchangers (1-789).csv")
buddies_data = pd.read_csv("AY24_25 Sem 1 NUS Buddies(1-606).csv")

exchangers = []
buddies = []

# Input the column names as per the CSV file
# For questions that allow multiple answers, split the answers by ';', ensure
# when creating the exchanger/buddy object, input as (answers[:-1]),
# where "answers" is the name of the variable of question that allows multiple answers
for _, data in exchangers_data.iterrows():
    name = data[exchanger_name]
    nEmail = data[exchanger_nEmail]
    pEmail = data[exchanger_pEmail]
    telehandle = data[exchanger_telehandle]
    hCountry = data[exchanger_hCountry]
    hUniversity = data[exchanger_hUniversity]
    major = data[exchanger_major]
    year = data[exchanger_year]
    faculty = data[exchanger_faculty].split(';')
    match_faculty = data[exchanger_match_faculty] == 'Yes'
    gender = data[exchanger_gender]
    match_gender = data[exchanger_match_gender]
    interest = data[exchanger_interest].split(';')
    comment = data[exchanger_comment]
    exchanger = Exchanger(name, nEmail, pEmail, telehandle, hCountry, hUniversity,
                          major, year, faculty[:-1], match_faculty, gender, match_gender, interest[:-1], comment)
    exchangers.append(exchanger)

# Same logic as above
for _, data in buddies_data.iterrows():
    name = data[buddy_name]
    nEmail = data[buddy_nEmail]
    pEmail = data[buddy_pEmail]
    telehandle = data[buddy_telehandle]
    major = data[buddy_major]
    year = data[buddy_year]
    faculty = data[buddy_faculty].split(';')
    match_faculty = data[buddy_match_faculty] == 'Yes'
    gender = data[buddy_gender]
    match_gender = data[buddy_match_gender]
    interest = data[buddy_interest].split(';')
    comment = data[buddy_comment]
    buddy = Buddy(name, nEmail, pEmail, telehandle, major, year, faculty[:-1], match_faculty,
                  gender, match_gender, interest[:-1], comment)
    buddies.append(buddy)

# Matching algorithm
# The alogrithm greedily assigns exchanger to buddies with the highest matching score
# Tldr: First come first serve
while exchangers and buddies:
    for exchanger in exchangers:
        scores = []
        for buddy in buddies:
            score = exchanger.matching_score(buddy)
            scores.append(score)

        best_score = max(scores)
        index = scores.index(best_score)
        best_buddy = buddies[index]

        if best_buddy.add_exchanger(exchanger):
            exchangers.remove(exchanger)
            buddies.remove(best_buddy)
            buddies.append(best_buddy)
        else:
            buddies.remove(best_buddy)
            matchings.append(best_buddy)

if buddies:
    for buddy in buddies:
        matchings.append(buddy)


# Export the matchings to a CSV file
# Name of each column in the resulting matchings.csv file
# Ensure that each column name is unique
matchings_data = pd.DataFrame(
    columns=[buddy_name,
             buddy_nEmail,
             buddy_pEmail,
             buddy_telehandle,
             buddy_major,
             buddy_year,
             buddy_faculty,
             buddy_match_faculty,
             buddy_gender,
             buddy_match_gender,
             buddy_interest,
             buddy_comment,
             exchanger_name,
             exchanger_nEmail,
             exchanger_pEmail,
             exchanger_telehandle,
             exchanger_hCountry,
             exchanger_hUniversity,
             exchanger_major,
             exchanger_faculty,
             exchanger_year,
             exchanger_match_faculty,
             exchanger_gender,
             exchanger_match_gender,
             exchanger_interest,
             exchanger_comment])

# Put the necessary information from the buddies and exchangers into the matchings_data
# Ensure that the column names are the same as the ones above
for buddy in matchings:
    for exchanger in buddy.buddies:
        matchings_data = matchings_data._append(
            {buddy_name: buddy.name,
             buddy_nEmail: buddy.nEmail,
             buddy_pEmail: buddy.pEmail,
             buddy_telehandle: buddy.tele,
             buddy_major: buddy.major,
             buddy_year: buddy.year,
             buddy_faculty: ';'.join(buddy.faculty),
             buddy_match_faculty: 'Yes' if buddy.match_faculty else 'No preference',
             buddy_gender: buddy.gender,
             buddy_match_gender: 'Yes' if buddy.match_gender else 'No preference',
             buddy_interest: ';'.join(buddy.interest),
             buddy_comment: buddy.comment,
             exchanger_name: exchanger.name,
             exchanger_nEmail: exchanger.nEmail,
             exchanger_pEmail: exchanger.pEmail,
             exchanger_telehandle: exchanger.telehandle,
             exchanger_hCountry: exchanger.hCountry,
             exchanger_hUniversity: exchanger.hUniversity,
             exchanger_major: exchanger.major,
             exchanger_faculty: ';'.join(exchanger.faculty),
             exchanger_year: exchanger.year,
             exchanger_match_faculty: 'Yes' if exchanger.match_faculty else 'No preference',
             exchanger_gender: exchanger.gender,
             exchanger_match_gender: 'Yes' if exchanger.match_gender else 'No preference',
             exchanger_interest: ';'.join(exchanger.interest),
             exchanger_comment: exchanger.comment},
            ignore_index=True)


matchings_data.to_csv('./matchings.csv', index=False)
