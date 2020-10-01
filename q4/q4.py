#!/usr/bin/env python3

from stackapi import StackAPI
import os
site = StackAPI('stackoverflow')

tags = input()
tags = tags.replace(" ",";")
name = tags.lower().replace(";","_")
filename = name + ".csv"


if os.path.exists(filename):
  os.remove(filename)

questions = site.fetch('questions',sort='votes',tagged=tags)

with open(filename, "a") as file1: 
    	file1.write("question_id,tag,link,tags,accepted_answer\n")

count = 1
for quest in questions['items']:
	if count>50:
		break
	if (quest['is_answered']==False or 'accepted_answer_id' not in quest or quest['accepted_answer_id']==None):
		continue
	question_id = quest['question_id']
	question_link = quest['link']
	question_tags = quest['tags']
	answer_id = quest['accepted_answer_id']
	answer = question_link + "/#" + str(answer_id)
	count+=1
	totaltags = '"'+str(question_tags)+'"'
	with open(filename, "a") as file1: 
    		file1.write(str(question_id)+","+name+","+question_link+","+totaltags+","+answer+"\n")
    		
#Reference:
#https://stackoverflow.com/questions/48086812/stackexchange-api-fetch-answers-to-a-specific-stack-post
