#You are given a string S and width W. 
#Your task is to wrap the string into a paragraph of width W .
#python2code

def wrap(string, max_width):
        
        res = textwrap.fill(string,max_width)
        
        return res
        
 if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
