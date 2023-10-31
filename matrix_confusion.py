confusionMatrix = [432,98,84,399]
print (confusionMatrix)

sensibility= confusionMatrix[0]/(confusionMatrix[0]+confusionMatrix[1])

specificity= confusionMatrix[3]/(confusionMatrix[3]+confusionMatrix[2])

precision= confusionMatrix[0]/(confusionMatrix[0]+confusionMatrix[2])

accuracy= (confusionMatrix[0]+confusionMatrix[3])/sum(confusionMatrix)

f_score= 2*((precision*sensibility)/(precision+sensibility))

print ("Accuracy: ", '%.2f' % accuracy)

print ("Precision: ", '%.2f' % precision)

print ("Sensibility: ", '%.2f' % sensibility)

print ("F-score: ", '%.2f' % f_score)

print ("Specificity: ", '%.2f' % specificity)