from random import randint
from server.app import db, bcrypt
from server.models import User, UserType

#name = input('Naam? ')
#email = input('E-Mail? ')
#typ = input('Type [admin,manager,technician,catcher,client]? ')

users = [
	(UserType.CLIENT, 'Boer Herman', 'boer@muizenval.io'),
	(UserType.CATCHER, 'Vanger Kees', 'vanger@muizenval.io'),
	(UserType.TECHNICIAN, 'Technicus Jos', 'technicus@muizenval.io'),
	(UserType.MANAGER, 'Manager Peter', 'manager@muizenval.io'),
	(UserType.ADMIN, 'Administrator Ralf', 'admin@muizenval.io'),
]

address = 'Kerklaan 69\n9876XY Groningen'

hashed_password = bcrypt.generate_password_hash('hallo').decode('utf-8')

for typ, name, email in users:
	phone = '06-' + str(randint(10000000, 99999999))
	user = User(
		type=typ,
		name=name, 
		email=email, 
		password=hashed_password,
		phone=phone,
		address = address
	)
	db.session.add(user)

db.session.commit()
print('Added')
