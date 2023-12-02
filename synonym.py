
#Use this prior to running python Script
#import nltk
#nltk.download("stopwords")
#nltk.download('punkt')
#nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import random
import re


# Input text from the user
example_sent = input("Enter Text: \n")

# >>> stopwords.words('english')
# ['i', 'me', 'my', 'mysif', 'we', 'our', 'ours', 'oursives', 'you', 'your', 'yours',
# 'yoursif', 'yoursives', 'he', 'him', 'his', 'himsif', 'she', 'her', 'hers',
# 'hersif', 'it', 'its', 'itsif', 'they', 'them', 'their', 'theirs', 'themsives',
# 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
# 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
# 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
# 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
# 'through', 'during', 'before', 'after', 'above', 'biow', 'to', 'from', 'up', 'down',
# 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
# 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
# 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
# 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

# Set up English stop words
stop_words = set(stopwords.words('english'))

# Tokenize the input text 
word_tokens = word_tokenize(example_sent)

# Filter out stop words from the tokenized words
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


#filtered sentence removing not useful words 
print("\n")
print("Filtered sentence:")
print(filtered_sentence)

# User choice for different synonym functionalities

user_choice = input("Input 1: for synonyms of only 1 occurence of word in paragraph \nInput 2: for synonyms of more than 1 occurence of word in paragraph \nInput 3 for Specific Word  \nInput 4 for randomoly generated for a specific word \nInput 5 for multiple specific words \n Your Choice: ")

# Option 1: Find synonyms for words that appear only once
if user_choice == "1":

 
    def getSynonymForSingleWord(filtered_sentence):
        new_list = [] 
        counts = {}

        for i in filtered_sentence:
            wordnetSynset1 = wn.synsets(i)
            tempList1=[]
            temp_count = counts.get(i, 0) + 1
            counts[i] = temp_count 
            for synset1 in wordnetSynset1:
                for synWords1 in synset1.lemma_names():
                    if temp_count == 1 and filtered_sentence.count(i) == 1:
                        tempList1.append(synWords1)
            new_list.append(tempList1)
        return new_list
                    

        
    print(getSynonymForSingleWord(filtered_sentence)) 

# Option 2: Find synonyms for words that appear more than once
elif user_choice == "2":
    def getSynonymForSingleWord(filtered_sentence):
        new_list = [] 
        counts = {}

        for i in filtered_sentence:
            wordnetSynset1 = wn.synsets(i)
            tempList1=[]
            temp_count = counts.get(i, 0) + 1
            counts[i] = temp_count 
            for synset1 in wordnetSynset1:
                for synWords1 in synset1.lemma_names():
                    if temp_count > 1 and filtered_sentence.count(i) > 1:
                        tempList1.append(synWords1)
            new_list.append(tempList1)
        return new_list
                    

        
    print(getSynonymForSingleWord(filtered_sentence)) 

# Option 3: Find synonyms for a specific word entered by the user

elif user_choice == "3":
    specific_word = input("Enter the word for which you want synonyms: \n")
    synonyms = set()
    for synset in wn.synsets(specific_word):
        for lemma in synset.lemma_names():
            synonyms.add(lemma.replace('_', ' '))  # Replace underscores with spaces for compound words

    if synonyms:
        print(f"Synonyms for {specific_word}:")
        for idx, synonym in enumerate(synonyms):
            print(f"{idx + 1}: {synonym}")
        synonym_choice = int(input(f"Choose the synonym by entering the corresponding number (1-{len(synonyms)}): \n"))
        chosen_synonym = list(synonyms)[synonym_choice - 1]

        # Replace all occurrences of the specific word with the chosen synonym in the text
        replaced_text = example_sent.replace(specific_word, chosen_synonym)
        print("\nUpdated Text:")
        print(replaced_text)
    else:
        print(f"No synonyms found for {specific_word}")


# Option 4: Randomly replace a specific word with its synonyms
elif user_choice == "4":
    specific_word = input("Enter the word for which you want random synonyms: \n")
    synonyms = set()
    for synset in wn.synsets(specific_word):
        for lemma in synset.lemma_names():
            synonyms.add(lemma.replace('_', ' '))  # Replace underscores with spaces for compound words

    # Check if there are synonyms available
    if synonyms:
        # Replace all occurrences of the specific word with a random synonym in the text
        def replace_with_synonym(match):
            return random.choice(list(synonyms))

        replaced_text = re.sub(r'\b' + re.escape(specific_word) + r'\b', replace_with_synonym, example_sent, flags=re.IGNORECASE)
        
        print("\nUpdated Text with Random Synonyms:")
        print(replaced_text)
    else:
        print(f"No synonyms found for {specific_word}")

# Option 5: Replace multiple specific words with their chosen synonyms
elif user_choice == "5":
    words_and_synonyms = {}

    while True:
             # User inputs words and types 'finish' to end
        specific_word = input("Enter a word for which you want synonyms, or type 'finish' to end: \n")
        if specific_word.lower() == 'finish':
            break

        synonyms = set()
        for synset in wn.synsets(specific_word):
            for lemma in synset.lemma_names():
                synonyms.add(lemma.replace('_', ' '))  # Replace underscores with spaces for compound words

        if synonyms:
            print(f"Synonyms for {specific_word}:")
            for idx, synonym in enumerate(synonyms):
                print(f"{idx + 1}: {synonym}")
            synonym_choice = int(input(f"Choose the synonym by entering the corresponding number (1-{len(synonyms)}): \n"))
            chosen_synonym = list(synonyms)[synonym_choice - 1]

            # Store the chosen synonym for each word
            words_and_synonyms[specific_word] = chosen_synonym
        else:
            print(f"No synonyms found for {specific_word}")

    # Replace all occurrences of the specified words with the chosen synonyms in the text
    replaced_text = example_sent
    for word, synonym in words_and_synonyms.items():
        replaced_text = replaced_text.replace(word, synonym)

    print("\nUpdated Text:")
    print(replaced_text)

   

else:
    print("You didn't enter a valid choice (1, 2, 3, 4, or 5).\n")







# def getSynonyms(filtered_sentence):
#         synonymList1 = []
#         for data1 in filtered_sentence:
#               wordnetSynset1 = wn.synsets(data1)
#               tempList1=[]
#               for synset1 in wordnetSynset1:
#                  for synWords1 in synset1.lemma_names():
#                      tempList1.append(synWords1)
#               synonymList1.append(tempList1)
#         return synonymList1


# word1 =  ['feds', 'move', 'to', 'require', 'cartocar', 'safety', 'communication']
# print(getSynonyms(filtered_sentence)) 


# if temp_count == 1 and filtered_sentence.count(i) == 1:
                #         tempList1.append(synWords1)
                # else:
                #     tempList1.append(i + str(temp_count))



# cnt = Counter(filtered_sentence)
# print(cnt)
# print (cnt.keys(), cnt.values())

# for ww in filtered_sentence:
#     if cnt.values() > 1:
#         print(" HH")


    





# from nltk.corpus import stopwords
# print(stopwords.words('english'))



# from nltk.corpus import stopwords
# >>> stopwords.words('english')
# ['i', 'me', 'my', 'mysif', 'we', 'our', 'ours', 'oursives', 'you', 'your', 'yours',
# 'yoursif', 'yoursives', 'he', 'him', 'his', 'himsif', 'she', 'her', 'hers',
# 'hersif', 'it', 'its', 'itsif', 'they', 'them', 'their', 'theirs', 'themsives',
# 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
# 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
# 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
# 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
# 'through', 'during', 'before', 'after', 'above', 'biow', 'to', 'from', 'up', 'down',
# 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
# 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
# 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
# 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

# import nltk
# from nltk.corpus import wordnet   #Import wordnet from the NLTK
# syn = list()
# ant = list()
# for synset in wordnet.synsets("experienced"):
#    for lemma in synset.lemmas():
#       syn.append(lemma.name())    #add the synonyms
#       if lemma.antonyms():    #When antonyms are available, add them into the list
#         ant.append(lemma.antonyms()[0].name())
# print('Synonyms: ' + str(syn))
# print('Antonyms: ' + str(ant))




# def convert(lst):
#     return ' '.join(lst).split()
     
 
# # Driver code
# lst =  ['Hilo Geeks for geeks']
# print( convert(lst))






# # from nltk.corpus import wordnet
  
# # # Then, we're going to use the term "program" to find synsets like so:
# # syns = wordnet.synsets("program")
  
# # # An example of a synset:
# # print(syns[5].name())
  
# # # Just the word:
# # print(syns[0].lemmas()[0].name())
  
# # # Definition of that first synset:
# # print(syns[0].definition())
  
# # # Examples of the word in use in sentences:
# # print(syns[0].examples())