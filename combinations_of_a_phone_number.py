digits="234"


def letterCombinations( digits: str):
        res = []
        hashmap={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        if digits == "":
            return []

        if len(digits) ==1 :
            return list(hashmap.get(digits[0]))

        fdigit = digits[0]
        
        for digit in digits[1:]:
            print(digit)
            for digitletter in hashmap.get(digit):
                for letter in hashmap.get(fdigit):
                    res.append("".join([letter,digitletter]))

        return res
    
    
print(letterCombinations(digits))