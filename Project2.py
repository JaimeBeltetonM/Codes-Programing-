print("Hello, world! This is Python 3!")
R = int(input("What do you think the rate of formation of stars suitable for the development of intelligent life is?"))
Fp = int(input("What is the number of stars that have a planetry system?"))
Ne = int(input("What is the number of planets per solar system that have an enviroment suitable for life?"))
FL = int(input("What is the fraction of suitable planets on which life actually appears?"))
Fi = int(input("What do you think the fraction of life bearing planets on which intelligent life emerges is?"))
Fc = int(input("What is the fraction of civilization that develops a technology that produces detectable signs of their existence"))
L = int(input("How many years did it take the civilization to produce their sign of life?"))
freshman = R * Fp * Ne * FL * Fi * Fc 
N = freshman * L
print("The number of civilizations in the Milky Way galaxy whose electromagnetic emissions are detectable is...")
print(N)