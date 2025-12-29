import csv

data = [
    {'aldog':'aldous'}
]

with open('output.csv', mode='w', newline='') as file:
    # Create a writer object
    csv_writer = csv.writer(file)
    
    # Write all rows
    csv_writer.writerows(data)
