from sqlalchemy import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine('sqlite:///univercity.db', echo=True)
meta = MetaData()
conn = engine.connect()

univercity = Table(
    'univercity', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('location', String)
)

faculty = Table(
    'faculty', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('univercity_id', Integer)
)

faculty2speciality = Table(
    'faculty2speciality', meta,
    Column('id', Integer, primary_key=True),
    Column('faculty_id', Integer),
    Column('speciality_id', Integer)
)

speciality = Table(
    'speciality', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('speciality_code', String)
)

speciality2subject = Table(
    'speciality2subject', meta,
    Column('id', Integer, primary_key=True),
    Column('faculty_id', Integer),
    Column('speciality_id', Integer)
)

subject = Table(
    'subject', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

student = Table(
    'student', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('univercity_id', Integer),
    Column('faculty_id', Integer),
    Column('speciality_id', Integer)
)

meta.create_all(engine)

# conn.execute(univercity.insert(), [
#     {'name': 'BSUIR', 'location': 'Minsk'},
#     {'name': 'BSU', 'location': 'Minsk'}
# ])

# conn.execute(faculty.insert(), [
#     {'name': 'Faculty of Computer Systems and Networks', 'univercity_id': 1},
#     {'name': 'Faculty of Mechanics and Mathematics', 'univercity_id': 2},
#     {'name': 'Faculty of Engineering and Economics', 'univercity_id': 1},
#     {'name': 'Faculty of International Relations', 'univercity_id': 2}
# ])

# conn.execute(speciality.insert(), [
#     {'name': 'Informatics and programming technologies', 'faculty_id': 1, 'speciality_code': '111X'},
#     {'name': 'Сomputers, systems and networks', 'faculty_id': 1, 'speciality_code': '222X'},
#     {'name': 'Web programming and Internet Technologies', 'faculty_id': 2, 'speciality_code': '333X'},
#     {'name': 'Digital marketing', 'faculty_id': 3, 'speciality_code': '444X'},
# ])

# conn.execute(student.insert(), [
#     {'name': 'Kiril', 'univercity_id': 1, 'faculty_id': 1, 'speciality_id': 2},
#     {'name': 'Dima', 'univercity_id': 1, 'faculty_id': 1, 'speciality_id': 1},
#     {'name': 'Yan', 'univercity_id': 1, 'faculty_id': 3, 'speciality_id': 4},
#     {'name': 'Darya', 'univercity_id': 2, 'faculty_id': 2, 'speciality_id': 3},
# ])


j = student.join(univercity, student.c.univercity_id == univercity.c.id)
stmt = select([student.c.name, univercity.c.name]).select_from(j)
result = conn.execute(stmt).fetchall()
print(result)

j = student.join(faculty, student.c.faculty_id == faculty.c.id)
stmt = select([student.c.name, faculty.c.name]).select_from(j)
result = conn.execute(stmt).fetchall()
print(result)

j = student.join(speciality, student.c.speciality_id == speciality.c.id)
stmt = select([student.c.name, speciality]).select_from(j)
result = conn.execute(stmt).fetchall()
print(result)
