array = []
student_num = int(input("How many students took the test?"))

while student_num > 0:
    score = [n for n in input("Enter the student name and grade separated by a space").split(" ")]
    array.append(score)
    student_num = student_num - 1


def get_top_scores(input_list):
    max = 0
    top_students = []
    for  in range(input_list):
        if  >= max:
            top_students.append()
        
#This is a def, meaning it will eventually print it out later in the code...
#You need to use the parameter atleast once in the def's code. it is labeled "input_list", so i think i know where to use it.
#How to use value data only to compare...
#I'll be back to this, later...