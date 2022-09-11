# Day 4 Act 3
# 1. Write a word bank program
# 2. The program will ask to enter a word
# 3. The program will store the word in a list
# 4. The program will ask if the user wants to try again. The user will input
# Y/y if Yes and N/n if No
# 5. If Yes, refer to step 2.
# 6. If No, Display the total number of words and all the words that user
# entered.



result = "y"
word_list = list()
while result.lower() == "y":
      word = str(input("Enter a word: "))
      word_list.append(word)
      result = str(input("Do you want to try again? (Y/N)"))
print("=================================")
print(f"Total Number of Words:  {len(word_list)}")
print("Word in the list:")
for word in word_list:
    print(word)

