import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Месяц": [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ],
    "Книги_2023": [3, 2, 4, 5, 6, 4, 3, 2, 5, 6, 4, 7],
    "Страницы_2024": [320, 280, 450, 500, 620, 480, 390, 350, 540, 610, 470, 700]
}

df = pd.DataFrame(data)


def plot_books_2023(df):
    plt.plot(
        df["Месяц"],
        df["Книги_2023"],
        marker='o',
        color='red',
        label='Прочитано книг'
    )
    plt.title("Прочитанные книги 2023")
    plt.xlabel("Месяцы")
    plt.ylabel("Количество книг")
    plt.grid(True)
    plt.legend()


def plot_pages_2024(df):
    plt.bar(
        df["Месяц"],
        df["Страницы_2024"],
        color='green',
        label='Прочитано страниц'
    )
    plt.title("Прочитанные страницы 2024")
    plt.xlabel("Месяцы")
    plt.ylabel("Количество страниц")
    plt.grid(True)
    plt.legend()


plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plot_books_2023(df)

plt.subplot(1, 2, 2)
plot_pages_2024(df)

plt.tight_layout()
plt.show()
