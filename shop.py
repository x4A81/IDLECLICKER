import globals
from upgrades import Upgrade

def setup_upgrades():
    globals.entities.append(Upgrade(1, 10, 0, 400, "Plastic Stools", "Increase profit by 10"))
    globals.entities.append(Upgrade(2, 0, 0.02, 1000, "Old Sign", "Increase tip chance by 2%"))

    globals.entities.append(Upgrade(3, 0, 0.05, 1500, "Radio", "Increase tip chance by 5%"))
    globals.entities.append(Upgrade(4, 15, 0, 1700, "Tables", "Increase profit by 15"))

    globals.entities.append(Upgrade(5, 0, 0.07, 1500, "Chalkboard Sign", "Increase tip chance by 7%"))
    globals.entities.append(Upgrade(6, 17, 0, 20000, "Cushions", "Increase profit by 17"))

    globals.entities.append(Upgrade(7, 0, 0.1, 1500, "Chalkboard Sign", "Increase tip chance by 10%"))
    globals.entities.append(Upgrade(8, 20, 0, 40000, "Wooden Stools", "Increase profit by 20"))

    globals.entities.append(Upgrade(7, 0, 0.15, 2000, "Table Cloth", "Increase tip chance by 15%"))
    globals.entities.append(Upgrade(8, 30, 0, 60000, "Extra Stove", "Increase profit by 30"))

