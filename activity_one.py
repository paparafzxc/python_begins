# asks the user to input a numerical score (between 0 and 100)
# If the score is greater than or equal to 90, print "A".
# If the score is between 80 and 89 (inclusive), print "B".
# If the score is between 70 and 79 (inclusive), print "C".
# If the score is between 60 and 69 (inclusive), print "D".
# If the score is less than 60, print "F".
# if the user enters a score that is less than 0 or greater than 100,
# display an error message: "Invalid score, please enter a score between 0 and 100.
def func():
    grade = float(input("Enter Grade:"))
    if 0 <= grade <= 100:
        if grade >= 90:
            print('A')
        elif 80 <= grade <= 90:
            print('B')
        elif 70 <= grade <= 80:
            print('C')
        elif 60 <= grade <= 70:
            print('D')
        else:
            print('F')
    else:
        print('Invalid')
    return func()
func()

