from datetime import datetime 

students = {}

while True :
    name = input(" name of the student or 'done' to start calculation or 'exit' to stop the program : ")
    if name.lower() == 'exit' :
        print(" the program has been closed")
        break
    if name.lower() == 'done' :
        break
    subject = input(" the subject : ")
    score = int(input(" your score : "))
    students[name] = {"subject" : subject , "score" : score }

if students :
    top = max(students, key = lambda f : students[f]["score"])
    low = min(students, key = lambda f : students[f]["score"])
    tl_students = len(students)
    sum_scores = sum(info["score"] for info in students.values())
    average = round(sum_scores / tl_students ,1 )

now = datetime.now() 
time = now.strftime("%Y-%m-%d %H:%M:%S")  
 
#  grade for class based on the average 
    
if 80 <= average <= 100 :
    class_g = "A"
elif 60 <= average <= 79 :
    class_g = "B"
elif 50 < average <= 59 :
    class_g = "C"
else :
    class_g = "F"   


with open("student_tracker.txt", "a") as s:
    for na, sub in students.items():
        score = sub["score"]
        
        # individual student grade
        if 90 <= score <= 100:
            grade = "A"
        elif 70 <= score <= 89:
            grade = "B"
        elif 50 <= score <= 69:
            grade = "C"
        else:
            grade = "F"

        s.write(f" student name: {na}, subject: {sub['subject']}, score: {score}, grade: {grade}\n")

    s.write(f"\nCurrent time: {time}\n")
    s.write("\nSummary:\n\n")
    s.write(f" Top student: {top} → {students[top]['score']}\n")
    s.write(f" Lowest student: {low} → {students[low]['score']}\n")
    s.write(f" Class average: {average} ({class_g})\n\n")

    
