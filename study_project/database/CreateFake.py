from faker import Faker
import random
from study_project.database.greendb_object import PersonPosition, Person
import greendb_object as gdb

def gener_user(iCount):
    fake_ua = Faker("uk-UA")
    fake_en = Faker("en-UK")
    iIndex = iCount
    while True:
        b_male = random.choice((True, False))
        if b_male:
            male = "male"
            f_name = fake_ua.first_name_male()
        else:
            male = "female"
            f_name = fake_ua.first_name_female()

        l_name = fake_ua.last_name()

        year = random.randint(1959,2006)
        d_last = (28 if (year % 4 == 0) else 30)
        b_day = f'{year:d}-{random.randint(1,12):02d}-{random.randint(1,d_last):02d}'

        e_mail = fake_ua.email()
        p_number = fake_ua.phone_number()

        login = fake_en.user_name()
        login_tlg = fake_en.first_name()

        tpl = (f_name, l_name, b_day, e_mail, p_number, login, login_tlg, male)

        # #str_user = f"""("{name}", {random.randint(20,80)}, "{male}", "{fake.country()}")"""
        # #yield str_user
        yield tpl
        iIndex -= 1
        if iIndex == 0:
            break

lst_pos = list(PersonPosition.iterator())

for pers in gener_user(10):
    person = Person(first_name=pers[0], position=random.choice(lst_pos), second_name=pers[1], email=pers[3],
             login_tlg=pers[6], login=pers[5], gender=pers[7], country='Ukraine', phone_number=pers[4],
             birthday=pers[2])
    person.db_add()
    print(person)

