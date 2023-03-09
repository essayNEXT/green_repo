import pg_green

db = pg_green.PDatabaseConnect()
print(db)
db.create_database(True);