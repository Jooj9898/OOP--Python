#Find the frequency of a word in a text
#1 Membership test:

count_dict = {}
for word in word_list:
   if word in count_dict:
       count_dict[word] += 1
   else:
       count_dict[word] = 1

##Exceptions:
count_dict = {}
for word in word_list:
   try:
       count_dict[word] += 1
   except KeyError:
       count_dict[word] = 1

#Get method:
count_dict = {}
for word in word_list:
   count_dict[word] = count_dict.get(word, 0) + 1
