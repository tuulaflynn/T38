import spacy
nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1, word2, word1.similarity(word2))
print(word3, word2, word3.similarity(word2))
print(word3, word1, word3.similarity(word1))

# It is interesting that cat and banana have around half the similarity of monkey and banana,
# intuitively I would think cat and banana have very little in common compared to monkey and banana.
# Although, it is impressive it has given banana and monkey have a higher similarity
# because enough though they are not similar types or words, it has recognised a similarity in their semantics
# i.e. people associate monkeys with eating bananas.

print("\nMy Example")
word_1 = nlp("hair")
word_2 = nlp("tooth")
word_3 = nlp("fingernail")

print(f"{word_1}, {word_2} - {word_1.similarity(word_2)}")
print(f"{word_2}, {word_3} - {word_2.similarity(word_3)}")
print(f"{word_3}, {word_1} - {word_3.similarity(word_1)}")

# Running the with nlp = spacy.load("en_core_web_sm") gives different similarity results.
# The results seem less accurate. For monkey banana and cat it gave similarity in the range 0.67 < 0.74,
# meaning that it saw less distinction in 3 words that aren't very similar.
# The results given for My Example gave a larger dissimilarity which ranged from 0.46 < 0.77, for words which are more
# similar than the first example.
# Results:

# cat monkey 0.7371058814668531
# banana monkey 0.7291608188578151
# banana cat 0.6775488148048872

# My Example
# hair, tooth - 0.4640638280558824
# tooth, fingernail - 0.6172779979964719
# fingernail, hair - 0.7612875746990798





# My background inputs
# tokens = nlp("mum apple brother son ")
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))
#
#
# sentence_to_compare = "Why is my cat on the car"
# sentences = ["Where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car",
#              "I\'d like my boat back", "I will name my dog Diana"]
#
# model_sentence = nlp(sentence_to_compare)
#
# print(model_sentence)
# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", similarity)


