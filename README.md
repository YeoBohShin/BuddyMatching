Simple code to match NUS buddies with Exchangers

Download the Matcher from the releases. Ensure that you download the correct Matcher for your specific computer, look at the tag for the respective Operating system.

Before trying to match, it is advise to perform preprocessing on the excel for optimal results.
Some possible data pre-processing:

1. Remove duplicate buddies/exchangers
2. Sort those with the preference of same gender or same faculty to appear first in the excel file. The one with the higher weightage should be sorted last.
   (Eg. if faculty is more important than gender, sort gender first then faculty.)

Opening the Matcher will open a new window, which will be the matcher.

Note for MacOS users, to open the matcher normally, you first have to navigate into the package.

1. Left click and show package content
2. Go to Contents then MacOS
3. Run the executable

You should see that a data.txt file is create, from there you can open the matcher normally.

Input the necessary data as needed.

Before clicking on Match:

1. Ensure that both, exchanger and buddies, excel files are stored in the same directory as the matcher file
2. Ensure that both, exchanger and buddies, excel files are saved as .csv format for the matcher to work.

Running the code will generate the matched excel file into the same directory as the matcher file.

Ensure that the matching excel file is closed before running the code if you want to generate new matchings.

The code ensures that every exchanger will have a buddy. Buddies are not guaranteed to have an exchanger matched to them.

Note that the algorithm does not account for any additional comments provided by exchangers/buddies, thus manual swapping is still required.

If there are any questions, contact me on Telegram at @bohshin.
