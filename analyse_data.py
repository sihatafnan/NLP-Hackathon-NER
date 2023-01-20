file = './data/train.txt'

# split ny newline
cnt = 0
with open(file) as f:
    # read all lines and split by null character
    content = f.read().split('\n')
    # split by newline
    str = ""
    for line in content:
        # split by space
        str += line
        if line == "":
            
            print(line)
            str = ""
        cnt+=1
        if cnt ==2:
            break
