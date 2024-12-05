import pandas as pd
import random
import math


class Matcher:

    def __init__(self, file_names, exchanger_data, exchanger_preference, buddy_data, buddy_preference, matching_preference):
        self.file_names = file_names
        self.exchanger_data = exchanger_data
        self.buddy_data = buddy_data
        self.exchanger_preference = exchanger_preference
        self.buddy_preference = buddy_preference
        self.matching_preference = matching_preference
        if (len(self.exchanger_preference) < 5):
            raise Exception(
                "Please fill up compulsory fields for exchanger preference")
        if (len(self.buddy_preference) < 5):
            raise Exception(
                "Please fill up compulsory fields for buddy preference")

    class Exchanger:

        def __init__(self, info, gender, match_gender, faculty, match_faculty, interest):
            self.info = info
            self.gender = gender
            self.match_gender = match_gender
            self.faculty = faculty
            self.match_faculty = match_faculty
            self.interest = interest

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

        def __init__(self, info, gender, match_gender, faculty, match_faculty, interest, matching_preference):
            self.info = info
            self.faculty = faculty
            self.match_faculty = match_faculty
            self.gender = gender
            self.match_gender = match_gender
            self.interest = interest
            self.odds = random.randint(0, 9)
            self.exchangers = []
            self.max_num_of_exchangers_per_buddy = matching_preference[0]
            self.percentage_of_buddies_with_max_exchangers = math.ceil(
                matching_preference[1] / 10)

        # Check if the buddy has reached the limit of exchangers
        def is_full(self):
            if self.odds < 10 - self.percentage_of_buddies_with_max_exchangers:
                if self.max_num_of_exchangers_per_buddy == 1:
                    return len(self.exchangers) > 0
                elif self.max_num_of_exchangers_per_buddy == 2:
                    return len(self.exchangers) > 1
                else:
                    return len(self.exchangers) > self.max_num_of_exchangers_per_buddy - 2
            else:
                return len(self.exchangers) > self.max_num_of_exchangers_per_buddy - 1

        def has_exchanger(self):
            return len(self.exchangers) > 0

        def add_exchanger(self, exchanger):
            if self.is_full():
                return False
            self.exchangers.append(exchanger)
            return True

    def match(self):
        matchings = []

        # Ensure that the name of the CSV files are correct
        exchangers_data = pd.read_csv(self.file_names[0])
        buddies_data = pd.read_csv(self.file_names[1])

        exchangers = []
        buddies = []

        # Input the column names as per the CSV file
        # For questions that allow multiple answers, split the answers by ';', ensure
        # when creating the exchanger/buddy object, input as (answers[:-1]),
        # where "answers" is the name of the variable of question that allows multiple answers
        for _, data in exchangers_data.iterrows():
            info = []
            exchanger_faculty, exchanger_match_faculty, exchanger_gender, exchanger_match_gender, exchanger_interest = self.exchanger_preference
            try:
                faculty = data[exchanger_faculty].split(';')
                match_faculty = data[exchanger_match_faculty] == 'Yes'
                gender = data[exchanger_gender]
                match_gender = data[exchanger_match_gender] == 'Yes'
                interest = data[exchanger_interest].split(';')
                for col in self.exchanger_data:
                    info.append(data[col])
            except:
                raise Exception(
                    "Please ensure that the column names for the exchanger data are correct")

            exchanger = self.Exchanger(info, gender, match_gender,
                                       faculty[:-1], match_faculty, interest[:-1])
            exchangers.append(exchanger)

        # Same logic as above
        for _, data in buddies_data.iterrows():
            info = []
            buddy_faculty, buddy_match_faculty, buddy_gender, buddy_match_gender, buddy_interest = self.buddy_preference
            try:
                faculty = data[buddy_faculty].split(';')
                match_faculty = data[buddy_match_faculty] == 'Yes'
                gender = data[buddy_gender]
                match_gender = data[buddy_match_gender]
                interest = data[buddy_interest].split(';')
                for col in self.buddy_data:
                    info.append(data[col])
            except:
                raise Exception(
                    "Please ensure that the column names for the buddy data are correct")
            buddy = self.Buddy(info, gender, match_gender,
                               faculty[:-1], match_faculty, interest[:-1], self.matching_preference)
            buddies.append(buddy)

        # Check if there are enough buddies for the exchangers
        if len(exchangers) > len(buddies) * self.matching_preference[0]:
            print("There are not enough buddies for the exchangers\n")
            print("Number of exchangers: ", len(exchangers))
            print("Number of buddies: ", len(buddies))
            print("Number of exchangers per buddy: ",
                  self.matching_preference[0])
            print("Ensure that the number of buddy * number of exchangers per buddy is greater than the number of exchangers")
            raise Exception("There are not enough buddies for the exchangers")

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

        for i in range(len(self.exchanger_data)):
            self.exchanger_data[i] += ' '

        # # Put the necessary information from the buddies and exchangers into the matchings_data
        # # Ensure that the column names are the same as the ones above

        results = []

        # Iterate through matchings to populate the rows list
        for buddy in matchings:
            for exchanger in buddy.exchangers:
                result = {self.buddy_data[i]: buddy.info[i]
                          for i in range(len(self.buddy_data))}
                result.update({buddy_faculty: ';'.join(buddy.faculty),
                               buddy_match_faculty: 'Yes' if buddy.match_faculty else 'No preference',
                               buddy_gender: buddy.gender,
                               buddy_match_gender: 'Yes' if buddy.match_gender else 'No preference',
                               buddy_interest: ';'.join(buddy.interest)})
                result.update({self.exchanger_data[i]: exchanger.info[i]
                               for i in range(len(self.exchanger_data))})

                result.update({
                    exchanger_faculty + ' ': ';'.join(exchanger.faculty),
                    exchanger_match_faculty + ' ': 'Yes' if exchanger.match_faculty else 'No preference',
                    exchanger_gender + ' ': exchanger.gender,
                    exchanger_match_gender + ' ': 'Yes' if exchanger.match_gender else 'No preference',
                    exchanger_interest + ' ': ';'.join(exchanger.interest),
                })

                # Append the row to the list
                results.append(result)

        # Create the DataFrame from the results list
        matchings_data = pd.DataFrame(results, columns=self.buddy_data + [
            buddy_faculty, buddy_match_faculty,
            buddy_gender, buddy_match_gender, buddy_interest
        ] + self.exchanger_data + [
            exchanger_gender + ' ',
            exchanger_match_gender + ' ',
            exchanger_faculty + ' ',
            exchanger_match_faculty + ' ',
            exchanger_interest + ' '
        ])

        for i in range(len(self.exchanger_data)):
            self.exchanger_data[i] = self.exchanger_data[i][:-1]

        matchings_data.to_csv(self.file_names[2], index=False)
