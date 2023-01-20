file = './data/train.txt'

# split ny newline
cnt = 0
with open(file) as f:
    # split by newline
    str = ""
    for line in f:
        # split by space
        print(line)
        cnt+=1
        if cnt ==3:
            break
