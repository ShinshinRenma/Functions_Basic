#x = [ [5,2,3], [10,8,9] ] 
#students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
#]
#sports_directory = {
#    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
#}
#z = [ {'x': 10, 'y': 20} ]

#x[1][0] = 15
#print(x)

#students[0]["last_name"] = "Bryant"
#print(students)

#sports_directory["soccer"][0] ="Andres"
#print(sports_directory)

# z[0]["y"] = 30
# print(z)

from multiprocessing.sharedctypes import Value
from turtle import xcor


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#def iterateDictionary(people):
#    for dictionary in people:
#        for key in dictionary:
#            print(dictionary[key])

#iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

# def iterate_dictionary2(key_name, some_list):
#    for x in some_list:
#        print(x[key_name])

# iterate_dictionary2("first_name", students)
# iterate_dictionary2("last_name", students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(str(len(some_dict["locations"])) + " LOCATIONS")
    for x in some_dict["locations"]:
        print(x)
    print(str(len(some_dict["instructors"])) + " INSTRUCTORS")
    for x in some_dict["instructors"]:
        print(x)

printInfo(dojo)
# output:
