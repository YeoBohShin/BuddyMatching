Simple code to match NUS buddies with Exchangers

Before you can run the code, you will need to download an Integrated Development Environment(IDE), its basically an application that allows you to write and run code. A good IDE to download will be Visual Studio Code(VSCode), if you do not have VSCode, you can download it [here](https://code.visualstudio.com/download).

Ensure that you install the necessary coding language and libraries needed to run the code.

First, ensure that python3 is installed on your computer. If you do not have python3, download it from [here](https://www.python.org/downloads/).

Open up VSCode and open the Matching.py file.

If you do not have the _pandas_ library, run the command **pip install pandas** in the terminal.

Now that the set-up is done, we can proceed to run the code.

Ensure that both, exchanger and buddies, excel files are stored in the same directory as this code file.
Ensure that both, exchanger and buddies, excel files are saved as .csv format for the code to work.

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
