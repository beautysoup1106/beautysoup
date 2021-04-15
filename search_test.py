import re

import pylru as pylru


class SearchEngineBase():
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented')

    def search(self, query):
        raise Exception('search not implemented')


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_query(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, word):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_test_in_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        text = text.lower()
        word_list = text.split(' ')
        word_list = filter(None, word_list)
        return set(word_list)

class BOWInvertIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertIndexEngine,self).__init__()
        self.inverted_index={}

    def process_corpus(self, id, text):
        words=self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word]=[]
            self.inverted_index[word].append(id)

    def search(self, query):
        query_words=list(self.parse_text_to_words(query))
        query_words_index=list()
        for query_word in query_words:
            query_words_index.append(0)

        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []

        result =[]
        while True:
            #首先，获得当前状态下所有倒序索引的index
            current_ids=[]

            for idx,query_word in enumerate(query_words):
                current_index=query_words_index[idx]
                current_inverted_list=self.inverted_index[query_word]

                #已经遍历到了某个倒序索引的末尾，结束search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            #然后，如果current_ids的所有元素都一样，那么表名这个单词在这个元素对应额文档中都出现了
            if all(x==current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index=[x+1 for x in query_words_index]
                continue

            #如果不是，那么我们就把最小的元素加1
            min_val=min(current_ids)
            min_val_pos=current_ids.index(min_val)
            query_words_index[min_val_pos]+=1

    @staticmethod
    def parse_text_to_words(text):
        text=re.sub(r'^\w ',' ',text)
        text=text.lower()
        word_list=text.split(' ')
        word_list=filter(None,word_list)

        return set(word_list)


class LRUCatche():
    def __init__(self,size=32):
        self.catche=pylru.lrucache(size)

    def has(self,key):
        return key in self.catche

    def get(self,key):

        return self.catche[key]
    def set(self,key,value):
        self.catche[key]=value

class BOWInvertedIndexEngineWithCatche(BOWInvertIndexEngine,LRUCatche):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCatche,self).__init__()
        LRUCatche.__init__()

    def search(self, query):
        if self.has(query):
            print('catch hit')
            return self.get(query)

        result=super(BOWInvertedIndexEngineWithCatche,self).search(query)
        self.set(query,result)

        return result