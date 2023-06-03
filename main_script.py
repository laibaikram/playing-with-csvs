import pandas as pd
import matplotlib.pyplot as plt

def generate_graph(data, column_name):
    column_data = data[column_name]
    
    # Bar graph
    plt.figure(figsize=(8, 6))
    plt.subplot(2, 2, 1)
    plt.bar(range(len(column_data)), column_data)
    plt.xlabel('Index')
    plt.ylabel(column_name)
    plt.title(f'Bar graph of {column_name}')
    
    # Line graph
    plt.subplot(2, 2, 2)
    plt.plot(column_data)
    plt.xlabel('Index')
    plt.ylabel(column_name)
    plt.title(f'Line graph of {column_name}')
    
    # Scatter plot
    plt.subplot(2, 2, 3)
    plt.scatter(range(len(column_data)), column_data)
    plt.xlabel('Index')
    plt.ylabel(column_name)
    plt.title(f'Scatter plot of {column_name}')
    
    # Histogram
    plt.subplot(2, 2, 4)
    plt.hist(column_data, bins='auto')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column_name}')
    
    plt.tight_layout()
    plt.show()

def main():
    # Assuming the CSV file is named "data.csv"
    csv_file = "data.csv"

    # Load CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file)
    
    # Iterate over each column
    for column_name in data.columns:
        generate_graph(data, column_name)

if __name__ == '__main__':
    main()
