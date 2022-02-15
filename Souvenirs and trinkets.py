souvenirs = 75
trinkets = 112

s = int(input('Введите количество сувениров: '))
t = int(input('Введите количество безделушек: '))

sm = s + souvenirs
tm = t + trinkets

package_weight = sm + tm

print(f"общий вес посылки: {package_weight} г")