import spacy
nlp=spacy.load("en_core_web_md")
sentence_to_compare="Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, \
    the illuminati trick Hulk into a shuttle and launch him into space to a planet\
    where Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into \
    slavery and trained as a gladiator."
    
def best_match(sentence):
    # nlp the reference sentence:
    model_sentence= nlp(sentence_to_compare)
    dict={}
    similarities=[]
    # split entries into names and descriptions:
    with open("movies.txt", "r") as file:
        for line in file:
            line= line.split(":")
            # create a dict of film descriptions with names for keys:
            dict[line[0]]=line[1]
            # apply similarity function to descriptions: 
            for value in dict.values():
                similarity= nlp(value).similarity(model_sentence)
            similarities.append(similarity)

    # find value of max similarity:
    max_sim= max(similarities)

    index=0

    # locate index of max similarity in list of similarities:
    for sim in similarities:
        if sim==max_sim:
            index= similarities.index(max_sim)
            
    # locate description in dict with max similarity: 
    for i, key in enumerate (dict):
        if i==index:
            print(f"We suggest you watch {key}next. Enjoy!")
            
best_match(sentence_to_compare)

            
   


