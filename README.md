Simple code to match NUS buddies with Exchangers

Ensure that you install the necessary coding language and libraries needed to run the code.

First, ensure that python3 is installed on your computer. If you do not have python3, download it from [here](https://www.python.org/downloads/)

Once python3 is downloaded, use the command _pip install pandas_.

Ensure that both excel files are stored in the same directory as this code file.
Ensure that both excel files are save in the .csv format for the code to work.

Before running the code, ensure that data pre-processing is done for optimal results.

Some possible data pre-processing:

1. Remove duplicate buddies/exchangers
2. Sort those with the preference of same gender or same faculty to appear first in the excel file. The one with the higher weightage should be sorted last.
   (Eg. if faculty is more important than gender, sort gender first then faculty.)

Running the code will generate the matching excel file into the same directory as the code file.

Ensure that the matching excel file is closed before running the code if you want to generate new matchings.

The code ensures that every exchanger will have a buddy. Buddies are not guaranteed to have an exchanger matched to them.

Note that the algorithm does not account for any additional comments provided by exchangers/buddies, thus manual swapping is still required.

If there are any questions, contact me on Telegram at @bohshin.
