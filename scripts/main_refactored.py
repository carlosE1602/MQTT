import sys
import math
import ast
import json

def calcula_cache(tam_ram, tam_cache, tam_bloco, way=1):
  bits_end = int(math.log2(tam_ram))
  bits_bloco = int(math.log2(tam_bloco))
  bits_cache = int(math.log2(tam_cache))
  bits_cache -= int(math.log2(way) + bits_bloco)
  bits_tag = int(bits_end - bits_bloco - bits_cache)
  return {"tag": bits_tag, "cache": bits_cache, "bloco": bits_bloco}


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
args = ast.literal_eval(json.loads(sys.argv[1])) 


# get the list with answer

response = json.loads(args['answer'])
params = args['params']

#response contains the values used to check if the answer is right
if(len(response) == 2):

  bits_tag, bits_cache, bits_block = response[0]
  way, ram_size, cache_size, block_size = response[1]
  result = calcula_cache(int(ram_size), int(cache_size), int(block_size), int(way))

  if(result["tag"] == int(bits_tag) and result["bloco"] == int(bits_block) and result["cache"] == int(bits_cache)):
    msg = f"{args['form_question']};{[True,response[1]]};{args['id']};{args['generate_time']};{args['send_time']};{args['session_start_time']};{params}"

    if params.count('SHOW_SOLUTION'):
      msg = msg + f";{result}"
    print(msg, end="")
  else: 
    msg = f"{args['form_question']};{[False,response[1]]};{args['id']};{args['generate_time']};{args['send_time']};{args['session_start_time']};{params}"
    if params.count('SHOW_SOLUTION'):
      msg = msg + f";{result}"
    print(msg, end="")
