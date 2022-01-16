def strip_punctuation(word):
    new_word = ""
    for i in range(len(word)):
        if word[i] in punctuation_chars:
            continue
        else:
            new_word += word[i]
    return new_word


def get_pos(string):
    c = 0
    new_string = strip_punctuation(string)
    for wrd in new_string.split():
        if wrd.lower() in positive_words:
            c += 1
    return c


def get_neg(string):
    c = 0
    new_string = strip_punctuation(string)
    for wrd in new_string.split():
        if wrd.lower() in negative_words:
            c += 1
    return c


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

rows = []
with open('project_twitter_data.csv') as file:
    lines = file.readlines()
    for line in lines[1:]:
        vals = line.strip().split(',')
        rows.append(vals)

with open('resulting_data.csv', 'w') as res_file:
    res_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")        
    for row in rows:
        if get_pos(row[0]) < get_neg(row[0]):
            netscore = get_pos(row[0])-get_neg(row[0])
        elif get_pos(row[0]) == get_neg(row[0]):
            netscore = 0
        else:
            netscore = get_pos(row[0])+get_neg(row[0])
        res_row = '{},{},{},{},{}'.format(row[1], row[2], get_pos(row[0]), get_neg(row[0]), netscore)
        res_file.write(res_row + '\n')    
