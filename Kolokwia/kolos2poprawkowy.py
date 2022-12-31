samogloski = ['a', 'e', 'i', 'o', 'u', 'y']




def cutting(s):


    def samogloska(char):
        return char in samogloski

    def cut_r(s, sum, samogloski):
        if s == "":
            return 0
        samo = 0
        for i in range(len(s)):
            if samogloska(s[i]):
                samo += 1
            if samo == 1:
                sum += cut_r(s[i+1:], sum+1, samogloski)
            if samo > 1:
                return sum
        if samo == 0:
            return 0
        else:
            return sum
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    return cut_r(s,0,samogloski)


print(cutting("informatyka"))