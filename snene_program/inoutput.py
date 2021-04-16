import re


def parse(text):
    text = re.sub(r'[^\w ]', ' ', text)
    text=text.lower()

    word_list=text.split(' ')
    word_list=filter(None,word_list)

    word_cnt={}

    for word in word_list:
        if word not in word_cnt:
            word_cnt[word]=0
        word_cnt[word]+=1


    sortes_word_cnt=sorted(word_cnt.items(),key=lambda kv:kv[1],reverse=True)

    return sortes_word_cnt


with open('../base_syntax/in.txt', 'r') as fin:
    text=fin.read()

word_and_freq=parse(text)

with open('../base_syntax/out.txt', 'w') as fout:
    for word,freq in word_and_freq:
        fout.write('{}  {}\n'.format(word,freq))

