'''
Created by : Ketan Wangade
Date : 12 March 2022
Purpose : Hash code compition file
'''

# Here we are reading all file data 
def read_hashcode_input_file():
    f = open("a_an_example.in.txt","r")
    lines = f.readlines()

    for line in lines:
        print(line)

def main():
    read_hashcode_input_file()

if __name__ == "__main__":
    main()