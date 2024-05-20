import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from function import file_auto_detection,create_new_df,modify_dataframe_columns,modify_dataframe_rows,clean_dataframe,view_dataframe,manage_dataframe,write_changes
from graphs import line_plot,bar_plot,histogram,pie_chart,stack_plot

def main(): 
    try:
        print("To open an existing file press 1\nTo work with a new file press 2")
        while True:
            try:
                file = int(input("\nWhat do you want to do? "))
                if file < 1 or file > 2:
                    print("Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        if file == 1:
            try:
                df = file_auto_detection()
            except Exception as e:
                print(f"An error occurred while opening the file: {e}")
                df = None
        elif file == 2:
            df = create_new_df()
        else:
            df = None

        if df is not None:
            while True:
                try:
                    print()
                    print("Modify columns - 1 \t Modify rows - 2 \t Clean data - 3")
                    print("View dataframe - 4 \t Manage dataframe - 5 \t Graphs - 6")
                    print("Enter 'quit' to exit.\t Note: file changes will be saved ")
                    print("Press enter to go back")
                    choice = input(">").lower()
                    if choice == "quit":
                        file_path = input("Enter the file path to save changes: ")
                        try:   
                            write_changes(df, file_path)
                        except ValueError as e :
                            print("An error occured while writing data to file")
                            break
                        break
                    choice = int(choice)  # Convert input to int for menu options
                    if choice == 1:
                        modify_dataframe_columns(df)
                    elif choice == 2:
                        modify_dataframe_rows(df)
                    elif choice == 3:
                        clean_dataframe(df)
                    elif choice == 4:
                        view_dataframe(df)
                    elif choice == 5:
                        manage_dataframe(df)
                    elif choice == 6:
                        print()
                        print("Line plots - 1 \t Bar plots - 2 \t Histograms - 3\nPie charts - 4 \t Area plots - 5")
                        choose = int(input("Enter the graph no. to plot: "))
                        if choose == 1:
                            column_x = input("Enter the name of the column for x axis (case sensitive): ")
                            column_y = input("Enter the name of the column for y axis (case sensitive): ")
                            line_plot(df, column_x, column_y)
                        elif choose == 2:
                            try:
                                no_of_columns = int(input("Enter the no. of columns you want to use: "))
                                columns_list = []
                                for i in range(no_of_columns):
                                            columns = input("Enter name of the columns (case sensitive): ")
                                            columns_list.append(columns)
                            except:
                                print("please enter a valid no.")
                            bar_plot(df,columns_list)
                        elif choose == 3:
                            histogram(df)
                        elif choose == 4:
                            column_data = input("Enter the column to be used as data: ")
                            column_label = input("Enter the column to be used as label: ")
                            pie_chart(df,column_data,column_label)
                        elif choose == 5:
                            no_of_columns = int(input("Enter no. of columns you want to use: "))
                            column = []
                            for i in range(no_of_columns):
                                column_data = input(f"Enter column name {i+1} (case sensitive):")
                                column.append(column_data)      
                            stack_plot(df,column)                     
                        else:
                            None
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter a valid number.")
                except Exception as e:
                    print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()