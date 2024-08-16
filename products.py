import os


def read_file(filename, products):
	
	with open (filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
	return products

# 能讓使用者輸入的程式
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append ([name, price])
	return products

# 印出購買紀錄的程式
def print_products(products):
	for p in products:
		print(p[0], '的商品價格是', p[1])

# 寫入檔案的程式
def write_file(filename, products):
	with open (filename, 'w') as f:
		f.write('商品' + ',' + '價格' + '\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	products = []
	filename = 'products.csv'
	if os.path.isfile(filename):# 檢查檔案在不在
		print('電腦:我有找到檔案喔!')
		products = read_file(filename, products)
	else:
		print('電腦:阿喔!找不到檔案呢!趕快輸入商品和價格來建立一個吧!')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

	