"""Generate sales report showing total melons each salesperson sold."""

# creates empty lists to fill with salespeople and how many melons they sold

salespeople = []
melons_sold = []

# opens sales-report file

f = open('sales-report.txt')

# iterates through each line in the file
# removes whitespace
# converts each line into a list

for line in f:
    line = line.rstrip()
    entries = line.split('|')

    # assigns variables salesperson, melons to respective list indices

    salesperson = entries[0]
    melons = int(entries[2])

    # checks if salesperson is already in salespeople list
    # adds melons to their melons_sold count

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons

    # adds salesperson to salespeople list if they are not already in list
    # adds melons to their melons_sold count

    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# prints a statement that describes how many melons each salesperson sold

for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
