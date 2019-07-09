from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')

def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/weathernlu')
	print(interpreter.parse(u"I have taken a loan from SBI for 20lac rupees in December 2015.They were late in processing the documents and asked for too many documents. They gave the loan very late.I had asked for 25 lacs but got only 20 lacs.The rate of interest at 14.3% is also higher compared to other banks. I am not happy with their services. My name is Dhanush Singh from Punjab."));
if __name__ == '__main__':
	train_nlu('./data/data.json', 'configure_spacy.json', './models/nlu')
	run_nlu()

	'''i=0
while i<len(l):
	if l[i]=='<' and l[i+1]=='s' and l[i+2]=='p' and l[i+3]=='a' and l[i+4]=='n':
		i=i+5
		while l[i]!='/':
				i=i+1
		i=i+6
	#elif l[i]=='S' and l[i+1]=='B' and l[i+2]=='I' and l[i+3]=='N':

	else:
		s=s+str(l[i])
		i=i+1'''