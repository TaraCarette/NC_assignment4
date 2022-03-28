import numpy as np
from sklearn import metrics

dataFile = "combined_xhosa.test"
scoreFile = "scores_xhosa.txt"
numEng = 123


# associate the data with the scores
with open(dataFile) as f:
    data = f.read().splitlines()

with open(scoreFile) as f:
    scores = f.read().splitlines()

# put all data in list with score and flag is english or not
scoreData = []
for i in range(0, len(data)):
    if i <= numEng:
        scoreData.append((data[i], float(scores[i]), 1))
    else:
        scoreData.append((data[i], float(scores[i]), 2))

# sort the data by score
scoreData.sort(key=lambda tup: tup[1])

sortedLabels = np.array([l[2] for l in scoreData])
sortedScores = np.array([l[1] for l in scoreData])

# calculate the curve
fpr, tpr, thresholds = metrics.roc_curve(sortedLabels, sortedScores, pos_label=2)
# then calculate the auc
print(metrics.auc(fpr, tpr))
