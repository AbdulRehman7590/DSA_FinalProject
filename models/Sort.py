import pandas as pd

class PakWheels:
    def load(self):
        try:
            # Specify the correct path to your CSV file
            df = pd.read_csv("D:\DSA\Final project\cs261f23pid28\inputs\Data.csv", encoding='utf-8')
            # Drop any rows with missing values
            df = df.dropna()            #It was adding an extra row with None data
            return df
        except FileNotFoundError:
            print("Error: The CSV file is not found.")
        except pd.errors.EmptyDataError:
            print("Error: The CSV file is empty.")
        except pd.errors.ParserError:
            print("Error: Unable to parse the CSV file.")

    def merge_sort(self, df, index):
        if len(df) > 1:
            mid = len(df) // 2
            left = df.iloc[:mid].copy()
            right = df.iloc[mid:].copy()

            self.merge_sort(left, index)
            self.merge_sort(right, index)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if str(left.iloc[i][index]) <= str(right.iloc[j][index]):
                    df.iloc[k] = left.iloc[i].copy()
                    i += 1
                else:
                    df.iloc[k] = right.iloc[j].copy()
                    j += 1
                k += 1

            while i < len(left):
                df.iloc[k] = left.iloc[i].copy()
                i += 1
                k += 1

            while j < len(right):
                df.iloc[k] = right.iloc[j].copy()                   #iloc to find integer location used in dataframe
                j += 1
                k += 1

    def sort_dataframe(self, df, index):
        self.merge_sort(df, index)

    def print_sorted_dataframe(self, df):
        print(df)

# Create an instance of PakWheels class
pak = PakWheels()

# Load the sample data
dataframe = pak.load()
print("Original DataFrame:")
print(dataframe)

# Specify the column to sort on (let's say 'Username' column for this example)
# Perform merge sort on the DataFrame
pak.sort_dataframe(dataframe, 'Email')

# Print the sorted DataFrame
print("\nSorted DataFrame:")
pak.print_sorted_dataframe(dataframe)
