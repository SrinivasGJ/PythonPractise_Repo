from datetime import datetime

targetfile_path="C:/Users/Jyothisrinivas_Gudla/PycharmProjects/pythonProject/News_generated.txt"



class Publication:
    def __init__(self):
        # self.text=text
        self.date=datetime.now().strftime('%Y-%m-%d')
        self.datetime=datetime.now().strftime("%Y-%m-%d %H:%M")
        output='News feed:\n'
        with open(targetfile_path, 'w') as file:
            file.write(output)
    def news(self,text,city):
        with open(targetfile_path, 'a') as file:
            file.write(f"""\nNews -------------------------\n{text}\n{city}, {self.datetime} \n""")
    def private_add(self,text,expiration_date):
        expiration_date= datetime.strptime(expiration_date, "%Y-%m-%d")
        current_date=datetime.strptime(self.date,"%Y-%m-%d")
        difference_days=(expiration_date - current_date).days
        with open(targetfile_path,'a') as file:
            file.write(f"""\nPrivate Ad ------------------\n{text}\nActual until {expiration_date}, {difference_days} days \n""")
    def article(self,text,topic):
        with open(targetfile_path,'a') as file:
            file.write(f'\nArticle--------\n{text} {topic}')


obj1=Publication()
obj1.news('Something happened','Hyderabad')
obj1.news('Something other happened','Hyderabad')
obj1.private_add('I want to sell a bike', '2025-01-31')
obj1.article('This is new article about', 'Football')
