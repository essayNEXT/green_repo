from study_project.database.pg_green import greenDB
import datetime

#===================================================================================== PPersonPosition ================
class PPersonPosition:
    """
    Класс для роботи зі списком посад
    Застосування:
    from <modul> import PersonPosition

    За замовчуванням список посад формується зі списку PositionList
    Конструктор читає з БД список посад, які є в БД, і зберігає у приватному словарі __positions
    Методи:
    db_add(pos_add = None, pos_upd = None) - Додає або змінює значення в БД
    get_code(position) - Return position's code
    iterator() - Повертає ітератор по списку посад
    """
    PositionList = ["гість", "admin", "администратор", "студент",
                    "тренер", "помічник тренеру", "директор"]

    # Конструктор
    def __init__(self):
        self.__positions = {}
        self.__db_get()

    def __db_get(self):
        """Reading all values from DB"""
        insert_quary = """SELECT * FROM person_position; """

        res = greenDB.read_db(insert_quary, True)
        self.__positions.clear()
        for tpl in res:
            self.__positions[tpl[1]] = tpl[0]

    def db_add(self, pos_add=None, pos_upd=None):
        """
        Додає або змінює значення в БД

        Parameters:
        pos_add (str): назва посади, яка додається до таблиці посад
                        За умовчанням - None
        pos_upd (str): назва посади, замість якої записується pos_add.
                        За умовчанням - None.
                        Якщо pos_add == None, в таблицю записується список за змовчуванням,
                                              який зберігається в PositionList
        """
        insert_quary = """INSERT INTO person_position (position_name) VALUES """
        if pos_add is None:
            quary = ""
            for str_pos in PPersonPosition.PositionList:
                if str_pos in self.__positions:
                    continue

                cur_value = f" ('{str_pos}')"
                if quary == "":
                    quary = quary + cur_value
                else:
                    quary = quary + ", " + cur_value

            if quary == "":
                return
            quary = insert_quary + quary + ";"
            greenDB.write_db(quary, True)
        else:
            # Вже їснує - вихід
            if pos_add in self.__positions:
                return

            # pos_add not exist
            # if pos_upd = None - just add pos_add into table
            if pos_upd is None:
                quary = insert_quary + f"('{pos_add}');"
                greenDB.write_db(quary, True)
            else:
                # if pos_upd is actual, it is updated with pos_add
                if not (pos_upd in self.__positions):
                    return  #
                quary = f"""UPDATE person_position set position_name='{pos_add}' where id_position={str(self.positions[pos_upd])};"""
                greenDB.write_db(quary, True)

        self.__db_get()

    def get_code(self, position):
        """
        Return position's code. Maybe use for set a link to the table
        Parameters:
            position (str): назва посади, для якої потрібен код

        Return:
            int: код в Базі Даних
        """
        if position in self.__positions:
            return self.__positions[position]
        else:
            return None

    def iterator(self):
        """
         Повертає ітератор, який генерує назви посад

         Return:
             iterator (str): код в Базі Даних
         """
        return self.__positions.keys()

    def __str__(self):
        """ Для друку значень посад з кодами в БД"""
        str_prn = ""
        for e in self.__positions.keys():
            str_prn += f"{e} ({self.__positions[e]})\n"
        return str_prn


#===================================================================================== PPermission ===================
class PPermission:
    """
    Класс для роботи зі списком дозволів
    Застосування:
    from <modul> import Permission

    За замовчуванням список посад формується зі списку PermissionList
    Конструктор читає з БД список, які є в БД, і зберігає у приватному словарі __permission
    Методи:
    db_add(permit_add = None, permit_upd = None) - Додає або змінює значення в БД
    get_code(position) - Return permission's code
    iterator() - Повертає ітератор по списку дозволів
    """
    PermissionList = ["none", "read", "read-write", "all"]

    # Конструктор
    def __init__(self):
        self.__permission = {}
        self.__db_get()

    def __db_get(self):
        """Reading all values from DB"""
        insert_quary = """SELECT * FROM permission; """

        res = greenDB.read_db(insert_quary, True)
        self.__permission.clear()
        for tpl in res:
            self.__permission[tpl[1]] = tpl[0]

    def db_add(self, permit_add=None, permit_upd=None):
        """
        Додає або змінює значення в БД

        Parameters:
        permit_add (str): назва посади, яка додається до таблиці посад
                        За умовчанням - None
        permit_upd (str): назва посади, замість якої записується pos_add.
                        За умовчанням - None.
                        Якщо ermit_add == None, в таблицю записується список за змовчуванням,
                                              який зберігається в PermissionList
        """
        insert_quary = """INSERT INTO permission (permit_name) VALUES """
        if permit_add is None:
            quary = ""
            for str_pos in PPermission.PermissionList:
                if str_pos in self.__permission:
                    continue

                cur_value = f" ('{str_pos}')"
                if quary == "":
                    quary = quary + cur_value
                else:
                    quary = quary + ", " + cur_value

            if quary == "":
                return
            quary = insert_quary + quary + ";"
            greenDB.write_db(quary, True)
        else:
            # Вже їснує - вихід
            if permit_add in self.__permission:
                return

            # permit_add not exist
            # if permit_upd = None - just add permit_add into table
            if permit_upd is None:
                quary = insert_quary + f"('{permit_add}');"
                greenDB.write_db(quary, True)
            else:
                # if permit_upd is actual, it is updated with permit_add
                if not (permit_upd in self.__permission):
                    return  #
                quary = f"UPDATE permission set permit_name='{permit_add}' " \
                        f"WHERE id_permit={str(self.permission[permit_upd])};"
                greenDB.write_db(quary, True)

        self.__db_get()

    def get_code(self, permit):
        """
        Return permission's code.
        The function can be used for set a link to the table
        Parameters:
            permit (str): назва дозволу, для якої потрібен код

        Return:
            int: код в Базі Даних
        """
        if permit in self.__permission:
            return self.__permission[permit]
        else:
            return None

    def iterator(self):
        """
         Повертає ітератор, який генерує назви дозволів

         Return:
             iterator (str): код в Базі Даних
         """
        return self.__permission.keys()

    def __str__(self):
        """ Для друку значень посад з кодами в БД"""
        str_prn = ""
        for e in self.__permission.keys():
            str_prn += f"{e} ({self.__permission[e]})\n"
        return str_prn



#======================================================================================== PCountry ==================
class PCountry:
    """
    Класс для роботи з даними про країну
    Застосування:
    from <modul> import Country
    """

    def __init__(self, name="", short_name="", phone_code:int=0, utc="", id:int=0):
        """
        Конструктор
        Parameters:
        name:str        -  назва країни
        short_name:str  -  позначення країни
        phone_code:str  -  телефонний код країни
        utc:str         -  зона зсуву часу (timezone)
        За замовчуванням: всі параметри дорівнюють пустому рядку

        Особливості:
            Якщо name - пустий рядок - всі дані встановлюються за замовчуванням
            Якщо name має значення, зчітується з БД відповідна запис.
                        Всі поля, які не задані, приймають значення з БД
        """
        if name == "":
            self.__setdefault()
        else:
            # якщо код БД відомий, тоді з БД не читаємо, читання було раніше
            if id == 0:
                self.__db_get(name)

            if self.__id == 0:
                self.__name = name
            if short_name != self.__short_name and short_name != "":
                self.__short_name = short_name
            if phone_code != self.__phonecode and phone_code != 0:
                self.__phonecode = phone_code
            if utc != self.__utc and utc != "":
                self.__utc = utc

    def __setdefault(self):
        """ Встановлення даних за замовчуванням """
        self.__id = 0
        self.__name: str = ""
        self.__short_name: str = ""
        self.__phonecode: int = 0
        self.__utc = ""

    def __db_get(self, country_name):
        """Reading all values from DB"""
        insert_quary = f"""SELECT id_country, country_name, short_name, phonecode, timezone
                            FROM countries WHERE country_name = '{country_name}';"""

        res = greenDB.read_db(insert_quary, True)
        if len(res) == 0:
            self.__setdefault()
            return None
        # Розпаковка результату
        self.__id, self.__name, self.__short_name, self.__phonecode, self.__utc = res[0]

    def db_add(self):
        """
        Додає або змінює значення в БД

        Особливості:
            Записує нову країну в БД, або змінює дані, якщо країна вже існує
        """
        if self.__id == 0:
            quary = f"INSERT INTO countries (country_name, short_name, phonecode, timezone) " \
                    f"VALUES ('{self.__name}','{self.__short_name}'" \
                    f", '{self.__phonecode}','{self.__utc}');"
            greenDB.write_db(quary, True)
        else:
            quary = f"UPDATE countries SET country_name='{self.__name}'" \
                    f", short_name='{self.__short_name}', phonecode='{self.__phonecode}'" \
                    f", timezone='{self.__utc}' WHERE id_country={self.__id};"
            greenDB.write_db(quary, True)

        self.__db_get(self.__name)

    @property
    def name(self):
        """
        Атрибут: name:str

        Повертає назву країни
        """
        return self.__name

    def get_code(self, position):
        """
        Return country's code in the DB
        or
        None, if there isn't the country in the DB table.
        Can be used for set a link to the table
        """
        if self.__id > 0:
            return self.__id
        else:
            return None

    def __str__(self):
        """
        Для друку
        """
        str_prn:str = f"name={self.__name} ({self.__short_name}): " \
                      f"Phone code={self.__phonecode}, Timezone={self.__utc}, " \
                      f"DataBase code={self.__id}"
        return str_prn

    def __retr__(self):
        """
        Для програміста
        """
        return f"PCountry(name={self.__name}, " \
               f"short_name={self.__short_name}, " \
               f"phone_code={self.__phonecode}, " \
               f"utc={self.__utc}, id={self.__id})"


#======================================================================================== PCountries ==================
class PCountries:
    """
    Клас для списку країн в БД
    Члени класу:
    __dct_countries - Список зберігається в словарі
        key - назва країни
        value - кортеж з даними tuple(id_code:int, short_name:str, phone_code:int, utc:str)

    Методи:
    getobject(self, name:str) - повертає екземпляр класу PCountry зі списку за ім'ям name
    def getcode(self, name:str)->int: - повертає код країни в БД
    """
    def __init__(self):
        """
        Конструктор. Зчитує з БД з таблиці countries всі записи
        """
        self.__db_get()

    def __db_get(self):
        """Reading all values from DB"""
        quary = "SELECT * FROM countries;"

        res = greenDB.read_db(quary, True)
        self.__dct_countries = {}
        if len(res) == 0:
            return None
        for tpl in res:
            # Розпаковка результату
            i_code, str_name, str_sname, i_phone, str_utc = tpl
            self.__dct_countries[str_name]=tuple(i_code, str_sname, i_phone, str_utc)

    def getobject(self, name:str)-> PCountry | None:
        """
        Отримати дані країни зі списку

        Параметри:
        name:str - назва країни

        Повертає:
        екземпляр класу PCountry з іменем name, якщо name їснує
        None - країна з назвою name відсутня в списку
        """
        if name in self.__dct_countries:
            i_code, str_sname, i_phone, str_utc = self.__dct_countries[name]
            return PCountry(name, str_sname, i_phone, str_utc)
        else:
            return None

    def getcode(self, name:str)->int:
        """
        Отримати код країни зі списку

        Параметри:
        name:str - назва країни

        Повертає:
        код країни в БД, якщо name їснує
        0 - країна з назвою name відсутня в списку
        """
        try:
            return self.__dct_countries[name][0]
        except:
            return 0


#=========================================================================================== PPerson =================
class PPerson:
    def __init__(self, first_name="", second_name="", middle_name=""
                 , email="l@s.d", login_tlg="", login="", gender=""
                 , country:str="", phone_number=""
                 , birthday=datetime.datetime.now()
                 , registry=datetime.datetime.now(), position="гість", permission="None"):

        self.id = 0

        if login_tlg != "" or login != "":
            self.db_read(login_tlg, login)

        if self.id > 0:
            # перевірка
            if first_name:
                self.first_name = first_name
            if second_name:
                self.second_name = second_name
            if middle_name:
                self.middle_name = middle_name
            if gender:
                self.gender = gender
            if country:
                self.country = country
            if phone_number:
                self.phone_number = phone_number
            if email:
                self.email = email
            if login:
                self.login = login
            if login_tlg:
                self.login_tlg = login_tlg

            if not birthday or birthday == datetime.datetime.now():
                if not self.birthday:
                    self.birthday = datetime.datetime.now()
            else: # параметр заданий
                if isinstance(birthday, str):
                    self.birthday = datetime.date.fromisoformat(birthday)
                else:
                    self.birthday = birthday

            if not registry or registry == datetime.datetime.now():
                if not self.registry:
                    self.registry = datetime.datetime.now()
            else: # параметр заданий
                if isinstance(registry, str):
                    self.registry = datetime.date.fromisoformat(registry)
                else:
                    self.registry = registry

            if position:
                self.position = position
            if permission:
                self.permit = permission

        if self.id == 0:
            self.first_name = first_name
            self.second_name = second_name
            self.middle_name = middle_name
            self.gender = gender
            self.country = country
            self.phone_number = phone_number
            self.email = email
            if isinstance(birthday, str):
                self.birthday = datetime.date.fromisoformat(birthday)
            else:
                self.birthday = birthday
            self.login = login
            self.login_tlg = login_tlg
            self.registry = registry
            self.position = position
            self.permit = permission
            self.id = 0


    def db_read(self, login_tlg = "", login = ""):
        """
        Read a person from DataBase
        Parameters:
        login_tlg:str Telegram login. Default: None
        login:str - login Default: None
        """
        str_quary = "SELECT * FROM people WHERE "
        if login_tlg:
            str_tlg = f"login_tlg = '{login_tlg}' "
        else:
            str_tlg = ""

        if login:
            str_log = f"login = '{login}' "
        else:
            str_log = ""

        str_between = "and " if str_log and str_tlg else ""
        str_quary = str_quary + str_tlg + str_between + str_log + ";"

        try:
            res = greenDB.read_db(str_quary, True)
            res = res[0]
            self.first_name = res[1]
            self.second_name = res[2]
            self.middle_name = res[3]
            self.gender = res[4]
            self.phone_number = res[6]
            self.email = res[7]
            self.birthday:datetime.date = res[8]
            self.login = res[9]
            self.login_tlg = res[10]
            self.registry = res[11]
            self.id = res[0]
            str_quary = f"SELECT cn.country_name, ps.permit_name, pp.position_name " \
                        f"FROM countries cn, permission ps, person_position pp " \
                        f"WHERE cn.id_country={res[5]} and ps.id_permit={res[13]} and pp.id_position = {res[12]};"
            res = greenDB.read_db(str_quary, True)
            res = res[0]
            self.country = res[0]
            self.position = res[2]
            self.permit = res[1]
        except:
            self.id = 0


    def db_add(self):
        """
        Додати або переписати в БД
        Залежить від значення id: 0 - додати, !=0 - переписати

        """
        if self.login_tlg == "": return
        if self.email == "": return
        if self.first_name == "": return
        if self.second_name == "": return

        cn = PCountry(self.country)
        country_id = cn.get_code(self.country)

        ps = PPermission()
        permit_id = ps.get_code(self.permit)
        if permit_id is None:
            ps.db_add(self.permit)
            permit_id = ps.get_code(self.permit)

        pp = PPersonPosition()
        position_id = pp.get_code(self.position)
        if position_id is None:
            pp.db_add(self.position)
            position_id = ps.get_code(self.permit)

        #
        if self.id == 0:
            quary = f"INSERT INTO people (first_name, second_name, middle_name, gender" \
                    f", phone_number, birthday, date_reg, login, login_tlg, email" \
                    f", country_id, position_id, permit_id) " \
                    f"VALUES ('{self.first_name}', '{self.second_name}'" \
                    f", '{self.middle_name}', '{self.gender}'" \
                    f", '{self.phone_number}', '{self.birthday}', '{self.registry}'" \
                    f", '{self.login}', '{self.login_tlg}', '{self.email}'" \
                    f", {country_id}, {position_id}, {permit_id}" \
                    f");"
            greenDB.write_db(quary, True)
        else:
            quary = f"UPDATE people SET first_name='{self.first_name}', second_name='{self.second_name}'" \
                    f", middle_name='{self.middle_name}', gender='{self.gender}'" \
                    f", phone_number='{self.phone_number}', birthday='{self.birthday}', email='{self.email}'" \
                    f", login='{self.login}', login_tlg='{self.login_tlg}', date_reg='{self.registry}'" \
                    f", country_id={country_id}, position_id={position_id}, permit_id={permit_id}" \
                    f" WHERE id_person={self.id};"
            greenDB.write_db(quary, True)

    def __repr__(self):
        return f"PPerson(first_name='{self.first_name}', second_name='{self.second_name}'" \
               f", middle_name='{self.middle_name}', email='{self.email}', login_tlg='{self.login_tlg}'" \
               f", login='{self.login}', gender='{self.gender}', country='{self.country}'" \
               f", phone_number='{self.phone_number}'" \
               f", birthday=date({self.birthday.year}, {self.birthday.month}, {self.birthday.day})" \
               f", registry=date({self.registry.year}, {self.registry.month}, {self.registry.day})" \
               f", position='{self.position}', permission='{self.permit}', id={self.id})"

PersonPosition = PPersonPosition()
#print(PersonPosition)
Permission = PPermission()
#print(Permission)
Person = PPerson




#cn2 = PCountry(name='United Kingdom', short_name='UK',phone_code=44, utc='0')
#cn2.db_add()
# print(pp)
# pp.db_add("unknown")
# pp.db_add(pos_upd="директор", pos_add="director")
# for i in pp.iterator():
#     print(i, pp.get_code(i))
#cc = PCountry(name="Ukraine")
#print(cc)
#pc = PCountries()
# person = PPerson()
# person.db_read('Zoe')
# print(person)
# person.db_read('Jacob')
# print(person)
# person.db_read('Karl')
# print(person)
