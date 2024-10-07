'''
Find a short quote and its author. Assign the quote to a variable and assign the name of the author to another variable.

Use fstring to create a new variable called message the replicates the following format:

"Michael Scott once said, "I'm not superstitious but I am a little stitious."
'''

Famous = "Valerie"

Quote = "Patience, young grasshopper"

print(f'{Famous} oonce  said, "{Quote}."')
print("{} once said, '{}.'".format(Famous, Quote))