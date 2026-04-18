print ("WELCOME TO THE GAME OF KAUN BANEGA CROREPATI (KBC)")
print ("YOU ARE VERY WELCOME TO THE GAME \n THE RULES ARE SIMPLE :\n JUST YOU HAVE TO CHOOSE THE CORRECT OPTION AND YOU WILL EARN  MORE AND MORE POINTS AS YOU PROCED IN THE GAME ") 


import random

questions = [
    ["Article for amendment?", "A. 356", "B. 368", "C. 370", "D. 360", "B"],
    ["First Indian Nobel Prize winner?", "A. C.V. Raman", "B. Rabindranath Tagore", "C. Mother Teresa", "D. Amartya Sen", "B"],
    ["Sorrow of Bihar river?", "A. Kosi", "B. Ganga", "C. Yamuna", "D. Damodar", "A"],
    ["RBI established year?", "A. 1935", "B. 1947", "C. 1920", "D. 1950", "A"],
    ["Mughal who removed Jizya?", "A. Aurangzeb", "B. Babur", "C. Akbar", "D. Shah Jahan", "C"],
    ["Deepest ocean trench?", "A. Mariana", "B. Tonga", "C. Java", "D. Puerto Rico", "A"],
    ["SI unit of electric flux?", "A. Volt", "B. Newton", "C. Weber", "D. Coulomb", "C"],
    ["Panchayati Raj committee?", "A. Sarkaria", "B. Balwant Rai Mehta", "C. Mandal", "D. Kothari", "B"],
    ["Bicameral state?", "A. Maharashtra", "B. UP", "C. Karnataka", "D. All", "D"],
    ["Vitamin for anemia?", "A. B1", "B. B6", "C. B12", "D. D", "C"],
    ["Founder of Gupta Empire?", "A. Maurya", "B. Samudragupta", "C. Chandragupta I", "D. Ashoka", "C"],
    ["Gas in Haber process?", "A. Oxygen", "B. Nitrogen", "C. Hydrogen", "D. Both B and C", "D"],
    ["First Mars satellite of India?", "A. Chandrayaan", "B. Mangalyaan", "C. INSAT", "D. GSAT", "B"],
    ["Anti-defection schedule?", "A. 8th", "B. 10th", "C. 7th", "D. 9th", "B"],
    ["Capital of India?", "A. Mumbai", "B. Chennai", "C. Kolkata", "D. New Delhi", "D"]
]

money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7000000]

random.shuffle(questions)

total = 0

for i in range(15):
    print("\nQuestion", i+1, "for", money[i])
    
    q = questions[i]
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])
    
    ans = input("Enter answer: ").upper()
    
    if ans == q[5]:
        print("Correct")
        total = money[i]
    else:
        print("Wrong. Correct answer:", q[5])
        break

print("\nYou won:", total)