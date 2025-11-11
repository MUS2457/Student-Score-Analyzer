from datetime import datetime
import json

def average(number) :
    return round(sum(number) / len(number),1) if number else 0

def grade(result) :
    if 90 <= result <= 100 :
        return 'A'
    elif 70 <= result <= 89 :
        return 'B'
    elif 50 <= result <= 69 :
        return 'C'
    else :
        return 'F'
        
students = {}

while True :
    name = input(" student name ,('done' to finish or 'exit' to quit) : ").strip()
    if name.lower() == 'exit' :
        print("program closed .")
        break
    if name.lower() == 'done' :
        break
    if name == "" :
        print("enter a valid number !")
        continue
    if name not in students :
        students[name] = {}

    while True :
        subject = input(f" enter subject for  {name} or 'done'' to finish : ").strip()  
        if subject.lower() == 'done' :
            break
        if subject == "" :
            print("enter a valid subject !")
            continue
        try :
            score = int(input(f"enter score for {name} in {subject}"))
        except ValueError :
            print("enter a valid score .")
            continue
        students[name][subject] = score

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")

if students :
    student_average = {}
    for name,subject in students.items() :
        scores = list(subject.values())
        avg_score = average(scores)
        student_average[name] = avg_score

    # lets find the top and lowest student !
    top    = max(student_average, key = student_average.get)  
    lowest = min(student_average, key = student_average.get)

    class_average = round(sum(student_average.values()) / len(student_average) ,1)

    if 80 <= class_average <= 100 :
        class_grade = 'A'
    elif 60 <= class_average <= 79 :
        class_grade = 'B'
    elif 50 <= class_average <= 59 :
        class_grade = 'C'    
    else :
        class_grade = 'F'     


data = {"students" : students, "student average" : student_average, "top student" : top,
        "top student grade" : grade(student_average[top]), " lowest student" : lowest, "lowest student grade" : grade(student_average[lowest]),
         "class average" : class_average, "class grade" : class_grade 
}              

with open("student_score_analyser_v3.txt", "w") as t :

    for name, subjects in students.items():
            t.write(f"{name}:\n")
            for subject, score in subjects.items():
                t.write(f"  {subject}: {score} → Grade: {grade(score)}\n")
            t.write(f"  Average: {student_average[name]} → Grade: {grade(student_average[name])}\n\n")

    t.write(f"Timestamp: {time}\n")
    t.write("=== Class Summary ===\n")
    t.write(f"Top student: {top} → {student_average[top]} ({grade(student_average[top])})\n")
    t.write(f"Lowest student: {lowest} → {student_average[lowest]} ({grade(student_average[lowest])})\n")
    t.write(f"Class average: {class_average} → {class_grade}\n")
    t.write("\n---------------------------\n\n")

with open("student_score_analyser_v3.json","w") as j :
    json.dump(data, j, indent=4)

print(json.dumps(data,indent=4))