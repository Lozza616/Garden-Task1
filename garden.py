import spacy

nlp = spacy.load('en_core_web_sm')

nlp_a = nlp("The man who whistles tunes pianos.")
nlp_b = nlp("Helen is expecting tomorrow to be a bad day.")
nlp_c = nlp("I convinced her children are noisy.")
nlp_d = nlp("We painted the wall with cracks.")
nlp_e = nlp("That Jill is never here hurts.")
list_of_garden_sentences = [nlp_a, nlp_b, nlp_c, nlp_d, nlp_e]
gardenpath_sentences = []

# iterates through each garden sentence stored in the list.
for sentence in list_of_garden_sentences:
    # uses .ents function
    list_of_tokens = []
    # iterates through each token in the sentence
    for token in sentence.ents:
        # Appends token to the list
        list_of_tokens.append(token)
        # Appends token label to the list
        list_of_tokens.append(token.label_)
    # Appends list of tokens and token labels to gardenpath_sentences list
    gardenpath_sentences.append(list_of_tokens)

print(gardenpath_sentences)

"Helen should be a 'PERSON' but is identified as GPE and 'tommorrow' is identified as a date"
