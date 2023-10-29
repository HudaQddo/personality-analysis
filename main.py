import tkinter as tk
from experta import *
import tkinter.font as tkFont
from Questions import englishQuestions
from Answers import englishAnswers
from ArabicQuestions import arabicQuestions
from ArabicAnswers import arabicAnswers
from ChoiceWeights import choiceWeights
from Personality import Personality
from Jobs import Jobs
from similarCharacters import SimilarCharacters

questions = englishQuestions
answers = englishAnswers

language = "EN"
f = open("language.txt", "r")
if f.read() == "AR":
    questions = arabicQuestions
    answers = arabicAnswers
    language = "AR"
f.close()

fact = {}
fact[0] = Personality('EI', 9)
fact[1] = Personality('SN', 9)
fact[2] = Personality('TF', 11)
fact[3] = Personality('JP', 11)

root = tk.Tk()

indexOfQuestion = 1
selectedAnswerNumber = 0

background = "white"
backgroundAnswerColor = "#99C4C8"
textAnswerColor = "#112B3C"
textQuestionColor = "#417D7A"
mainColor = "#293462"

oneFont = tkFont.Font(family="Tahoma", size=15, weight="bold")
twoFont = tkFont.Font(family="Tahoma", size=20)
threeFont = tkFont.Font(family="Tahoma", size=15)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg=background)
canvas.grid(columnspan=3, rowspan=15)

number = "Question " + str(indexOfQuestion) + " / " + str(len(questions))
if language == "AR":
    number = "السؤال " + str(indexOfQuestion) + " / " + str(len(questions))
numberOfQuestion = tk.Label(root, text=number, font=oneFont, bg=background, fg=mainColor)
numberOfQuestion.grid(columnspan = 3, column = 0, row = 0)

subQuestion = tk.Label(root, text=questions[1], wraplength=1250, fg=textQuestionColor, bg=background, font=twoFont)
subQuestion.grid(columnspan=3, column = 0,row = 2)

subAnswer1 = tk.Button(root, text=answers[1][0], bd=0, pady=5, command=lambda *args: checkAnswer(1), width=100, fg=textAnswerColor, bg=background, font=threeFont)
subAnswer1.grid(columnspan=3, column = 0,row = 3)
subAnswer2 = tk.Button(root, text=answers[1][1], bd=0, pady=5, command=lambda *args: checkAnswer(2), width=100, fg=textAnswerColor, bg=background, font=threeFont)
subAnswer2.grid(columnspan=3, column = 0,row = 4)
subAnswer3 = tk.Button(root, text=answers[1][2], bd=0, pady=5, command=lambda *args: checkAnswer(3), width=100, fg=textAnswerColor, bg=background, font=threeFont)
subAnswer3.grid(columnspan=3, column = 0,row = 5)
subAnswer4 = tk.Button(root, text="", bd=0, pady=5, command=lambda *args: checkAnswer(4), width=100, fg=textAnswerColor, bg=background, font=threeFont)
subAnswer4.grid(columnspan=3, column = 0,row = 6)
subAnswer5 = tk.Button(root, text="", bd=0, pady=5, command=lambda *args: checkAnswer(5), width=100, fg=textAnswerColor, bg=background, font=threeFont)
subAnswer5.grid(columnspan=3, column = 0,row = 7)

nextButton = tk.Button(root, text="Next", command=lambda *args: clickButtonNext(), font=("Tahoma",13), bg=mainColor, fg="white", height=2, width=13)
nextButton.grid(columnspan=3, column = 0,row = 8)
if language == "AR":
    nextButton['text'] = "التالي"

note = tk.Label(root, text="",font=twoFont, bg=background, fg="red")
note.grid(columnspan=3, column = 0,row = 9)

def checkAnswer(ind):
    global selectedAnswerNumber
    if ind == 1:
        selectedAnswerNumber = ind
        subAnswer1['bg'] = backgroundAnswerColor
        subAnswer2['bg'] = background
        subAnswer3['bg'] = background
        subAnswer4['bg'] = background
        subAnswer5['bg'] = background
    elif ind == 2:
        selectedAnswerNumber = ind
        subAnswer1['bg'] = background
        subAnswer2['bg'] = backgroundAnswerColor
        subAnswer3['bg'] = background
        subAnswer4['bg'] = background
        subAnswer5['bg'] = background
    elif ind == 3:
        selectedAnswerNumber = ind
        subAnswer1['bg'] = background
        subAnswer2['bg'] = background
        subAnswer3['bg'] = backgroundAnswerColor
        subAnswer4['bg'] = background
        subAnswer5['bg'] = background
    elif ind == 4 and len(answers[indexOfQuestion]) >= 4:
        selectedAnswerNumber = ind
        subAnswer1['bg'] = background
        subAnswer2['bg'] = background
        subAnswer3['bg'] = background
        subAnswer4['bg'] = backgroundAnswerColor
        subAnswer5['bg'] = background
    elif ind == 5 and len(answers[indexOfQuestion]) == 5:
        selectedAnswerNumber = ind
        subAnswer1['bg'] = background
        subAnswer2['bg'] = background
        subAnswer3['bg'] = background
        subAnswer4['bg'] = background
        subAnswer5['bg'] = backgroundAnswerColor
    
def swapQuestion(innerIndex, numberAnswer):
    expertSystem = rules()
    expertSystem.reset()
    expertSystem.declare(Fact(question = questions[innerIndex], answer = answers[innerIndex], number = numberAnswer))
    expertSystem.run()

def clickButtonNext():
    global selectedAnswerNumber
    
    if selectedAnswerNumber == 0:
        if language == "EN":
            note['text'] = "Please choose an answer"
        else:
            note['text'] = "رجاء قم باختيار إجابة"
        return
    
    global indexOfQuestion
    swapQuestion(indexOfQuestion, selectedAnswerNumber)
    
    if indexOfQuestion == 34 :
        if language == "EN":
            nextButton['text'] = "Result"
        else:
            nextButton['text'] = "النتيجة"
    
    if indexOfQuestion == 35 :
        openResult()
        return
    
    selectedAnswerNumber = 0
    indexOfQuestion += 1
    if language == "EN":
        number = "Question " + str(indexOfQuestion) + " / " + str(len(questions))
    else:
        number = "السؤال " + str(indexOfQuestion) + " / " + str(len(questions))
    numberOfQuestion['text'] = number
    subQuestion['text'] = questions[indexOfQuestion]
    subAnswer1['text'] = answers[indexOfQuestion][0]
    subAnswer1["bg"] = background
    subAnswer2['text'] = answers[indexOfQuestion][1]
    subAnswer2["bg"] = background
    subAnswer3['text'] = answers[indexOfQuestion][2]
    subAnswer3["bg"] = background
    if len(answers[indexOfQuestion]) >= 4:
        subAnswer4['text'] = answers[indexOfQuestion][3]
        subAnswer4["bg"] = background
        if len(answers[indexOfQuestion]) == 5:
            subAnswer5['text'] = answers[indexOfQuestion][4]
            subAnswer5["bg"] = background
        else:
            subAnswer5['text'] = ""
            subAnswer5["bg"] = background
    else:
        subAnswer4['text'] = ""
        subAnswer4["bg"] = background
    
    note['text'] = ""

def openResult():
    namePersonal, ratePersonal = characterResult()

    root.destroy()
    rootResult = tk.Tk()

    screen_width = rootResult.winfo_screenwidth()
    screen_height = rootResult.winfo_screenheight()
    canvasResult = tk.Canvas(rootResult, width=screen_width, height=screen_height, bg='white')
    canvasResult.grid(columnspan=3, rowspan=8)

    title = tk.Label(rootResult, text="Test Result", font=("Tohamo",25), bg='white', fg=mainColor)
    title.grid(column = 1, row = 0)
    if language == "AR":
        title['text'] = "نتيجة الاختبار"
    
    result = tk.Label(rootResult, text=namePersonal, font=threeFont, bg='white', fg=textQuestionColor)
    result.grid(column = 1, row = 1)

    tk.Label(rootResult, text="E", font=twoFont, bg=background).grid(column=0, row=2)
    EI = tk.Scale(rootResult, from_=0, to=100, length=600, bg="#006E7F", orient=tk.HORIZONTAL)
    EI.set(ratePersonal[0])
    EI['state'] = tk.DISABLED
    EI.grid(column=1, row=2)
    tk.Label(rootResult, text="I", font=twoFont, bg=background).grid(column=2, row=2)

    tk.Label(rootResult, text="S", font=twoFont, bg=background).grid(column=0, row=3)
    SN = tk.Scale(rootResult, from_=0, to=100, length=600, bg="#764AF1", orient=tk.HORIZONTAL)
    SN.set(ratePersonal[1])
    SN['state'] = tk.DISABLED
    SN.grid(column=1, row=3)
    tk.Label(rootResult, text="N", font=twoFont, bg=background).grid(column=2, row=3)

    tk.Label(rootResult, text="T", font=twoFont, bg=background).grid(column=0, row=4)
    TF = tk.Scale(rootResult, from_=0, to=100, length=600, bg="#5F7161", orient=tk.HORIZONTAL)
    TF.set(ratePersonal[2])
    TF['state'] = tk.DISABLED
    TF.grid(column=1, row=4)
    tk.Label(rootResult, text="F", font=twoFont, bg=background).grid(column=2, row=4)

    tk.Label(rootResult, text="J", font=twoFont, bg=background).grid(column=0, row=5)
    JP = tk.Scale(rootResult, from_=0, to=100, length=600, bg="#B1BCE6", orient=tk.HORIZONTAL)
    JP.set(ratePersonal[3])
    JP['state'] = tk.DISABLED
    JP.grid(column=1, row=5)
    tk.Label(rootResult, text="P", font=twoFont, bg=background).grid(column=2, row=5)


    careerButton = tk.Button(rootResult, text="Career ideas", command=lambda *args: openJob(namePersonal), font=("Tahoma",13), bg=mainColor, fg="white", height=2, width=13)
    careerButton.grid(column=1, row=6)
    if language == "AR":
        careerButton['text'] = "أفكار وظيفية"

def openJob(typePersonal):
    rootJob = tk.Tk()
    screen_width = rootJob.winfo_screenwidth()
    screen_height = rootJob.winfo_screenheight()

    canvasExplain = tk.Canvas(rootJob, width=screen_width, height=screen_height, bg='white')
    canvasExplain.grid(columnspan=3, rowspan=8)
    
    title = tk.Label(rootJob, text="Careers suitble for your character : ", font=("Tahoma",20), bg=background ,fg=mainColor)
    title.grid(column=1, row=0)
    personality = tk.Label(rootJob, text=typePersonal, font=("Tahoma",20), bg=background ,fg=mainColor)
    personality.grid(column=1, row=1)
    
    if language == "AR":
        title['text'] = "وظائف مناسبة لشخصيتك "
    
    j = Jobs()
    jobs = j.getJobs(typePersonal)
    
    tk.Label(rootJob, text=jobs[0], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(column=0, row=2)
    tk.Label(rootJob, text=jobs[1], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(column=1, row=2)
    tk.Label(rootJob, text=jobs[2], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(column=2, row=2)
    tk.Label(rootJob, text=jobs[3], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(columnspan=2, column=0, row=3)
    tk.Label(rootJob, text=jobs[4], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(columnspan=2, column=1, row=3)

    similarCharactersButton = tk.Button(rootJob, text="Similar personalities", command=lambda *args: openSimilarCharacters(typePersonal), font=("Tahoma",13), bg=mainColor, fg="white", height=2, width=25)
    similarCharactersButton.grid(column=1, row=4)
    if language == "AR":
        similarCharactersButton['text'] = "شخصيات مشابهة"

def openSimilarCharacters(typePersonal):
    rootSimilarCharacters = tk.Tk()
    screen_width = rootSimilarCharacters.winfo_screenwidth()
    screen_height = rootSimilarCharacters.winfo_screenheight()

    canvasExplain = tk.Canvas(rootSimilarCharacters, width=screen_width, height=screen_height, bg='white')
    canvasExplain.grid(columnspan=3, rowspan=8)
    
    title = tk.Label(rootSimilarCharacters, text="Similar Characters:", font=("Tahoma",20), bg=background ,fg=mainColor)
    title.grid(column=1, row=0)
    personality = tk.Label(rootSimilarCharacters, text=typePersonal, font=("Tahoma",20), bg=background ,fg=mainColor)
    personality.grid(column=1, row=1)
    
    if language == "AR":
        title['text'] = "شخصيات مشابهة لشخصيتك"
    
    similarCharacters = SimilarCharacters()
    characters = similarCharacters.getSimilarCharacters(typePersonal)
    
    tk.Label(rootSimilarCharacters, text=characters[0], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(column=0, row=2)
    tk.Label(rootSimilarCharacters, text=characters[1], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(column=1, row=2)
    tk.Label(rootSimilarCharacters, text=characters[2], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(column=2, row=2)
    tk.Label(rootSimilarCharacters, text=characters[3], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(columnspan=2, column=0, row=3)
    tk.Label(rootSimilarCharacters, text=characters[4], font=("Tahoma",15), bg=background, fg=textQuestionColor).grid(columnspan=2, column=1, row=3)

def characterResult():
    [characterE, valE, n] = fact[0].finalResults()
    [characterS, valS, n] = fact[1].finalResults()
    [characterT, valT, n] = fact[2].finalResults()
    [characterJ, valJ, n] = fact[3].finalResults()
    name = characterE + characterS + characterT + characterJ
    values = [valE, valS, valT, valJ]
    
    return name, values

class rules(KnowledgeEngine):
    
    @Rule(Fact(question = questions[1], answer = answers[1], number = MATCH.num))
    def rule1(self, num):
        fact[0].updateValues(choiceWeights[1][0][num-1])
        
    @Rule(Fact(question = questions[2], answer = answers[2], number = MATCH.num))
    def rule2(self, num):
        fact[0].updateValues(choiceWeights[2][0][num-1])
        
    @Rule(Fact(question = questions[3], answer = answers[3], number = MATCH.num))
    def rule3(self, num):
        fact[0].updateValues(choiceWeights[3][0][num-1])

    @Rule(Fact(question = questions[4], answer = answers[4], number = MATCH.num))
    def rule4(self, num):
        fact[0].updateValues(choiceWeights[4][0][num-1])
        
    @Rule(Fact(question = questions[5], answer = answers[5], number = MATCH.num))
    def rule5(self, num):
        fact[0].updateValues(choiceWeights[5][0][num-1])
        
    @Rule(Fact(question = questions[6], answer = answers[6], number = MATCH.num))
    def rule6(self, num):
        fact[0].updateValues(choiceWeights[6][0][num-1])

    @Rule(Fact(question = questions[7], answer = answers[7], number = MATCH.num))
    def rule7(self, num):
        fact[0].updateValues(choiceWeights[7][0][num-1])

    @Rule(Fact(question = questions[8], answer = answers[8], number = MATCH.num))
    def rule8(self, num):
        fact[0].updateValues(choiceWeights[8][0][num-1])

    @Rule(Fact(question = questions[9], answer = answers[9], number = MATCH.num))
    def rule9(self, num):
        fact[0].updateValues(choiceWeights[9][0][num-1])

    @Rule(Fact(question = questions[10], answer = answers[10], number = MATCH.num))
    def rule10(self, num):
        fact[1].updateValues(choiceWeights[10][0][num-1])

    @Rule(Fact(question = questions[11], answer = answers[11], number = MATCH.num))
    def rule11(self, num):
        fact[1].updateValues(choiceWeights[11][0][num-1])

    @Rule(Fact(question = questions[12], answer = answers[12], number = MATCH.num))
    def rule12(self, num):
        fact[1].updateValues(choiceWeights[12][0][num-1])
        fact[3].updateValues(choiceWeights[12][1][num-1])

    @Rule(Fact(question = questions[13], answer = answers[13], number = MATCH.num))
    def rule13(self, num):
        fact[2].updateValues(choiceWeights[13][0][num-1])

    @Rule(Fact(question = questions[14], answer = answers[14], number = MATCH.num))
    def rule14(self, num):
        fact[1].updateValues(choiceWeights[14][0][num-1])

    @Rule(Fact(question = questions[15], answer = answers[15], number = MATCH.num))
    def rule15(self, num):
        fact[1].updateValues(choiceWeights[15][0][num-1])

    @Rule(Fact(question = questions[16], answer = answers[16], number = MATCH.num))
    def rule16(self, num):
        fact[1].updateValues(choiceWeights[16][0][num-1])
        fact[2].updateValues(choiceWeights[16][1][num-1])

    @Rule(Fact(question = questions[17], answer = answers[17], number = MATCH.num))
    def rule17(self, num):
        fact[2].updateValues(choiceWeights[17][0][num-1])

    @Rule(Fact(question = questions[18], answer = answers[18], number = MATCH.num))
    def rule18(self, num):
        fact[2].updateValues(choiceWeights[18][0][num-1])

    @Rule(Fact(question = questions[19], answer = answers[19], number = MATCH.num))
    def rule19(self, num):
        fact[2].updateValues(choiceWeights[19][0][num-1])
    
    @Rule(Fact(question = questions[20], answer = answers[20], number = MATCH.num))
    def rule20(self, num):
        fact[2].updateValues(choiceWeights[20][0][num-1])

    @Rule(Fact(question = questions[21], answer = answers[2], number = MATCH.num))
    def rule21(self, num):
        fact[1].updateValues(choiceWeights[21][0][num-1])
        fact[2].updateValues(choiceWeights[21][1][num-1])

    @Rule(Fact(question = questions[22], answer = answers[22], number = MATCH.num))
    def rule22(self, num):
        fact[2].updateValues(choiceWeights[22][0][num-1])

    @Rule(Fact(question = questions[23], answer = answers[23], number = MATCH.num))
    def rule23(self, num):
        fact[3].updateValues(choiceWeights[23][0][num-1])

    @Rule(Fact(question = questions[24], answer = answers[24], number = MATCH.num))
    def rule24(self, num):
        fact[3].updateValues(choiceWeights[24][0][num-1]) 

    @Rule(Fact(question = questions[25], answer = answers[25], number = MATCH.num))
    def rule25(self, num):
        fact[3].updateValues(choiceWeights[25][0][num-1])

    @Rule(Fact(question = questions[26], answer = answers[26], number = MATCH.num))
    def rule26(self, num):
        fact[3].updateValues(choiceWeights[26][0][num-1])

    @Rule(Fact(question = questions[27], answer = answers[27], number = MATCH.num))
    def rule27(self, num):
        fact[3].updateValues(choiceWeights[27][0][num-1])

    @Rule(Fact(question = questions[28], answer = answers[28], number = MATCH.num))
    def rules28(self, num):
        fact[2].updateValues(choiceWeights[28][0][num-1])
        fact[1].updateValues(choiceWeights[28][1][num-1])

    @Rule(Fact(question = questions[29], answer = answers[29], number = MATCH.num))
    def rules29(self, num):
        fact[3].updateValues(choiceWeights[29][0][num-1])

    @Rule(Fact(question = questions[30], answer = answers[30], number = MATCH.num))
    def rules30(self, num):
        fact[3].updateValues(choiceWeights[30][0][num-1])
        fact[2].updateValues(choiceWeights[30][1][num-1])
    
    @Rule(Fact(question = questions[31], answer = answers[31], number = MATCH.num))
    def rules31(self, num):
        fact[3].updateValues(choiceWeights[31][0][num-1])

    @Rule(Fact(question = questions[32], answer = answers[32], number = MATCH.num))
    def rule32(self, num):
        fact[3].updateValues(choiceWeights[32][0][num-1])

    @Rule(Fact(question = questions[33], answer = answers[33], number = MATCH.num))
    def rule33(self, num):
        fact[2].updateValues(choiceWeights[33][0][num-1])
    
    @Rule(Fact(question = questions[34], answer = answers[34], number = MATCH.num))
    def rule34(self, num):
        fact[3].updateValues(choiceWeights[34][0][num-1])

    @Rule(Fact(question = questions[35], answer = answers[35], number = MATCH.num))
    def rule35(self, num):
        fact[1].updateValues(choiceWeights[35][0][num-1])

root.mainloop()