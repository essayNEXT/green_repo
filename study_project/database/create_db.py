from study_project.database.pg_green import PDatabaseConnect as DB

db = DB()
print(db)
db.create_database(True)