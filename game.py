class Room:
    def __init__(self, name, description, item=None, required_item=None):
        self.name = name
        self.description = description
        self.item = item  # Item present in the room
        self.required_item = required_item  # Item required to enter the room
        self.paths = {}

    def add_path(self, room, direction):
        self.paths[direction] = room

class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms["Home Town"]
        self.inventory = []  # Player's inventory

    def create_rooms(self):
        rooms = {
            "Home Town": Room("Home Town", "You are in your home town, bustling with traders and travelers. The air is filled with the scent of exotic spices."),
            "Forest": Room("Forest", "The forest is dense and mysterious. Sounds of unknown creatures echo through the towering trees.", required_item="honey"),
            "Tower": Room("Tower", "The mage's tower looms high, its top lost in the clouds. Ancient runes glow faintly on the door."),
            "Desert": Room("Desert", "Endless dunes stretch to the horizon, the heat a constant wave. Mirage or not, you think you see a structure in the distance.", item="torch"),
            "Clearing": Room("Clearing", "A serene clearing, bathed in a warm, golden light. The dragon egg rests in the center, almost humming with energy."),
            "Beekeeper's Hut": Room("Beekeeper's Hut", "The small hut is surrounded by buzzing hives. The air smells sweet with honey.", item="honey"),
            "Ancient Ruins": Room("Ancient Ruins", "Crumbled stone structures are all that remain of a once-great civilization. There's an aura of mystery.", item="rope"),
            "Mountain Pass": Room("Mountain Pass", "A narrow path winds through towering peaks. The wind howls, and each step feels like a leap of faith.", required_item="rope"),
            "Cave Entrance": Room("Cave Entrance", "The mouth of a cave opens before you, darkness stretching beyond. A faint, eerie glow emanates from within.", required_item="torch"),
        }

        # Defining paths between rooms
        rooms["Home Town"].add_path(rooms["Forest"], "forest")
        rooms["Home Town"].add_path(rooms["Desert"], "desert")
        rooms["Home Town"].add_path(rooms["Beekeeper's Hut"], "beekeeper's hut")
        rooms["Forest"].add_path(rooms["Home Town"], "home")
        rooms["Forest"].add_path(rooms["Tower"], "tower")
        rooms["Tower"].add_path(rooms["Forest"], "forest")
        rooms["Desert"].add_path(rooms["Home Town"], "home")
        rooms["Desert"].add_path(rooms["Ancient Ruins"], "ancient ruins")
        rooms["Beekeeper's Hut"].add_path(rooms["Home Town"], "home")
        rooms["Beekeeper's Hut"].add_path(rooms["Forest"], "forest")
        rooms["Ancient Ruins"].add_path(rooms["Desert"], "desert")
        rooms["Ancient Ruins"].add_path(rooms["Mountain Pass"], "mountain pass")
        rooms["Mountain Pass"].add_path(rooms["Ancient Ruins"], "ancient ruins")
        rooms["Mountain Pass"].add_path(rooms["Cave Entrance"], "cave entrance")
        rooms["Cave Entrance"].add_path(rooms["Mountain Pass"], "mountain pass")
        rooms["Cave Entrance"].add_path(rooms["Clearing"], "clearing")

        return rooms

    def play(self):
        while True:
            print("\n" + self.current_room.description)

            if self.current_room.item:
                print(f"You find {self.current_room.item} here.")
                self.inventory.append(self.current_room.item)
                print(f"{self.current_room.item} has been added to your inventory.")
                # Remove the item from the room once picked up
                self.current_room.item = None

            if self.current_room.name == "Clearing":
                print("\nYour quest has been successful! You've found the dragon egg.")
                break

            print("\nThere are paths leading to: " + ", ".join(self.current_room.paths.keys()))
            print("Inventory:", ", ".join(self.inventory))
            choice = input("\nWhere do you want to go? ").strip().lower()

            if choice in self.current_room.paths:
                next_room = self.current_room.paths[choice]
                if next_room.required_item and next_room.required_item not in self.inventory:
                    print(f"You need {next_room.required_item} to proceed.")
                else:
                    self.current_room = next_room
            else:
                print("You can't go that way!")

if __name__ == "__main__":
    game = Game()
    game.play()
