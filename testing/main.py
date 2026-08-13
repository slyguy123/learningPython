def main():
    list = ["book", "pen", "notebook"]
    #print(list)
    for item in list:
        if item == "pen":
            item = 10
    #    print(item)

    list2 = [1, 2, 3, 4, 5]
    #print(list2)
    #for key, value in enumerate(list2):
        #if value == 3:
        #    list2[key] = 10
    
    fullList = list(zip(list, list2))
    print(fullList)

def plus(a, b):
    return a + b

if __name__ == "__main__":
    main()



