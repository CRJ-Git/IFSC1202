x = int(input("Please enter a two digit number: "))

swaptens = x % 10
swapones = x // 10

print("Swapped Number:","{:>2d}{:<2d}".format(swaptens, swapones))