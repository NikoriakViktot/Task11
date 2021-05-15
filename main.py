class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class Product_Store(Product):

    def add(self, product, amount):
        self.product = product
        self.amount = amount

    def set_discount (self, identifier, percent, identifier_type="name" ):
        self.identifier = identifier
        self.percent = percent
        self.identifier_type = identifier_type

    def sell_product(self, product_name, amount):
        self.product_name = product_name
        self.amount = amount


    def get_income(self):
        #сума проданих товарів

    def get_all_products(self):
        # всі товари в магазині

      def get_product_info(self, product_name):
          self.product_name = product_name
        return
    # кортеж з назвою продукта та кількістю в магазині



if __name__ == '__main__':

    product1 = Product( 'Холодильник' , 'Sumsung',  59.95)
    product2 = Product( 'Телевізор' 'Sumsung', 34.95)
    product3 = Product('Телефон', 'Sumsung', 14.95)


