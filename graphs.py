import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def customize_plot():
    """
    Interactively customize the current plot based on user input.
    """
    customizations = {}

    # Grid option
    grid = input("Do you want to add a grid? (yes/no, default: no): ").strip().lower() or 'no'
    customizations['grid'] = True if grid == 'yes' else False
    print()
    print("Press enter to skip")
    print()
    # Background color
    color = input("Enter background color (e.g., lightgray, white, etc., default: white): ").strip() or 'white'
    customizations['color'] = color

    # Font size
    fontsize = input("Enter font size (e.g., 12, 14, 16, default: 12): ").strip()
    customizations['fontsize'] = int(fontsize) if fontsize.isdigit() else 12

    # Font family
    fontfamily = input("Enter font family (e.g., serif, sans-serif, default: sans-serif): ").strip() or 'sans-serif'
    customizations['fontfamily'] = fontfamily

    # Font weight
    fontweight = input("Enter font weight (e.g., normal, bold, default: normal): ").strip() or 'normal'
    customizations['fontweight'] = fontweight

    # Tick rotation
    rotation = input("Enter rotation angle for ticks (e.g., 0, 45, 90, default: 0): ").strip()
    customizations['rotation'] = int(rotation) if rotation.isdigit() else 0

    # Tick marker length
    tick_markers = input("Enter tick marker length (e.g., 5, 10, default: 5): ").strip()
    customizations['tick_markers'] = int(tick_markers) if tick_markers.isdigit() else 5

    apply_customizations(customizations)

def apply_customizations(customizations):
    """
    Apply customizations to the current plot.

    Parameters:
    customizations (dict): A dictionary containing customization options.
    """
    if 'grid' in customizations:
        plt.grid(customizations['grid'])
    
    if 'color' in customizations:
        plt.gca().set_facecolor(customizations['color'])
    
    if 'fontsize' in customizations:
        plt.rcParams.update({'font.size': customizations['fontsize']})
    
    if 'fontfamily' in customizations:
        plt.rcParams.update({'font.family': customizations['fontfamily']})
    
    if 'fontweight' in customizations:
        plt.rcParams.update({'font.weight': customizations['fontweight']})
    
    if 'rotation' in customizations:
        plt.xticks(rotation=customizations['rotation'])
        plt.yticks(rotation=customizations['rotation'])
    
    if 'tick_markers' in customizations:
        plt.tick_params(axis='both', which='both', length=customizations['tick_markers'])
    
    plt.tight_layout()

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
        customize = input("Do you want to customize the graph (yes/no): ").lower()
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes" and customize == "yes":
            customize_plot()
            plt.savefig(f"{title}.png")
            plt.show()  
        elif choose == "no" and customize == "yes":
            customize_plot()
            plt.show()
        elif choose == "yes" and customize_plot() == "no":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no" and customize_plot() == "no":
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
        customize = input("Do you want to customize the graph (yes/no): ").lower()
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes" and customize == "yes":
            customize_plot()
            plt.savefig(f"{title}.png")
            plt.show()  
        elif choose == "no" and customize == "yes":
            customize_plot()
            plt.show()
        elif choose == "yes" and customize_plot() == "no":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no" and customize_plot() == "no":
            plt.show()
    except:
        print("Please enter valid input.")


def histogram(df):
    columnname = input("Enter the name of the attribute: ")

    if columnname in df.columns:
        plt.hist(df[columnname], bins=16, color='skyblue', edgecolor='black')
        plt.xlabel(columnname)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {columnname}')
    else:
        print("Column not found")
    try:
        customize = input("Do you want to customize the graph (yes/no): ").lower()
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes" and customize == "yes":
            customize_plot()
            plt.savefig(f"Histogram of {columnname}.png")
            plt.show()  
        elif choose == "no" and customize == "yes":
            customize_plot()
            plt.show()
        elif choose == "yes" and customize_plot() == "no":
            plt.savefig(f"Histogram of {columnname}.png")
            plt.show()
        elif choose == "no" and customize_plot() == "no":
            plt.show()
    except:
        print("Please enter valid input.")



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
        customize = input("Do you want to customize the graph (yes/no): ").lower()
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes" and customize == "yes":
            customize_plot()
            plt.savefig(f"{title}.png")
            plt.show()  
        elif choose == "no" and customize == "yes":
            customize_plot()
            plt.show()
        elif choose == "yes" and customize_plot() == "no":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no" and customize_plot() == "no":
            plt.show()
    except:
        print("Please enter valid input.")

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
        customize = input("Do you want to customize the graph (yes/no): ").lower()
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes" and customize == "yes":
            customize_plot()
            plt.savefig(f"{title}.png")
            plt.show()  
        elif choose == "no" and customize == "yes":
            customize_plot()
            plt.show()
        elif choose == "yes" and customize_plot() == "no":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no" and customize_plot() == "no":
            plt.show()
    except:
        print("Please enter valid input.")

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
        customize = input("Do you want to customize the graph (yes/no): ").lower()
        choose = input("Do you want to export the graph (yes/no): ").lower()
        if choose == "yes" and customize == "yes":
            customize_plot()
            plt.savefig(f"{title}.png")
            plt.show()  
        elif choose == "no" and customize == "yes":
            customize_plot()
            plt.show()
        elif choose == "yes" and customize_plot() == "no":
            plt.savefig(f"{title}.png")
            plt.show()
        elif choose == "no" and customize_plot() == "no":
            plt.show()
    except:
        print("Please enter valid input.")
