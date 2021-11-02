import unittest

############ Pregunta 1 #######################

def reverseList(list):
    a = len(list)
    if a<= 1:
        print(list)
    else:
        for i in range(0,int(a/2)):
            list[i] , list[(-1-i)] = list[(-1-i)], list[i]
        print(list)
    return list


class reverseListTest(unittest.TestCase):

    def testTwo(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])

    def testThree(self):
       self.assertEqual(reverseList([1,2,3,4,5]), [5,4,3,2,1])
    
    def testFour(self):
       self.assertEqual(reverseList([1]), [1])

if __name__ == '__main__':
    unittest.main()
"""
############ Pregunta 2 #######################
"""
def isPalindrome(string):
    a = []
    b = []
    for i in range(len(string)):
        a.append(string[i])
    print(a)
    for j in range(len(string)-1,-1,-1):
        b.append(string[j])
    print(b)
    if a == b:
        return f"{string} is a Palindrome"
    else:
        return f"{string} is not a Palindrome"

class isPalindromeTest(unittest.TestCase):

    def testTwo(self):
        self.assertEqual(isPalindrome("HannaH"), "HannaH is a Palindrome")

    def testThree(self):
       self.assertEqual(isPalindrome("Rose"), "Rose is not a Palindrome")
    
    

if __name__ == '__main__':
    unittest.main()



############ Pregunta 3 #######################

def monedas(centavos):
    a = [0,0,0,0]
    
    a[0] = int(centavos/25)
    a[1] = int((centavos%25)/10)
    a[2] = int(((centavos%25)%10)/5)
    a[3] = ((centavos%25)%10)%5
    print(a)
    return a



class monedasTest(unittest.TestCase):

    def testTwo(self):
        self.assertEqual(monedas(87), [3,1,0,2])

    def testThree(self):
       self.assertEqual(monedas(75), [3,0,0,0])
    
    def testFour(self):
       self.assertEqual(monedas(33), [1,0,1,3])
    
    def testfive(self):
        self.assertEqual(monedas(108), [4,0,1,3])
    
    def testSix(self):
        self.assertEqual(monedas(17), [0,1,1,2])
    

if __name__ == '__main__':
    unittest.main()

########### Pregunta 4 ####################

def Factorial(entero):
    if entero == 0 or entero == 1:
        return 1
    elif entero == 2:
        return 2
    else:
        return entero*Factorial(entero-1)

class factorialTest(unittest.TestCase):

    def testTwo(self):
        self.assertEqual(Factorial(4), 24)

    def testThree(self):
       self.assertEqual(Factorial(5), 120)
    
    def testFour(self):
       self.assertEqual(Factorial(9), 362880)
    
  
if __name__ == '__main__':
    unittest.main()



########## Pregunta 5 ############

def fibonacci(entero):
    if entero == 1:
        return 0
    elif entero == 2:
        return 1
    elif entero == 3:
        return fibonacci(2) + fibonacci(1)
    else:
        return fibonacci(entero-1) + fibonacci(entero-2)


class fibonacciTest(unittest.TestCase):

    def testTwo(self):
        self.assertEqual(fibonacci(4), 2)

    def testThree(self):
       self.assertEqual(fibonacci(5), 3)
    
    def testFour(self):
       self.assertEqual(fibonacci(9), 21)
    
  
if __name__ == '__main__':
    unittest.main()