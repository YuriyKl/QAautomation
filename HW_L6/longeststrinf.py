# #!/usr/bin/python3

longeststr = ''
longeststr_len = 0
somefile = "somefile"

with open(somefile, 'r') as f:
    for line in f:
        if len(line) > longeststr_len:
            longeststr_len = len(line)
            longeststr = line

print (longeststr)