import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Загружаем
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())  # Колво точек
    data = []
    for line in lines[1:n + 1]:
        x, y = map(float, line.strip().split())
        data.append((x, y))

    return pd.DataFrame(data, columns=['X', 'Y'])


def plot_data(df, file_name):
    """
    Картинка
    """
    plt.figure(figsize=(8, 5))
    plt.scatter(df['X'], df['Y'], color='b', label=f'Кол-во точек: {len(df)}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'График данных {file_name}')
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.savefig(f"{file_name}.png")
    plt.close()


# тело
for i in range(1, 6):
    file_name = f"C:/Users/Михаил/Desktop/хрюникс/4сем/{i:03d}.dat"
    df = load_data(file_name)
    plot_data(df, f"plot_{i:03d}")
