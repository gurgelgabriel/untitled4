
grade_1 = int(input("math"))      # that ask your grade in number depending of the subject in that case "math"
grade_2 = int(input("physics"))   # that ask your grade in number depending of the subject in that case "physics"
grade_3 = int(input("comp sci"))  # that ask your grade in number depending of the subject in that case "comp sci"
grade_4 = int(input("english"))   # that ask your grade in number depending of the subject in that case "english"
grade_5 = int(input ("gls"))      # that ask your grade in number depending of the subject in that case "gls"
grade_s = (grade_1 + grade_2 + grade_3 + grade_4 + grade_5)/5 # this creates a variable grade_s that makes the averege of all your grades
print(grade_s) # print the value of the variable grade_s
if grade_s >= 79.5: # in case your grade_s is bigger than 79.5 it wil print "acepted" if not you will print"failed"
    print("accepted")
else:
    print("failed")