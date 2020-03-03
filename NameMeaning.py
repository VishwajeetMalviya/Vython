def MeaningOfName(char):
    if char == 'a' or char == 'A':
        return 'Awesome'
    if char == 'b' or char == 'B':
        return 'Beautiful'
    if char == 'c' or char == 'C':
        return 'Cute'
    if char == 'd' or char == 'D':
        return 'Dashing'
    if char == 'e' or char == 'E':
        return 'Energetic'
    if char == 'f' or char == 'F':
        return 'Fabulous'
    if char == 'g' or char == 'G':
        return 'Genius'
    if char == 'h' or char == 'H':
        return 'Honest'
    if char == 'i' or char == 'I':
        return 'Innovative'
    if char == 'j' or char == 'J':
        return 'Joyful'
    if char == 'k' or char == 'K':
        return 'Kind'
    if char == 'l' or char == 'L':
        return 'Legend'
    if char == 'm' or char == 'M':
        return 'Motivating'
    if char == 'n' or char == 'N':
        return 'Nice'
    if char == 'o' or char == 'O':
        return 'OutStanding'
    if char == 'p' or char == 'P':
        return 'Positive'
    if char == 'q' or char == 'Q':
        return 'Quiet'
    if char == 'r' or char == 'R':
        return 'Respected'
    if char == 's' or char == 'S':
        return 'Skilled'
    if char == 't' or char == 'T':
        return 'Truthful'
    if char == 'u' or char == 'U':
        return 'Upstanding'
    if char == 'v' or char == 'V':
        return 'Valuable'
    if char == 'w' or char == 'W':
        return 'Wonderful'
    if char == 'x' or char == 'X':
        return 'Xoxo'
    if char == 'y' or char == 'Y':
        return 'Yummy'
    if char == 'z' or char == 'Z':
        return 'Zealous'
  
if __name__ == "__main__":
    print("Meaning of your name.")
    string1 = input("Enter Your Name : ")
    leng = len(string1)
    for i1 in range(0,leng):
        print(string1[i1] + ' = ' + MeaningOfName(string1[i1]))
    

