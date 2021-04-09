# Final Project -- UFC Match Outcome Predictor

## Overview

Gambling and "The Fight Game" have always gone hand in hand.  There are countless analysts that make a living off of predicting fight outcomes based on the eye test or on data that has no proven correlation to actual wins. Even worse, the casual fan is typically basing their predictions on the most basic statistics provided by the broadcast during the "tale of the tape" introduction, i.e. heights, weight, record, rank, ect.

![tale_of_tape.jpg](https://github.com/agregorash/final_project/blob/main/Resources/tale_of_tape.jpg)

So where is the real edge? 

With the power of data this analysis will uncover the top variables correlated to wins in the largest mixed martial arts organization in the world, the UFC.  In addition, using supervised machine learning this analysis will classify winners with an accuracy of at least 75%.

DISCLAIMER: This analysis was formed for educational purposes and should not be used for gambling or financial gain.

### Questions we hope to answer with data:

**1. What are the top 5 fighter metrics that contribute to winning a UFC match?**

**2. Which of the fighter metrics carry more weight than the others?**

**3. How much do biometric physical factors, i.e. age, height, weight, affect the outcome of the match?**

**4. Does having a higher rank predict the outcome?**

**5. Do the number of win streaks necessarily predict a higher chance of winning?**

![image_1](https://github.com/agregorash/final_project/blob/priis/x/seg2/image_1.png)

## Resources

Through a Kaggle search we identified a robust dataset containing 137 variables pertaining to 4,566 fight records dating from 3/21/2010- 2/6/2021. 

**- Data Sources:** [most-recent-event.csv](https://github.com/agregorash/final_project/blob/main/Resources/most-recent-event.csv), [resources-master.csv](https://github.com/agregorash/final_project/blob/main/Resources/ufc-master.csv), [upcoming-event.csv](https://github.com/agregorash/final_project/blob/main/Resources/upcoming-event.csv)

**- Technologies Used:**
- **Data Cleaning and Analysis:** Python and Pandas used for data scrubbing and for performing exploratory data analysis
- **Database Storage:** PgAdmin to manage PostgresSQL and will integrate D3, HTML & JSS to display the data
- **Machine Learning:** Numpy and Pandas data wrangling libraries along with Seaborn & Scikit-Learn/ our training and testing setup is train test split sklearn.
- **Dashboard:** Tableau, Google Slides, Python and Pandas, Seaborn, MatPlotLib

## Project Details

#### Data Exploration Phase

* Differences in all statistics for each fight were calculated using the following function: “Blue corner score minus (-) Red corner score” where a negative score actually favors the Red corner fighter.  These calculations were done in order to concentrate the variables and increase their correlation to wins.

* Exploring historical data of past matchups in the UFC for past multiple years, it was found that the great majority of the time, the fighter in the red corner has a slightly greater chance as the victor in a match-up.

#### Machine Learning

* Description of preliminary data preprocessing
* Description of preliminary feature engineering and preliminary feature selection, including their decision- making process
* Description of how data was split into training and testing sets
* Explanation of model choice, including limitations and benefits

Using the [resources-master.csv](https://github.com/agregorash/final_project/blob/main/Resources/ufc-master.csv) file, we first wanted to create a baseline classification model [Simple_Model.ipynb](https://github.com/agregorash/final_project/blob/main/ML/Simple_Model.ipynb) in order to establish a benchmark of how well a winner could be predicted without data preprocessing and feature engineering.  Using the Dummy Classifier, which allows us to run the model with null values, the model predicted winners with 51.75% accuracy.

We then set out to create a model that would perform better than our baseline model, by first preprocessing the data and implementing feature engineering- [data_preprocessing.ipynb](https://github.com/agregorash/final_project/blob/main/ML/data_preprocessing.ipynb).  In this dataset we were dealing with 137 variables many of which contained a significant amount of null values.  In order to ensure key variables were not eliminated, we first encoded the winning column and ran a correlation function in pandas to see which variables most correlated to winners.  After that, we recognized that the majority of our variables were duplicates in a sense- statistics for the Red Corner fighter, and statistics for the Blue Corner figher.  To incresase correlation and concentrate the data, we subtracted all Red Corner statistics from Blue Corner statistics (Blue-Red) and created 'difference' variables.  Then we dropped all variables that were common to both fighters in that fight; such as date, location, weight class, ect.  Looking at the data further we recognized there was a large chunk of variables associated to rankings in a given weight class that contained a significant amount of null values.  After further analysis only one of these rankings columns was pertinent and all the others were dropped.  Then columns with strings were encoded, and false NaN columns were filled with their true value of 0.  Feature engineering and data preprocessing resulted 40 clean and concise variables to be fed into the classification models.

For our improved model we decided to compare the results between a Random Forest classifier and a Deep Neural Network[ufc_RF_vs_NN.ipynb](https://github.com/agregorash/final_project/blob/main/ML/ufc_RF_vs_NN.ipynb), because we were looking to classify winners with a very large dataset.  We tinkered with different train/test splits but results were best with a standard 25% test split.  The RF Classifier resulted in 78% accuracy while the Deep NN resulted in 76% accuracy.  It does not seem that either model was overfit, and they were able to predict winners of the fights with over 75% accuracy.  

![image_2](https://github.com/agregorash/final_project/blob/priis/x/seg2/image_2.png)

#### Database

In Visual Studio Code, we used the SQLalchemy library within Python to create a Postgres database [engine](https://github.com/agregorash/final_project/commit/5226eb402790633a7b0fd2d98c887178e139bd60) and make connections and create queries within PGAdmin. 
From this database we have created tables in PGAdmin named [Original](https://github.com/agregorash/final_project/blob/main/Database/originaltable.py) and [Master](https://github.com/agregorash/final_project/blob/main/Database/mastertable.py). 
For comparison of data of different fighter stats these two tables, Original and Master are left [joined](https://github.com/agregorash/final_project/commit/ea68f955559de8223ca18dcfeb0d98d8cfb6d0ad) on their indices and their joined [table](https://github.com/agregorash/final_project/blob/main/Database/Seg2Data/ViewMasterTableOriginalTableJoin.PNG) is viewed in PGAdmin as fighter comparisons.

#### Results
![cm.PNG](https://github.com/agregorash/final_project/blob/main/Resources/cm.PNG)
```
[(0.09371278924756822, 'sig_str_landed_bout_diff'),
 (0.07322299039122629, 'ev_diff'),
 (0.06649627355115442, 'odds_diff'),
 (0.05467294529755924, 'tot_str_landed_bout_diff'),
 (0.04309730671872242, 'sig_str_pct_bout_diff'),
 (0.041293308302487015, 'tot_str_attempted_bout_diff'),
 (0.03981271071059609, 'sig_str_dif'),
 (0.038691324197812044, 'avg_td_dif'),
 (0.03792105149725804, 'pass_bout_diff'),
 (0.03312924027637572, 'age_dif'),
 (0.0318583831513803, 'sig_str_attempted_bout_diff'),
 (0.031366939727302395, 'avg_sub_att_dif'),
 (0.030977152153706743, 'total_round_dif'),
 (0.03053441075092353, 'reach_dif'),
 (0.026207058330942615, 'height_dif'),
 (0.025897685861511234, 'kd_bout_diff'),
 (0.024335036416857133, 'avg_sig_str_pct_diff'),
 (0.02290230179793294, 'loss_dif'),
 (0.022780723959308514, 'td_pct_bout_diff'),
 (0.02245627665762514, 'td_landed_bout_diff'),
 (0.021917345103222123, 'sub_attempts_bout_diff'),
 (0.020848136817350923, 'win_dif'),
 (0.019330181830940606, 'longest_win_streak_dif'),
 (0.017138135156105915, 'win_by_Decision_Unanimous_diff'),
 (0.016860588676356744, 'ko_dif'),
 (0.015556149540612775, 'sub_dif'),
 (0.015405355453385393, 'win_streak_dif'),
 (0.014421074078504377, 'Stance_diff'),
 (0.013423505705208245, 'lose_streak_dif'),
 (0.01210350529804968, 'td_attempted_bout_diff'),
 (0.0115495521520556, 'win_by_Decision_Split_diff'),
 (0.010019448579594636, 'total_title_bout_dif'),
 (0.0054070386721871465, 'better_rank_enc'),
 (0.0035116495422187755, 'rev_bout_diff'),
 (0.003130775171274207, 'win_by_TKO_Doctor_Stoppage_diff'),
 (0.002803076296398146, 'win_by_Decision_Majority_diff'),
 (0.0027666052721854735, 'title_bout'),
 (0.0024419676560992133, 'draw_diff'),
 (0.0, 'avg_TD_pct_diff')]
```


