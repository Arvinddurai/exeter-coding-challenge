import csv, sys, time
import os
import psutil

def initialize_french_dictionary():
    with open('C:/exeter/TranslateWords Challenge/french_dictionary.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            french_dict[row[0]] = [row[1],0]

def translate(input_file):
    fp1 = open('t8.shakespeare.translate.txt', 'w')
    check_list = french_dict.keys()
    with open(input_file, 'r') as input_text:
        while True:
            line = input_text.readline()
            if not line:
                break
            buffer = ''
            for word in line.split():
                filtered = filter(str.isalpha,word)
                query = "".join(filtered)
                if query in check_list:
                    query_success = french_dict[query][0]
                    french_dict[query][1] += 1
                    word = word.replace(query, query_success)
                buffer += word + ' '
            buffer = buffer.strip()
            fp1.write(buffer + '\n')
    fp1.close()
    return True


def generate_performance(process_time, memory_info):
    with open('performance.txt', 'w') as file:
        file.write(f"Time to process : {process_time} seconds\n") 
        file.write(f"Memory used : {memory_info} MB")
    

if __name__ == '__main__':
    process_start_time = time.time()
    french_dict = {}
    input_file = 'C:/exeter/TranslateWords Challenge/t8.shakespeare.txt'

    if len(sys.argv) == 2:
        input_file = sys.argv[1]

    initialize_french_dictionary()
    translate(input_file)
    process_complete_time = time.time()
    memory_used = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    process_time = process_complete_time - process_start_time

    generate_performance(process_time, memory_used)
