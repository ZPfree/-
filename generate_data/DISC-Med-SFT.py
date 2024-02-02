import random
import json
import random

def read_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [json.loads(line) for line in lines]

def process_conversations(data):
    #if len(data) % 2:
        # The last round of conversation solely consists of input
        # without any output.
        # Discard the input part of the last round, as this part is ignored in
        # the loss calculation.
     #   data.pop()
    processed_data = [] 
    for conversation in data:
        #print(conversation)
        #print(len(conversation['conversation']))#role 长度
        processed_conversation = []
        cl = len(conversation['conversation'])
        if cl%2:
            conversation['conversation'].pop()
        system = "你是一个医疗助手，请提供我医疗建议"
        preconversation =  []
        for j in range(0, cl-1, 2):
             #print("+++",j)
             #print(conversation['conversation'][j]['content'])
             q_a = {}
             if j == 0:
                    q_a = {'system':system, 'input':conversation['conversation'][j]['content'], 'output':conversation['conversation'][j+1]['content']}
             else:
                    q_a = {'input':conversation['conversation'][j]['content'], 'output':conversation['conversation'][j+1]['content']}
                # print(q_a)
             preconversation.append(q_a)
        #processed_conversation.append(preconversation)
      
           # print(turn)
        processed_data.append({
              'conversation': preconversation
         })  
    #print(processed_data)
    return processed_data

def main():
    input_file_path = '/root/DISC-Med-SFT_released.jsonl'
    output_file_path = '/root/muturn3.jsonl'
    data = read_jsonl(input_file_path)
    #print(data[1:2])
    processed_data = process_conversations(data)
    #print(processed_data)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
      for item in processed_data:
          output_file.write(json.dumps(item) + '\n')

if __name__ == '__main__':
    main()
