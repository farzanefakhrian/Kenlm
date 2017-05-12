# -*- coding: utf-8 -*-

import kenlm
import linecache
import random
import operator
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path,"mod.arpa")
a= input ("calculating score 1 - generating sentence 2 : ")
if a==1 :
	cs= input("Please enter a sentence : ")
	model = kenlm.LanguageModel('mod.arpa')
	print ("P is")
	print(10**model.score(cs))
	print("logP is ")
	print(model.score(cs))
	

elif a==2 :
	wgs= input("please enter a word to generate a sentence : ")

	f = open("mod.arpa", "r")
	word = wgs

	i=0
	for line in f:  
		if line == "\\2-grams:\n":
	    		
	    		break
		i = i+1
	startLine = i+2
	gram2num=i+2
	line = linecache.getline(file_path, gram2num)
	generatedSent = word


        while word != "</s>" and word != "." and word != "!" and word != "?":
            words = []
            dic = {}
            gram2num = startLine
            line = linecache.getline(file_path, gram2num)
            while line != "\end\\\n":
                bigram = line.split()
                if(len(bigram) > 0 and bigram[1] == word):
                    dic[bigram[2]] = bigram[0]
                gram2num += 1
                line = linecache.getline(file_path, gram2num)
            dic = sorted(dic.items(), key=operator.itemgetter(1),reverse= True)
            for i in range(0,len(dic)):
                if(i < 10):
            	    words.append(dic[i][0])
            if(len(words)):
                word = random.choice(words)
                generatedSent += " "
                generatedSent += word
            else:
                break
        print generatedSent
	


