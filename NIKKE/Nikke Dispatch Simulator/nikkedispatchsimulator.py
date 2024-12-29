# -*- coding: utf-8 -*-

import random
import nikkedispatchsimulator_helper as helper

inventory = {"gems": 0, "core_dust_hour": 0, "credits_hour": 0,
             "gold_box": 0, "purple_box": 0, "gold_kit": 0, "purple_kit": 0, "blue_kit": 0, "doll_box": 0,
             "r_bond_ticket": 0, "sr_bond_ticket": 0, "r_boost_module": 0, "sr_boost_module": 0,
             "purple_mold": 0, "gold_mold": 0, "sr_doll": 0, "r_doll": 0}

simulated_total_inventory = {}

cached_no_reset_result = {'gems': 1581.0633333333333, 'core_dust_hour': 65.035,
                                     'credits_hour': 114.28466666666667, 'gold_box': 0.0,
                                     'purple_box': 0.0, 'gold_kit': 13.668333333333333,
                                     'purple_kit': 41.21966666666667, 'blue_kit': 246.86,
                                     'doll_box': 94.88333333333334, 'r_bond_ticket': 24.437333333333335,
                                     'sr_bond_ticket': 40.86366666666667, 'r_boost_module': 423.5466666666667,
                                     'sr_boost_module': 164.55133333333333, 'purple_mold': 23.31,
                                     'gold_mold': 1.7223333333333333, 'sr_doll': 0.8036666666666666,
                                     'r_doll': 2.683333333333333}

cached_most_economic_route_result = {'gems': 1988.37 - 589.3833333333, 'core_dust_hour': 81.85866666666666,
                                     'credits_hour': 143.724, 'gold_box': 0.0, 'purple_box': 0.0,
                                     'gold_kit': 16.555, 'purple_kit': 48.95333333333333, 'blue_kit': 247.679,
                                     'doll_box': 94.70666666666666, 'r_bond_ticket': 18.017333333333333,
                                     'sr_bond_ticket': 30.305, 'r_boost_module': 313.7683333333333,
                                     'sr_boost_module': 121.69766666666666, 'purple_mold': 17.302,
                                     'gold_mold': 1.276, 'sr_doll': 0.8533333333333334, 'r_doll': 2.637}
gems_spent = 0

please_doll_claim = [["doll_box", 60], ["gold_kit", 2], ["gold_box", 2],
                     ["purple_kit", 3],
                     ["doll_box", 40], ["gold_kit", 1], ["purple_kit", 2], ["gold_box", 1], ["purple_box", 2]]

please_material_claim = [["gems", 15], ["gems", 20], ["gems", 25], ["gems", 30],
                         ["core_dust_hour", 2], ["core_dust_hour", 3],
                         ["credits_hour", 2], ["credits_hour", 3]]

doll_gacha_choices = [
    {"name": "blue_kit", "quantity": 2, "probability": 0.15}, 
    {"name": "blue_kit", "quantity": 3, "probability": 0.15}, 
    {"name": "purple_kit", "quantity": 2, "probability": 0.06},
    {"name": "purple_kit", "quantity": 3, "probability": 0.03},
    {"name": "gold_kit", "quantity": 1, "probability": 0.04},
    {"name": "gold_kit", "quantity": 2, "probability": 0.02},
    {"name": "purple_box", "quantity": 1, "probability": 0.15},
    {"name": "purple_box", "quantity": 2, "probability": 0.08},
    {"name": "gold_box", "quantity": 1, "probability": 0.08},
    {"name": "gold_box", "quantity": 2, "probability": 0.04},
    {"name": "doll_box", "quantity": 20, "probability": 0.03},
    {"name": "doll_box", "quantity": 30, "probability": 0.07},
    {"name": "doll_box", "quantity": 40, "probability": 0.07},
    {"name": "doll_box", "quantity": 60, "probability": 0.03},
]

material_gacha_choices = [
    {"name": "gems", "quantity": 15, "probability": 0.064287},
    {"name": "gems", "quantity": 20, "probability": 0.030002},
    {"name": "gems", "quantity": 25, "probability": 0.100002},
    {"name": "gems", "quantity": 30, "probability": 0.039998},
    {"name": "core_dust_hour", "quantity": 2, "probability": 0.017144},
    {"name": "core_dust_hour", "quantity": 2, "probability": 0.057144},
    {"name": "core_dust_hour", "quantity": 3, "probability": 0.022856},
    {"name": "credits_hour", "quantity": 2, "probability": 0.030002},
    {"name": "credits_hour", "quantity": 2, "probability": 0.100002},
    {"name": "credits_hour", "quantity": 3, "probability": 0.039998},
    {"name": "r_bond_ticket", "quantity": 2, "probability": 0.021429},
    {"name": "r_bond_ticket", "quantity": 3, "probability": 0.012858},
    {"name": "sr_bond_ticket", "quantity": 2, "probability": 0.042858},
    {"name": "sr_bond_ticket", "quantity": 3, "probability": 0.017142},
    {"name": "r_boost_module", "quantity": 10, "probability": 0.064287},
    {"name": "r_boost_module", "quantity": 15, "probability": 0.051432},
    {"name": "sr_boost_module", "quantity": 2, "probability": 0.171432},
    {"name": "sr_boost_module", "quantity": 3, "probability": 0.068568},
    {"name": "purple_mold", "quantity": 1, "probability": 0.008572},
    {"name": "purple_mold", "quantity": 2, "probability": 0.028572},
    {"name": "purple_mold", "quantity": 2, "probability": 0.005714},
    {"name": "gold_mold", "quantity": 1, "probability": 0.005714},
]

def doll_gacha():
    
    # Extract the item names, quantities, and probabilities
    names = [doll_gacha_choice['name'] for doll_gacha_choice in doll_gacha_choices]
    quantities = [doll_gacha_choice['quantity'] for doll_gacha_choice in doll_gacha_choices]
    probabilities = [doll_gacha_choice['probability'] for doll_gacha_choice in doll_gacha_choices]

    # Use random.choices() to select an item based on probabilities
    selected_item_index = random.choices(range(len(doll_gacha_choices)), weights=probabilities, k=1)[0]

    # Get the selected item
    selected_item = names[selected_item_index]
    selected_item_quantity = quantities[selected_item_index]

    # Return the selected item and its quantity as a dictionary
    return [selected_item, selected_item_quantity]

def material_gacha():
    
    # Extract the item names, quantities, and probabilities
    names = [material_gacha_choice['name'] for material_gacha_choice in material_gacha_choices]
    quantities = [material_gacha_choice['quantity'] for material_gacha_choice in material_gacha_choices]
    probabilities = [material_gacha_choice['probability'] for material_gacha_choice in material_gacha_choices]

    # Use random.choices() to select an item based on probabilities
    selected_item_index = random.choices(range(len(material_gacha_choices)), weights=probabilities, k=1)[0]

    # Get the selected item
    selected_item = names[selected_item_index]
    selected_item_quantity = quantities[selected_item_index]

    # Return the selected item and its quantity as a dictionary
    return [selected_item, selected_item_quantity]

def open_all_mileage_boxes():
    items = [["sr_doll", 1], ["r_doll", 1]]
    probabilities = [0.2, 0.8]
        
    while (inventory["doll_box"] >= 200):
        selected_item = random.choices(items, weights=probabilities, k=1)[0]
        inventory[selected_item[0]] += selected_item[1]
        inventory["doll_box"] -= 200
        
def convert_all_blue_dolls():
    items = [["sr_doll", 1], ["purple_kit", 20], ["gold_kit", 10]]
    probabilities = [0.15, 0.55, 0.3]
        
    while (inventory["r_doll"] >= 5):
        selected_item = random.choices(items, weights=probabilities, k=1)[0]
        inventory[selected_item[0]] += selected_item[1]
        inventory["r_doll"] -= 5
    
def convert_purple_box():
    items = [["purple_kit", 1], ["blue_kit", 3]]
    probabilities = [0.2, 0.8]
    
    for i in range(inventory["purple_box"]):
        selected_item = random.choices(items, weights=probabilities, k=1)[0]
        inventory["purple_box"] -= 1
        inventory[selected_item[0]] += selected_item[1]
    
def convert_gold_box():
    items = [["gold_kit", 2], ["purple_kit", 2], ["blue_kit", 5]]
    probabilities = [0.1, 0.2, 0.7]
    
    for i in range(inventory["gold_box"]):
        selected_item = random.choices(items, weights=probabilities, k=1)[0]
        inventory["gold_box"] -= 1
        inventory[selected_item[0]] += selected_item[1]

"""def convert_boxes_into_kits():
        
    for item_name, quantity in inventory.items():
        if item_name == "purple_box" and quantity > 0:
            convert_purple_box(quantity)
        elif item_name == "gold_box" and quantity > 0:
            convert_gold_box(quantity)"""
    
def transfer_claimed_to_inventory(claimed_materials):
    for item_type, quantity in claimed_materials:
        if item_type in inventory:
            inventory[item_type] += quantity
        #else:
        #    inventory[item_type] = quantity
    
def new_dispatch(method, threshold = 6):
    claimed_materials = []
    
    doll_unclaimed = 4
    material_unclaimed = 10
    
    global gems_spent
    gems_spent -= 50
    
    if (method == "kisenix"):
        while (doll_unclaimed + material_unclaimed >= threshold):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
                elif item in please_material_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    material_unclaimed -= 1  
                    
        else:
            claimed_materials.extend(current_dispatch_list)
            
    elif (method == "kisenix_cheaper"):
        while (doll_unclaimed + material_unclaimed >= 7 or (doll_unclaimed == 1 and material_unclaimed >= 5)):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
                elif item in please_material_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    material_unclaimed -= 1  
                    
        else:
            claimed_materials.extend(current_dispatch_list)
            
    elif (method == "akusetsu"):
        while (True):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())               
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
                
            
            if (any(item[0] == "gems" for item in current_dispatch_list)):
                claimed_materials.extend(current_dispatch_list)
                break
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
    elif (method == "gems_only"):
        while (doll_unclaimed + material_unclaimed >= threshold):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())          
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
                elif item[0] in ["gems"]:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    material_unclaimed -= 1  
                    
        else:
            claimed_materials.extend(current_dispatch_list)
    
    elif (method == "most_economic_but_gems_only"):
        while (material_unclaimed >= 6):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
                elif item[0] in ["gems"]:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    material_unclaimed -= 1  
                    
        else:
            claimed_materials.extend(current_dispatch_list)
            
    elif (method == "most_economic_route_6"):
        while (material_unclaimed >= 6):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
                elif item in please_material_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    material_unclaimed -= 1   
                    
        else:
            claimed_materials.extend(current_dispatch_list)
            
    elif (method == "most_economic_route_5"):
        while (material_unclaimed >= 5):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
                elif item in please_material_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    material_unclaimed -= 1   
                    
        else:
            claimed_materials.extend(current_dispatch_list)
            
    elif (method == "kira"):
        while (doll_unclaimed >= 1):
        
            gems_spent += 50
            
            current_dispatch_list = []
            
            for i in range(doll_unclaimed):
                current_dispatch_list.append(doll_gacha())
            for i in range(material_unclaimed):
                current_dispatch_list.append(material_gacha())
            
            for index, item in enumerate(current_dispatch_list):
                if item in please_doll_claim:
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    doll_unclaimed -= 1
                    
                elif item[0] == "gems":
                    claimed_materials.append(item)
                    current_dispatch_list[index] = ["", 0]
                    material_unclaimed -= 1    
                    
        else:
            claimed_materials.extend(current_dispatch_list)
            
    elif (method == "no_reset"):
        gems_spent += 50
        
        current_dispatch_list = []
        
        for i in range(doll_unclaimed):
            current_dispatch_list.append(doll_gacha())
        for i in range(material_unclaimed):
            current_dispatch_list.append(material_gacha())
        claimed_materials.extend(current_dispatch_list)
        
            
    transfer_claimed_to_inventory(claimed_materials)
    
if __name__ == "__main__":
    
    # ONLY CHANGE THIS
    method = "kisenix"
    threshold = 6 #only for kisenix and gems_only, leave 6-7 for default
    convert_boxes_to_kits = True
    open_mileage_and_convert_blue_dolls_to_kits = True
    simulation_times = 3000
    
    
    # DO NOT TOUCH
    print("Method used:", method)
    
    print(helper.get_method_description(method, threshold), "\n")
        
    if (convert_boxes_to_kits):
        print("Boxes are converted into kits.\n")
    else:
        print("Boxes are not converted into kits.\n")
        
    if (open_mileage_and_convert_blue_dolls_to_kits):
        print("Mileage boxes are opened and dolls are converted.\n")
    else:
        print("Mileage boxes are unopened and dolls are not converted.\n")
        
        
    for i in range(simulation_times):
        inventory = inventory.fromkeys(inventory, 0)
        for j in range(30):
            new_dispatch(method, threshold)
        if (convert_boxes_to_kits):
            convert_purple_box()
            convert_gold_box()
        if (open_mileage_and_convert_blue_dolls_to_kits):
            open_all_mileage_boxes()
            convert_all_blue_dolls()
        for key, value in inventory.items():
            simulated_total_inventory[key] = simulated_total_inventory.get(key, 0) + value
    
    print(f"Gems spent over 30 days (averaged over {simulation_times}x simulated runs):", gems_spent/simulation_times)
    print(f"Items obtained over 30 days (averaged over {simulation_times}x simulated runs):")
    divided_data = {key: value / simulation_times for key, value in simulated_total_inventory.items()}
    
    for key, value in divided_data.items():
        print(f"- {key.replace('_', ' ').title()} = {value:.2f}")
        
    print("Net gems earning:", divided_data.get("gems") - gems_spent/simulation_times)
    
    if(method != "most_economic_route_6"):
        print("\nADDITIONAL COMPARISON VS MOST ECONOMIC ROUTE 6\n")
        keys_to_show = ["core_dust_hour", "credits_hour", "gold_kit", "purple_kit", "blue_kit"]
        comparison = {key: divided_data[key] - cached_most_economic_route_result[key] for key in keys_to_show
                      if key in divided_data and key in cached_most_economic_route_result}
        for key, value in comparison.items():
            print(f"- {key.replace('_', ' ').title()} = {value:+.2f}")
        print("Net gems earning:", (divided_data.get("gems") - gems_spent/simulation_times) - cached_most_economic_route_result["gems"])
            
    if(method != "no_reset"):
        print("\nADDITIONAL COMPARISON VS NO RESET\n")
        keys_to_show = ["core_dust_hour", "credits_hour", "gold_kit", "purple_kit", "blue_kit"]
        comparison = {key: divided_data[key] - cached_no_reset_result[key] for key in keys_to_show
                      if key in divided_data and key in cached_no_reset_result}
        for key, value in comparison.items():
            print(f"- {key.replace('_', ' ').title()} = {value:+.2f}")
        print("Net gems earning:", (divided_data.get("gems") - gems_spent/simulation_times) - cached_no_reset_result["gems"])
        
    