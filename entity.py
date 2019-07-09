import spacy
import numbers
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("I have taken a loan from SBI for 20lac rupees in December 2015.They were late in processing the documents and asked for too many documents. They gave the loan very late.I had asked for 25 lacs but got only 20 lacs.The rate of interest at 14.3% is also higher compared to other banks. I am not happy with their services. My name is Dhanush Singh from Punjab.")
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
for entity in doc.ents:
    print(entity.text, entity.label_)
l=displacy.render(doc, style="ent")
p=0
c=0
ph=0
i=0
s=""
while i<len(l):
	p=0
	if isinstance(l[i], numbers.Integral):
		#print("p")
		while isinstance(l[i], numbers.Integral) and i<len(l):
			p=p*10+i
			i=i+1;
		if i-p+1==12:
			c=1
		elif i-p+1==10:
			ph=1

	if l[i]=='<' and l[i+1]=='s' and l[i+2]=='p' and l[i+3]=='a' and l[i+4]=='n':
		i=i+5
		while l[i]!='/':
				i=i+1
		i=i+6
	#elif l[i]=='S' and l[i+1]=='B' and l[i+2]=='I' and l[i+3]=='N':

	else:
		s=s+str(l[i])
		i=i+1
if c==1:
	s=s+"<div class=\"entities\" style=\"line-height: 2.5; direction: ltr\">Card/Bank-account number:<mark class=\"entity\" style=\"background: 7aecec; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone\">"+str(p)+"</mark></div>"
elif ph==1:
	s=s+"<div class=\"entities\" style=\"line-height: 2.5; direction: ltr\">Phone number:<mark class=\"entity\" style=\"background: 7aecec; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone\">"+str(p)+"</mark></div>"
print(s)