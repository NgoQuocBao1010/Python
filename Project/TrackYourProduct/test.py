'''
def getSearchURL(product_name, website_name):
		
		product_name 	= str(product_name)
		product_name 	= product_name.strip()

		if website_name in ('tiki', 'dofzone'):
			converted_name	= product_name.replace(' ', '%20')
		else:
			converted_name	= product_name.replace(' ', '+')

		return {
			'cellphones'	: 'https://cellphones.com.vn/catalogsearch/result/?q=',
			'tainghe'   	: 'https://tainghe.com.vn/tim?q=',
			'thegioididong'	: 'https://www.thegioididong.com/tim-kiem?key=',
			'taingheviet'	: 'https://taingheviet.com/tim-kiem.html?category=&key=',
			'dofzone'		: 'https://dof.zone/search?q=',
			'tiki'			: 'https://tiki.vn/search?q=',
		}.get(website_name) + converted_name


# *********************** Handle Websites ***********************#
# Each website has different layout, so each of them requires seperate function to retrieve information

def thegioididong(product_name):
	URL = getSearchURL(product_name, 'thegioididong')
	result = []

	class_name = {
		'phone'		: 'cat42',
		'headphone'	: 'cat54'
	}

	source 		= requests.get(URL, headers=headers)
	soup    	= BeautifulSoup(source.content, 'html.parser')

	products 		= soup.find_all('li', class_=class_name.get('phone'))

	if len(products) == 0:
		products 	= soup.find_all('li', class_=class_name.get('headphone'))

	for product in products:
		name 	= product.h3.text
		price 	= product.strong.text
		link 	= 'https://www.thegioididong.com/' + product.a['href']
		result.append((name, price, link))

		if len(result) > 2:
			break

	return result


def taingheviet(product_name):
	URL = getSearchURL(product_name, 'taingheviet')
	result = []

	source = requests.get(URL, headers=headers)
	soup    = BeautifulSoup(source.content, 'html.parser')

	for product in soup.find_all('div', class_='col-4'):
		name = product.find(class_='product__title').text
		price = product.span.text
		link  = product.find('a', class_='link-unstyled')['href']
		result.append((name, price, link))

		if len(result) > 2:
			break

	return result


def dofzone(product_name):
	URL = getSearchURL(product_name, 'dofzone')
	result = []

	source = requests.get(URL, headers=headers)
	soup    = BeautifulSoup(source.content, 'html.parser')

	for product in soup.find_all('div', class_='product-block'):
		product_info 	= product.find('a', class_='prdListName img front')
		name 			= product_info['rel-name']
		price 			= product_info['rel-price']
		link 			= 'https://dof.zone' + product_info['href']

		result.append((name, price, link))

		if len(result) > 2:
			break

	return result


def tiki(product_name):
	URL = getSearchURL(product_name, 'tiki')
	result = []

	source = requests.get(URL, headers=headers)
	soup    = BeautifulSoup(source.content, 'html.parser')

	for product in soup.find_all('div', class_='product-item search-div-product-item'):
		name 	= product['data-title']
		price 	= product['data-price']
		link 	= product.find('a', class_='search-a-product-item')['href']
		result.append((name, price, link))

		if len(result) > 2:
			break

	return result


def cellphones(product_name):
	URL = getSearchURL(product_name, 'cellphones')
	result = []

	source = requests.get(URL, headers=headers)
	soup    = BeautifulSoup(source.content, 'html.parser')

	for product in soup.find_all('div', class_='lt-product-group-info'):

		name 	= product.h3.text.replace('\t', '').replace('\n', '')
		price 	= product.find('span', class_='price').text
		link 	= product.a['href']

		if price != 'Sắp về hàng':
			result.append((name, price, link))

		if len(result) > 2:
			break

	return result


def tainghe(product_name):
	URL = getSearchURL(product_name, 'tainghe')
	result = []

	source = requests.get(URL, headers=headers)
	soup    = BeautifulSoup(source.content, 'html.parser')

	products = soup.find('div', class_='product-list').find_all('li', class_='item')

	for product in products:
		name 	= product.find('a', class_='p-name').text
		price 	= product.find('span', class_='p-price').text
		link 	= 'https://tainghe.com.vn' + product.find('a', class_='p-name')['href']
		result.append((name, price, link))

		if len(result) > 2:
			break

	return result
'''

t1 = '20000mAh'
print(t1.lower())