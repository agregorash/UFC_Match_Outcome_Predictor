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

## Project Details

#### Data Exploration Phase

Differences in the average accuracy of takedowns taking place between fighters were calculated by using the following function: “Blue corner score minus (-) Red corner score” where a negative score actually favors the Red corner fighter.

Exploring historical data of past matchups in the UFC for past multiple years, it was found that the great majority of the time, the fighter in the red corner has a slightly greater chance as the victor in a match-up

#### Analysis Phase 


### Resources

Through a Kaggle search we identified a robust dataset containing 137 variables pertaining to 4,566 fight records dating from 3/21/2010- 2/6/2021. 

**- Data Sources** [most-recent-event.csv](https://github.com/agregorash/final_project/blob/main/Resources/most-recent-event.csv), [resources-master.csv](https://github.com/agregorash/final_project/blob/main/Resources/ufc-master.csv), [upcoming-event.csv](https://github.com/agregorash/final_project/blob/main/Resources/upcoming-event.csv)

**- Technologies Used**
- **Data Cleaning and Analysis:** Python and Pandas used for data scrubbing and for performing exploratory data analysis
- **Database Storage:** PgAdmin to manage PostgresSQL and will integrate D3, HTML & JSS to display the data
- **Machine Learning:** Numpy and Pandas data wrangling libraries along with Seaborn & Scikit-Learn/ our training and testing setup is train test split sklearn.
- **Dashboard:** Tableau, Google Slides, Python and Pandas, Seaborn, MatPlotLib

### Communication Protocols

Team has established a communication line through a team slack channel.  Group meetings will occur through zoom weekly, one hour before TA office hours ( 06:00PM Friday, 11:00AM Saturday & Sunday), in addition to designated class hours on Tuesday and Thursday.
When making commits to the main branch team members are responsible for communicating with the team through the slack channel what they are commiting and whether there are any connections being made to established working code.  If there are connections being made to existing code, the team member attempting to add code is responsible for reaching another team member to double check work, preferably the team member who had added the established code, to ensure there are no conflicts.

#### Roles & Expectations

Roles have been randomly assigned and are listed below:

![image (2)](https://github.com/agregorash/final_project/blob/main/Guidelines/image%20(2).png)

Each member is expected to complete their assigned work at the 'Mastery' standard for each section of the project, outlined in the rubric and found in the [Guidelines](https://github.com/agregorash/final_project/blob/main/Guidelines/Module%2B20%2B-Project%2BRubrics%2B-%2BSegment%2B1.pdf) folder of this repository.

Once a member has finished their work for each section they are expected to reach out to the other team members and offer to help, as workloads will vary section to section, ensuring that everyone is contributing equally.


