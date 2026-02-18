cards = []

cards.append("2 of Spades")
cards.append("Queen of Diamonds")
cards.append("King of Hearts")
cards.append("Ace of Clubs")

top_card = cards.pop()
# print(top_card)

# print(cards[-1]) # top card without removing it

if not cards: 
    print("Card Stack is now empty")
else: 
    print(f"There are {len(cards)} remaining in the deck")

s = "(inc)rement()("

empty = set()
bracket1 = set()
bracket2 = set()

for i in s: 
    empty.update(i)

for x in empty: 
    if "(" == x: 
        bracket1.add(x)

for y in empty: 
    if ")" == y: 
        bracket2.add(y)

open_close = bracket1.union(bracket2)

if len(open_close) == 2:
    print(True)
else: 
    print(False)

empty_list = []

for z in s:
    empty_list.append(z)

print(empty_list)

num_of_bracket1 = empty_list.count("(")
num_of_bracket2 = empty_list.count(")")

result = num_of_bracket1 + num_of_bracket2 

print(result)

if result%2 != 0: 
    print(False)
else: 
    print(True)