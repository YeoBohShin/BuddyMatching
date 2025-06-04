Simple code to match NUS buddies with Exchangers

### Set-up

Download the Matcher from the releases. Ensure that you download the correct Matcher for your specific computer, look at the tag for the respective Operating system.

** Note: **

1. Ensure that both exchanger and buddies, excel files are stored in the same directory as the Matcher.

2. Ensure that both, exchanger and buddies, excel files are saved as .csv format for the Matcher to work.

Before trying to match, it is advise to perform preprocessing on the excel for optimal results.

Some possible data pre-processing:

1. Remove duplicate buddies/exchangers

2. Sort those with the preference of same gender or same faculty to appear first in the excel file. The one
   with the higher weightage should be sorted last.

   Eg. if faculty is more important than gender, sort gender first then faculty.

   Result of this should list exchangers in the following order:

   faculty yes gender yes

   faculty yes gender no

   faculty no gender yes

   faculty no gender no

The Matcher will open in a new window. (Might take a while to open)

This section only applies if you have downloaded the application from GitHub

Note for MacOS users, you must navigate into the package to run the Matcher.

1.  Left click and show package content
2.  Go to Contents and then MacOS
3.  Run the executable

### Application

The Matcher matches exchangers to buddies based on a greedy algorithm. The algorithm works by comparing an exchanger's preferences and interest with every buddy available. The buddy with the most matched preferences and interests is matched with the exchanger. The algorithm ensures that every exchanger will have a buddy. However, buddies are not guaranteed to have an exchanger matched to them.

**Note that the algorithm does not account for any additional comments provided by exchangers/buddies, thus manual swapping is still required. **

Once the application is open, there are 7 sections to fill up.

1. Matching Points
   This portion is to input the weightages of each label.

   Values inputed represents how many points is given for every matched label between an exchanger and a buddy

Input a value between xx and xx for each label. The higher the value, the more weightage the label has (i.e., the more important it is)

2. Matching Preferences
   This portion is to input the distribution of exchangers among buddies.

   1. Max Number of Exchanger per Buddy: How many exchangers a buddy can have at most at 1 time.

   2. Percentage of Buddies with Max Exchangers: Input a value between 0 and 100 to signify the proportion

      of buddies that are matched with the value inputed in the previous field. A higher percentage means more buddies are matched with max number of exchangers, meaning there will be lesser buddies assigned overall.

3. Input the Name of Files Below
   This portion is to input the names of the Excel files.

   Ensure that the format of the file is written in the name of the file. E.g If the file is saved as a csv file, include the “.csv” at the back of the file name.

   1. Exchanger Excel File Name: Name of the Excel file containing information of the exchangers
   2. Buddy Excel File Name: Name of the Excel file containing information of the buddies
   3. Matching Output Excel File Name: Name of the File that will be outputed if matching is successful

4. Input the Name of Columns from the Exchanger Excel File that You want in the Output File Below
   This portion is to input the names of the columns of the excel into the output file.

   For example, if you want the name of the exchanger to appear in the output excel file, input the name of the column that has the name of the exchangers in the exchanger excel file.

5. Input the Name of Corresponding Compulsory Columns from Exchangers Excel File Below
   This portion is to input the compulsory fields needed for the algorithm.

   Copy over the respective name of the columns containing the value of each label.

6. Input the Name of Columns from the Buddy Excel File that You Want in the Output File Below
   Similar to point 4 but for the buddies excel file.

7. Input the Name of Corresponding Compulsory Columns from Buddies Excel File Below
   Similar to point 5 but for the buddies excel file.

Running the code will generate the matched excel file into the same directory as the matcher application.

Ensure that the matched excel file is closed before running the code if you want to generate new matchings.

If there are any questions, contact me on Telegram at @bohshin.
