import os
import random
import json
import shutil

script = os.getcwd()+ "\\output\\scripts"
sound = os.getcwd()+ "\\output\\sound\\vo"
yoursound = os.getcwd()+ "\\sounds"
config = os.getcwd()+ "\\config"

sounds = []
lists = []
exports = []

def main():
    print("TF2 Sound Randomizer")
    print("------------------------------------")

    while True:
        print("Choose operation:")
        print("1 - Randomize")
        print("2 - Randomize With Your Sounds")
        print("3 - Reset Scripts")
        print("4 - Exit\n")

        choice = input("Enter choice: ")
        if choice == '4':
            break
        if choice == '1':
            print("Randomizing")
            setupRandomize()
            randomize()
            break
        if choice == '2':
            print("Randomizing")
            setupRandomize2()
            randomize()
            break
        if choice == '3':
            print("Resetting")
            resetScripts()
            break

def resetScripts():
    for path, subdirs, files in os.walk(os.getcwd() + "\\scripts"):
        for file_name in files:
            print(file_name)
            os.makedirs(script, exist_ok=True)
            shutil.copy(path + "\\" + file_name, script + "\\" + file_name)
    print("Reset script files!")
    main()

def setupRandomize2():
    with open(config + "\\exports.json", 'r') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            if(value == True):
                exports.append(key + ".txt")

    for path, subdirs, files in os.walk(yoursound):
        for file_name in files:
            print(file_name)
            source = sound + path.split("\\sounds")[1]
            os.makedirs(source, exist_ok=True)
            source = source + "\\" + file_name
            with open(source, 'w') as new_file:
                pass
            shutil.copy(path + "\\" + file_name, source)
            sounds.append(")vo\\" + source.split("sound\\vo\\")[1])



def setupRandomize():
    with open(config + "\\config.json", 'r') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            if(value == True):
                lists.append(key + ".txt")
    with open(config + "\\exports.json", 'r') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            if(value == True):
                exports.append(key + ".txt")

    for path, subdirs, files in os.walk(config):
        for file_name in files:
            if file_name in lists:
                print(file_name)
                with open(config+ "\\"+file_name, 'r') as file:
                    for line in file.readlines():
                        if "custom" in file_name:
                            sounds.append(")vo\\"+line.replace("\n", ""))
                        else:
                            sounds.append(line.replace("\n", ""))

def randomize():
    for path, subdirs, files in os.walk(script):
        for file_name in files:
            source = path + "\\" + file_name
            destination = path + "\\" + file_name
            if(file_name in exports):
                with open(path+ "\\"+file_name, 'r') as file:
                    txt = ""    
                    count = 0
                    for line in file.readlines():
                        if '"wave"' in line:
                            rand = random.randint(0, len(sounds) -1)
                            line = '	"wave"		"' + sounds[rand] +'"\n'
                            print(sounds[rand])
                            
                        if(count == 0):
                            txt = line
                        else:
                            txt = txt + line
                        count += 1
                #print(txt)
                with open(path+ "\\"+file_name, 'w') as file:
                    file.write(txt)
    print("FINISHED RANDOMIZING!")


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
    os._exit(0)
                