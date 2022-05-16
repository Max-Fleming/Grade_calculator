import os

# all the list we need are dictionaries so we can automate the later table format using similar keys
# earnedPoints and gradePoints will be changed based on input data so for now all values are 0
earnedPoints = {'Exercises': 0, 'Assignments': 0, 'Projects': 0, 'Quizzes': 0, 'Exams': 0, 'Final': 0}
totalPoints = {'Exercises': 200, 'Assignments': 200, 'Projects': 100, 'Quizzes': 100, 'Exams': 200, 'Final': 100}
weightedPoints = {'Exercises': 5, 'Assignments': 10, 'Projects': 20, 'Quizzes': 25, 'Exams': 50, 'Final': 10}
gradePoints = {'Exercises': 0, 'Assignments': 0, 'Projects': 0, 'Quizzes': 0, 'Exams': 0, 'Final': 0}

# This prints instructions for the user to input the correct values
print('Add up all points earned for each grade topic')
print('\n\n')

# this is where we will prompt the user to input their points into the earnedPoints dictionary
earnedPoints['Exercises'] = input('Enter your total points earned for Exercises: ')
earnedPoints['Assignments'] = input('Enter your total points earned for Assignments: ')
earnedPoints['Projects'] = input('Enter your total points earned for Projects: ')
earnedPoints['Quizzes'] = input('Enter your total points earned for Quizzes: ')
earnedPoints['Exams'] = input('Enter your total points earned for Exams: ')
earnedPoints['Final'] = input('Enter your total points earned for Final: ')

os.system('cls')

# This will print the headers of the table of points we will display
print(f'{"Category": <12} | {"Pts Earned": ^12} | {"Total Points": ^12} | {"Weight": ^6} | {"Grade": ^6} |')
print(f'__________________________________________________________________')

# this for loop will calculate the total weighted grade points for each category while also formating each row of the table
# using the keys in every dictionary
for key in gradePoints.keys():
    gradePoints[key] = (int(earnedPoints[key]) / totalPoints[key]) * weightedPoints[key]
    print(
        f'{key: <12} | {int(earnedPoints[key]): >12} | {totalPoints[key]: >12} | {weightedPoints[key]: >6} | {gradePoints[key]: >6.2f} |')


finalGrade = gradePoints['Exercises'] + gradePoints['Assignments'] + gradePoints['Projects'] + gradePoints['Quizzes'] + gradePoints['Exams'] + gradePoints['Final']
print(f'\nFinal Grade: {finalGrade: .2f}')
