    # personality-trait
NLP 2022 Project - Project 23

Chathushka Hendalage(Y67689797),
Achira Hendalage(2208083),
Piushana Abeygunawardena(Y69231913),
Ashan Walpitage(Y63562881)


# Compatible version
Python - V3.0 or up



# Project File Details

We have seperated code in to tasks in the project assignment. All files can be run individually. All output .csv files will be saved inside the "Results" folder.
All source data sets are inside the Datasets folder. 

task1 and task1_part2 -> Used to pre-process raw data (HP1, HP2, HP3)

task2 and task2_part2_pca -> To perform Principal component analysis, this generates a plot with 2 principle components. Please note that all 109 characters from the 3 movies are plotted in 2 dimensions depending on their personalities. There are overlapped characters have the same set of personality values.This is due to the results of the personality trait being boolean values and therefore its quite easy for multiple characters to have the same personality matrix.

task3_cosine_sim -> Find the cosine similarity. This file uses the function "cosine_similarity()" and calculates the cosine similarites of all the 109 characters against each other. At the end it generates a color sensitive chart to visualize which characters are similar.(for exampple the darker diagonal in the matrix represents their similarity with themselves and hence it appears dark. A clearer representation of this is interpretted in "Figure 6" of the report highlighing main characters.

task5.py -> Find the personality of each sentence and the character using Johannes Wieser implementation. the corresponding .csv files are also generated.

task6.py -> Find the personality of each person sum of all results

task6_1 -> Find the cosine similarity between sum of each person personality and against each sentence and the standard deviation

task7_sentimental_analysis -> To perform Sentimental analysis



# Standard deviation results
HP1 - 4.365901167848306
HP2 - 4.58804902825555
HP3 - 4.025253494012407

All - 4.339336322062046

Standard dev. of cosine similarity = 0.4426342019510506
