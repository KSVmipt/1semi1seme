import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(description="BudgetTracker - Excel file from bank to plots")
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
    if nameOfFile[-4:] == 'xlsx':
        dataset = pd.read_excel(nameOfFile)
        return dataset
    else:
        print("Error, your file isn't Excel file. Format of Excel file is xlsx!")
        return 0
        
def showPlot(dataset):
    try:
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
    except AttributeError:
        return 0

def showBar(dataset):
    try:
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
    except AttributeError:
        return 0
    

def startScript():
    try:
        showBar(loadData(parseArgs()))
        showPlot(loadData(parseArgs()))
        print('All works without errors!')
    except FileNotFoundError:
        print("Error! File don't finded!")

startScript()