import csv
import tflearn
from tflearn.data_utils import load_csv
name = "swolo"
colour = "swolo"
wantName = "swolo"
want = "swolo"
go_On = "swolo"
colours = ["Purple", "Red", "Blue", "White", "Black", "Grey", "Yellow", "Green", "Brown", "Pink", "Orange"]
male = ["Male", "Boy", "Man", "male", "boy", "man"]
female = ["Female", "Girl", "Woman", "female", "girl", "woman"]
def choose():
    want = input("Hey, would you like to read or write something?\n").split()
    if "read" in want:
        read()
    elif "write" in want:
        write()
    elif "Write" in want:
        write()
    elif "Predict" in want:
        predicting()
    elif "predict" in want:
        predicting()
    elif "Read" in want:
        read()
    elif "No" in want:
        print("Goodbye")
    elif "no" in want:
        print("Goodbye")
    else:
        print("Error, unable to understand your meaning. Please try again")
        choose()
def write():
    name = input("What's your name? \n")
    name.capitalize()
    print("Hello " + name + "!")
    sex = input("What's your gender?\n")
    sex.capitalize()
    if sex in female:
        sex = 1
    if sex in male:
        sex = 0
    else:
        sex = 2
    age = input("How old are you?\n")
    # if age != int:
    #     print("Just your age please.")
    #     age = input("How old are you?\n")
    #     if age != int:
    #         print("You Failed.")
    #         return
    colour = input("What's your favourite colour, %s? \n" %name)
    colour.capitalize()
    if colour not in colours:
        print("Sorry, that colour is not in my database, try to be simpler")
        colour = input("What's your favourite colour, %s? \n" % name)
        if colour not in colours:
            print("You Failed.")
            return
    if colour in colours:
        colourNum = str((colours.index(colour)))
    print("Nice choice!")
    f = open('Colour.csv', 'a', newline='')
    f.write("\n" + name + ", " + sex + ", " + age + ", " + colourNum)
    f.close()
    end()

def read():
    wantName = input("Who's favorite colour would you like to know?\n")
    wantName.capitalize()
    if wantName.endswith('\'s'):
        wantName = wantName[:-2]
    elif wantName.endswith('s\''):
        wantName = wantName[:-2]
    elif wantName.endswith('s'):
        wantName = wantName[:-1]
    with open("Colour.csv") as f:
        for i in f:
            if i[3]:
                for c in colours:
                    if c.index(colour) == i:
                        i = c
                        print(i)
        for line in f:
            if wantName in line:
                print(line)
    end()

def end():
    want = input("Hey, would you like to read or write something?\n").split()
    if "read" in want:
        read()
    elif "write" in want:
        write()
    elif "Write" in want:
        write()
    elif "Read" in want:
        read()
    elif "yes" in want:
        choose()
    elif "Yes" in want:
        choose()
    elif "No" in want:
        print("Goodbye")
    elif "no" in want:
        print("Goodbye")
    elif "Predict" in want:
        predicting()
    elif "predict" in want:
        predicting()
    else:
        print("Error, unable to understand your meaning. Please try again")
        end()

def predicting():
    data, labels = load_csv("Colour.csv", target_column=1, categorical_labels=True, n_classes=2, columns_to_ignore=[0])
    name = input("What's your name? \n")
    name.capitalize()
    colour = input("What's your favourite colour, %s? \n" % name)
    colour.capitalize()
    if colour not in colours:
        print("Sorry, that colour is not in my database, try to be simpler")
        colour = input("What's your favourite colour, %s? \n" % name)
        colour.capitalize()
        if colour not in colours:
            print("You Failed.")
            return
    if colour in colours:
        colourNum = str((colours.index(colour)))
    age = input("How old are you?\n")

    net = tflearn.input_data(shape=[None, 2])  # An input layer, with variable input size of examples with 6 features (the [None, 6])
    net = tflearn.fully_connected(net, 32)  # Two hidden layers with 32 nodes
    net = tflearn.fully_connected(net, 32)  # net tells the computer to add it to the line above
    net = tflearn.fully_connected(net, 2, activation='softmax')  # An output later of 2 nodes, and a "softmax" activation (more on activations later)
    net = tflearn.regression(net)  # find the pattern

    model = tflearn.DNN(net)
    model.fit(data, labels, n_epoch=100, batch_size=16, show_metric=True)

    predict = model.predict([[age, colourNum]])[0][0]
    predict = round(predict, 0)
    if predict == 1:
        print("You are a Male.")
    else:
        print("You are a Female.")
# print("Welcome!")
# choose()
predicting()
