#! /opt/local/bin/python

# import pymysql # WORKS IN py 3.3
# conn = pymysql.connect(host='127.0.0.1', user='root', db='US_MENU')
# cur = conn.cursor()

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', db='US_MENU')
cursor = conn.cursor()

drop_restaurants = '''DROP TABLE restaurants'''
drop_menu_items  = '''DROP TABLE menu_items'''

# Execute the SQL commands
cursor.execute(drop_menu_items)
# Commit your changes in the database
conn.commit()
cursor.execute(drop_restaurants)
conn.commit()


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
conn.commit()
cursor.execute(make_menu_items)
conn.commit()


def get_max_rest_id():
	cursor.execute('''SELECT MAX(id) FROM restaurants;''')
	return int(cursor.fetchall()[0][0])



insert_txt = '''INSERT INTO restaurants (restaurant_name, zip) 
	VALUES ('titos', '%s')''' % (2)
cursor.execute(insert_txt)
conn.commit()


select_all_restaurants = '''SELECT * FROM restaurants'''
cursor.execute(select_all_restaurants)
results = cursor.fetchall()

for row in results:
	print(row)





cur.execute('USE US_MENU')
cur.execute('DROP TABLE restaurants')
cur.execute()
cur.execute()



# This seems to be required for pymysql entries to be seen by Sequel Pro
cur.execute("GRANT ALL ON restaurants TO PUBLIC")



for r in cur:
	print(r)
	


cur.close()
conn.close()



food_list = open('./food_network_data.txt', 'r')

food_set = set()
for line in food_list.readlines():
	line = line.strip().split('\t')
	for item in line:
		food_set.add(item)

for season in ['spring', 'summer', 'fall', 'winter']:
	food_set.remove(season)






