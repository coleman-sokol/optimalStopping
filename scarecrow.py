import random
#no same numbers - 11

class LineUp:
    def __init__(self, quantities=[3, 11], lowerBound=11, upperBound=85):
        self.candidates = []
        self.quantities = quantities
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.breakpoints = []
        self.name = input(" >> ").strip()
        for group in range(len(quantities)):
            self.candidates.append([])
            for candidate in range(quantities[group]):
                n = random.randint(lowerBound, upperBound)
                while n in self.candidates[-1]:
                    n = random.randint(lowerBound, upperBound)
                self.candidates[-1].append(n)
    def logdata(self, filePath):
        with open(filePath, "a+") as f:
            for group in range(len(self.quantities)):
                for candidate in self.candidates[group]:
                    f.write(str(candidate) + " ")
                f.write("| " + str(self.breakpoints[group]+1)+ " | ")
            f.write(str(self.lowerBound) + "-" + str(self.upperBound) + " | " + self.name + "\n")
            f.close()
print("\n\n\nPlease enter your first name and the first letter of your last name, with no spaces in between.\nFor example, John Smith would type \"JohnS\"")
test = LineUp()
input("".join(["\"When Do You Stop?\"\n",
"You must hire a new assistant. The candidates are interviewed in a random order (i.e. the best person could be first, second... last).\n",
"After each interview the candidate is given a score. You can then choose to hire them or move on to the next candidate.\n",
"You can not return to a previous candidate. If you do not hire anyone you automatically hire the last person.\n",
"The first game involves 3 candidates, the second game involves 11 candidates.\n",
"Good luck!\n\nPress enter to begin.\n"]))
for group in range(len(test.quantities)):
    print("\nYou will be choosing from a group of " + str(len(test.candidates[group])) + " candidates.\n\nCandidate Group " + str(group+1) + ": ")
    hired = False
    for candidate in range(len(test.candidates[group])):
        while True:
            print("  Candidate " + str(candidate+1) + ": Rank " + str(test.candidates[group][candidate]))
            decision = "yes" if candidate == len(test.candidates[group])-1 else input("    Would you like to hire this candidate?\n   >> ").lower()
            if decision in "yes" and len(decision) > 0:
                test.breakpoints.append(candidate)
                print("You have hired Candidate " + str(candidate+1) + ", ranked " + str(len(test.candidates[group])-sorted(test.candidates[group]).index(test.candidates[group][candidate])) + " out of " + str(len(test.candidates[group])) + ".\n  Here's the list of all the candidates: " + str(test.candidates[group]))
                hired = True
                break
            elif decision in "no" and len(decision) > 0:
                break
            else:
                print("Please select yes or no.")
        if hired:
            break
test.logdata("data.txt")
print("\n"*5)
