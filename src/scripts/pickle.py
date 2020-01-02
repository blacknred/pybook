# Pickle
import pickle

shoplistfile = 'shoplist.data'  # имя файла, в котором мы сохраним объект
shoplist = ['яблоки', 'манго', 'морковь']  # список покупок
f = open(shoplistfile, 'wb')  # Запись в файл
pickle.dump(shoplist, f)  # помещаем объект в файл
f.close()
del shoplist  # уничтожаем переменную shoplist
f = open(shoplistfile, 'rb')  # Считываем из хранилища
storedlist = pickle.load(f)  # загружаем объект из файла
print(storedlist)
# Вывод:
#['яблоки', 'манго', 'морковь']
