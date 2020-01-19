def count_substring(string, sub_string):
    res = 0
    n = len(string)
    k = len(sub_string)
    for i in range(n-k+1):
        if sub_string == string[i:i+k]:
            res += 1
    return res

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count