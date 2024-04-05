class Details:
 def __init__ (student,name,number):
    student.name= name
    student.number= number

 def display_info(student):
    print(f"hi welcome to infinitude  {student.name}")
    print(f"The {student.name} 's mobile number is   {student.number} .")



details1=Details("varun","8897051453")
details2=Details("sai","7654986658")



#print(f"My name is {details1.name}.")
details1.display_info()
#print(f"My name is {details2.name}.")
details2.display_info()