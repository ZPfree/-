import random
import json
def read_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [json.loads(line) for line in lines]

def split_data(data, train_ratio=0.95):
    random.shuffle(data)
    train_size = int(len(data) * train_ratio)
    return data[:train_size], data[train_size:]

def main():
    file_path = '/root/muturn3.jsonl'
    data = read_jsonl(file_path)
    train_data, test_data = split_data(data)

    # Save the train and test data to separate files
    with open('/root/ft-med//data/train_data1.jsonl', 'w',encoding='utf-8') as train_file:
        for item in train_data:
            train_file.write(json.dumps(item) + '\n')

    with open('/root/ft-med/data/test_data1.jsonl', 'w',encoding='utf-8') as test_file:
        for item in test_data:
            test_file.write(json.dumps(item) + '\n')

if __name__ == '__main__':
    main()
