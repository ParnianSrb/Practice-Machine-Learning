# Simple Machine Learning - Using Decision Tree Classifier

import csv
from sklearn import tree

x = []
y = []

with open('ghadvaznkafsh.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[1:4])
        y.append(line[4])

    '''
    print(x[0], y[0])
    this gives me the first line which is:
    ['180', '79', '42']
    [مرد]
    '''
# now we have collected our data in x and y the way we want, we make a classifier
clf = tree.DecisionClassifier()
clf = clf.fit(x, y)

new_data = [[190, 89, 43], [160, 56, 39]]
answer = clf.predict(new_data)

