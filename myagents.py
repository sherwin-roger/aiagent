from datetime import date
from translate import Translator

from bs4 import BeautifulSoup
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def getWeather(city):
	city = city.replace(" ", "+")
	res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	print("Searching...\n")
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	print(location)
	print(time)
	print(info)
	print(weather+"°C")

class Environment():
    def __init__(self,data):
        self.data = data
        self.creator="Sherwin Roger"
      
    def getData(self):
        print(self.data)

class Agent(Environment):
    def __init__(self,setName,questions):
        super().__init__(questions)
        self.name = setName
        print("Hi im",self.name)

    def Chat(self):
        print(self.getData())
        while(1):
            question=int(input("Ask your Question\n"))
            match question:
                case 1:
                    today = date.today()
                    print("Today's date:", today)
                case 2:
                    calculate=input("Enter the expression you want to calculate\n")
                    print(eval(calculate))
                case 3:
                    city = input("Enter the Name of City -> \n")
                    city = city+" weather"
                    getWeather(city)
                    print("Have a Nice Day:)")
                case 4:
                    language=input("Enter the language you want to speak....\n")
                    translator= Translator(to_lang=language)
                    sentence = input("Enter the sentence you want to convert into....\n")
                    translation = translator.translate(sentence)
                    print(translation)
                case 5:
                    print(self.creator)
                case 6:
                    print("Bye Bye!!")
                    exit()

if __name__== '__main__':
    chatbot = input("Hi give a name for me...\n")
    questions=["1) What is the current date and time?","2) Open Calculator","3) What’s the weather like today?","4) Use Translator","5) Who’s your Creator?\n 6)exit"]
    bot = Agent(chatbot,questions)
    bot.Chat()