import subprocess
from time import sleep

def station():
    subprocess.run(["catimg","-H", "50", "./images/station.png"]) 
    print("Here we have the base station, it orchestrates all of the other devices on the farm!\nIt is powered by a solar panel and it features a large antenna to send commands and recieve data from all the other devices! [4]")
    
def drone():
    subprocess.run(["catimg","-H", "50", "./images/drone.png"])
    print("This little drone flies around the farm, taking thousands of high quality pictures each day.\nIt brings these pictures back to the base station to perform analysis, and it sleeps in a little solar powered drone port [5].")

def jackal():
    subprocess.run(["catimg","-H", "50", "./images/jackal.png"])
    print("This is a ground rover, a small wheeled robot that goes around collecting data and charging underground sensors [6].\nHe has a very large battery that allows it to charge up several sensors wirelessly, allowing underground sensors to stay in the ground for months at a time [1].")

def underground():
    subprocess.run(["catimg","-H", "50", "./images/underground.png"])
    print("Here we have an underground sensor, it gathers data on soil moisture, temperature, root density, and many other things [1]!\nLarge arrays of these sensors provide the majority of data hat the farm will use [1].")

def biosensor():
    subprocess.run(["catimg","-H", "40", "./images/biosensor.png"])
    print("This is a biosensor, a genetically modified organism that produces some useful output [2]. Most biosensors work by glowing when they're exposed to something (such as a bacteria or virus) [3].\nThis glow is then read by a digital sensor, and reported to the base station [3].")

def sources():
    print("\nSOURCES:\n")
    print("1. Bogena, H. R., Weuthen, A., & Huisman, J. A. (2022).\n\tRecent Developments in Wireless Soil Moisture Sensing to Support Scientific Research and Agricultural Management.\n\tSensors, 22(24), 9792. https://doi.org/10.3390/s22249792")
    print("2. Brooks, R. (2025, December 8).\n\tLiving Sensors Turn Soybeans into Fungal Disease Detectives. AgWeb.\n\thttps://www.agweb.com/news/crops/soybeans/living-sensors-turn-soybeans-fungal-disease-detectives")
    print("3. Elli, G., Hamed, S., Petrelli, M., Ibba, P., Ciocca, M., Lugli, P., & Petti, L. (2022).\n\tField-Effect Transistor-Based Biosensors for Environmental and Agricultural Monitoring. (2022).\n\tSensors, 22(11), 4178. doi:10.3390/s22114178")    
    print("4. Pagano, A., Croce, D., Tinnirello, I., & Vitale, G. (2023).\n\tA Survey on LoRa for Smart Agriculture: Current Trends and Future Perspectives.\n\tIEEE Internet of Things Journal, 10(4), 3664-3679.")
    print("5. Wei, Z., Jia, J., Niu, Y., Wang, L., Wu, H., Yang, H., & Feng, Z. (2025).\n\tIntegrated Sensing and Communication Channel Modeling: A Survey.\n\tIEEE Internet of Things Journal, 12(12), 18850–18864. doi:10.1109/JIOT.2024.3449377B")
    print("6. Xu, Y., Wang, L., Gao, Q., Zhao, W., Zhang, H., Lin, F., … He, J. (2026).\n\tEdge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things:\n\tA Lyapunov-Based Learning Approach.\n\tIEEE Internet of Things Journal, 13(3), 3726–3742. doi:10.1109/JIOT.2025.3631071")
    print()
    sleep(3)
    print("\nImages:\n")
    print("Adobe Stock. Farm Cartoon Image. Adobe Stock.\n\thttps://t4.ftcdn.net/jpg/01/08/29/11/360_F_108291157_ZZgrI4K5nJ0VcVXZuoXQZ40CInCxTvKs.jpg")
    print("Clearpath Robotics. Jackal UGV. Clearpath Robotics.\n\thttps://s3.amazonaws.com/assets.clearpathrobotics.com/wp-content/uploads/2024/02/10152751/Jackal-Manipulation.74.png")
    print("ModelAI. Starling 2 Max Drone. ModelAI.\n\thttps://www.modalai.com/cdn/shop/files/modalai-inc-drone-starling-2-max-outdoor-gps-denied-development-drone-1125059458_1200x1200.png?v=1738708179")
    print("NVidia. NVidia Jetson TX1 Image. NVidia.\n\thttps://developer-blogs.nvidia.com/wp-content/uploads/2015/11/JTX1_devkit.png")
    print("PNGTree. Car Battery Transparant Image. PNGTree.\n\thttps://png.pngtree.com/png-vector/20251010/ourmid/pngtree-automotive-car-battery-power-source-energy-storage-for-vehicles-png-image_17680109.webp")
    print("VecTeezy. Human Cells PNG. VecTeezy.\n\thttps://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLWj3thf4kmZMB8E-1XXw8-k4ky_rKHFjDUg&s")
    print()

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
                biosensor()
                l[3] = 1
            case "5":
                underground()
                l[4] = 1
            case _:
                print("Error: Incorrect choice!")
                continue 
        input("Ready to go back?\n")
        if 0 not in l:
            print("You've explored the whole farm!!!\nHopefully you've learned something new today!\n")
            break

    sources()
    sleep(1)
    print("Goodbye!")