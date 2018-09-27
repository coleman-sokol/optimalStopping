import random
#no same numbers - 11

class LineUp:
    def __init__(self, quantities=[3, 11], lowerBound=1, upperBound=149):
        self.offers = []
        self.quantities = quantities
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.breakpoints = []
        self.name = input(" >> ").strip()
        for group in range(len(quantities)):
            self.offers.append([])
            for offer in range(quantities[group]):
                n = random.randint(lowerBound, upperBound)
                while n in self.offers[-1]:
                    n = random.randint(lowerBound, upperBound)
                self.offers[-1].append(n)
    def logdata(self, filePath):
        with open(filePath, "a+") as f:
            for group in range(len(self.quantities)):
                for offer in self.offers[group]:
                    f.write(str(offer) + " ")
                f.write("| " + str(self.breakpoints[group]+1)+ " | ")
            f.write(str(self.lowerBound) + "-" + str(self.upperBound) + " | " + self.name + "\n")
            f.close()
print("\n\n\nPlease enter your first name and the first letter of your last name, with no spaces in between.\nFor example, John Smith would type \"JohnS\"")
test = LineUp()
input("".join(["\n\n\"When Do You Stop?\"\n",
"You're playing a game for money where you get to keep the amount of money on offer.\n",
"If you reject the offer you get offered a different random amount (it can be higher or lower).\n",
"You can not return to a previous offer. If you reject all of the offers you are automatically given the final amount (which is also random).\n",
"The first game gives you up to 3 offers, the second game up to 11 offers.\n",
"Good luck!\n\nPress enter to begin.\n"]))
for group in range(len(test.quantities)):
    print("\nYou will be choosing from a group of " + str(len(test.offers[group])) + " offers.\n\nOffer Group " + str(group+1) + ": ")
    chosen = False
    for offer in range(len(test.offers[group])):
        while True:
            print("  Offer " + str(offer+1) + ": $" + str(test.offers[group][offer]))
            decision = "yes" if offer == len(test.offers[group])-1 else input("    Would you like to choose this offer?\n   >> ").lower()
            if decision in "yes" and len(decision) > 0:
                test.breakpoints.append(offer)
                print("You have chosen offer " + str(offer+1) + ", ranked " + str(len(test.offers[group])-sorted(test.offers[group]).index(test.offers[group][offer])) + " out of " + str(len(test.offers[group])) + ".\n  Here's the list of all the offers: " + str(test.offers[group]))
                chosen = True
                break
            elif decision in "no" and len(decision) > 0:
                break
            else:
                print("Please select yes or no.")
        if chosen:
            break
test.logdata("dollardata.txt")
print("\n"*5)
