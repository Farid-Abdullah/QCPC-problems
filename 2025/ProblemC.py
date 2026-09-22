
# There is confusion in the quesion. or its just a trick.....
# for example, if n = 5, Anna: 1, Brian:2, Anna:1, Brian: one card is left but he cannot take 1 because it violates rule 3. So who wins when rule 3 is impossible to not violate?
# For the quesion to make sense, I will assume rule 3 violation leads to loss as well, just like rule 4.

# But if rule 3 leads to immediate loss, then the game is trivial and Anna can win all the time no matter what.

t = int(input())
for _ in range(t):
    n = int(input())
    print("Anna") # since Anna wins all the time.
