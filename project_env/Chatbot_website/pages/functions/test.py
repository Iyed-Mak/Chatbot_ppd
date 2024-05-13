import google.generativeai as genai
import re
from datetime import datetime
import datetime as t

class chat:
      # ==========================
      def __init__(self):
          self.genai=genai
          self.genai.configure(api_key="AIzaSyCFnNB6dqWfufLNPAZEXn5TJtuTOtF-AFI")
          self.model=genai.GenerativeModel('gemini-pro')
          self.conversation=None
          self.temperature=0.8
          self.conversation_history=[
          self.construct_message('i want you to extract from the input message tasks associated with there dates and put them in dictionery  that i can load it in python and for ecah task has his date as a key as  if no tasks are found output an empty list."you are invited for a party  next saturday"',role='user'),
          self.construct_message('Sure, I can extract from the input message tasks associated with their dates and put them in a JSON file that you can load in Python with the key as \'text\'. If no tasks are found, I will output an empty list.for example,{date : task}', role='model')
          ]

      # ==========================
      def start_chat(self):
          self.conversation=self.model.start_chat(history=self.conversation_history)

      # ==========================
      def history(self):
          self.conversation_history=[
              {'role':message.role,'text':message.parts[0]} for message in self.conversation_history
          ]      

      
      # ==========================
      
        
        
      # ==========================
      def construct_message(self,text,role="user"):
          return {
              'role':role,
              'parts':[text],
          }
      # ==========================
      def geratetive_config(self,temperature):
          return genai.GenerationConfig(
              temperature=temperature
          )
      
      # ==========================
    
      
      # ==========================

      # ==========================
      def send_prompt(self,prompt,temperature=0.1):
          if(self.temperature<0 or self.temperature>1):
              raise GenaiAIExeption("the temperiture is not  between 1 and 0")
          if(not prompt):
              raise GenaiAIExeption("the prompt can not be empty")
          try :
              response=self.conversation.send_message(
                  content=prompt,
                  generation_config=self.geratetive_config(temperature)   
              )
              response.resolve()
              # print(self.remove_special_characters((response.candidates[0].content.parts[0].text).split('Output:')[1]).split('datetimedatetime'))
              #  self.getTask((response.candidates[0].content.parts[0].text).split('Output:')[1])
              # msg = self.getTask((self.remove_special_characters((response.candidates[0].content.parts[0].text).split('\n```\n\nOutput:\n\n```\n')[1])).split(','))

              return response
          except Exception as e :
                  print(f'{e}')
                  
        

def remove_special_characters(text):
        pattern = r'[^:,a-zA-Z0-9()\s\-|]'  # Keep only alphanumeric characters and whitespace
        cleaned_text = re.sub(pattern, '', text)
        cleaned_text = cleaned_text.replace('\n','')
        return cleaned_text

def getTask(tasks,dates):
  messages = {
  }
  for a,i in zip(tasks,dates):
      try : 
      #   task = task.replace(',','')
        # date_tuple = eval(time)
        # time = datetime(*date_tuple)
        # time = time.strftime("%Y-%m-%d %H:%M:%S")
        messages[a] = i
      except Exception as e :
          print(f'split exception : {i}')
  return(messages)

user_input='Hello, Hassan i need to meet you tomorrow at 8:00 AM And after tomorrow we have a tp at 1pm  and dont forget to attend td session in 2235/02/2   Twitter <https://twitter.com/a_benhamida_del> / ResearchGate <https://www.researchgate.net/profile/Adel-Benhamida> / Google Scholar <https://scholar.google.com/citations?user=a6ErONEAAAAJ&hl=en> 0656901687'

def main(user_input):
    chatbot=chat()
    chatbot.start_chat()
    prompt = "act like an email reader so give us only what we need so don't add any thing from you"
    chatbot.send_prompt(prompt,temperature=0.1)
    prompt = f"extract from this text only the tasks and the times of this tasks , each line must have the task and there time without any added text the hole output must be in number of tasks lines : {user_input}"
    msg = chatbot.send_prompt(prompt,temperature=0.1)
    msg = msg.candidates[0].content.parts[0].text

    prompt = f"extract from this text all the tasks without any times and separate them with '|' : 'task1|task2'   : {msg}"
    tasks = chatbot.send_prompt(prompt,temperature=0.1)
    tasks = tasks.candidates[0].content.parts[0].text

    prompt = f"extract only from this text all the dates associated to the tasks without mantioning any task name consediring that the current date is {t.date.today()} ,the format of dates must be like yyyy/MM/dd hh/mm/ss  and separate them with '|' example if the task doesn't have a date tel me : 'task_time1|task_time2'   : {msg}"
    dates = chatbot.send_prompt(prompt,temperature=0.1)
    dates = dates.candidates[0].content.parts[0].text

    tasks = remove_special_characters(tasks).split('|')
    dates = remove_special_characters(dates).split('|')
    # print(dates)
    # print(tasks)
    print(getTask(tasks,dates))
    
    # try:
    #   items = msg.items()
    #   items_list = list(items)
    #   return items_list          
    # except:
    #   print('No Task')    

# user_input='i want you to extract from the following message tasks associated with their dates and put them in a python dictionary format. each task has its date as a key for example,"2024/5/01, 18:00":"you have an apointment". and  if no tasks are found output an empty list. message: i am inviting you for the wedding of my sister next saturday and dont forget to attend the tp session next monday at 11, preparing slides and materials for an upcoming client presentation due on May 15, 2024}'
# user_input = ''
# user_input = " You're a meticulous personal assistant entrusted with organizing the schedule for a busy professional. Your attention to detail is unmatched, ensuring that all appointments and tasks are thoroughly noted and managed effectively.Task: I want you to extract from the following message tasks associated with their dates and put them in a python dictionary format. Each task has its date as a key, for example, '2024/5/01, 18:00': 'you have an appointment'. If no tasks are found, output an empty list.Bear in mind the importance of accuracy and precision in extracting tasks and dates from the provided message. Ensure that the extracted information is structured neatly in a Python dictionary format with the date-time stamp as the key and the task description as the corresponding value.For example:Message: 'Meeting on 2024/5/01 at 10:00 AM - Discuss project updates. Buy groceries by 2024/5/02, 6:00 PM.'Output:{'2024/5/01, 10:00': 'Discuss project updates','2024/5/02, 18:00': 'Buy groceries'} message: Urgent Tasks and Deadlines Dear [Recipient], I hope this message finds you well. I'm reaching out to remind you of some imminent responsibilities that require your attention. These include finalizing and submitting the project proposal on May 10, 2024: preparing slides and materials for an upcoming client presentation due on May 15, 2024, compiling data and analysis for the quarterly report by May 20, 2024, and attending our weekly team meetings held every Monday at 10:00 AM."

# print(main(user_input))
main(user_input)



