import matplotlib.pyplot as plt

# data = [1, 2.5, 2, 3.2, 3, 3.4, 4, 4.1, 4.3]
# plt.hist(data)
# plt.show()

x = ['Дизайн', 'Строители', 'Кухня', 'Стройматериалы', 'Межкомнатные двери', 'Техника', 'Заливка пола']
#       1         2            3           4                    5                 6           7         

x_diz = 60000
x_stroitel = 15000 + 10000 + 10000 + 15000 + 20000 + 200000
x_kuhnya = 220000
x_material = 126000 + 5000 + 72000 + 167000 + 22000 + 12000
x_dveri = 90000
x_tehn = 150000 + 50000
x_pol = 75000
y = [x_diz, x_stroitel, x_kuhnya, x_material, x_dveri, x_tehn, x_pol]

plt.bar(x, y)
plt.ylabel("price")
plt.title("название ")
plt.show()