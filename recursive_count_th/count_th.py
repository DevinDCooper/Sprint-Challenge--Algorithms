'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
# checking the length of our word is it's less then 2 index return 0
    if len(word) < 2:
        return 0
        # 1st 2 elements matche count it 1 and recursive call on all but first element
    if "th" in word[:2]:
        return 1 + count_th(word[1:])
    # 1st element doesn't match don't count 0 and recursive call on all but the first element
    else:
        return 0 + count_th(word[1:])
    
    # TBC
    

