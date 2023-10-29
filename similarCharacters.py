from ast import Str
from mimetypes import init


class SimilarCharacters: 
    def __init__(self) :
        self.personalities = [  "ESTJ" , "ESTP" , "ESFJ" , "ESFP" ,
                                "ENTJ" , "ENTP" , "ENFJ" , "ENFP" ,
                                "ISTJ" , "ISTP" , "ISFJ" , "ISFP" ,
                                "INTJ" , "INTP" , "INFJ" , "INFP" ]
        
        self.similarCharacters = {}
        self.similarCharacters[self.personalities[0]] = ["Robb Stark", "Violet Crawley", "Boromir", "Laura Linney", "Frank Sinatra"]
        self.similarCharacters[self.personalities[1]] = ["Madonna", "Nicolass Sarkozy", "Eddie Murphy", "Jack Nicholson", "Ernest Hemingway"]
        self.similarCharacters[self.personalities[2]] = ["Bill Clinton", "Steve Harvey", "Tennifer Lopez", "Taylor Swift", "Monica"]
        self.similarCharacters[self.personalities[3]] = ["Elton John", "Marilyn Monroe", "Jamie Oliver", "Adele", "Jamie Foxx"]
        self.similarCharacters[self.personalities[4]] = ["Steve Jobs", "Gordon Ramsay", "Jim Carrey", "Whoopi Goldberg", "Harrison Ford"]
        self.similarCharacters[self.personalities[5]] = ["Thomas Edison", "Sacha Baron Cohen", "Captain Jack Sparrow", "Mark Watney", "Julian Sark"]
        self.similarCharacters[self.personalities[6]] = ["Barack Obama", "Oprah Winfrey", "John Cusack", "Ben Affleck", "Jennifer Lawrence"]
        self.similarCharacters[self.personalities[7]] = ["Will Smith", "Spider Man", "Robert Downey Jr", "Robin Williams", "Russell Brand"]
        self.similarCharacters[self.personalities[8]] = ["Angela Merkel", "Condoleeza Rice", "Dana Scully", "Denzel Washington", "Sting"]
        self.similarCharacters[self.personalities[9]] = ["Tom Cruise", "Jessica Jones", "Michelle Rodriguez", "Daniel Craig", "Milla Jovovich"]
        self.similarCharacters[self.personalities[10]] = ["Dr. Watson", "Qeen Elizabeth 2", "Kate Middleton", "Selena Gomez", "Vin Diesel"]
        self.similarCharacters[self.personalities[11]] = ["Lana Del Rey", "Jung Kook", "Avril Lavigne", "Kevin Costne", "Frida Kahlo"]
        self.similarCharacters[self.personalities[12]] = ["Michelle Obama", "Jay Gatsby", "Walter White", "Samantha Power", "Elon Musk"]
        self.similarCharacters[self.personalities[13]] = ["Bill Gates", "Albert Einstein", "Isaac Newton", "Blaise Pascal", "Bruce Banner"]
        self.similarCharacters[self.personalities[14]] = ["Nelson Mandela", "Lady Gaga", "Rose Bukater", "Tom Kirkman", "James Wilson"]
        self.similarCharacters[self.personalities[15]] = ["Johnny Depp", "William Shakespeare", "Alicia Keys", "Julia Roberts", "Arwen"]

    def getSimilarCharacters(self , personality) :
        return self.similarCharacters[personality]