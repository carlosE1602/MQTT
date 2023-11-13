#be sure that u have paho-mqtt installed
class AbstractMqtt():
 
  def print_message(self, msg, width = 100):

    def format(m: str):
      if m == 'False':
        return "Resposta Errada"
      elif m == 'True':
        return "Resposta Correta"
      else: return m

    msg = map(format, msg)



    print("*" * width)
    print("*" + " " * (width - 2) + "*")
    print("*" + " " * (width - 2) + "*")
    for m in msg:
      print("*" + " " * ((width - len(m)) // 2 - 1) + m + " " * ((width - len(m)) // 2) + "*")
    print("*" + " " * (width - 2) + "*")
    print("*" + " " * (width - 2) + "*")
    print("*" * width)




  
