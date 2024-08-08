# we are given a string1 that is smaller than s2 
# if there is a permutation of s1 in s2 return true
from collections import defaultdict

def ifpermutation(s1,s2):

    window_size = len(s1)

    s1_frequency_dict = defaultdict(lambda:0)
    for c in s1:
        s1_frequency_dict[c] +=1

    # count all the fequencies in the 

    s2_window_dict =  defaultdict(lambda:0)

    # intialize the first set of frequences 
    for c in s2[:window_size]:
        s2_window_dict[c] +=1


    if s2_window_dict == s1_frequency_dict:
        return True
    
    #now apply sliding window

    for i in range(0,len(s2)-window_size):
        # remove the char at position i and compare
        char_i = s2[i]
        s2_window_dict[char_i] -=1

        if s2_window_dict[char_i] == 0:
            del s2_window_dict[char_i]

        # add in the next
        s2_window_dict[s2[i+window_size]] += 1

        if s2_window_dict == s1_frequency_dict:
            return True
 
    return False




if __name__ == '__main__':
    s1 = "abc"
    s2 = "lecabee"
    print(ifpermutation(s1, s2))