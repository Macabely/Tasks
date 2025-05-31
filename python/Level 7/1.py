import faker
mail = faker.Faker()
for i in range(10):
   username = mail.user_name()
   domain = mail.domain_name()
   print(f"{username}@{domain}")