emails = (
    ("Ali", "ali@gmail.com"),
    ("Vali", "vali@yandex.ru"),
    ("Sami", "sami@mail.ru")
)

domains = []

for name, email in emails:
    domain = email.split("@")[1]
    domains.append(domain)

print(domains)
