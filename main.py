import pandas as pd
import numpy as np
from matplotlib import pyplot
from matplotlib.ticker import FuncFormatter
from scipy import stats

file_mau = pd.read_excel(r"data.xlsx", skipfooter=5, sheet_name="Sheet1")

lista = (file_mau['Tuổi'].unique())
listb = (file_mau[2019].unique())
listc = (file_mau[2021].unique())
listd = (file_mau[2020].unique())

def calculate (year):
    # Chuyển cột "2020" thành một Series
    data = file_mau[year]

    # Tính mean (trung bình)
    mean_value = data.mean()

    # Tính median (trung vị)
    median_value = data.median()

    # Tính mode (mode)
    mode_value = data.mode()[0]  # Mode có thể trả về nhiều giá trị, chọn giá trị đầu tiên

    # Tính phương sai (Variance)
    variance_value = data.var()

    # Tính độ lệch chuẩn (Standard Deviation)
    std_dev_value = data.std()

    # Tính tổng (Sum)
    sum_value = data.sum()

    # Tìm giá trị lớn nhất (Maximum)
    max_value = data.max()

    # Tìm giá trị nhỏ nhất (Minimum)
    min_value = data.min()

    # Độ tin cậy (confidence level)
    confidence_level = float(input("Enter confidence level:"))

    # Số lượng quan sát trong mẫu
    n = len(data)

    # Độ tự do (degrees of freedom)
    df = n - 1

    # Mean của mẫu
    mean = np.mean(data)

    # Độ lệch chuẩn của mẫu
    std_dev = np.std(data, ddof=1)

    # Tính margin of error
    margin_of_error = stats.t.ppf((1 + confidence_level) / 2, df) * (std_dev / np.sqrt(n))

    # Tính confidence interval
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    print("Year:", year)
    print("Mean (Trung bình):", mean_value)
    print("Median (Trung vị):", median_value)
    print("Mode (Mode):", mode_value)
    print("Variance (Phương sai):", variance_value)
    print("Standard Deviation (Độ lệch chuẩn):", std_dev_value)
    print("Sum (Tổng):", sum_value)
    print("Maximum (Tối đa):", max_value)
    print("Minimum (Tối thiểu):", min_value)
    print("Confidence Interval: ({:.2f}, {:.2f})".format(lower_bound, upper_bound))
    print("------------------------------------------")

while True:
    user_input = input("Enter a year (Enter '0' to exit): ")
    if user_input == '0':
        print("Exiting the loop...")
        break
    else:
        calculate(int (user_input))


def millions_formatter(x, pos):
    # Formatter function to convert numbers to millions.
    return '{:.0f}'.format(x)

def draw_multiline(a, b, c, d):
    ages = a
    year19 = b
    year20 = c
    year21 = d
    # pyplot.style.use('dark_background')
    ages = np.arange(len(a)) 
    width = 0.25

    pyplot.bar(ages - width, year19, width, color='red', label='Year 19')
    pyplot.bar(ages, year20, width, color='#000BFF', label='Year 20')
    pyplot.bar(ages + width, year21, width, color='#B40062', label='Year 21')
    
    pyplot.xlabel("2019 ,2020, 2021")
    pyplot.ylabel("People (Million)")
    pyplot.title("Số lao động có việc làm trong nền kinh tế")
    pyplot.legend(['Year 2019', 'Year 2020', 'Year 2021']) 
    pyplot.grid(True)
    pyplot.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))  # Apply custom formatter
    pyplot.xticks(ages, a)
    pyplot.savefig("multiline.png")
    pyplot.show()

draw_multiline(lista, listb, listc, listd)

