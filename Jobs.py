from ast import Str
from mimetypes import init


class Jobs: 
    def __init__(self) :
        self.personalities = [  "ESTJ" , "ESTP" , "ESFJ" , "ESFP" ,
                                "ENTJ" , "ENTP" , "ENFJ" , "ENFP" ,
                                "ISTJ" , "ISTP" , "ISFJ" , "ISFP" ,
                                "INTJ" , "INTP" , "INFJ" , "INFP" ]
        
        self.jobs = {}
        self.jobs[self.personalities[0]] = ["Building Inspector" , "Hotel Manager" , "Paralegal" , "Police Officer" , "Real Estate Agent"]
        self.jobs[self.personalities[1]] = ["Actor" , "Entrepreneur" , "Marketer" , "Paramedic" , "Stockbroker"]
        self.jobs[self.personalities[2]] = ["Bookkeeper" , "Caterer" , "Medical Researcher" , "Office Manager" , "Optometrist"]
        self.jobs[self.personalities[3]] = ["Event planner" , "Firefighter" , "Flight Attendant" , "Tour Guide" , "Wait Staff"]
        self.jobs[self.personalities[4]] = ["Budget Analyst" , "Business Administrator" , "Construction Manager" , "Judge" , "Public Relations Specialist"]
        self.jobs[self.personalities[5]] = ["Attorney" , "Copywriter" , "Creative Director" , "Financial Planner" , "Systems Analyst"]
        self.jobs[self.personalities[6]] = ["Art Director" , "Market Research Analyst" , "Mediator" , "Public Speaker" , "Real Estate Broker"]
        self.jobs[self.personalities[7]] = ["Campaign Manager" , "Dance Instructor" , "Editor" , "Urban Planner" , "Youth Mentor"]
        self.jobs[self.personalities[8]] = ["Actuary" , "Civil Engineer" , "Curator" , "Dentist" , "Lawyer"]
        self.jobs[self.personalities[9]] = ["Airline Pilot" , "Chef" , "Economist" , "Health Inspector" , "Mechanic"]
        self.jobs[self.personalities[10]] = ["Accountant" , "Account Manager" , "Administrative Officer" , "Customer Service Representative" , "Research Analyst"]
        self.jobs[self.personalities[11]] = ["Archaeologisst" , "Bookkeeper" , "Dietician" , "Occupational Therapist" , "Veterinarian"]
        self.jobs[self.personalities[12]] = ["Architect" , "Business Strategist" , "Investigator" , "Microbiologist" , "Statistician"]
        self.jobs[self.personalities[13]] = ["Biomedical Engineer" , "Composer" , "Computer Systems Analyst" , "Environmental Scientist" , "Marketing Consultant"]
        self.jobs[self.personalities[14]] = ["HR Manager" , "Massage Therapist" , "Physical Therapist" , "Psychologist" , "School Counselor"]
        self.jobs[self.personalities[15]] = ["Artist" , "Film Editor" , "Journalist" , "Museum Curator" , "Registered Nurse"]

    def getJobs(self , personality) :
        return self.jobs[personality]