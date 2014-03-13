# yelp sample
# c=urlopen('http://www.yelp.com/search?find_desc=restaurants&find_loc=Warren%2C+MI&ns=1#attrs=RestaurantsPriceRange2.3,RestaurantsPriceRange2.4')

from urllib import urlopen
from bs4 import BeautifulSoup




# Restaurants in Denver, CO, starting with first results, price range $$$-$$$
c=urlopen('http://www.allmenus.com/pa/pittsburgh/-/american/&filters=none?sort=popular&filters=none')
soup=BeautifulSoup(c.read())
restaurant_list = soup.find_all("div", attrs={"class": "basics"})

for current_restaurant in restaurant_list:
	current_cuisine_list = current_restaurant.find_all('li')
	if len(current_cuisine_list) == 1:
		if current_cuisine_list[0].string == 'American':
			current_url = current_restaurant.a.get('href')
			current_name = current_restaurant.a.string
			current_address = current_restaurant.find('p', attrs={"class": "restaurant_address"}).string
			restaurant_menu = BeautifulSoup(urlopen("http://www.allmenus.com/" + current_url).read())
			menu_list = restaurant_menu.find_all('li', attrs={"class": "menu_item"})




current_link = 'http://www.yelp.com/' + restaurant_list[0].a.get('href')


# On menu page
# <div class="menu-item-details">
# <li class="menu-item-price-amount">
# <p class="menu-item-details-description">


