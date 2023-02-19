import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwd4DBM$",
    database= "alltables"
    )
mycursor= mydb.cursor()
mycursor.execute('create table car(regNo varchar(10) primary key, chasisNo varchar(17), manufacturer varchar(20), model varchar(30), seats int)')
mycursor.execute('create table person(name varchar(30), age int, gender varchar(6), licence varchar(20) primary key, contact int, emergencyContact int)')
mycursor.execute('create table rent(carNo varchar(10), plicence varchar(20), tookAt int)')
data= [
    ('KA19P8487', 'JH4NA1150RT000268', 'Renault', 'Kwid', 5),
    ('KA19P8488', '1G8ZG127XWZ157259', 'Maruti', 'Alto k10', 5),
    ('KA19P8489', '5N3ZA0NE6AN906847', 'Hyundai', 'Santro', 5),
    ('KA19P8490', 'JH4DA1850JS005062', 'Bajaj', 'Qute', 4),
    ('KA19P8491', 'SCA1S684X4UX07444', 'Datsun', 'Redi-GO', 5),
    ('KA19P8492', 'JH4DB1570PS000858', 'Maruti', 'Alto-800', 5),
    ('KA19P8493', 'ZCFJS7458M1953433', 'Tata', 'Tiago', 5),
    ('KA19P8494', '1J4FA29P4YP728937', 'Maruti', 'S-presso', 5),
    ('KA19P8495', '1FVACYDT19HAJ2694', 'Maruti', 'Suzuki-eco', 7),
    ('KA19P8496', '1G8MF35X68Y131819', 'Maruti', 'Suzuki-WagonR', 5),
    ('KA19P8497', 'JF2SHADC3DG417185', 'Mahindra', 'XUV300 Turbosport', 5),
    ('KA19P8498', 'JT3HJ85J6T0133046', 'Maruti', 'Suzuku Grand Vitara', 5),
    ('KA19P8499', '3VWSB81H8WM210368', 'Mahindra', 'Bolero NEo', 7),
    ('KA19P8500', 'JH4KA8162MC010197', 'Toyota', 'Urban Cruiser', 5),
    ('KA19P8501', 'JH4CC2560RC008414', 'Mahindra', 'Scorpio Classic', 7),
    ('KA19P8502', 'JG1MR215XJK752025', 'Hyundai', 'i20', 5),
    ('KA19P8503', '2CNBJ13C3Y6924710', 'Tata', 'Nexon', 5),
    ('KA19P8504', 'JH4KA3151KC019450', 'Hyundai', 'Verna', 5),
    ('KA19P8505', 'JN8AZ2NE5C9016953', 'Skoda', 'KushaQ', 5),
    ('KA19P8506', 'JH4KA8170NC000665', 'Toyota', 'Innova-Crysta', 7),
    ('KA19P8507', 'WAUDFAFL6DN014563', 'Lamborghini', 'Aventador', 2),
    ('KA19P8508', 'JH4DA9460MS032070', 'Rolls-Royce', 'Phantom', 5),
    ('KA19P8509', '1MEBP67D5BF617327', 'Rolls-Royce', 'Drophead-Coupe', 5),
    ('KA19P8510', 'JH4NA1150MT000683', 'Bugatti', 'Veyron Grand sports', 2),
    ('KA19P8511', 'ZDM1UB5W86B016210', 'BMW', 'X7', 7),
    ('KA19P8512', '3VWPG71K97M122542', 'Mercedes', 'Maybach-S', 5),
    ('KA19P8513', '5FNRL18613B046732', 'Toyota', 'Landcruiser', 8),
    ('KA19P8514', '3VWDX7AJ5BM006256', 'Mercedes', 'G-Wagon', 5)
    ]
mycursor.executemany('insert into car values(%s, %s, %s, %s, %s)', data)
mydb.commit()
