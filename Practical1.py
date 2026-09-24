n=print("enter Marks of 5 Subjects")
Subject1=int(input("enter marks of Python:"))
Subject2=int(input("enter marks of java:"))
Subject3=int(input("enter marks of ADBMS:"))
Subject4=int(input("enter marks of Client Side:"))
Subject5=int(input("enter marks of Soft Skill:"))

sum = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
print("Total Marks: ",sum)

average= sum/5
print("Average Marks of subjects",average)


percentage = (sum/500)*100
print("percentage obtained by student:",percentage,"%")



