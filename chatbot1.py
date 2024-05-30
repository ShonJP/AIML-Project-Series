class SimpleChatbot:
  def __init__(self):
      self.context = {}
      self.greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
      self.farewells = ["Goodbye!", "See you later!", "Bye!", "Take care!"]
      self.questions = {
          "how are you": "I'm a chatbot, so I don't have feelings, but thank you for asking!",
          "what's your name": "I'm called Chatbot.",
          "what can you do": "I can chat with you and answer basic questions.",
          "how old are you": "I was created quite recently, so I'm very young.",
          "what's the weather": "I'm not sure about the weather, but it's always a good day to chat!"
      }

  def greet(self):
      return self.greetings[0]  # simple static greeting

  def farewell(self):
      return self.farewells[0]  # simple static farewell

  def respond_to_question(self, user_input):
      for question in self.questions:
          if question in user_input.lower():
              return self.questions[question]
      return "I'm sorry, I don't understand that."

  def remember_context(self, key, value):
      self.context[key] = value

  def recall_context(self, key):
      return self.context.get(key, None)

  def ask_questions(self):
      questions_to_ask = [
          "What's your name?",
          "How are you feeling today?",
          "Do you like chatting with bots?"
      ]
      responses = {}
      for question in questions_to_ask:
          user_response = input(question + " ")
          responses[question] = user_response
          self.remember_context(question, user_response)
      return responses

  def chat(self):
      print(self.greet())
      while True:
          user_input = input("You: ")
          if any(farewell in user_input.lower() for farewell in ["bye", "goodbye", "exit"]):
              print(self.farewell())
              break
          if any(greeting in user_input.lower() for greeting in ["hello", "hi", "hey"]):
              print(self.greet())
              continue
          response = self.respond_to_question(user_input)
          if response == "I'm sorry, I don't understand that.":
              print(response)
              self.ask_questions()
          else:
              print(response)


if __name__ == "__main__":
  bot = SimpleChatbot()
  bot.chat()
