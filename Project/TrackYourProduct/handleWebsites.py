from bs4 import BeautifulSoup
import requests
from requests_html import HTML, HTMLSession

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


class productObject():
	'''
		Class contains name, price and link of the product
		if the price is unregconizable it will be set to 0 VND
	'''
	def __init__(self, name, price, link):
		self.name 	= name
		self.price 	= price
		self.link	= link
		self.price 	= self.convertPrice()


	def convertPrice(self):
		number = '0123456789'
		result = '0'

		for letter in self.price:
			if letter in number:
				result += letter

		return int(result)


	# ==================Comaparison(Depend on the price)================== #
	def __eq__(self, other):
		return self.price == other.price


	def __ne__(self, other):
		return self.price != other.price

	def __gt__(self, other):
		return self.price > other.price


	def __ge__(self, other):
		return self.price >= other.price


	def __lt__(self, other):
		return self.price < other.price


	def __le__(self, other):
		return self.price <= other.price


	# =======================String Method========================== #
	def __str__(self):
		return 'Name: ' + self.name + '\nPrice: ' + f'{(str(self.price))}' + '\nLink: ' + self.link


class WebsitesCraping():
	'''
		Contains all the products that are scrapped in all the websites
		Product name should be as specific as possible to maximize the efficent of the search algorithm
	'''
	WEBSITE_NAME 	= ['cellphones', 
					   'tainghe', 
					   'thegioididong', 
					   'taingheviet', 
					   'dofzone', 
					   'tiki']


	def __init__(self, product_name, decending=False):
		self.product_name 		= product_name
		self.items				= [] # list contains all scrapped items 
		self.scrappedItems		= 10 # maximum items can be scrapped in 1 website
		self.decending			= decending
		self.sraping()


	def getSearchURL(self, website_name):
		'''
			Get the url when the product is search on website
		'''
		self.product_name 	= str(self.product_name).strip()

		if website_name in ('tiki', 'dofzone'):
			converted_name	= self.product_name.replace(' ', '%20')
		else:
			converted_name	= self.product_name.replace(' ', '+')

		return {
			'cellphones'	: 'https://cellphones.com.vn/catalogsearch/result/?q=',
			'tainghe'   	: 'https://tainghe.com.vn/tim?q=',
			'thegioididong'	: 'https://www.thegioididong.com/tim-kiem?key=',
			'taingheviet'	: 'https://taingheviet.com/tim-kiem.html?category=&key=',
			'dofzone'		: 'https://dof.zone/search?q=',
			'tiki'			: 'https://tiki.vn/search?q=',
		}.get(website_name) + converted_name


	def generateSoupObject(self, website_name):
		'''
			Generate soup object
		'''
		URL 		= self.getSearchURL(website_name)
		source 		= requests.get(URL, headers=headers)
		soup    	= BeautifulSoup(source.content, 'html.parser')

		return soup


	def checkForCorrectItem(self, item_name):
		'''
			Re-check the items' name to see whether its match the product name 
		'''
		words_in_search_name  	= self.product_name.split(' ')
		matched_words 			= 0

		for word in words_in_search_name:
			if word.lower() in item_name.lower():
				matched_words += 1

		return matched_words == len(words_in_search_name)
		

	def sraping(self):
		'''
			Scrapping process
			Differnt websites have different layous, therefore they need different way to scrap data
			All the items that sorted will be stored in the self.items in the ascending order by price by default
		'''
		for website in self.WEBSITE_NAME:
			soup 	= self.generateSoupObject(website)
			foundItems 	= []

			if website 		== 'thegioididong':
				class_name = {
					'phone'		: 'cat42',
					'headphone'	: 'cat54'
				}

				products 		= soup.find_all('li', class_=class_name.get('phone'))

				if len(products) == 0:
					products 	= soup.find_all('li', class_=class_name.get('headphone'))

				for product in products:
					if len(foundItems) >= self.scrappedItems:
						break

					name 	= product.h3.text
					if not self.checkForCorrectItem(name):
						continue
					
					price 	= product.strong.text
					link 	= 'https://www.thegioididong.com/' + product.a['href']
					foundItems.append(productObject(name, price, link))

			elif website 	== 'taingheviet':
				products = soup.find_all('div', class_='col-4')

				for product in products:
					if len(foundItems) >= self.scrappedItems:
						break

					name = product.find(class_='product__title').text

					if self.checkForCorrectItem(name):
						break

					price = product.span.text
					link  = product.find('a', class_='link-unstyled')['href']
					foundItems.append(productObject(name, price, link))

			elif website 	== 'dofzone':
				products  = soup.find_all('div', class_='product-block')
				for product in products:
					if len(foundItems) >= self.scrappedItems:
						break

					product_info 	= product.find('a', class_='prdListName img front')

					name 			= product_info['rel-name']
					if not self.checkForCorrectItem(name):
						continue

					price 			= product_info['rel-price']
					link 			= 'https://dof.zone' + product_info['href']
					foundItems.append(productObject(name, price, link))

			elif website 	== 'tiki':
				products  = soup.find_all('div', class_='product-item search-div-product-item')
				for product in products:
					if len(foundItems) >= self.scrappedItems:
						break

					name 			= product['data-title']
					if not self.checkForCorrectItem(name):
						continue

					price 			= product['data-price']
					link 			= product.find('a', class_='search-a-product-item')['href']
					foundItems.append(productObject(name, price, link))

			elif website 	== 'cellphones':
				products  = soup.find_all('div', class_='lt-product-group-info')
				for product in products:
					if len(foundItems) >= self.scrappedItems:
						break

					name 			= product.h3.text.replace('\t', '').replace('\n', '')
					if not self.checkForCorrectItem(name):
						continue

					price 			= product.find('span', class_='price').text
					link 			= product.a['href']
					foundItems.append(productObject(name, price, link))

			elif website 	== 'tainghe':
				products  = soup.find('div', class_='product-list').find_all('li', class_='item')
				for product in products:
					if len(foundItems) >= self.scrappedItems:
						break

					name 			= product.find('a', class_='p-name').text
					if not self.checkForCorrectItem(name):
						continue

					price 			= product.find('span', class_='p-price').text
					link 			= 'https://tainghe.com.vn' + product.find('a', class_='p-name')['href']
					foundItems.append(productObject(name, price, link))


			for product in foundItems:
				if product.price > 0:
					self.items.append(product)

		self.items.sort(reverse=self.decending)


	

# a = WebsitesCraping('tai nghe jabra 75t')
# print(a.items)
