# Final Project -- UFC Match Outcome Predictor

## Overview

UFC enthusiasts typically use bets and odds to favour who will win a fight. We thought it would be interesting to use data, i.e. fighter statistics and metrics, to create an educated prediction on who will win the fight. 

We will be analyzing data with various machine learning algorithms to predict fight outcomes in the largest mixed martial arts organization in the world, the UFC.

### Questions we hope to answer with data:

**1. What are the top 5 fighter metrics that contribute to winning a UFC match?**

**2. Which of the fighter metrics carry more weight than the others?**

**3. How much do biometric physical factors, i.e. age, height, weight, affect the outcome of the match?**

**4. Does having a higher rank predict the outcome?**

**5. Do the number of win streaks necessarily predict a higher chance of winning?**

![image_1](https://github.com/agregorash/final_project/blob/priis/x/seg2/image_1.png)

## Project Details

#### Data Exploration Phase

* Differences in the average accuracy of takedowns taking place between fighters were calculated by using the following function: “Blue corner score minus (-) Red corner score” where a negative score actually favors the Red corner fighter.

* Exploring historical data of past matchups in the UFC for past multiple years, it was found that the great majority of the time, the fighter in the red corner has a slightly greater chance as the victor in a match-up.

#### Analysis Phase (Andrew to populate below)

* Description of preliminary data preprocessing
* Description of preliminary feature engineering and preliminary feature selection, including their decision- making process
* Description of how data was split into training and testing sets
* Explanation of model choice, including limitations and benefits

Using the [resources-master.csv](https://github.com/agregorash/final_project/blob/main/Resources/ufc-master.csv) file, we first wanted to create a baseline classification model [Simple_Model.ipynb](https://github.com/agregorash/final_project/blob/main/ML/Simple_Model.ipynb) in order to establish a benchmark of how well a winner could be predicted without data preprocessing and feature engineering.  Using the Dummy Classifier, which allows us to run the model with null values, the model predicted winners with 51.75% accuracy.

We then set out to create a model that would perform better than our baseline model, by first preprocessing the data and implementing feature engineering- [data_preprocessing.ipynb](https://github.com/agregorash/final_project/blob/main/ML/data_preprocessing.ipynb).  In this dataset we were dealing with 137 variables many of which contained a significant amount of null values.  In order to ensure key variables were not eliminated, we first encoded the winning column and ran a correlation function in pandas to see which variables most correlated to winners.  After that, we recognized that the majority of our variables were duplicates in a sense- statistics for the Red Corner fighter, and statistics for the Blue Corner figher.  To incresase correlation and concentrate the data, we subtracted all Red Corner statistics from Blue Corner statistics (Blue-Red) and created 'difference' variables.  Then we dropped all variables that were common to both fighters in that fight; such as date, location, weight class, ect.  Looking at the data further we recognized there was a large chunk of variables associated to rankings in a given weight class that contained a significant amount of null values.  After further analysis only one of these rankings columns was pertinent and all the others were dropped.  Then columns with strings were encoded, and false NaN columns were filled with their true value of 0.

For our improved model we decided to compare the results between a Random Forest classifier and a Deep Neural Network[ufc_RF_vs_NN.ipynb](https://github.com/agregorash/final_project/blob/main/ML/ufc_RF_vs_NN.ipynb), because we were looking to classify winners with a very large dataset.  We tinkered with different train/test splits but results were best with a standard 25% test split.  The RF Classifier resulted in 78% accuracy while the Deep NN resulted in 76% accuracy.  It does not seem that either model was overfit, and they were able to predict winners of the fights with over 75% accuracy.  

![image_2](https://github.com/agregorash/final_project/blob/priis/x/seg2/image_2.png)

## Resources

Through a Kaggle search we identified a robust dataset containing 137 variables pertaining to 4,566 fight records dating from 3/21/2010- 2/6/2021. 

**- Data Sources:** [most-recent-event.csv](https://github.com/agregorash/final_project/blob/main/Resources/most-recent-event.csv), [resources-master.csv](https://github.com/agregorash/final_project/blob/main/Resources/ufc-master.csv), [upcoming-event.csv](https://github.com/agregorash/final_project/blob/main/Resources/upcoming-event.csv)

**- Technologies Used:**
- **Data Cleaning and Analysis:** Python and Pandas used for data scrubbing and for performing exploratory data analysis
- **Database Storage:** PgAdmin to manage PostgresSQL and will integrate D3, HTML & JSS to display the data
- **Machine Learning:** Numpy and Pandas data wrangling libraries along with Seaborn & Scikit-Learn/ our training and testing setup is train test split sklearn.
- **Dashboard:** Tableau, Google Slides, Python and Pandas, Seaborn, MatPlotLib

## Team Communication Protocols

Team has established a communication line through a team slack channel.  Group meetings will occur through zoom weekly, one hour before TA office hours ( 06:00PM Friday, 11:00AM Saturday & Sunday), in addition to designated class hours on Tuesday and Thursday.
When making commits to the main branch team members are responsible for communicating with the team through the slack channel what they are commiting and whether there are any connections being made to established working code.  If there are connections being made to existing code, the team member attempting to add code is responsible for reaching another team member to double check work, preferably the team member who had added the established code, to ensure there are no conflicts.

#### Roles & Expectations

Roles have been randomly assigned and are listed below:

![image (2)](https://github.com/agregorash/final_project/blob/main/Guidelines/image%20(2).png)

Each member is expected to complete their assigned work at the 'Mastery' standard for each section of the project, outlined in the rubric and found in the [Guidelines](https://github.com/agregorash/final_project/blob/main/Guidelines/Module%2B20%2B-Full%2BRubric_Final%2BProject.pdf) folder of this repository.

Once a member has finished their work for each section they are expected to reach out to the other team members and offer to help, as workloads will vary section to section, ensuring that everyone is contributing equally.


