






def LCS(s):
    '''
    takes a string, returns longest substring of continuous ordered alphabets, e.g 'a' then 'b' then 'c'
    the alphabets are circular, e.g xyzabc is a valic streak of length 6
    '''
    longest_streak = 0
    j  = 1
    while(j<len(s)):
        i = j
        streak = s[i-1]
        
        while (ord(s[i]) == (ord(s[i-1])+1)) or (ord(s[i-1]) == ord(s[i])+25):
            streak+= s[i]
            i+=1
            if(i == len(s)):
                break
        if(i>j):
            j = i
        if(len(streak)>longest_streak):
            longest_streak = len(streak)
        if(i == len(s)):
            break
        j+=1
        
    return longest_streak


print('The longest streak is: ',LCS("xzyzabcabcafkdal;jfwxyzabcdefgksal;fdjklas;fhdhufuhb"))
        

        
        
