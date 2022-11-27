
def main():
    csvRead()

def csvRead():    
    with open("csv-file.txt") as f:
        for line in f:
            # row = line.strip().split(",") # The file has 3 variables - method 1
            food, taste, color = line.strip().split(",") # If it has 3 vars, why not just call it directly?
            #print(f"{food} tastes{taste} and looks{color}.", sep="") # Remove all trailing space in the line. It adds spaces first somehow.
            
def csvReadDict():
    basket = []
    with open ("csv-file.txt") as f:
        for line in f:
            food, taste, color = line.strip().split(",")
            cart = {"Food": food, "Taste" : taste, "Color" : color}
            basket.append(cart)
            
    for cart in sorted(basket, key=lambda x: x["Food"], reverse=True): # When modifying dicts, sorted() needs a comparator. Lists doesn't need a comparator to work
        # When using lambdas, it will return the value of key or results into the function based on is input there. In this case "Food" is used as an input to be returned.
        print(f"{cart['Food']} tastes{cart['Taste']} and looks{cart['Color']}.") # why the fuck did i add a colon - ex: {cart:['Food']}
#main()
csvReadDict()