bidders = []
winner = {
    "name": "",
    "bid": 0
}


def run():
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))

    bidders.append({
        "name": name,
        "bid": bid
    })

    run_again = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    # Clear console here (import os)
    # lambda: os.system("cls") for Windows
    # lambda: os.system("clear") for Linux, OS X

    if run_again == "yes":
        run()


run()

for bidder in bidders:
    if bidder["bid"] > winner["bid"]:
        winner["name"] = bidder["name"]
        winner["bid"] = bidder["bid"]

print(f"The winner is {winner['name']} with a bid of ${winner['bid']}.")
