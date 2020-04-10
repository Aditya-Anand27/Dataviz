# Dataviz
For this challenge, I’ve taken up the Titanic Dataset. I’ll first list why I believe the dataset is of use more than century on, and then walk through how I played around with it

Usefulness:
The Titanic disaster is a base for many social psychology classes even today (eg. https://www.psychologytoday.com/us/blog/the-fair-society/201204/lessons-the-titanic). As my results on the dataset will show, there were preconceived biases that led to certain types of people having a higher chance of survival than others, and the dataset helps to quantify what the ramifications of those biases were. It also helps to chart economic and social trends from that era to the present, as we can compare the age/sex/fare of the people aboard the titanic to that of a similar cruise ship today, to see what the changes are

Playing with the Data:

1.	First I print the head of the dataset, and see there are some columns which are not immediately obvious. A little google search reveals that SibSp stands for Sibling/Spouse and Parch stands for Parent/Child. 
2.	Also, we see that Sex is represented as male and female. To make processing easier, I convert that into 1 for male and 2 for female. I also drop the name column entirely, as there isn’t any valuable information to gain from that (I mean, I can count the number of people beginning with a given letter, but that’s worthless)
3.	The head of the data shows that everyone with PClass==3 has Cabin == nan. A simple Counter function helps to show that IS NOT the case for the rest of the data
4.	I then find out where null values are. The age column is too important to leave with nan values, so I take the mean of the remaining data for the nan values
5.	First, I figure out information from the Titanic not related to survival. This is involves plotting Fare and PClass against the place they embarked. It becomes evident that the place C (Cherbough) has the most people in PClass==1. This may indicate the region is wealthy, helping to find out economic trends between then and now as I had previously mentioned.
6.	I then try to find a relation between PClass and Sex. While the first and second are fairly equal, men greatly outnumber women in the third class. The film ‘Titanic’ got that one right
7.	I then move on to the crux of the dataset. I figure out the number of people who survived, and delve into the specifics of the same
8.	Seaborn plots between Survival and Sex/PClass indicates that those who were female, and were in Class 1 were much more likely to survive, then those who were male and not in Class1
9.	I then plot graphs of Age vs Survival. I do this twice, one with data where I have imputed the mean, and one where I have not. Both of this show that young children were more likely to survive. I iterate through the dataset to find actual values to confirm this, and find that children<=10 years had nearly a 60% chance to survive, while those >10 years had only a 37% chance to survive
10.	I then tried to find intersections between already established findings. I knew that people who were female and people who were first class had a higher chance of survival, so I figured out the probability of survival for women in Pclass==1 and men in Pclass!=1. The difference was considerable.
96% of first class women survived
Only 14% of men not in first class survived
11.	I then plotted trend for people who had siblings/spouses/parents/children onboard. Turned out that those with family onboard were more likely to survive.
12.	However, this was subject to bias. A quick iteration showed that PClass 3 was LESS likely to have family onboard, which may have sung the survival percentages. So I removed PClass 3 from the equation and then compared survival percentages for those who did and did not have family on the ship. Once again, those with family had better chances
13.	By now, I knew that the best bet to survive was to be a female, first class passenger with family. I counted the number of people who fit the description, and came to know they had a (drumroll please) 100% chance to survive. This was in accordance to the rest of the results.

To Summarize:
Higher chance to survive:

•	Women

•	Youngs kids

•	First class

•	People with family

The more of these criteria you fit, the better your odds were
      




