import csv 
with open("employee_birtday.txt", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Department","Birthday month"])
    writer.writerow(["John Smith","Accounting", "November"])
    writer.writerow(["Erica Mayers", "IT","March"])
    writer.writerow(["Jennifer maik", "Math", "June"])