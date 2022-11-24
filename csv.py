
def main():
    csvRead()

def csvRead():    
    with open("csv-file.txt") as f:
        for line in f:
            # row = line.strip().split(",") # The file has 3 variables - method 1
            food, taste, color = line.strip().split(",") # If it has 3 vars, why not just call it directly?
            print(f"{food} tastes{taste} and looks{color}.", sep="") # Remove all trailing space in the line. It adds spaces first somehow.
            
main()