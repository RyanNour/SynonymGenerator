
#Use this prior to running python Script
#import nltk
#nltk.download("stopwords")
#nltk.download('punkt')
#nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn


example_sent = input("Enter Text: \n")


stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(example_sent)
  
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


#filtered sentence removing not useful words 
print("\n")
print("Filtered sentence:")
print(filtered_sentence)

user_choice = input("Input 1: for synonyms of only 1 occurence of word in paragraph or Enter 2: for synonyms of more than 1 occurence of word in paragraph \n")


if user_choice == "1":

#words only used once in paragraph  
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

else:
    print("You didnt enter 1 or 2\n")









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