import globals
from upgrades import Upgrade

class Shop:
    def __init__(self):
        self.setup_upgrades()

    def setup_upgrades(self):
        globals.entities.append(Upgrade(1, 10, 0, 100, "Plastic Stools", "+10 profit"))
        globals.entities.append(Upgrade(2, 0, 0.02, 500, "Old Sign", "+2% Tip Chance"))

        globals.entities.append(Upgrade(3, 0, 0.05, 1500, "Radio", "+5% Tip Chance"))
        globals.entities.append(Upgrade(4, 15, 0, 1700, "Tables", "+15 profit"))

        globals.entities.append(Upgrade(5, 0, 0.07, 1500, "Chalk Board", "+7% Tip Chance"))
        globals.entities.append(Upgrade(6, 17, 0, 20000, "Cushions", "+17 profit"))

        globals.entities.append(Upgrade(7, 0, 0.1, 1500, "Upgrade Sign", "+10% Tip Chance"))
        globals.entities.append(Upgrade(8, 20, 0, 40000, "Wooden Stools", "+20 profit"))

        globals.entities.append(Upgrade(9, 0, 0.15, 2000, "Table Cloth", "+15% Tip Chance"))
        globals.entities.append(Upgrade(10, 30, 0, 60000, "Extra Stove", "+30 profit"))

