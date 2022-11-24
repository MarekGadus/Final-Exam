
def matrix(array):
    evenORodd=0
    output=""
    
    for line in array:
        
        if evenORodd%2==0:
            evenORodd2=0
            
            for wordEVEN in line:
                if evenORodd2%2==0:
                    output+=wordEVEN
                    
                else:
                    pass
                evenORodd2+=1
                
        else:
            evenORodd2=0
            
            for wordODD in line:
                if evenORodd2%2!=0:
                    output+=wordODD
                    
                else:
                    pass
                evenORodd2+=1
                
        evenORodd+=1
    return output

print(matrix([["n","x"],["m","o"]]))    
print(matrix([["h", "p", "e"],["k", "l", "a"],["l", "m", "o"]]))          
    
import unittest

class Testsum(unittest.TestCase):

    def test_method1(self):

        
    
        self.assertEqual(matrix([["n","x"],["m","o"]]),"no")
        
    def test_method2(self):

        
    
        self.assertEqual(matrix([["h", "p", "e"],["k", "l", "a"],["l", "m", "o"]]),"hello")
        
        
        
if __name__== '__main__':
    unittest.main()