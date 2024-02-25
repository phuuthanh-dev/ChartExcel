import pandas as pd
import numpy as np
from matplotlib import pyplot
from matplotlib.ticker import FuncFormatter

file_mau = pd.read_excel(r"data.xlsx", sheet_name="Sheet1")

# print(file_mau.columns)
# print(file_mau.loc[file_mau['Tuổi'] == "15-19", 2013].sum())

lista = (file_mau['Tuổi'].unique())
print(lista)
listb = (file_mau[2020].unique())
print(listb)
listc = (file_mau[2021].unique())
print(listc)
listd = (file_mau[2019].unique())
print(listd)

# res = [eval(i) for i in listb]

# for tb in lista:
#     lista.__add__ = print(file_mau.loc[file_mau['education'] == tb, 'income'].sum())

def millions_formatter(x, pos):
    """
    Formatter function to convert numbers to millions.
    """
    return '{:.0f}'.format(x)

def draw_multiline(a, b, c, d):
    ages = a
    year20 = b
    year21 = c
    year22 = d
    # pyplot.style.use('dark_background')
    ages = np.arange(len(a)) 
    width = 0.25

    pyplot.bar(ages - width, b, width, color='red', label='Company A')
    pyplot.bar(ages, c, width, color='#000BFF', label='Company B')
    pyplot.bar(ages + width, d, width, color='#B40062', label='Company C')
    
    pyplot.xlabel("2019 ,2020, 2021")
    pyplot.ylabel("People (Million)")
    pyplot.title("Số lao động có việc làm trong nền kinh tế")
    pyplot.legend(['Year 2018', 'Year 2019', 'Year 2020']) 
    pyplot.grid(True)
    pyplot.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))  # Apply custom formatter
    pyplot.xticks(ages, a)
    pyplot.savefig("multiline.png")
    pyplot.show()

draw_multiline(lista, listb, listc, listd)

