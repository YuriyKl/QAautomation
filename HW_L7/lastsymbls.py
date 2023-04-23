# #!/usr/bin/python3

file_path = input("Input path to file: ")
symbol_number = int(input("Input last N symbols which should be printed: "))+1

def read_last(file_path =file_path, symbol_number =symbol_number):
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                if len(line) > 0:
                   # line_n = line[-symbol_number:]
                    # print(line_n)
                    first, last_N, _ = line.partition(line[-symbol_number:])
                    print(last_N)

read_last(file_path, symbol_number)