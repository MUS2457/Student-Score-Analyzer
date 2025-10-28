def avg(score) :
    if len(score) == 0 :
        return 0
    else :
        return round(sum(score.values()) / len(score) ,1)

students = {}                  # 3 weeks of coding !!

while True :
    name = input(" name of the student and 'Done' to calculate") 
    if name.capitalize() == 'Done' :
        break
    score = int(input("score of the student"))
    students[name] = score
  
max_score = max(students , key = students.get) 
min_score = min(students , key = students.get)   

for name,score in students.items() :
    if 90 <= score  <= 100 :
        grade = "A"
    elif 75 <= score <= 89 :
        grade = "B"   
    elif 60 <= score <= 74 :
        grade = "C"     
    else :
        grade = "F"    
    print(f" {name} has the score {score} with the grade {grade}")
print(" results :")   
print(" number of students ", len(students))
print("total of all score" , sum(students.values()))
print("the averge of the class is :" ,avg(students))
print("the highest scores goes to :", max_score, " with score equal to :", students[max_score])
print("the lowest scores goes to :", min_score, " with score equal to :", students[min_score])