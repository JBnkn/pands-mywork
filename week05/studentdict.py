# studentdict.py
# author: Joseph Benkanoun
# stores student name and a list of courses and grades in a dict
# then print out the data

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99 
        }
    ]
}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"])) 