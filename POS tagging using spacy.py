import spacy

# load english language model

nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])

text = "This is a sample sentence."

# create spacy 

doc = nlp(text)

for token in doc:
    print(token.text,'->',token.pos_)
for token in doc:
    # check token pos
    if token.pos_=='NOUN':
        # print token
        print(token.text)
