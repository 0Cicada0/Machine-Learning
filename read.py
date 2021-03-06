import csv
import tflearn
from tflearn.data_utils import load_csv
class writeML:
    def __init__(self, age, sex, name, colour):
        self.name = "swolo"
        self.colour = "swolo"
        self.wantName = "swolo"
        self.want = "swolo"
        self.go_On = "swolo"
        self.colours = ["Purple", "Red", "Blue", "White", "Black", "Grey", "Yellow", "Green", "Brown", "Pink", "Orange"]
        self.male = ["Male", "Boy", "Man", "male", "boy", "man"]
        self.female = ["Female", "Girl", "Woman", "female", "girl", "woman"]
        self.predict = None
        self.age = age
        self.sex = sex
        self.name = name
        self.colour = colour

    def go(self):
        print("Welcome!")
        self.choose()

    def choose(self):
        want = input("Hey, would you like to predict or write something?\n").split()
        # if "read" in want:
        #     read()
        if "write" in want:
            self.write()
        elif "Write" in want:
            self.write()
        elif "Predict" in want:
            self.predicting()
        elif "predict" in want:
            self.predicting()
        # elif "Read" in want:
        #     read()
        elif "No" in want:
            print("Goodbye")
        elif "no" in want:
            print("Goodbye")
        else:
            print("Error, unable to understand your meaning. Please try again")
            self.choose()
    def write(self):
        # name = input("What's your name? \n")
        self.name.capitalize()
        # print("Hello " + self.name + "!")
        # sex = input("What's your gender?\n")
        self.sex.capitalize()
        if self.sex in self.female:
            self.sex = "1"
        elif self.sex in self.male:
            self.sex = "0"
        else:
            self.sex = "2"
        # age = input("How old are you?\n")
        # if age != int:
        #     print("Just your age please.")
        #     age = input("How old are you?\n")
        #     if age != int:
        #         print("You Failed.")
        #         return
        # colour = input("What's your favourite colour, %s? \n" %name)
        self.colour.capitalize()
        if self.colour not in self.colours:
            # print("Sorry, that colour is not in my database, try to be simpler")
            colour = input("What's your favourite colour, %s? \n" % self.name)
            if colour not in self.colours:
                # print("You Failed.")
                return
        if self.colour in self.colours:
            colourNum = str((self.colours.index(self.colour)))
        # print("Nice choice!")
        # str(self.age)
        # str(colourNum)
        # str(self.sex)
        # str(self.name)
        f = open('Colour.csv', 'a', newline='')
        f.write("\n" + self.name + ", " + self.sex + ", " + str(self.age) + ", " + colourNum)
        f.close()
        # self.end()

    # def read():
    #     wantName = input("Who's favorite colour would you like to know?\n")
    #     wantName.capitalize()
    #     if wantName.endswith('\'s'):
    #         wantName = wantName[:-2]
    #     elif wantName.endswith('s\''):
    #         wantName = wantName[:-2]
    #     elif wantName.endswith('s'):
    #         wantName = wantName[:-1]
    #     reader = csv.reader(Colour.csv, delimiter=',')
    #     for f in reader:
    #         for i in f:
    #             print(i)
    #             for c in colours:
    #                 if c.index(colour) == i:
    #                     i = c
    #                     print(i)
    #         # for line in f:
    #         #     if wantName in line:
    #         #         print(line)
    #     end()

    def end(self):
        want = input("Hey, would you like to predict or write something?\n").split()
        # if "read" in want:
        #     read()
        if "write" in want:
            self.write()
        elif "Write" in want:
            self.write()
        # elif "Read" in want:
        #     read()
        elif "yes" in want:
            self.choose()
        elif "Yes" in want:
            self.choose()
        elif "No" in want:
            print("Goodbye")
        elif "no" in want:
            print("Goodbye")
        elif "Predict" in want:
            self.predicting()
        elif "predict" in want:
            self.predicting()
        else:
            print("Error, unable to understand your meaning. Please try again")
            self.end()

    def predicting(self):
        data, labels = load_csv("Colour.csv", target_column=1, categorical_labels=True, n_classes=2, columns_to_ignore=[0])
        # name = input("What's your name? \n")
        self.name.capitalize()
        # colour = input("What's your favourite colour, %s? \n" % name)
        self.colour.capitalize()
        if self.colour not in self.colours:
            # print("Sorry, that colour is not in my database, try to be simpler")
            colour = input("What's your favourite colour, %s? \n" % self.name)
            colour.capitalize()
            if colour not in self.colours:
                # print("You Failed.")
                return
        if self.colour in self.colours:
            colourNum = str((self.colours.index(self.colour)))
        # age = input("How old are you?\n")

        net = tflearn.input_data(shape=[None, 2])  # An input layer, with variable input size of examples with 6 features (the [None, 6])
        net = tflearn.fully_connected(net, 32)  # Two hidden layers with 32 nodes
        net = tflearn.fully_connected(net, 32)  # net tells the computer to add it to the line above
        net = tflearn.fully_connected(net, 2, activation='softmax')  # An output later of 2 nodes, and a "softmax" activation (more on activations later)
        net = tflearn.regression(net)  # find the pattern

        model = tflearn.DNN(net)
        model.fit(data, labels, n_epoch=100, batch_size=16, show_metric=True)

        predict = model.predict([[self.age, colourNum]])[0][0]
        # print(predict)
        predict = round(predict, 0)
        if predict == 1:
            self.predict = "Male"

        else:
            self.predict = "Female"
