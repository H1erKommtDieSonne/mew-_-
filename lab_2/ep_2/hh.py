import numpy as np
import matplotlib.pyplot as plt
import glob
import os


folder_path = "C:/Users/Михаил/Desktop/хрюникс/4сем/2laba/2/signals/"
file_names = glob.glob(folder_path + "signal*.dat")


for file_name in file_names:

    data = np.loadtxt(file_name)
    n = len(data)


    threshold = 3 * np.std(data)
    data_cleaned = np.where(np.abs(data) > threshold, np.median(data), data)


    window_size = min(10, len(data_cleaned))
    kernel = np.ones(window_size) / window_size
    data_smoothed = np.convolve(data_cleaned, kernel, mode='same')


    plt.figure(figsize=(12, 6))
    plt.plot(data, label='Оригинальный сигнал', alpha=0.5, color='blue')
    plt.plot(data_smoothed, label='Сглаженный сигнал', linewidth=2, color='red')
    plt.legend()
    plt.title(f"Обработка данных: {os.path.basename(file_name)}")
    plt.grid()

    output_file = f"{file_name.split('.')[0]}.png"
    plt.savefig(output_file)
    plt.close()
