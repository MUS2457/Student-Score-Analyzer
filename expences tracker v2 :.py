expences = {}

while True :
    name = input(" your product name and 'done' to calculate : ")
    if name.lower() == 'done' :
        break 
    category = input(" the category of your product : ")
    price = int(input(" the price : "))
    expences[name] = { "category" : category , "price" : price }

sum_expences = sum( item["price"] for item in expences.values())
average = round(sum_expences / len(expences) ,1 )
max_expences = max(expences , key = lambda e : expences[e]["price"])
min_expences = min(expences , key = lambda e : expences[e]["price"])
    
print(" results : ")
print("sum of all expences : ",sum_expences)
print("average",average)
print("most expencive product" ,max_expences, " with the price of ",expences[max_expences]["price"])
print("most cheap product",min_expences, " with the price of ",expences[min_expences]["price"])