students = [

        ("Ali", ["Fizika", "Matematika"]),
        ("Laylo", ["Ingliz tili"]),
        ("Jasur", ["Matematika", "Informatika"])
]

subject = input("Subject: ")


count = 0 
for sutudents in students:
    if subject in sutudents[1]:
        count += 1  


print(count)