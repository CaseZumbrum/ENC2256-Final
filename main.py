import subprocess

def station():
    subprocess.run(["catimg","-H", "50", "./images/station.png"]) 
    print("Here we have the base station, it orchestrates all of the other devices on the farm!\nIt is powered by a solar panel and it features a large antenna to send commands and recieve data from all the other devices!")
    
def drone():
    subprocess.run(["catimg","-H", "50", "./images/drone.png"])
    print("This little drone flies around the farm, taking thousands of high quality pictures each day.\nIt brings these pictures back to the base station to perform analysis, and it sleeps in a little solar powered drone port.")

def jackal():
    subprocess.run(["catimg","-H", "50", "./images/jackal.png"])
    print("This is a ground rover, a small wheeled robot that goes around collecting data and charging underground sensors.\nHe has a very large battery that allows it to charge up several sensors wirelessly, allowing underground sensors to stay in the ground for months at a time.")

def underground():
    subprocess.run(["catimg","-H", "50", "./images/underground.png"])
    print("Here we have an underground sensor, it gathers data on soil moisture, temperature, root density, and many other things!\nLarge arrays of these sensors provide the majority of data hat the farm will use.")

def biosensor():
    subprocess.run(["catimg","-H", "40", "./images/biosensor.png"])
    print("This is a biosensor, a genetically modified organism that produces some useful output. Most biosensors work by glowing when they're exposed to something (such as a bacteria or virus).\nThis glow is then read by a digital sensor, and reported to the base station.")


if __name__ == "__main__":
    l = [0]*5
    print("Welcome to the Smart Farm!\nThrough this game you will explore various aspects of a modern smart farm!")
    input("Are you ready?\n")
    while True:
        subprocess.run(["catimg","-H", "70", "./images/farm.png"]) 
        choice = input("Where do you want to go? [1-5] (0 to quit): ")
        match choice:
            case "0":
                break
            case "1": 
                station()
                l[0] = 1
            case "2":
                drone()
                l[1] = 1
            case "3":
                jackal()
                l[2] = 1
            case "4":
                underground()
                l[3] = 1
            case "5":
                biosensor()
                l[4] = 1
            case _:
                print("Error: Incorrect choice!")
                continue 
        input("Ready to go back?\n")
        if 0 not in l:
            print("You've explored the whole farm!!!\nHopefully you've learned something new today!\n")
            break

    print("Goodbye!")