import sys
import math
import ast
import json

def avalia(inp, question):
    letter = "abcd"
    i = 0
    solution = ""
    
    for q in question:
      if q == '0':
          solution += "~"+letter[i]
      elif q == '1':
          solution += letter[i]
      else:
        solution += "."
      i+= 1
    return inp == solution, "Solução: " + solution


"""
{"form_question":form_question,
             "answer": answer,
              "id": id,
              "generate_time": initialTime,
             "send_time": responseTime,
             "session_start_time" : t
              "params": ['SHOW_SOLUTION']
      }

"""

# convert args string into respective dict
args = ast.literal_eval(str(sys.argv[1])) 

# get the list with answer

response = ast.literal_eval(args['answer'])
params = args['params']

#response contains the values used to check if the answer is right
if(len(response) == 2):
  inp = response[0]
  question = response[1]
  result, solution = avalia(inp, question)

  if(result):
    msg = f"{args['form_question']};{[True,response[1]]};{args['id']};{args['generate_time']};{args['send_time']};{args['session_start_time']};{params}"

    if params.count('SHOW_SOLUTION'):
      msg = msg + f";{solution}"
    print(msg, end="")
  else: 
    msg = f"{args['form_question']};{[False,response[1]]};{args['id']};{args['generate_time']};{args['send_time']};{args['session_start_time']};{params}"
    if params.count('SHOW_SOLUTION'):
      msg = msg + f";{solution}"
    print(msg, end="")
