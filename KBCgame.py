#KBC
questions=[["Which language was used to create Facebook?", "Python", "French", "Java", "C++", 4],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What is the capital city of Japan?", "Beijing", "Tokyo", "Seoul", "Bangkok", 2],
    ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "NaCl", 1],
    ["Which gas is most abundant in the Earth's atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 3],
    ["What is the hardest natural substance on Earth?", "Gold", "Diamond", "Silver", "Iron", 2],
    ["Which planet is the hottest in the solar system?", "Mercury", "Venus", "Earth", "Mars", 2],
    ["Who was the first President of the United States?", "Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams", 3],
    ["In which year did the Titanic sink?", "1905", "1912", "1918", "1923", 2],
    ["Which ancient civilization built the Pyramids?", "Romans", "Greeks", "Egyptians", "Mayans", 3],
    ["Who was the famous Greek philosopher who taught Alexander the Great?", "Socrates", "Plato", "Aristotle", "Pythagoras", 3],
    ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen", 3],
    ["Which novel begins with the line 'Call me Ishmael'?", "1984", "Moby-Dick", "To Kill a Mockingbird", "The Great Gatsby", 2],
    ["Who wrote the Harry Potter series?", "J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "C.S. Lewis", 2],
    ["Which book is considered the first novel ever written?", "Don Quixote", "The Tale of Genji", "The Canterbury Tales", "Beowulf", 2],
    ["Which is the largest desert in the world?", "Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Desert", 4],
    ["What is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", 2],
    ["Mount Everest is located in which mountain range?", "Andes", "Alps", "Himalayas", "Rockies", 3],
    ["Which country has the largest population in the world?", "India", "United States", "China", "Indonesia", 3],
    ["Which country won the FIFA World Cup in 2018?", "Brazil", "Germany", "France", "Argentina", 3],
    ["Which sport is known as 'The Beautiful Game'?", "Basketball", "Football (Soccer)", "Tennis", "Rugby", 2]

           ]
levels = [1000,2000,3000,5000,10000,15000,20000,25000,30000,32000,40000,50000,60000,700000,100000000,1200000]
money = 0
i = 0
for i in range(len(questions)):
  question = questions[i]
  print(f"\n\nYou are ready for Rs. {levels[i]}")
  print(f"Your question is {question[0]}")
  print(f"a. {question[1]}          b. {question[2]}")
  print(f"c. {question[3]}          d. {question[4]}")

  #user reply

  reply = int(input("Enter your answer (1-4): "))
  if(reply == question[-1]):
   print(f"Correct answer,you have won Rs.{levels[i]}")
   if(i==4):
    money = 10000
   elif(i==9):
     money = 32000
   elif(i == 14):
    money == 100000000
   else:
    money = levels[i]
  else:
   print("Wrong Answer!")
   break

print(f"Your take home money is Rs.{money}")