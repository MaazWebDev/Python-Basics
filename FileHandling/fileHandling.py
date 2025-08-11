# File Handling :

f = open('SalesDataAi (1).txt')
print(f.readline())




# with open('SalesDataAi (1).txt','r') as file:
#     first_line = file.readline().strip()

# parts = first_line.split('\t')
# print(parts)

with open("SalesDataAi (1).txt", "r") as file:
    for line in file:
        parts = line.strip().split("\t")  # split with tab
        print(parts)



total_unit_price = 0

with open("SalesDataAI (1).txt", "r") as file:
    next(file)  # Skip header line
    for line in file:
        parts = line.strip().split("\t")  # Split by tab
        unit_price = int(parts[-1])  # Last column is Unit Price
        total_unit_price += unit_price

print("Total Unit Price:", total_unit_price)
