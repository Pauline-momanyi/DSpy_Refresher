class Math:
    # static methods don't change. They don't act on anything so they don't take the self arg
    
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def pr():
        print ("run")
        
        
print(Math.add5(10))
Math.pr()