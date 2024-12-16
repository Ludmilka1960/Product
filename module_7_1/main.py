

class Product:
    def __init__(self,name,weight:float,category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"Название:'{self.name}' ,Вес:{self.weight} ,Категория:'{self.category}'\n"


class Shop:
    __file_name = "product.txt"


    @classmethod
    def get_products(cls):
        try:
            with open(cls.__file_name,'r',encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self,*products):
        existing_products = self.get_products().splitlines()
        new_products = []
        for product in products :
            if product not in existing_products:
                new_products.append(product)
            else:
                print(f"Продукт {self.name} уже есть в магазине")
            if new_products:
                with open(self.__file_name,'a',encoding='utf-8') as file:
                    for product in new_products:
                        file.write(f"{product}\n")


s1 = Shop()
p1 = Product('Яблоко', 30.4, 'Фрукты')
p2 = Product('Помидор' , 5.4 , 'Овощи')
p3 = Product('Банан' , 15.1 , 'Фрукты')

s1.add(p1,p2)
s1.add(p2,p3)
print(s1.get_products())
p4 = Product('Помидор', 12.5, "Овощи")
s1.add(p4)
print(s1.get_products())


