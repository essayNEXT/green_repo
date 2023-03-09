"""Створює таблиці в БД, якщо вони відсутні"""

from pg_green import PDatabaseConnect as DB

db = DB()
print(db)

# Список SQL запитів на створення таблиць
table_lst = [
               # Таблиця рівня доступу Permission
               """CREATE TABLE IF NOT EXISTS permission
               (
                   id_permit SERIAL PRIMARY KEY,    
                   permit_name TEXT UNIQUE
               );
               """
            ,
               # Таблиця посад/стану людини
               """CREATE TABLE IF NOT EXISTS person_position (
                   id_position   SERIAL PRIMARY KEY,
                   position_name TEXT UNIQUE
                   );
               """
            ,
                # Таблиця навчальних спеціальностей
               """CREATE TABLE IF NOT EXISTS speciality_list (
                   id_speclist     SERIAL PRIMARY KEY,
                   speciality_name TEXT NOT NULL
                   );
                   """
            ,
                # Таблиця навчальних курсів
               """CREATE TABLE IF NOT EXISTS course (
                       id_course   SERIAL PRIMARY KEY,
                       course_name TEXT NOT NULL
                       );
                       """
            ,
                # Таблиця змісту спеціальностей.
                # Реалізація багато-до-багатьох між спеціальностями та курсами
                # тому що один курс може уввійти у декількох спеціальностях
                # зовнішній ключ - курс
                # зовнішній ключ-назва спеціальності
                """CREATE TABLE IF NOT EXISTS speciality
                       (
                           id_speciality SERIAL PRIMARY KEY,
                           spec_id       INTEGER NOT NULL,
                           course_id     INTEGER NOT NULL,
                               FOREIGN KEY (spec_id) REFERENCES speciality_list(id_speclist),
                               FOREIGN KEY (course_id) REFERENCES course(id_course)
                       );
                """
            ,
                # Таблиця тем курсу
                #     lecture_name - назва теми
                #     lecture_topik - тема
                #     lecture_link  - посилання
                #     course_id - зовнішній ключ - курс, якому належить тема
                #
                """CREATE TABLE IF NOT EXISTS lecture
                   (
                       id_lecture    SERIAL PRIMARY KEY,
                       lecture_name  TEXT NOT NULL,
                       lecture_topik TEXT NOT NULL,
                       lecture_link  TEXT NOT NULL,
                       course_id     INTEGER NOT NULL,
                           FOREIGN KEY (course_id) REFERENCES course(id_course)
                   );
                """
            ,
                # Таблиця завдань за кожною темою
                #     task_topik - завдання
                #     lecture_id - зовнішній ключ - тема курсу, до якої належить завдання
                #
                """CREATE TABLE IF NOT EXISTS task
                   (
                       id_task    SERIAL PRIMARY KEY,
                       task_topik TEXT NOT NULL,
                       lecture_id INTEGER NOT NULL,
                           FOREIGN KEY (lecture_id) REFERENCES lecture(id_lecture)
                   );
                """
            ,
                # Таблиця людей People
                # position_id - зовнішній ключ, зв'язує з табліцею посад
                # permit_id - зовнішній ключ, зв'язує з табліцєю типів прав доступу
                #
                """CREATE TABLE IF NOT EXISTS people
                        (
                            id_person    SERIAL PRIMARY KEY,
                            first_name   TEXT NOT NULL,
                            second_name  TEXT NOT NULL,
                            middle_name  TEXT,
                            gender TEXT  NOT NULL,
                            country TEXT NOT NULL,
                            phone_number TEXT,
                            email        TEXT NOT NULL,
                            birthday     date,
                            login        TEXT NOT NULL,
                            login_tlg    TEXT NOT NULL,
                            date_reg     date DEFAULT CURRENT_DATE,
                            position_id   INTEGER NOT NULL,
                            permit_id   INTEGER NOT NULL,
                                FOREIGN KEY (position_id) REFERENCES person_position(id_position),
                                FOREIGN KEY (permit_id) REFERENCES permission(id_permit)
                        );
                """
            ,
                # Таблиця навчальних груп
                # id_group - первинний ключ
                # speciality_id - спеціальність - зовнішній ключ, зв'язує з табліцею спеціальностей
                # group_name - назва групи
                # start_date - початок навчання
                # finish_date - дата кінця
                # tutor_id - тренер - зовнішній ключ, зв'язує з табліцею людей
                # tutor_vise_id - помічник тренера - зовнішній ключ, зв'язує з табліцєю людей
                #
                """CREATE TABLE IF NOT EXISTS study_group
                        (
                            id_group      SERIAL PRIMARY KEY,
                            group_name    TEXT NOT NULL,
                            start_date    date NOT NULL,
                            finish_date   date NOT NULL,
                            speciality_id INTEGER NOT NULL,
                            tutor_id      INTEGER NOT NULL,
                            tutor_vise_id INTEGER NOT NULL,
                                FOREIGN KEY(speciality_id) REFERENCES speciality(id_speciality),
                                FOREIGN KEY(tutor_id) REFERENCES people(id_person),
                                FOREIGN KEY(tutor_vise_id) REFERENCES people(id_person)
                        );
                """
            ,
                # Таблиця складу груп
                # id_group - первинний ключ
                # speciality_id - спеціальність - зовнішній ключ, зв'язує з табліцею спеціальностей
                # group_name - назва групи
                # start_date - початок навчання
                # finish_date - дата кінця
                # tutor_id - тренер - зовнішній ключ, зв'язує з табліцею людей
                # tutor_vise_id - помічник тренера - зовнішній ключ, зв'язує з табліцєю людей
                #
                """CREATE TABLE IF NOT EXISTS group_list
                    (
                        id_grouplist SERIAL PRIMARY KEY,
                        student_id   INTEGER NOT NULL,
                        group_id     INTEGER NOT NULL,
                            FOREIGN KEY(group_id) REFERENCES study_group(id_group),
                            FOREIGN KEY(student_id) REFERENCES people(id_person)
                    );
                """
            ,
                # Таблиця розкладу занять груп
                # id_schedule - первинний ключ
                # group_id - група - зовнішній ключ, зв'язує з табліцею StydyGroup
                # lecture_id - лекція - зовнішній ключ, зв'язує з табліцею Lecture
                # lecture_date - дата
                # lecture_time - час
                # lesson_link - посилання на відео-зв'язок
                # lesson_state - стан заняття: відбулось/не відбулось
                #
                """CREATE TABLE IF NOT EXISTS schedule
                    (
                        id_schedule SERIAL PRIMARY KEY,
                        group_id      INTEGER NOT NULL,
                        lecture_id    INTEGER NOT NULL,
                        lecture_date  date NOT NULL,
                        lecture_time  time NOT NULL,
                        lecture_link  text NOT NULL,
                        lecture_state INTEGER,
                            FOREIGN KEY(group_id) REFERENCES study_group(id_group),
                            FOREIGN KEY(lecture_id) REFERENCES lecture(id_lecture)
                    );
                """
            ,
                # Таблиця оцінювання завдань
                # id_grade - первинний ключ
                # student_id - студент групи - зовнішній ключ, зв'язує з табліцею GroupList
                # task_id - завдання зі складу завдань теми - зовнішній ключ, зв'язує з табліцею Task
                # mark - оцінка
                # mark_time - дата та час оцінювання
                # comment - коментарій помічника тренера
                #
                """CREATE TABLE IF NOT EXISTS grade
                        (
                            id_grade   SERIAL PRIMARY KEY,
                            student_id INTEGER NOT NULL,
                            task_id    INTEGER NOT NULL,
                            mark       numeric DEFAULT 1  CHECK (mark > 0),
                            mark_time  timestamp NOT NULL,
                            comment    text,
                                FOREIGN KEY(student_id) REFERENCES group_list(id_grouplist),
                                FOREIGN KEY(task_id) REFERENCES task(id_task)
                        );
                """
            ,
                # Таблиця відвідування завдань
                # id_attend - первинний ключ
                # student_id - студент групи - зовнішній ключ, зв'язує з табліцею StydyGroup
                # task_id - завдання зі складу завдань теми - зовнішній ключ, зв'язує з табліцею Task
                # mark - оцінка
                # mark_time - дата та час оцінювання
                # comment - коментарій помічника тренера
                #
                """CREATE TABLE IF NOT EXISTS attendence
                        (
                            id_attend     SERIAL PRIMARY KEY,
                            student_id    INTEGER NOT NULL,
                            schedule_id   INTEGER NOT NULL,
                            student_state boolean DEFAULT FALSE,
                                FOREIGN KEY(student_id) REFERENCES group_list(id_grouplist),
                                FOREIGN KEY(schedule_id) REFERENCES schedule(id_schedule)
                        );
                """
            ]
# Список перевається в db для виконання запитів SQL
db.create_database_tables(table_lst, True)
