import pandas as pd
import random

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
    name = data['Full Name in English (as on your Passport):']
    nEmail = data['NUS email address (exxxxxxx@u.nus.edu):']
    pEmail = data['Personal email address:']
    telehandle = data['Telegram Handle (do not include the @):']
    hCountry = data['Home Country:']
    hUniversity = data['Home University (in English):']
    major = data['Major of study (if any):']
    faculty = data['Faculty of study at NUS:'].split(';')
    year = data['Year of study at home university (as of Aug 2024)']
    match_faculty = data['Would you want to be matched with a buddy from the same faculty?'] == 'Yes'
    interest = data['Share with us your interests! (Top 3)'].split(';')
    gender = data['Gender:']
    match_gender = data['Would you want to be matched with a buddy of the same gender?'] == 'Yes'
    comment = data['(Optional) If you have any other comments or preferences regarding the matching, please let us know below!']
    exchanger = Exchanger(name, nEmail, pEmail, telehandle, hCountry, hUniversity,
                          major, year, faculty[:-1], match_faculty, gender, match_gender, interest[:-1], comment)
    exchangers.append(exchanger)

# Same logic as above
for _, data in buddies_data.iterrows():
    name = data['Full Name (as on your student card):']
    nEmail = data['NUS email address (exxxxxxx@u.nus.edu):']
    pEmail = data['Personal email address:']
    telehandle = data['Telegram Handle (do not include the @):']
    major = data['Major:']
    year = data['Year and semester of study (as of AY24/25 Sem 1):']
    faculty = data['Faculty:'].split(';')
    match_faculty = data['Would you like to be matched with exchangers from the same faculty?'] == 'Yes'
    gender = data['Gender:']
    match_gender = data[
        'Would you like to be matched with exchanger of the same gender? (If applicable)'] == 'Yes'
    interest = data['Share with us your interests! (Top 3)'].split(';')
    comment = data['(Optional) If you have any other comments or preferences regarding the matching, please let us know below!']
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
    columns=['Full Name (as on your student card):',
             'NUS email address(exxxxxxx@u.nus.edu): ',
             'Personal email address:',
             'Telegram Handle(do not include the @):',
             'Major:',
             'Year of study(as of AY23 / 24):',
             'Faculty:',
             'Would you prefer to be matched with exchanger from the same faculty?',
             'I am a:',
             'Would you prefer to be matched with exchanger from the same gender? (If applicable)',
             'Please share with us your interests. (Top 3!)',
             '(Optional) If you have any other comments or preferences regarding the matching, please let us know below!',
             'Full Name in English (as on your Passport):',
             'NUS email address:',
             'Personal email addres:',
             'Telegram Handle:',
             'Home Country:',
             'Home University (in English):',
             'Major of study (if any):',
             'Faculty of study at NUS:',
             'Year of study at home university (as of Aug 2023)',
             'Would you want to be matched with a buddy from the same faculty?',
             'I am:',
             'Would you want to be matched with a buddy of the same gender? ',
             'Please share with us your interests (Top 3!)',
             '(Optional) If you have any other comment or preferences regarding the matching, please let us know below!'])

# Put the necessary information from the buddies and exchangers into the matchings_data
# Ensure that the column names are the same as the ones above
for buddy in matchings:
    for exchanger in buddy.buddies:
        matchings_data = matchings_data._append(
            {'Full Name (as on your student card):': buddy.name,
             'NUS email address(exxxxxxx@u.nus.edu): ': buddy.nEmail,
             'Personal email address:': buddy.pEmail,
             'Telegram Handle(do not include the @):': buddy.tele,
             'Major:': buddy.major,
             'Year of study(as of AY23 / 24):': buddy.year,
                'Faculty:': ';'.join(buddy.faculty),
                'Would you prefer to be matched with exchanger from the same faculty?': 'Yes' if buddy.match_faculty else 'No preference',
                'I am a:': buddy.gender,
                'Would you prefer to be matched with exchanger from the same gender? (If applicable)': 'Yes' if buddy.match_gender else 'No preference',
                'Please share with us your interests. (Top 3!)': ';'.join(buddy.interest),
                '(Optional) If you have any other comments or preferences regarding the matching, please let us know below!': buddy.comment,
                'Full Name in English (as on your Passport):': exchanger.name,
                'NUS email address:': exchanger.nEmail,
                'Personal email addres:': exchanger.pEmail,
                'Telegram Handle:': exchanger.telehandle,
                'Home Country:': exchanger.hCountry,
                'Home University (in English):': exchanger.hUniversity,
                'Major of study (if any):': exchanger.major,
                'Faculty of study at NUS:': ';'.join(exchanger.faculty),
                'Year of study at home university (as of Aug 2023)': exchanger.year,
                'Would you want to be matched with a buddy from the same faculty?': 'Yes' if exchanger.match_faculty else 'No preference',
                'I am:': exchanger.gender,
                'Would you want to be matched with a buddy of the same gender? ': 'Yes' if exchanger.match_gender else 'No preference',
                'Please share with us your interests (Top 3!)': ';'.join(exchanger.interest),
             '(Optional) If you have any other comment or preferences regarding the matching, please let us know below!': exchanger.comment},
            ignore_index=True)


matchings_data.to_csv('./matchings.csv', index=False)
