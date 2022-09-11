


# 1. Create New Python File
# 2. The user will input 4 information (2 nouns and 2 adjectives)
# 3. Search for any poem or song on the internet (use 1 stanza only)
# 4. Replace the poem or song lyrics string with the nouns and adjectives from user's input.
# 5. Display the original song and poem and display the result (nouns and adjectives must be in ALL CAPS).










# Now I'm a fat house cat
# Cursing my sore blunt tongue
# Watching the warm poison rats
# Curl through the wide fence cracks
# Pissing on magazine photos
# Those fishing lures thrown in the cold and clean
# Blood of Christ mountain stream

noun_1 = input("Please enter the first noun word here: ").upper()
noun_2 = input("Please enter the second noun word here: ").upper()
adj_1 = input("Please enter the first adjective word here: ").upper()
adj_2 = input("Please enter the second adjective word here: ").upper()


line_1 = "Now I'm a " + adj_1 + " house " + noun_1
print(line_1)

line_2 = "Cursing my " + adj_2 + " " + adj_1  + " " + noun_2
print(line_2)

line_3 = "Watching the " + adj_1 + " poison " + noun_1
print(line_3)

line_4 = "Curl through the " + adj_1  + " " + noun_2
print(line_4)

line_5 = "Pissing on " + noun_1
print(line_5)

line_6 = "Those fishing lures thrown in the " + adj_1  + " and "  + adj_2 
print(line_6)

line_7 = "Blood of Christ " + noun_2
print(line_7)
