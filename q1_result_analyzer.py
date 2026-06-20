def analyze_result(name,roll,marks):
    total=sum(marks)
    average=total/len(marks)

    if average>=90:
        grade="A"
    elif average>=75:
        grade="B"
    elif average>=60:
        grade="C"
    elif average>=40:
        grade="D"
    else:
        grade="Fail"
    print("Student:",name,"(Roll:",roll,")")
    print("Total:",total,"Average:",average)
    print("Grade:",grade)

    print("Subjects below 40:",end=" ")
    found=False
    for i in range(len(marks)):
        if marks[i]<40:
            print("Subjet",i+1,end=" ")
            found=True
            
    if not found:
        print("None")

name="Aarav"
roll=101
marks=[88.5,35.0,76.0,92.5,48.0]

analyze_result(name,roll,marks)
        
        
          
