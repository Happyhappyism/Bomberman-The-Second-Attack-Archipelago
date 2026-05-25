### Used to generate Poptracker json files
import json
from .Regions import region_data_table
from .Locations import location_data_table
from .Items import item_data_table
import logging
logger = logging.getLogger("Tracker")

class trackerstate:
    def has(item, count=1):
        if count > 1:
            return f"{item}:{count}"
        else:
            return item

    def can_reach_location(location):
        region_name = location_data_table[location].region
        return f"@{region_name.replace(","," -")}/{location}"

    def can_reach_region(region):
        return f"@{region.replace(","," -")}"

    def has_all_elements(): # Debug, checks to see if you have all the element stones
        return "$has_all_elements"

    def can_destroy_with_immunity(immunities):
        # stones = ["Fire Stone","Ice Stone","Wind Stone","Earth Stone","Lightning Stone","Dark Stone","Light Stone"]
        
        # for badstone in immunities:
        #     stones.pop(stones.index(badstone))
        # for havestone in stones:
        #     if state.has(havestone, player):
        #         return True
        element_string = ""
        for element in immunities:
            element_string += f"{element}_"

        return f"$can_destroy_with_immunity|{element_string[:-1]}"

    def can_open_car():
        return "$can_open_car"

    def has_all_guardian(): # Debug, checks to see if you have all the guardian armor
        return "$has_all_guardian"

    def can_build_ice():
        return "$can_build_ice"

    def has_multibomb(): # has a bomb that can place more than 1 of itself
        return "$has_multibomb"

    def can_destroy():
        return "$can_destroy"

    def can_kill_chompers():
        return "$can_kill_chompers"

    def can_bomb_jump(): # Depreciated? 
        return "$can_bomb_jump"

    def can_drain_aquanet_fountain():
        return "$can_drain_aquanet_fountain"

    def can_hit_high_object():
        return "$can_hit_high_object"

    def starlight_card_hunt():
        return "$starlight_card_hunt"

    def can_hit_fountain():
        return "$can_hit_fountain"

    def can_build_ladder(cnt=1):
        if cnt > 1:
            return "$can_build_ladder|cnt"
        else:
            return "$can_build_ladder"

    def can_move_bombs(): # Can kick or throw
        return "$can_move_bombs"

    
location_rule_track = {

        # Alcatraz
        "Alcatraz Part Red":
            lambda state: [f"{state.can_reach_region("Alcatraz, Prison Bridge")}"],
        "Alcatraz Part Yellow":
            lambda state: [f"{state.has("Guardian Glove")}"],
        "Alcatraz Generator":
            lambda state: [f"{state.can_hit_high_object()}"],

        # Aquanet
        "Aquanet Part Blue":
            lambda state: [f"{state.can_build_ladder(3)}"],
        "Aquanet Guardian Armor":
            lambda state: [f"{state.has("Earth Stone")}"],
        "Aquanet Remote Fountain Room":
            lambda state: [f"{state.has("Guardian Glove")}"],
        "Aquanet Remote To the Tower":
            lambda state: [f"{state.has("Guardian Glove")}"],
         # Glove
        #"Aquanet Behemos Defeated":
        #    lambda state: [f"{state.has("Guardian Glove")},{state.has("Bomb")}"],
        #"Aquanet Remote To the Tower":
        #    lambda state: [f"{
         # Ice bomb + Fire Bomb
        "Aquanet Part Yellow":
            lambda state: [f"{state.has("Wind Stone")},{state.has("Guardian Glove")}"],
        "Aquanet Generator":
            lambda state: [f"{state.has("Ice Stone")},{state.can_destroy_with_immunity( ["Ice Stone","Dark Stone"])}"],


        # Horizon
        "Horizon Right Blue Jewel":
            lambda state: [f"{state.can_destroy_with_immunity(["Wind Stone"])}",f"{state.can_move_bombs()}"],
        "Horizon Part Blue":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Horizon Remote Second Trial":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Horizon Part Red":
            lambda state: [f"{state.can_build_ladder( 1)}"],

         # Two Blue Gems
        "Horizon Remote Final Deposit":
            lambda state: [f"{state.has("Guardian Glove")}"],
         # Wind Bomb
        "Horizon Right Green Jewel":
            lambda state: [f"{state.has("Wind Stone")}"],
        
        "Horizon Guardian Armor":
            lambda state: [f"{state.has("Lightning Stone")},{state.has("Wind Stone")},{state.has("Guardian Glove")}"],
        "Horizon Part Yellow":
            lambda state: [f"{state.has("Wind Stone")}"],
         # Two Green Gem
        "Horizon Left Green Jewel":
            lambda state: [f"{state.has("Wind Stone")}"],
        "Horizon Right Green Jewel":
            lambda state: [f"{state.has("Guardian Helmet")},{state.has("Wind Stone")}"],
        "Horizon Middle Green Jewel":
            lambda state: [f"{state.has("Wind Stone")},{state.has("Green Gems")}"],
        
        "Horizon Red Jewel":
            lambda state: [f"{state.has("Wind Stone")},{state.has("Green Gems")}"],
         # Red Gem
        "Horizon Generator":
            lambda state: [f"{state.has("Wind Stone")},{state.can_move_bombs()}"],

        # Starlight
        "Starlight Part Red":
            lambda state: [f"{state.can_build_ladder( 3)}"],
        "Starlight Part Blue":
            lambda state: [f"{state.can_move_bombs()},{state.can_reach_region("Starlight, Slots Room")}"],
        "Starlight Remote Casino Lobby":
            lambda state: [f"{state.can_build_ladder( 2)}"],
        "Starlight Remote Waiting Room":
            lambda state: [f"{state.has("Wind Stone")},{state.can_hit_high_object()}"],
        "Starlight Generator":
            lambda state: [f"{state.has("Lightning Stone")},{state.can_build_ice()},{state.can_move_bombs()}"],
        "Starlight Zhael Defeated":
            lambda state: [f"{state.can_destroy_with_immunity( ["Dark Stone"])}"],
        "Starlight Part Yellow":
            lambda state: [f"{state.can_reach_location("Starlight Zhael Defeated")}"],
        "Starlight King Of Clubs":
            lambda state: [f"{state.starlight_card_hunt()}"],
        "Starlight Knight Of Diamonds":
            lambda state: [f"{state.starlight_card_hunt()}"],
        "Starlight Ace Of Spades":
            lambda state: [f"{state.starlight_card_hunt()}"],
        "Starlight Queen Of Hearts":
            lambda state: [f"{state.starlight_card_hunt()}"],

        # Neverland
        "Neverland Part Red":
            lambda state: [f"{state.has("Wind Stone")}",f"{state.can_build_ladder( 2)}"],
        "Neverland Remote Bonus Room":
            lambda state: [f"{state.has("Wind Stone")}",f"{state.can_build_ladder( 3)}"],
        "Neverland Part Blue":
            lambda state: [f"{state.can_build_ladder( 3)}"],
        "Neverland Molok Defeated":
            lambda state: [f"{state.can_destroy_with_immunity( ["Dark Stone"])}"],
        #"Neverland Guardian Armor":
        #    lambda state: [f"{state.has("Dark Stone")},{((state.has("Ice Stone")},{state.can_move_bombs() )or state.has("Wind Stone"))}"],
        "Neverland Generator":
            lambda state: [f"{state.has("Earth Stone")},{state.can_build_ice()},{state.has("Guardian Boots")},{state.has("Wind Stone")}"],
        
        # Epikyur
        "Epikyur Haunted House Pass":
            lambda state: [f"{state.has("Guardian Glove")}"],
        "Epikyur Coaster Battery":
            lambda state: [f"{state.has("Haunted House Pass")}"],
        "Epikyur Zoniha Defeated":
            lambda state: [f"{state.can_destroy_with_immunity( ["Dark Stone"])}"],
        "Epikyur Glove Center Fountain":
            lambda state: [f"{state.can_build_ice()}"],
        "Epikyur Part Green":
            lambda state: [f"{state.has("Wind Stone")}"],
        "Epikyur Part Yellow":
            lambda state: [f"{state.can_build_ladder( 2)}"],
        "Epikyur Museum Pass":
            lambda state: [f"{state.has("Lightning Stone")}"],
        "Epikyur Generator":
            lambda state: [f"{state.has("Lightning Stone")},{state.has("Wind Stone")},{state.has("BombUp", 2)},{state.has("Guardian Boots")},{state.has("Guardian Glove")}",f"{state.has("Lightning Stone")},{state.has("Wind Stone")},{state.has("BombUp", 2)},{state.has("Guardian Boots")}{state.has("Light Stone")}"],
            
        # Thantos
        "Thantos Part Yellow": 
            lambda state: [f"{state.has("Earth Stone")}"],
        "Thantos Generator":
            lambda state: [f"{state.can_build_ice()},{state.has("Dark Stone")},{state.has("Wind Stone")},{state.has("Earth Stone")}"],
        "Thantos Lower Train Battery":
            lambda state: [f"{state.can_open_car()}"],
        "Thantos Upper Train Battery":
            lambda state: [f"{state.can_open_car()},{state.has("Lightning Stone")}",f"{state.has("Earth Stone")}"] ,
        "Thantos Part Red":
            lambda state: [f"{state.can_open_car()},{state.has("Light Stone")}"],
        "Thantos Part Blue":
            lambda state: [f"{state.can_destroy_with_immunity( ["Dark Stone"])}"],
        "Thantos Remote Crevice":
            lambda state: [f"{state.has("Wind Stone")}"],
        "Thantos Part Green":
            lambda state: [f"{state.has("Wind Stone")},{state.has("Earth Stone")}"],
        "Thantos Bulzeeb Defeated":
            lambda state: [f"{state.can_destroy_with_immunity( ["Dark Stone"])}"],

        # Noah'
        "Noah Card Key 1":
            lambda state: [f"{state.has("Guardian Boots")}"],
        "Noah Card Key 2":
            lambda state: [f"{state.has("Lightning Stone")},{state.has("Earth Stone")}"],
        "Noah Card Key 3":
            lambda state: [f"{state.has("Lightning Stone")},{state.has("Earth Stone")}"],

        # Pommy Transforms
        "Pommy Beast Transformation":
            lambda state: [f"{state.has("Pommy Animal Gene")}"],
        "Pommy Penguin Transformation":
            lambda state: [f"{state.has("Pommy Animal Gene")}"],
        "Pommy Dinosaur Transformation":
            lambda state: [f"{state.has("Pommy Beast Gene")}"],
        "Pommy Shadow Transformation":
            lambda state: [f"{state.has("Pommy Beast Gene")}",f"{state.has("Pommy Penguin Gene")}"],
        "Pommy Dragon Transformation":
            lambda state: [f"{state.has("Pommy Beast Gene")}"],
        "Pommy Bird Transformation":
            lambda state: [f"{state.has("Pommy Penguin Gene")}"],
        "Pommy Chicken Transformation":
            lambda state: [f"{state.has("Pommy Penguin Gene")}"],
        
        "Pommy Claw Transformation":
            lambda state: [f"{state.has("Pommy Knuckle Gene")}"],
        "Pommy Hammer Transformation":
            lambda state: [f"{state.has("Pommy Knuckle Gene")}"],
        "Pommy Pixie Transformation":
            lambda state: [f"{state.has("Pommy Claw Gene")}",f"{state.has("Pommy Hammer Gene")}"],
        "Pommy Cat Transformation":
            lambda state: [f"{state.has("Pommy Claw Gene")}"],
        "Pommy Devil Transformation":
            lambda state: [f"{state.has("Pommy Claw Gene")}"],
        "Pommy Knight Transformation":
            lambda state: [f"{state.has("Pommy Hammer Gene")}"],
        "Pommy Mage Transformation":
            lambda state: [f"{state.has("Pommy Hammer Gene")}"],
}

region_rules_track = {
        "Menu -> Alcatraz":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone","Light Stone"])}"],
        "Menu -> Aquanet":
            lambda state: [f"{state.has("Aquanet Coordinates")}"],
        "Menu -> Horizon":
            lambda state: [f"{state.has("Horizon Coordinates")}"],
        "Menu -> Starlight":
            lambda state: [f"{state.has("Starlight Coordinates")}"],
        "Menu -> Neverland":
            lambda state: [f"{state.has("Neverland Coordinates")}"],
        "Menu -> Epikyur":
            lambda state: [f"{state.has("Epikyur Coordinates")}"],
        "Menu -> Thantos":
            lambda state: [f"{state.has("Thantos Coordinates")}"],

        "Noah -> Noah Core":
            lambda state: [f"{state.has_all_elements()}, {state.has_all_guardian()}"],
        "Menu -> Shop":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Shop -> Shop Aquanet":
            lambda state: [f"{state.can_reach_location("Aquanet Generator")}"],
        "Shop -> Shop Horizon":
            lambda state: [f"{state.can_reach_location("Horizon Generator")}"],
        "Shop -> Shop Starlight":
            lambda state: [f"{state.can_reach_location("Starlight Generator")}"],
        "Shop -> Shop Neverland":
            lambda state: [f"{state.can_reach_location("Neverland Generator")}"],
        "Shop -> Shop Epikyur":
            lambda state: [f"{state.can_reach_location("Epikyur Generator")}"],
        "Shop -> Shop Thantos":
            lambda state: [f"{state.can_reach_location("Thantos Generator")}"],
 
 
        # Alcatraz
        "Alcatraz, Prison -> Alcatraz, Secret Room 1":
            lambda state: [f"{state.can_reach_location("Alcatraz Baelfael Defeated")}"],
        "Alcatraz, Sewer Entrance -> Alcatraz, Twisted Sewers":
	        lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Alcatraz, Security Room A -> Alcatraz, Security Room B":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone"])}"],
        "Alcatraz, Security Room B -> Alcatraz, Sewage Disposal":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone"])}"],
        "Alcatraz, Sewage Disposal -> Alcatraz, Secret Room 2":
            lambda state: [f"{state.can_reach_location("Alcatraz Baelfael Defeated")}"],
        "Alcatraz, Twisted Sewers -> Alcatraz, Through the Pipe":
            lambda state: [f"{state.can_reach_location("Alcatraz Baelfael Defeated")}"],
        
        "Alcatraz, Through the Pipe -> Alcatraz, Prison Bridge":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Alcatraz, Pipe Room B -> Alcatraz, Final Defense Unit":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone"])}"],
 
        # Aquanet
        "Aquanet, First Room -> Aquanet, Second Room":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Aquanet, Swimming Pool Spa -> Aquanet, Behind the Moat":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Aquanet, Swimming Pool Spa -> Aquanet, Secret Room 1":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Aquanet, Around the Moat -> Aquanet, Secret Room 2":
            lambda state: [f"{state.has("Earth Stone")}"],
        "Aquanet, Around the Moat -> Aquanet, Secret Room 2":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Aquanet, Elevator Hub -> Aquanet, Hidden Balcony":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Aquanet, Hidden Balcony -> Aquanet, Water Channels":
            lambda state: [f"{state.can_destroy_with_immunity(["Ice Stone"])}"],
        "Aquanet, Water Channels -> Aquanet, Fountain Room":
            lambda state: [f"{state.can_drain_aquanet_fountain()}"],
        "Aquanet, Elevator Hub -> Aquanet, Behemos' Lair":
            lambda state: [f"{state.can_drain_aquanet_fountain()}, {state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Aquanet, Tower 1F -> Aquanet, Tower 2F":
            lambda state: [f"{state.has("Fire Stone")}, {state.has("Ice Stone")}, {state.has("Guardian Glove")}"],
        "Aquanet, Tower 2F -> Aquanet, Tower 3F":
            lambda state: [f"{state.can_build_ice()}, {state.can_destroy_with_immunity(["Ice Stone"])}"],
        "Aquanet, Fountain Room -> Aquanet, Secret Room 3":
            lambda state: [f"{state.can_reach_location("Aquanet Generator")}"],

        # Horizon
        "Horizon, Eastern Tower -> Horizon, First Trial":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone","Wind Stone"])}"],
        "Horizon, Leading Road -> Horizon, Resting Point":
            lambda state: [f"{state.has("Blue Gems")}, {state.can_destroy_with_immunity(["Wind Stone"])}"],
        "Horizon, Floating Temple -> Horizon, Secret Room 1":
            lambda state: [f"{state.has("Wind Stone")}"],
        "Horizon, Last Route -> Horizon, Fourth Trial":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone"])}"],
        "Horizon, Fourth Trial -> Horizon, Secret Room 2":
            lambda state: [f"{state.has("Lightning Stone")}, {state.has("Guardian Helmet")}, {state.has("Guardian Glove")}, {state.has("Wind Stone")}"],
        "Horizon, Final Deposit -> Horizon, Gravity Generator Room":
            lambda state: [f"{state.has("Red Gem")}"],
 
        # Starlight
        "Starlight, Parking Lot -> Starlight, Closed Road":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Starlight, Closed Road -> Starlight, Fountain Square":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Starlight, Closed Road -> Starlight, Hidden Room":
            lambda state: [f"{state.can_reach_location("Starlight Zhael Defeated")}"],
        "Starlight, Fountain Square -> Starlight, Small Inlet":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone", "Wind Stone"])}"],
        "Starlight, Small Inlet -> Starlight, Alleyway":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Starlight, Casino Entrance -> Starlight, Casino Lobby":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone", "Wind Stone"])}"],
        "Starlight, Casino Lobby -> Starlight, Slots Room":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone"])}"],
        "Starlight, Casino Lobby -> Starlight, Betting Room":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Starlight, Waiting Room -> Starlight, Stage Area":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Starlight, Slots Room -> Starlight, Lookout Point":
            lambda state: [f"{state.can_reach_location("Starlight Zhael Defeated")}, {state.can_reach_region("Starlight, Slots Room")}"],
        "Starlight, Fountain Square -> Starlight, Gravity Generator Room":
            lambda state: [f"{state.has("Royal Straight")}"],
 

        # Neverland
        "Neverland, Entry Point -> Neverland, Through the Line of Fire":
            lambda state: [f"{state.can_kill_chompers()}"],
        "Neverland, Intersection -> Neverland, Secret Room 1":
            lambda state: [f"{state.has("Dark Stone")}, {state.has("Ice Stone")}, {state.can_move_bombs()}", f"{state.has("Dark Stone")},{state.has("Wind Stone")}"],
        "Neverland, Intersection -> Neverland, Conveyor Belts":
            lambda state: [f"{state.can_kill_chompers()}"],
        "Neverland, Intersection -> Neverland, Potholes":
            lambda state: [f"{state.can_kill_chompers()}"],
        "Neverland, Potholes -> Neverland, Second Passageway":
            lambda state: [f"{state.can_destroy_with_immunity(["Light Stone","Wind Stone"])}, {state.can_reach_region("Neverland, Conveyor Belts")}"],
        "Neverland, Carrier Works -> Neverland, Switch Room":
            lambda state: [f"{state.has("Skates")}, {state.can_kill_chompers()}", f"{state.can_move_bombs()}, {state.can_kill_chompers()}"],
        "Neverland, Switch Room -> Neverland, Secret Room 2":
            lambda state: [f"{state.has("Ice Stone")}, {state.can_move_bombs()}, {state.can_reach_location("Neverland Molok Defeated")}"],
        "Neverland, Furnace -> Neverland, Safe Point":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Neverland, Bridge Room -> Neverland, Third Passageway":
            lambda state: [f"{state.can_reach_region("Neverland, Cage Room")}"],
 
        # Epikyur
        "Epikyur, Center Fountain -> Epikyur, Tattered Bridge":
            lambda state: [f"{state.has("Ice Stone")}, {state.has("Guardian Glove")}", f"{state.has("Ice Stone")}, {state.has("FireUp", 3)}"],
        "Epikyur, Tattered Bridge -> Epikyur, Haunted House Yard":
            lambda state: [f"{state.has("Earth Stone")}"],
        "Epikyur, Haunted House Yard -> Epikyur, Haunted House Lobby":
            lambda state: [f"{state.has("Guardian Glove")}"],
        "Epikyur, Haunted House Lobby -> Epikyur, Haunted House Spike Traps":
            lambda state: [f"{state.has("Wind Stone")}"],
        "Epikyur, Haunted House Storeroom -> Epikyur, Haunted House Coaster Start":
            lambda state: [f"{state.has("Museum Pass")}"],
        "Epikyur, Haunted House Coaster Start -> Epikyur, Coaster Finish":
            lambda state: [f"{state.has("Coaster Battery")}"],
        "Epikyur, Center Fountain -> Epikyur, Castle of Time First Room":
            lambda state: [f"{state.can_reach_location("Epikyur Zoniha Defeated")}"],
        "Epikyur, Center Fountain -> Epikyur, Misaligned Bridge":
            lambda state: [f"{state.has("Earth Stone")}"],
        "Epikyur, Castle of Time Second Room -> Epikyur, Gravity Generator Room":
            lambda state: [f"{state.has("Fire Stone")}, {state.has("Ice Stone")}, {state.has("Wind Stone")}, {state.has("Lightning Stone")}, {state.has("Earth Stone")}"],
 
        # Thantos
        "Thantos, Hangout -> Thantos, Secret Room 1":
            lambda state: [f"{state.has("Earth Stone")}"],
        "Thantos, Back Alley -> Thantos, Gravity Generator Room":
            lambda state: [f"{state.has("Dark Stone")}"],
        "Thantos, Streets -> Thantos, Wrecked Lot":
            lambda state: [f"{state.has("Earth Stone")}", f"{state.has("Guardian Glove")}"],
        "Thantos, Wrecked Lot -> Thantos, Battle for the Battery":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Thantos, Battle for the Battery -> Thantos, Compactor":
            lambda state: [f"{state.has("Light Stone")}"],
        #"Thantos, Wrecked Lot -> Thantos, Battery Ambush":
        "Thantos, Subway Entrance -> Thantos, Aboard the Subway":
            lambda state: [f"{state.has("Train Batteries")}"],
        "Thantos, Supposed Dead End -> Thantos, The Crevice":
            lambda state: [f"{state.can_destroy_with_immunity(["Dark Stone"])}"],
        "Thantos, The Crevice -> Thantos, Voltage Storage Unit":
            lambda state: [f"{state.has("Wind Stone")}"],
        "Thantos, Voltage Storage Unit -> Thantos, Secret Room 3":
            lambda state: [f"{state.has("Earth Stone")}"],
        "Thantos, Hidden Territory -> Thantos, Top of the Tower":
            lambda state: [f"{state.has("Lightning Stone")}, {state.has("Guardian Boots")}, {state.can_reach_region("Thantos, Voltage Storage Unit")}"],
			
			        #"Aquanet -> Aquanet Elevator":
        #    lambda state: [f"(state.has("Guardian Glove")}, {has_multibomb()}, {state.has("BombUp")})}", f"{state.can_build_ice()}"],
        #"Aquanet Elevator -> Aquanet Tower":
        #    lambda state: [f"{state.can_hit_fountain()}, {state.has("Fire Stone")}"],
        
        #"Horizon -> Horizon Basement":
        #    lambda state: [f"{state.has("Blue Gems")}, {state.can_destroy_with_immunity(state,player,["Wind Stone"])}"],
        
        #"Starlight -> Starlight Card Hunt":
        #    lambda state: [f"{state.can_destroy_with_immunity(state, ["Fire Stone","Earth Stone","Wind Stone","Light Stone"])}"],
        
        #"Epikyur -> Epikyur Haunted House":
        #    lambda state: [f"{state.can_hit_fountain()}, {state.has("Guardian Glove")}, {state.has("Wind Stone")}, {state.has("Earth Stone")}"],
        #"Epikyur -> Epikyur Museum":
        #    lambda state: [f"{state.has("Earth Stone")}"],
        #"Epikyur Haunted House -> Epikyur Coaster":
        #    lambda state: [f"{state.has("Earth Stone")}, {state.has("Museum Pass")}"],
        
        #"Thantos -> Thantos Trainside":
        #    lambda state: [f"{state.has("Train Batteries")}, {state.can_destroy_with_immunity(state, ["Dark Stone"])}"],
} 


def find_item(data, target_name):
    for item in data:
        if "name" not in item:
            continue
        if item["name"] == target_name:
            return item
        # If there are children, search them recursively
        if "children" in item:
            found = find_item(item["children"], target_name)
            if found:
                return found
    return None

# class trackerstate:
#     def has(item, player):
#         return item
        
# def populate_location_json(player):
#     test_var = lambda state: state.has("test item", player)
#     tester_var = test_var(trackerstate)
#     print(tester_var)

# populate_location_json("player")

def gen_item_automapping():
    item_list = {}
    for item, data in item_data_table.items():
        item_list[hex(data.code)] = f"{ "{{"} '{item}', 'toggle' {"}}"}"
    return item_list

def gen_location_automapping():
    location_list = {}
    for location, data in location_data_table.items():
        location_list[hex(data.address)] = f"{ "{{"}' @{data.region}/{location}'{"}}"}"
    return location_list

def gen_connection_table():
    connection_table = {}
    for region, data in region_data_table.items():
        for connection in region_data_table[region].connecting_regions:
            #if connection not in connection_table:
            #    connection_table[connection] = []
            #connection_table[connection].append(f"@{region}")
            connection_table[connection.replace(","," -")]= f"@{region.replace(","," -")}"
    return connection_table

def gen_region_access(player):
    region_access = {}
    for region_connection, rule_data in region_rules_track.items():
        connected_region = (region_connection.split(" -> ")[1]).replace(","," -")
        region_access[connected_region] = rule_data(trackerstate)
    return region_access

def get_map_name(loc_name):
    try:
        map_name = ""
        loc_region = loc_name.split(" ")[0]
        match loc_region:
            case "Shop":
                return "Space"
            case "Pommy":
                return "Space"
            case "Noah":
                return "Space"
            case _:
                return loc_region
        return loc_region
    
    except Exception as e:
        logger.warning(f"Error getting image path: {e}")
        return None, None

def get_loc_img(loc_type, loc_name):
    try:
        img_type = ""
        match loc_type:
            case "Boss":
                img_type = "boss"
            case "Generator":
                img_type = "gravity"
            case "Custom":
                part_color = loc_name.split(" ")[2]
                img_type = f"part{part_color.lower()}"
            case "Event":
                img_type = "event"
            case "Powerup":
                power_type = loc_name.split(" ")[1]
                img_type = power_type.lower()
            case "Gene":
                img_type = "gene"
            case "Shop":
                img_type = "shop"
            case _:
                return None, None
        closed_path = f"images/chest/{img_type}closed.png"
        open_path = f"images/chest/{img_type}open.png"
        return closed_path, open_path
    except Exception as e:
        logger.warning(f"Error getting image path: {e}")
        return None, None

def gen_item_json():
    #for location, data in location_data_table.items():
    # #    logger.warning(f"[{hex(data.address)}] = {"{{"}  @'{data.region}/{location}'  {"}}"},")
    item_json = {}
    for item, data in item_data_table.items():
        entry_data = {}
        entry_data["name"] = item
        entry_data["type"] = "toggle"
        entry_data["img"] = f"images/items/{item.lower().replace(" ","")}.png"
        entry_data["codes"] = item
        item_json.append(entry_data)
    return item_json

def connect_location_to_regions(region_list):
    region_locations = {}
    for region in region_list:
        region_locations[region] = []
    for location, data in location_data_table.items():
        loc_region = (data.region).replace(","," -")
        region_locations[loc_region].append(location)

    return region_locations

def populate_location_json():
    player = "player"
    out_json = []

    region_access = gen_region_access(player)
    connection_table = gen_connection_table()
    region_list = [region.replace(","," -") for region, data in region_data_table.items()]
    region_locations = connect_location_to_regions(region_list)
    #logger.warning(f"region_access: {region_access}")
    x_pos = 50
    y_pos = 50
    for region, data in region_data_table.items():
        entry_data = {}
        region_fix = region.replace(","," -")
        entry_data["name"] = region_fix

        # Create Region access rules
        entry_data["access_rules"] = []
        if region_fix in connection_table:
            if region_fix in region_access:
                for rule in region_access[region_fix]:
                    entry_data["access_rules"].append(f"{connection_table[region_fix]}, {rule}")
            else:
                entry_data["access_rules"].append(f"{connection_table[region_fix]}")

        # Add locations
        if region_fix in region_locations:
            if region_locations[region_fix]:
                entry_data["sections"] = []
                entry_data["map_locations"] = []
                for region_loc in region_locations[region_fix]:
                    section_data = {}
                    section_data["name"] = region_loc
                    section_data["item_count"] = 1
                    if region_loc in location_rule_track:
                        loc_rules = location_rule_track[region_loc]
                        section_data["access_rules"] = loc_rules(trackerstate)
                    loc_img_closed, loc_img_open = get_loc_img(location_data_table[region_loc].loc_type,region_loc)
                    if loc_img_closed:
                        section_data["chest_unopened_img"] = loc_img_closed
                        section_data["chest_opened_img"] = loc_img_open
                    entry_data["sections"].append(section_data)

                    map_data = {}
                map_data["map"] = get_map_name(region_loc)#region_loc.split(" ")[0]
                map_data["x"] = x_pos
                map_data["y"] = y_pos
                entry_data["map_locations"].append(map_data)
                x_pos += 10
                if x_pos > 400:
                    x_pos = 50
                    y_pos += 10

        
        #for location, data in location_data_table.items():

        out_json.append(entry_data)
    return out_json






