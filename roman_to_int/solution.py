def romanToInt(s):
        val= {"I":1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M": 1000} 
        final = 0
        for i in range (0,len(s)):
            # print(val[s[i]])
            if len(s) == 1:
                return val[s[i]]
            if i == 0:
                final += val[s[i]]
            elif val[s[i]] <= val[s[i-1]]:
                final += (val[s[i]])
            elif val[s[i]] > val[s[i-1]]:
                if final < val[s[i]]:
                    final= (val[s[i]])-final
                else:
                    # val[s[i]] -= val[s[i-1]]
                    final += (val[s[i]]- 2*val[s[i-1]])
                    print("final", final)
            print(final)
        return final

print(romanToInt("MCMXCIV"))

