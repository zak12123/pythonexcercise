#vowel counter
text = input('Enter an  word or phrase ? ')# we asign a variable and input what we want
text = text.lower()# We asign text to be a lower case
vowel_count = 0 # Are vowel count is set to 0 so we can add to it
for char in text:# starts a for loop
  if char in 'a e u i o' :# if statement to determine whether one of the chars in the character consists of the vowels
      #vowel_count += 1# we increase the vowel couner by 1 if statement is true
      vowel_count = vowel_count + 1
print (f'Your text has {vowel_count} vowels.')# we display out the number of vowels in given word or phrase using f strings


