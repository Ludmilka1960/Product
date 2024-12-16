from fileinput import close

__file_name = "E:\product.txt"
f = open('products.txt''w')
s = f.read()
print(s)
f.close()
f = open('products.txt''r')
s = f.read()
print(s)
f.close()
f = open('products.txt''w')
s = f.read()
print(s)
close()


