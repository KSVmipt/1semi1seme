import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(description="BudgetTracker - Ecxel file from bank to plots")
    parser.add_argument(
        '-f',
        '--file',
        type=str,
        default='a',
        help='input relative file directory'
    )
    arguments = parser.parse_args()
    file = str(arguments.file)
    print((file))
    return file

def loadData(nameOfFile):
    dataset = pd.read_excel(nameOfFile)
    return dataset
        
def showPlot(dataset):
    if dataset.empty != True:
        fig, ax = plt.subplots(constrained_layout=True)
        dataset['День'] = [int(x.split()[0]) for x in dataset['Дата']]

        sns.lineplot(
            data=dataset,
            x='День',
            y='Сумма',
            hue='Категория',
            ax=ax
        )
        ax.legend()
        plt.show()
    else:
        print("File not founded!")

def showBar(dataset):
    if dataset.empty != True:
        fig, ax = plt.subplots(constrained_layout=True)
        sns.barplot(
            data = dataset,
            y= 'Категория',
            x= 'Сумма',
            orient = 'h',
            estimator = 'sum',
            errorbar=None,
            ax=ax
        )
        plt.show()
    else:
        print("File not founded!")

try:
    showBar(loadData(parseArgs()))
    showPlot(loadData(parseArgs()))
except FileNotFoundError:
    print('Ошибка файл не найден или не существует!')