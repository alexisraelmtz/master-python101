def possibleCombs(axisList):
    output = []
    for pair in axisList:
        if pair == 2:
            output.append(1)
            continue
        else:
            ans, rem = divmod(pair, 4)
            if rem == 0 or rem == 2:
                output.append(ans+1)
            elif rem == 1 or rem == 3:
                output.append(0)

    return output


axisList = [4, 5, 6]
print(possibleCombs(axisList))

""""
First find possible combinations by hand and look for a possible pattern.

After a couple of tries, confirmed that if the N is divisible by 4, you get(N/4)+1 possible combinations.

And after noticing that dividing N by 4 with remainder 2 will not change the outcome, so I added it as a base case. As well as another base case for N = 2 because it only has 1 combination.

And lastly, ignored reminders equal to 3 or 1, because they don't have a possible combination.
"""
