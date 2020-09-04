# Author: Juma Al-Maskari jpa5637@psu.edu
course1 = input("Enter your course 1 letter grade:")
credit1 = float(input("Enter your course 1 credit:"))
gradepoint1=0.0
if course1 == "A":
  print("Grade point for course 1 is: 4.0")
  gradepoint1+=4
elif course1 == "A-":
  print("Grade point for course 1 is: 3.67")
  gradepoint1+=3.67
elif course1 == "B+":
  print("Grade point for course 1 is: 3.33")
  gradepoint1+=3.33
elif course1 == "B":
  print("Grade point for course 1 is: 3.0")
  gradepoint1+=3.0
elif course1 == "B-":
   print("Grade point for course 1 is: 2.67")
   gradepoint1+=2.67
elif course1 == "C+":
 print("Grade point for course 1 is: 2.33")
 gradepoint1+=2.33
elif course1 == "C":
  print("Grade point for course 1 is: 2.0")
  gradepoint1+=2.0
elif course1 == "D":
  print("Grade point for course 1 is: 1.0")
  gradepoint1+=1.0
else:
  print("Grade point for course 1 is: 0.0")
  gradepoint1=0

  # the second course

course2 = input("Enter your course 2 letter grade:")
credit2 = float(input("Enter your course 2 credit:"))
gradepoint2=0.0
if course2 == "A":
  print(f"Grade point for course 2 is: 4.0")
  gradepoint2+=4
elif course2 == "A-":
  print(f"Grade point for course 2 is: 3.67")
  gradepoint2+=3.67
elif course2 == "B+":
  print(f"Grade point for course 2 is: 3.33")
  gradepoint2+=3.33
elif course2 == "B":
  print(f"Grade point for course 2 is: 3.0")
  gradepoint2+=3.0
elif course2 == "B-":
   print(f"Grade point for course 2 is: 2.67")
   gradepoint2+=2.67
elif course2 == "C+":
 print(f"Grade point for course 2 is: 2.33")
 gradepoint2+=2.33
elif course2 == "C":
  print(f"Grade point for course 2 is: 2.0")
  gradepoint2+=2.0
elif course2 == "D":
  print(f"Grade point for course 2 is: 1.0")
  gradepoint2+=1.0
else:
  print(f"Grade point for course 2 is: 0.0")
  gradepoint2=0

  # the third course



course3 = input("Enter your course 3 letter grade:")
credit3 = float(input("Enter your course 3 credit:"))
gradepoint3=0.0
if course3 == "A":
  print(f"Grade point for course 3 is: 4.0")
  gradepoint3+=4
elif course3 == "A-":
  print(f"Grade point for course 3 is: 3.67")
  gradepoint3+=3.67
elif course3 == "B+":
  print(f"Grade point for course 3 is: 3.33")
  gradepoint3+=3.33
elif course3 == "B":
  print(f"Grade point for course 3 is: 3.0")
  gradepoint3+=3.0
elif course3 == "B-":
   print(f"Grade point for course 3 is: 2.67")
   gradepoint3+=2.67
elif course3 == "C+":
 print(f"Grade point for course 3 is: 2.33")
 gradepoint3+=2.33
elif course3 == "C":
  print(f"Grade point for course 3 is: 2.0")
  gradepoint3+=2.0
elif course3 == "D":
  print(f"Grade point for course 3 is: 1.0")
  gradepoint3+=1.0
else:
  print(f"Grade point for course 3 is: 0.0")
  gradepoint3=0
GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)
print(f"Your GPA is: {GPA}")