last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]


subjects = ["physics","calculus","poetry","history"]

grades = [98,97,85,88]

# Create a two-dimensional list with subjects and grades
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]


gradebook.append (["computer science",100])

gradebook.append (["visual arts",93])

gradebook[-1][-1]+=5

gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = gradebook + last_semester_gradebook

for grade in full_gradebook:
    print (grade )