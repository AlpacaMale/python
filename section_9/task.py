bidders = {}

while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidders[name] = price
    print("Are there any other bidders? Types 'yes or no'.")
    more_bidders = input()
    if more_bidders == "no":
        break
winner = max(bidders.items(), key=lambda x: x[1])
print(f"The winner is {winner[0]} with a bid of ${winner[1]}")
