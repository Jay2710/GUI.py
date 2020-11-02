                                                   #String
str = "Let the game begin"
print(len(str))
print(str[0:19])#For 0 to 19 words in string
print(str[0:19:2])#Slicing of the string
print(str[::-1])#For reversing the string
print(str.isalnum())#For finding the string is the alpha numeric or not
print(str.endswith("begin"))#For finding there is a string or not
print(str.upper())#For capetalized whole string
print(str.find("game"))#For  finding the word in the string
print(str.replace("game", "Show"))#For replacing the word in the string

                                                   #List Starts

home = ["hello", "world", "india", "bharat", 78, 98]
numbers = [2, 9, 3, 7, 5, 0]
print(home)
print(home[2])#Finding specific vlaue word
print(numbers[3])
print(max(numbers)) #For finding the maximum no. in the list
print(min(numbers)) #For finding the minimum no. in the list
numbers.append(11) #For joining in the end
print(numbers)
numbers.insert(2, 13) #For inserting no. in between list
print(numbers)
numbers.remove(13) #For removing no. from in between list
print(numbers)
numbers.pop() #For removing last element
print(numbers)
numbers[2] = 8
print(numbers)
numbers.sort() #For sorting of numbers
print(numbers)
numbers.reverse() #For reversing the numbers
print(numbers)

                                                         #Tuples

#tpl = (1, 2, 3)
#tpl[1] = 4  (Tuples value can not be changes it shows error) Immutable

                                                         #Dictionary

d1 = {"set": "collection of objects",
      "Mutable": "can be changed ",
      "Immutable": "can not be changed"
      }
print("Type your word")
word = input()
print(d1[word])


