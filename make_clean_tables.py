#! /opt/local/bin/python
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', db='US_MENU')
cursor = conn.cursor()


cursor.execute('USE US_MENU')

# DEPENDENT TABLES MUST BE DELETED FIRST
cursor.execute('DROP TABLE menu_items')
cursor.execute('DROP TABLE restaurants')


make_restaurants = '''CREATE TABLE restaurants 
	(id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	restaurant_name VARCHAR(50), 
	zip VARCHAR(5), 
	menu_url VARCHAR(200))'''

make_menu_items = '''CREATE TABLE menu_items 
	(restaurant_id INT NOT NULL, 
	menu_item VARCHAR(50), price DECIMAL(5,2), 
	CONSTRAINT restaurant_menu_id_fk 
	FOREIGN KEY (restaurant_id) 
	REFERENCES restaurants (id))'''



# Execute the SQL commands
cursor.execute(make_restaurants)
cursor.execute(make_menu_items)
conn.commit()


# This seems to be required for pymysql entries to be seen by Sequel Pro
cursor.execute("GRANT ALL ON restaurants TO PUBLIC")


cursor.close()
conn.close()








