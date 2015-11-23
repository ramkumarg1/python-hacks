import numpy as np
import re
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn import preprocessing
import json

mydict = {}

x_nor_array = []
y_nor_array = []
for lines in open("training.txt","r"):
	fields = lines.split('\t')
	x_nor_array.append(fields[0].encode('ascii','ignore'))
	y_nor_array.append(fields[1])

X_train = np.array(x_nor_array)
y_train_text = np.array(y_nor_array)

lb = preprocessing.LabelBinarizer()
Y = lb.fit_transform(y_train_text)

classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])

classifier.fit(X_train, Y)

#for tweets in open("tweets","r"):
total = 'Total'
while True:
	try:
		tweetsj = json.loads(raw_input())
		tweets = tweetsj['text'].encode('utf-8')
		if not tweets.strip().startswith('RT'):
			tweets = re.sub(r'(\@\w+|\#\w+)','',tweets)
			read_to_list = []
			read_to_list.append(tweets)
			new_array = np.array(read_to_list)
			predicted = classifier.predict(new_array)
			all_labels = lb.inverse_transform(predicted)
			for item, labels in zip(new_array, all_labels):
				#print '%s => %s' % (item.strip(), ''.join(labels).strip())
				senti = ''.join(labels).strip()
				mydict[senti] = mydict.get(senti,0) + 1
				mydict[total] = mydict.get(total,0) + 1
				print mydict
			
	except: 
		continue
