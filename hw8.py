import sqlite3

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)


def select_all_cities(connection):
    sql = '''SELECT * FROM countries'''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
        print(r)


def select_id_title(connection):
    sql = "SELECT id, title FROM cities"
    cursor = connection.cursor()
    cursor.execute(sql)
    for r in cursor.fetchall():
        id, title = r
        print(f'{id}, {title}')


def select_emp_info(connection, number):
    sql = '''SELECT employees.first_name, 
                    employees.last_name, countires.title, cities.title, cities.area
             FROM employees
             INNER JOIN cities ON employees.city_id = cities.id
             INNER JOIN countires ON cities.country_id = countires.id
             WHERE cities.id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (number,))
        for r in cursor.fetchall():
            first_name, last_name, country, city, area = r
            print(f'Name: {first_name} {last_name}, Country: {country}, City: {city}, Area: {area}')
    except sqlite3.Error as e:
        print(e)


connection = create_connection("Data.db")


if connection:
    try:
        while True:
            print ('Список городов: ')
            select_id_title(connection)
            number = int(input(f'Вы можете отобразить список сотрудников '
                           'по выбранному id города из перечня городов ниже,'
                           ' для выхода из программы введите 0\n'))
            if number == 0:
                break
            elif number in range(8):
                select_emp_info(connection, number)
            else:
                raise ValueError("Enter numbers between 0 and 7!")

    except sqlite3.Error as e:
        print(e)



