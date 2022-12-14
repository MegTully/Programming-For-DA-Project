# Programming-For-DA-Project
by Megan Tully

This repository contains five files, a .gitignore file to stop unnecessary files being uploaded, a folder called pictures which contains the image used in the project, the main file which is a jupyter notebook called Programming_For_DA_Project, a csv file that contains the dataset downloaded and used in the main file called games_sales_data and lastly this README file with some information on the repository.

This repository was created for my project in Programming For Data Analysis. The aim of the project was to choose a  real-world phenomenon and find some data based on this phenomenon, investigate the data and then synthesise your own new dataset using the data you collected. With the key focus being researching and synthesising your data.


# Programming-For-DA-Project Jupyter Notebook File

## How to run this file (.ipynb)

1. Download both the dataset and the main jupyter notebook file from this repository to your local machine.
2. Open up your command line, I used CMDer which can be found [here](https://cmder.app/).
3. Navigate to the folder where you downloaded the above files.
4. Type "jupyter notebook" into the terminal and it should open up jupyter notebook in your browser with these files in it.

<b>Note</b>: You need to have jupyter notebook installed on your machine. I have [Anaconda](https://www.anaconda.com/) downloaded which contains jupyter notebook. You also need a recent version of [Python](https://www.python.org/downloads/) on your local machine.

You can also use [Visual Studio](https://code.visualstudio.com/download) code to run this file by opening the folder containing the downloaded files inside the application.

### Required Packages (linked to user guides):
1. [pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) 
2. [matplotlib](https://matplotlib.org/stable/users/index.html)
3. [seaborn](https://seaborn.pydata.org/tutorial.html)
4. [numpy](https://numpy.org/doc/stable/user/)
5. [fitter](https://fitter.readthedocs.io/en/latest/)
6. [scipy](https://docs.scipy.org/doc/scipy/tutorial/index.html)

## Project Summary

I decided to base this project on video games so I used a dataset with information on video game sales, user scores and critic scores throughout the years. I analysed the dataset by looking at all the statistics and the relationships between the variables which gave a great insight into how video games have progressed throughout the years. I then researched and tried to implement a few methods to sythesise a new dataset using the dataset I already had. The method I went with in the end was using numpy and scipy libraries to generate random numbers for each column using according to the distribution that was observed for their corresponding columns in the original dataset found online. I created a new dataframe with all the synthesised columns as a new dataset.   