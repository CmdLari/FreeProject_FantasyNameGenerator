import random

class fantasyNameGenerator:


    
    def __init__(self):
        self.vocals = ["a", "e", "i", "o", "u"]
        self.consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t"] 
        self.rareConsonants = ["z", "y", "x", "v", "w"]
        self.all = ["a", "e", "i", "o", "u", "y", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "z", "x"]

        
    def buildAName(self):

        name = self.firstLetter()
        name = self.addLetter(name)
        name = self.lastLetter(name)

        print(name.capitalize())


    def firstLetter(self):
        return random.choice(self.all)
                
    def checkLetterBefore(self, name):
        if name[-1] =='c':
            rnd=random.randint(0,1)
            if rnd=='0':
                name+='h'
        if name[-1] =='l':
            rnd=random.randint(0,2)
            if rnd=='0':
                name+='l'
            elif rnd=='1':
                name+='h'
        return name

                
    
    def addLetter(self, name):
        rnd=random.randint(4, 8)
        self.checkLetterBefore(name)
        for x in range(1, rnd):
            if x%2==1:
                name+=self.addVocal()
                self.checkLetterBefore(name)
            if x%2==0:
                name+=self.addConsonant()
                self.checkLetterBefore(name)

        return name
    

    def addVocal(self):
        return random.choice(self.vocals)

    def addConsonant(self):
        rnd = random.randint(0,3)
        if rnd==3:
            return random.choice(self.rareConsonants)
        else:
            return random.choice(self.consonants)

    def lastLetter(self, name):
        name+=random.choice(self.vocals)
        return name

fantasyNameGenerator().buildAName()


    