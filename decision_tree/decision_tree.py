
#-------------------------------------------------------------------------
# AUTHOR: Blake Costello
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: started embarassingly late
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#encode the original categorical training features into numbers and add to the 4D array X.
#--> add your Python code here
for row in db:
    converted_row = []
    #Age
    if row[0] == 'Young':
        converted_row.append(0)
    elif row[0] == 'Presbyopic':
        converted_row.append(1)
    elif row[0] == 'Prepresbyopic':
        converted_row.append(2)

    #Glasses
    if row[1] == 'Myope':
        converted_row.append(0)
    elif row[1] == 'Hypermetrope':
        converted_row.append(1)

    #stigma
    if row[2] == 'No':
        converted_row.append(0)
    elif row[2] == 'Yes':
        converted_row.append(1)

    #tears
    if row[3] == 'Reduced':
        converted_row.append(0)
    elif row[3] == 'Normal':
        converted_row.append(1)
    X.append(converted_row)

#encode the original categorical training classes into numbers and add to the vector Y.
for row in db:
    if row[4] == 'Yes':
        Y.append(1)
    else:
        Y.append(0)


#fitting the decision tree to the data using entropy as your impurity measure
#--> addd your Python code here
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = cld.fit(X,Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()