# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input('Enter Score: ')
try:
    fscore = float(score)
except:
    print('Error, please enter numeric value')
    quit()
if fscore > 1.0 :
    print('Error, value out of range')
    print('Please enter suitable value')
    quit()
elif fscore <= 1.0 and fscore >= 0.9 :
    print('Grade A')
elif fscore < 0.9 and fscore >= 0.8 :
    print('Grade B')
elif fscore < 0.8 and fscore >= 0.7 :
    print('Grade C')
elif fscore < 0.7 and fscore >= 0.6 :
    print('Grade D')
elif fscore < 0.6 :
    print('Grade F')
