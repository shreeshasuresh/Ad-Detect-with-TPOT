import pandas

# Open and read the predicted labels file and the actual label file.
a = open("actual-GB.csv")
b = open("result-GB.csv")
actual = a.read()
given = b.read()

# Initialization of variables which keep count of true +ves, true -ves and false +ves, false -ves. 
trueAd = 0
trueSong = 0
falseAd = 0
falseSong = 0
count = 0

# Iterate each line/class label
for each in actual:
    count += 1
    # 0 -> Ad label
    # 1 -> Song label
    if each == given[count] and each == "0":
        # Both class label match to Ad
        trueAd +=1
    elif each == given[count] and each == "1":
        # Both class label match to Song
        trueSong += 1
    elif each == "0" and given[count] == "1":
        # Prediction match to Song, but it is Ad
        falseSong +=1
    elif each == "1" and given[count] == "0":
        # Prediction match to Ad, but it is Song
        falseAd += 1

# Print the confusion matrix
print "Confusion Matrix  ActualAd | ActualSong"
print "     PredictAd   "+str(trueAd)+" | "+str(falseAd)
print "   PredictSong   "+str(falseSong)+" | "+str(trueSong)

