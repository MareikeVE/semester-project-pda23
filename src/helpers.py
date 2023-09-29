import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



def merged_data(df1, df2):
    #merge test and training data from paper to randomly separate later
    total_adult_data_df = pd.concat([df1, df2], axis=0)

    # Replace all '?' with np.NaN
    total_adult_data_df = total_adult_data_df.replace('?', np.NaN)

    return total_adult_data_df




def replace_data_income(df, column):
    def replace_data(df, column):
        df[column] = df[column].replace('<=50K.', '<=50K')
        df[column] = df[column].replace('>50K.', '>50K')

        return df



def create_diagram(df, column):
    # Create a new figure for each chart
    plt.figure(figsize=(12, 10))

    # Check the data type of the column
    if df[column].dtype == 'object':
        # Create a bar chart for categorical data
        sns.countplot(data=df, x=column)
        plt.xticks(rotation=45)
        plt.title(f'Balkendiagramm für die Variable {column.capitalize()}')
    else:
        # Create a histogram for numerical data
        sns.histplot(data=df, x=column, kde=True)
        plt.title(f'Histogramm für die Variable {column.capitalize()}')

    # Show the chart
    plt.tight_layout()
    plt.show()


def create_diagrams(df):
    # Loop through the columns of the DataFrame
    df.reset_index(drop=True, inplace=True)
    for column in df.columns:
        create_diagram(df, column)



def create_bar_diagram_relationship(df, column1, column2):
    plt.figure(figsize=(8, 6))
    sns.countplot(x=column1, hue=column2, data=df)
    plt.xlabel(column1.capitalize())
    plt.ylabel('Count')
    plt.title(f'Beziehung zwischen {column1.capitalize()} and {column2.capitalize()}')

    plt.show()

def create_boxplot_diagram_relationship(df, column1, column2):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=column1, y=column2, data=df)
    plt.xlabel('Sex')
    plt.ylabel('Hours per Week')
    plt.title(f'Box Plot {column1.capitalize()} and {column2.capitalize()}')

    plt.show()