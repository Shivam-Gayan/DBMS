import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def line_plot(df, x=None, y=None):
    # Check if both x and y are None
    if x is None and y is None:
        print("Error: At least one of 'x' or 'y' must be provided.")
        return
    
    if x is not None and x not in df.columns:
        print(f"Error: Column '{x}' does not exist in the DataFrame.")
        return
    if y is not None and y not in df.columns:
        print(f"Error: Column '{y}' does not exist in the DataFrame.")
        return
    if x is not None and y is not None:
        if df[x].dtype not in ["int64", "float64"] or df[y].dtype not in ["int64", "float64"]:
            print(f"Error: Columns are not numeric.")
            return
    elif x is None and y is not None:
        if df[y].dtype not in ["int64", "float64"]:
            print(f"Error: Column '{y}' is not numeric.")
            return
    elif x is not None and y is None:
        if df[x].dtype not in ["int64", "float64"]:
            print(f"Error: Column '{x}' is not numeric.")
            return

    name_x = input("Enter the label for x axis: ")
    name_y = input("Enter the label for y axis: ")
    title = input("Enter the title for the graph: ")

    if x is not None and y is not None:
        plt.plot(df[x], df[y])
    elif y is not None:
        plt.plot(df.index, df[y])
    elif x is not None:
        plt.plot(df.index, df[x])

    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(title)
    
    try:
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes":
            plt.savefig(f"{title}.png")
            plt.show()  
        elif choose == "no":
            plt.show()
    except:
        print("Please enter valid input.")

def bar_plot(df, columns):

    # Validate that all columns are present in the DataFrame
    for column in columns:
        if column not in df.columns:
            print(f"Error: Column '{column}' does not exist in the DataFrame.")
            return
    
    # Validate that all columns are numeric
    for column in columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            print(f"Error: Column '{column}' is not numeric.")
            return
    
    # Accept input for labels
    labels = []
    for column in columns:
        label = input(f"Enter the label for {column}: ")
        labels.append(label)

    # Plot the data
    df[columns].plot(kind='bar')
    
    # Set custom x-axis ticks and labels
    plt.xticks(ticks=range(len(df)), labels=df.index, rotation=45, ha='right')
    name_x = input("Enter the label for x axis: ")
    name_y = input("Enter the label for y axis: ")
    title = input("Enter the title for the graph: ")
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(title)
    plt.legend(labels)
    
    try:
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no":
            plt.show()
    except:
        print("please enter valid input")

def histogram(df):
    columnname = input("Enter the name of the attribute: ")

    if columnname in df.columns:
        plt.hist(df[columnname], bins=16, color='skyblue', edgecolor='black')
        plt.xlabel(columnname)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {columnname}')
        try:
            choose = input("Do you want to export the graph (yes/no): ").lower()
            if choose == "yes":
                plt.savefig(f"Histogram of {columnname}.png")
                plt.show()
            elif choose == "no":
                plt.show()
        except:
            print("please enter valid input")
    else:
        print("Column not found")


def pie_chart(df, size_column, labels_column=None):

    # Validate that size_column exists in the DataFrame
    if size_column not in df.columns:
        print(f"Error: Column '{size_column}' does not exist in the DataFrame.")
        return
    
    # Validate that size_column contains numeric values
    if not pd.api.types.is_numeric_dtype(df[size_column]):
        print(f"Error: Column '{size_column}' does not contain numeric values.")
        return
    
    # Extract sizes from the DataFrame
    sizes = df[size_column].tolist()
    
    # Extract labels from the DataFrame if provided
    if labels_column:
        # Validate that labels_column exists in the DataFrame
        if labels_column not in df.columns:
            print(f"Error: Column '{labels_column}' does not exist in the DataFrame.")
            return
        labels = df[labels_column].tolist()
    else:
        labels = df.index.tolist()
    
    # Plot the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    title = input("Enter the title for the graph: ")
    plt.title(title)
    
    try:
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no":
            plt.show()
    except:
        print("please enter valid input")

def stack_plot(df, columns):

    # Validate that all columns are present in the DataFrame
    for column in columns:
        if column not in df.columns:
            print(f"Error: Column '{column}' does not exist in the DataFrame.")
            return
    
    # Validate that all columns contain numeric values
    for column in columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            print(f"Error: Column '{column}' is not numeric.")
            return
    
    # Plot the stack plot
    plt.stackplot(df.index, *[df[column] for column in columns], labels=columns)
    name_x = input("Enter the label for x axis: ")
    name_y = input("Enter the label for y axis: ")
    title = input("Enter the title for the graph: ")
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(title)
    plt.legend()
    
    try:
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no":
            plt.show()
    except:
        print("please enter valid input")

def scatter_plot(df,column_x,column_y,size):
    
    if column_x not in df.columns:
        print(f"Error: Column '{column_x}' does not exist in the DataFrame.")
        return
    if column_y not in df.columns:
        print(f"Error: Column '{column_y}' does not exist in the DataFrame.")
        return
    
    if not pd.api.types.is_numeric_dtype(df[column_x]):
        print(f"Error: Column '{column_x}' does not contain numeric values.")
        return
    
    if not pd.api.types.is_numeric_dtype(df[column_y]):
        print(f"Error: Column '{column_y}' does not contain numeric values.")
        return
    
    df.plot.scatter(x=column_x,y=column_y, s=size)
    name_x = input("Enter the label for x axis: ")
    name_y = input("Enter the label for y axis: ")
    title = input("Enter the title for the graph: ")
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(title)
    
    try:
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no":
            plt.show()
    except:
        print("please enter valid input")