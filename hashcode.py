'''
Created by : Ketan Wangade
Date : 12 March 2022
Purpose : Hash code compition file
'''

class HashCode:

# Here we are reading all file data 
    def read_hashcode_input_file(self):
        f = open("a_an_example.in.txt","r")
        lines = f.readlines()

        for line in lines:
            print(line)

x = HashCode()
x.read_hashcode_input_file()