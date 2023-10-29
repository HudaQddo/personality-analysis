class Personality:
    
    def __init__(self , name , occurrence) :
        self.name = name
        self.occurrence = occurrence
        self.positive = 0
        self.negative = 0

    def finalResults(self) :
        posValue = (self.positive / self.occurrence) * 100
        negValue = (self.negative / self.occurrence) * 100
        value = max(posValue , negValue)
        if value == posValue : 
            personality = self.name[0]
        else :
            personality = self.name[1]
        return personality , posValue , negValue
    
    def updateValues(self , value):
        if value > 0 :
            self.positive += 1
        elif value < 0 :
            self.negative += 1
        else:
            self.occurrence -= 1
            
            