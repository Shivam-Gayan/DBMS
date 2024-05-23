import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

def file_auto_detection(): # to automatically read file according to their file type
    file_formats = {
        "xlsx": pd.read_excel,
        "xls": pd.read_excel,
        "csv": pd.read_csv,
        "html": pd.read_html,
        "json": pd.read_json,
        "parquet": pd.read_parquet,
        "feather": pd.read_feather,
        "pickle": pd.read_pickle,
        "stata": pd.read_stata,
        "sas": pd.read_sas,
        "spss": pd.read_spss,
        "fwf": pd.read_fwf,
    }
    
    files = input("Enter file path: ")
    file_extension = files.split(".")[-1]  # file extension

    if file_extension in file_formats:
        df = file_formats[file_extension](files)
        return df
    else:
        print("File type not supported.")
        return None
    
def create_new_df():
    data = {}
    column_types = {}
    
    # List of valid pandas data types
    valid_dtypes = [
        'int', 'float', 'str', 'bool', 'datetime', 'category', 'timedelta'
    ]
    
    # Collect column names and their data types
    print("Note: if the columns are not given by the user empty dataframe will be created.")
    while True:
        column_name = input("Enter column name (press Enter to stop adding columns): ")
        if column_name == "":
            break
        else:
            if column_name in data:
                print(f"Column name '{column_name}' already exists. Please enter a unique column name.")
            else:
                while True:
                    column_type = input(f"Enter data type for column '{column_name}' ({', '.join(valid_dtypes)}): ").strip().lower()
                    if column_type in valid_dtypes:
                        break
                    else:
                        print(f"Invalid data type. Please enter one of the following: {', '.join(valid_dtypes)}.")
                data[column_name] = []
                column_types[column_name] = column_type
    
    if not data:
        print("No columns added. DataFrame creation aborted.")
        return pd.DataFrame()  # Return an empty DataFrame
    
    # Collect row data
    num_columns = len(data)
    while True:
        row_data = input("Enter row data separated by commas (press Enter to stop adding rows): ")
        if row_data == "":
            break
        else:
            row_values = row_data.split(",")
            if len(row_values) != num_columns:
                print(f"Error: Expected {num_columns} values, but got {len(row_values)}. Please try again.")
                continue
            for i, col_name in enumerate(data.keys()):
                try:
                    if column_types[col_name] == 'int':
                        data[col_name].append(int(row_values[i]))
                    elif column_types[col_name] == 'float':
                        data[col_name].append(float(row_values[i]))
                    elif column_types[col_name] == 'bool':
                        data[col_name].append(row_values[i].strip().lower() in ['true', '1', 'yes'])
                    elif column_types[col_name] == 'datetime':
                        data[col_name].append(pd.to_datetime(row_values[i]))
                    elif column_types[col_name] == 'timedelta':
                        data[col_name].append(pd.to_timedelta(row_values[i]))
                    elif column_types[col_name] == 'category':
                        data[col_name].append(row_values[i])
                    else:
                        data[col_name].append(row_values[i])
                except ValueError as e:
                    print(f"Error: {e}. Please enter the row data again.")
                    # Remove the partially added row values
                    for col in data.keys():
                        if len(data[col]) > len(data[col]) - num_columns:
                            data[col] = data[col][:-1]
                    break
            else:
                continue
            break
    
    # Create DataFrame and convert to appropriate data types
    df = pd.DataFrame(data)
    for col_name, col_type in column_types.items():
        try:
            if col_type == 'category':
                df[col_name] = df[col_name].astype('category')
            elif col_type == 'datetime':
                df[col_name] = pd.to_datetime(df[col_name])
            elif col_type == 'timedelta':
                df[col_name] = pd.to_timedelta(df[col_name])
            else:
                df[col_name] = df[col_name].astype(col_type)
        except Exception as e:
            print(f"Error converting column '{col_name}' to {col_type}: {e}")
    
    print("DataFrame created successfully")
    return df


def modify_dataframe_columns(df): # to modify column
    print()
    print("1 - add a column \n2 - insert column at a specified index \n3 - remove a column \n4 - set column index \n5 - change column names")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Add a column
        column_name = input("Enter the name of the new column: ")
        column_data = input("Enter data for the new column separated by commas: ").split(',')
        df[column_name] = column_data

    elif choice == "2":
        # Insert column at a specified index
        column_name = input("Enter the name of the new column: ")
        column_data = input("Enter data for the new column separated by commas: ").split(',')
        index = int(input("Enter the index where you want to insert the column: "))
        df.insert(index, column_name, column_data)

    elif choice == "3":
        # Remove a column
        column_name = input("Enter the name of the column to remove: ")
        df.drop(columns=[column_name], inplace=True)
    
    elif choice == "4":
        #set index of columns
        column_name = input("Enter new indexes for the columns separated by commas: ").split(',')
        df.columns = column_name

    elif choice == "5":
        #change column names
        new_names = {}
        for column in df.columns:
            new_name = input(f"Enter new name for column '{column}': ")
            new_names[column] = new_name
            df.rename(columns=new_names, inplace=True)
    else:
        print()
    print()
    return df

def modify_dataframe_rows(df):
    print()
    print("1 - Add a row \n2 - Insert a row at a specified index \n3 - Remove a row \n4 - Set labeled row indexes")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Add a row
        new_row = {}
        for column in df.columns:
            value = input(f"Enter value for column '{column}': ")
            new_row[column] = value
        df = df.append(new_row, ignore_index=True)

    elif choice == "2":
        # Insert row at a specified index
        index = int(input("Enter the index where you want to insert the row: "))
        new_row = {}
        for column in df.columns:
            value = input(f"Enter value for column '{column}': ")
            new_row[column] = value
        df = df.append(new_row, ignore_index=True)
        df = df.reindex([*df.index[:index], len(df.index), *df.index[index:]])

    elif choice == "3":
        # Remove a row
        index = int(input("Enter the index of the row to remove: "))
        df = df.drop(index=index,inplace=True)

    elif choice == "4":
        # Set labeled row indexes
        new_index_labels = input("Enter new index labels for the rows separated by commas: ").split(',')
        df.index = new_index_labels

    else:
        print()

    return df

def clean_dataframe(df):
    print()
    print("1 - Handle Missing Values \n2 - Remove Duplicates \n3 - Drop Rows or Columns \n4 - Fill Missing Values \n5 - Reset Index")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Handle missing values
        print("Fill missing values:")
        print("1. Forward fill")
        print("2. Backward fill")
        print("3. Fill with custom value")
        fill_choice = input("Enter your choice: ")

        if fill_choice == "1":
            df.fillna(method='ffill', inplace=True)  # Forward fill missing values
        elif fill_choice == "2":
            df.fillna(method='bfill', inplace=True)  # Backward fill missing values
        elif fill_choice == "3":
            custom_value = input("Enter value to fill missing values with: ")
            df.fillna(custom_value, inplace=True)
        else:
            print("Invalid choice")

    elif choice == "2":
        # Remove duplicates
        df.drop_duplicates(inplace=True)

    elif choice == "3":
        # Drop rows or columns
        drop_choice = input("Drop rows or columns? (R for rows, C for columns): ").upper()
        if drop_choice == "R":
            indices = input("Enter indices of rows to drop (comma-separated): ").split(',')
            df.drop(indices, axis=0, inplace=True)
        elif drop_choice == "C":
            columns = input("Enter names of columns to drop (comma-separated): ").split(',')
            df.drop(columns, axis=1, inplace=True)
        else:
            print("Invalid choice")

    elif choice == "4":
        # Fill missing values
        value = input("Enter value to fill missing values with: ")
        df.fillna(value, inplace=True)

    elif choice == "5":
        # Reset index
        df.reset_index(drop=True, inplace=True)

    else:
        print()

    return df

def view_dataframe(df):
    print()
    print("1 - View by Label \n2 - View by Index \n3 - View first n records \n4 - View Last n records")

    choice = input("Enter your choice: ")

    if choice == "1":
        # View by label (loc)
        label = input("Enter row label or column name (comma-separated if both): ").split(',')
        if len(label) == 1:
            print(df.loc[label[0]])
        elif len(label) == 2:
            print(df.loc[label[0], label[1]])
        else:
            print("Invalid input")

    elif choice == "2":
        # View by index (iloc)
        index = input("Enter row index or column index (comma-separated if both): ").split(',')
        index = [int(i) if i.isdigit() else i for i in index]  # Convert to int if index is numeric
        if len(index) == 1:
            print(df.iloc[index[0]])
        elif len(index) == 2:
            print(df.iloc[index[0], index[1]])
        else:
            print("Invalid input")
    elif choice == "3":
        try:
            choose = int(input("Enter no. of n records to view: "))
        except:
            print("Must be validate data")
        print(df.head(choose))
    elif choice == "4":
        try:
            choose = int(input("Enter no. of n records to view: "))
        except:
            print("Must be validate data")
        print(df.tail(choose))
    else:
        print("Invalid choice")
    return None

def manage_dataframe(df):
    print()
    print("DataFrame Management Options:")
    print("1 - View DataFrame Info")
    print("2 - Change DataFrame Settings")
    print("3 - Count Values")
    print("4 - Transpose DataFrame and Export")

    choice = input("Enter your choice: ")

    if choice == "1":
        # View DataFrame Info
        print(df.info())

    elif choice == "2":
        # Change DataFrame Settings
        print("Current Settings:")
        print(f"1. Display Max Rows: {pd.get_option('display.max_rows')}")
        print(f"2. Display Max Columns: {pd.get_option('display.max_columns')}")
        print(f"3. Display Width: {pd.get_option('display.width')}")
        print(f"4. Change Settings")

        setting_choice = input("Enter your choice: ")

        if setting_choice == "4":
            setting_name = input("Enter setting name to change (1-3): ")
            new_value = input("Enter new value: ")

            if setting_name == "1":
                pd.set_option('display.max_rows', int(new_value))
            elif setting_name == "2":
                pd.set_option('display.max_columns', int(new_value))
            elif setting_name == "3":
                pd.set_option('display.width', int(new_value))
            else:
                print("Invalid setting name")

    elif choice == "3":
        # Count Values
        axis = input("Enter axis (0 for rows, 1 for columns): ")
        print(df.count(axis=int(axis)))

    elif choice == "4":
        # Transpose DataFrame and Export
        new_name = input("Enter desired name for transposed DataFrame file: ")
        transposed_df = df.transpose()
        transposed_df.to_csv(f"{new_name}.csv")
        print(f"Transposed DataFrame exported as '{new_name}.csv'")

    else:
        print()
    return df


def write_changes(df, file_path):
    file_formats = {
        "xlsx": df.to_excel,
        "xls": df.to_excel,
        "csv": df.to_csv,
        "html": df.to_html,
        "json": df.to_json,
        "parquet": df.to_parquet,
        "feather": df.to_feather,
        "pickle": df.to_pickle,
    }
    
    file_extension = file_path.split(".")[-1].lower()

    if file_extension in file_formats:
        write_func = file_formats[file_extension]
        write_func(file_path, index=False)  # We assume not writing index to file
        print("writing changes to the dataframe")
        print(f"Changes saved to {file_extension.upper()} file.")
    elif file_extension == "":
        return None
    else:
        print("File type not supported for writing changes.")

def get_filter_data():
    """Prompts the user to input filter data for multiple columns and returns it as a dictionary."""
    filter_dict = {}
    print()
    while True:
        column = input("Enter the column name to filter (or 'done' to finish): ")
        if column.lower() == 'done':
            break

        if column not in filter_dict:
            filter_dict[column] = []

        while True:
            while True:
                filter_type = input(f"Enter the filter type (gt, lt, ge, le, eq, ne, startswith, endswith, contains, isin) for column '{column}': ")
                if filter_type not in ['gt', 'lt', 'ge', 'le', 'eq', 'ne', 'startswith', 'endswith', 'contains', 'isin']:
                    print("Invalid filter type. Please enter a valid filter type.")
                else:
                    break

            criteria = input(f"Enter the filter criteria for column '{column}': ")

            # Convert criteria to the appropriate type based on filter type
            if filter_type in ['gt', 'lt', 'ge', 'le', 'eq', 'ne']:
                try:
                    criteria = float(criteria)
                except ValueError:
                    print("Invalid input for criteria. Please enter a numeric value.")
                    continue
            elif filter_type == 'isin':
                criteria = criteria.split(',')

            filter_data = {
                'type': filter_type,
                'criteria': criteria
            }

            filter_dict[column].append(filter_data)

            more_conditions = input(f"Do you want to add another condition for column '{column}'? (yes/no): ")
            if more_conditions.lower() != 'yes':
                break

    return filter_dict

def apply_filters(df, column, filters):
    """Applies a list of filters to a specified column in the DataFrame."""
    mask = pd.Series([True] * len(df), index=df.index)
    
    for filter_data in filters:
        filter_type = filter_data['type']
        criteria = filter_data['criteria']
        
        # Determine the data type of the column
        column_dtype = df[column].dtype
        
        if filter_type in ['gt', 'lt', 'ge', 'le', 'eq', 'ne']:
            if pd.api.types.is_numeric_dtype(column_dtype):
                if filter_type == 'gt':
                    mask &= df[column] > criteria
                elif filter_type == 'lt':
                    mask &= df[column] < criteria
                elif filter_type == 'ge':
                    mask &= df[column] >= criteria
                elif filter_type == 'le':
                    mask &= df[column] <= criteria
                elif filter_type == 'eq':
                    mask &= df[column] == criteria
                elif filter_type == 'ne':
                    mask &= df[column] != criteria
            else:
                print(f"Error: Filter type '{filter_type}' is not supported for non-numeric column '{column}'.")
                return None

        elif filter_type in ['startswith', 'endswith', 'contains']:
            if pd.api.types.is_string_dtype(column_dtype):
                if filter_type == 'startswith':
                    mask &= df[column].str.lower().str.startswith(criteria.lower())
                elif filter_type == 'endswith':
                    mask &= df[column].str.lower().str.endswith(criteria.lower())
                elif filter_type == 'contains':
                    mask &= df[column].str.lower().str.contains(criteria.lower())
            else:
                print(f"Error: Filter type '{filter_type}' is not supported for non-string column '{column}'.")
                return None

        elif filter_type == 'isin':
            if isinstance(criteria, (list, set, pd.Series)):
                mask &= df[column].isin(criteria)
            else:
                print(f"Error: Criteria for 'isin' filter must be a list, set, or Series.")
                return None

        else:
            print(f"Error: Filter type '{filter_type}' is not supported.")
            return None

    return mask

def filter_dataframe(df, filter_dict):

    combined_mask = pd.Series([True] * len(df), index=df.index)
    valid_columns = []
    initial_length = len(df)

    for column, filters in filter_dict.items():
        if column not in df.columns:
            print(f"Error: Column '{column}' not found in DataFrame.")
            continue
        
        # Apply all filters for the current column and update the combined mask
        column_mask = apply_filters(df, column, filters)
        
        if column_mask is not None:
            combined_mask &= column_mask
            valid_columns.append(column)
            if len(valid_columns) > 0 :
                print(f"DataFrame after applying filters: {filters} on column '{column}'")
                print(df[column_mask])

    # Filter the DataFrame using the combined mask
    filtered_df = df[combined_mask]
    
    # Check if there are valid columns and the final filtered DataFrame has fewer rows than the initial DataFrame
    if len(valid_columns) > 1 or (len(valid_columns) == 1 and len(filtered_df) < initial_length):
        print("Final filtered DataFrame:")
        print(filtered_df)
    elif len(valid_columns) == 0:
        print("No valid filters applied. No changes made to the DataFrame.")
    else:
        print("Invalid filter criteria applied. No valid filtered data to display.")

    return filtered_df

# Example usage
df = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': ['foo', 'bar', 'baz', 'qux', 'quux'],
    'C': [True, False, True, False, True]
})

