import matplotlib_inline
import numpy as np
import matplotlib.pyplot as plt

matplotlib_inline

dataset = [11, 345, 20,346, 22, 19, 21, 23, 27, 29, 17, 15, 28, 25, 340]
# z score
outlir = []
# print(sum(dataset))
# print(len(dataset))
# print(sum(dataset)/len(dataset))

def find_outler(data):
    threshold = 2  # falls in 3rd S.D.
    mean1 = np.mean(data)
    # print(mean1)
    std1 = np.std(data)
    #print(std1)

    for i in data:
        zscre = []
        zscore = (i - mean1) / std1
        zscre.append(zscore)
        print(zscore)
        if np.abs(zscore) > threshold:
            outlir.append(i)
    return outlir


out = find_outler(dataset)
print(out)

# IQR 75%-25% values in dataset
print(sorted(dataset))
q1,q3 = np.percentile(dataset,[25,75])
print(q1,q3)
diff = q3-q1
print(diff)

lowerq1 = q1 - (1.5*diff)
upperq3 = q3 + (1.5*diff)
print(lowerq1, upperq3)

