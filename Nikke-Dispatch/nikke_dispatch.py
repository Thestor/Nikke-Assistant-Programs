# -*- coding: utf-8 -*-

import numpy as np
import random
import time


def get_method_description(method_name, threshold = 0):
    """Returns the method descriptions."""
    if method_name == "kisenix":
        return f"""• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• If sum of unclaimed doll dispatches + material dispatches is {threshold} or above, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif method_name == "kisenix_cheaper":
        return """• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• Reset algorithm varies depending on number of open slots type.
• Repeat until condition is not satisfied, then claim all."""

    elif method_name == "kisenix_more_expensive":
        return """• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• Reset algorithm varies depending on number of open slots type.
• Repeat until condition is not satisfied, then claim all."""

    elif method_name == "akusetsu":
        return """• Take all doll dispatches that are at least B or above.
• If there is at least 1 gem dispatch, take all."""

    elif method_name == "gems_only":
        return f"""• Take all doll dispatches that are at least B or above.
• Take all gems dispatches.
• If sum of unclaimed doll dispatches + material dispatches is {threshold}, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif method_name == "most_economic_but_gems_only":
        return """• Take all doll dispatches that are at least B or above.
• Take all gems dispatches.
• If sum of unclaimed material dispatches is 6 or above, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif method_name == "most_economic_route":
        return f"""• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• If sum of unclaimed material dispatches is {threshold} or above, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif method_name == "kira":
        return f"""• Take all doll kit dispatches that are at least A or above.
• Settle for B-ranked kits or above, or the 60 doll boxes, when only {threshold} doll dispatch{"es " if threshold > 1 else " "}remain{"s." if threshold == 1 else "."}
• Take all 25/30 gems dispatches or 3 core boxes.
• Only after no doll dispatches remain then you claim all."""

    elif method_name == "no_reset":
        return "No reset is done at all."

    raise ValueError(f'{method_name} is an invalid method.')


def convert_cum_prob(rel_prob: list) -> list:
    """Returns the cumulative probability of a relative list."""
    cum_doll_prob = np.zeros(len(rel_prob))
    total_prob = 0
    for i, p_val in enumerate(rel_prob):
        total_prob += p_val
        cum_doll_prob[i] = total_prob
    return cum_doll_prob


cached_no_reset_result = {
    'gems': 1581.0633333333333,
    'core_dust_hour': 65.035,
    'credits_hour': 114.28466666666667,
    'gold_box': 0.0,
    'purple_box': 0.0,
    'gold_kit': 13.668333333333333,
    'purple_kit': 41.21966666666667,
    'blue_kit': 246.86,
    'doll_box': 94.88333333333334,
    'r_bond_ticket': 24.437333333333335,
    'sr_bond_ticket': 40.86366666666667,
    'r_boost_module': 423.5466666666667,
    'sr_boost_module': 164.55133333333333,
    'purple_mold': 23.31,
    'gold_mold': 1.7223333333333333,
    'sr_doll': 0.8036666666666666,
    'r_doll': 2.683333333333333
}

SOLO_RAID_DROPS = [
    ["r_doll", 7],
    ["sr_doll", 3],
    ["purple_box", 12],
    ["gold_box", 51]
]

cached_most_economic_route_result = {
    'gems': 1988.37 - 589.3833333333,
    'core_dust_hour': 81.85866666666666,
    'credits_hour': 143.724,
    'gold_box': 0.0,
    'purple_box': 0.0,
    'gold_kit': 16.555,
    'purple_kit': 48.95333333333333,
    'blue_kit': 247.679,
    'doll_box': 94.70666666666666,
    'r_bond_ticket': 18.017333333333333,
    'sr_bond_ticket': 30.305,
    'r_boost_module': 313.7683333333333,
    'sr_boost_module': 121.69766666666666,
    'purple_mold': 17.302,
    'gold_mold': 1.276,
    'sr_doll': 0.8533333333333334,
    'r_doll': 2.637
}

please_doll_claim = [
    ['doll_box', 60],
    ['gold_kit', 2],
    ['gold_box', 2],
    ['purple_kit', 3],
    ['doll_box', 40],
    ['gold_kit', 1],
    ['purple_kit', 2],
    ['gold_box', 1],
    ['purple_box', 2]
]
kira_doll_claim = [
    ['gold_kit', 2],
    ['gold_box', 2],
    ['purple_kit', 3],
]
kira_settle_claim = [
    ['doll_box', 60],
    ['gold_kit', 2],
    ['gold_box', 2],
    ['purple_kit', 3],
    ['gold_kit', 1],
    ['purple_kit', 2],
    ['gold_box', 1],
    ['purple_box', 2]
]

please_material_claim = [
    ['gems', 15],
    ['gems', 20],
    ['gems', 25],
    ['gems', 30],
    ['core_dust_hour', 2],
    ['core_dust_hour', 3],
    ['credits_hour', 2],
    ['credits_hour', 3]
]
kira_mat_claim = [
    ['gems', 25],
    ['gems', 30],
    ['core_dust_hour', 3],
]

doll_gacha_choices = [
    {'name': 'blue_kit', 'quantity': 2, 'probability': 0.15},
    {'name': 'blue_kit', 'quantity': 3, 'probability': 0.15},
    {'name': 'purple_kit', 'quantity': 2, 'probability': 0.06},
    {'name': 'purple_kit', 'quantity': 3, 'probability': 0.03},
    {'name': 'gold_kit', 'quantity': 1, 'probability': 0.04},
    {'name': 'gold_kit', 'quantity': 2, 'probability': 0.02},
    {'name': 'purple_box', 'quantity': 1, 'probability': 0.15},
    {'name': 'purple_box', 'quantity': 2, 'probability': 0.08},
    {'name': 'gold_box', 'quantity': 1, 'probability': 0.08},
    {'name': 'gold_box', 'quantity': 2, 'probability': 0.04},
    {'name': 'doll_box', 'quantity': 20, 'probability': 0.03},
    {'name': 'doll_box', 'quantity': 30, 'probability': 0.07},
    {'name': 'doll_box', 'quantity': 40, 'probability': 0.07},
    {'name': 'doll_box', 'quantity': 60, 'probability': 0.03},
]
doll_prob = [x['probability'] for x in doll_gacha_choices]
cum_doll_prob = convert_cum_prob(doll_prob)

# List of dispatch tier probabilities respectively, in %
dispatch_p = np.array([
    0.7143,
    0.4286,
    1.4286,
    0.5714
])
dispatch_p /= 100
material_gacha_choices = [
    {'name': 'gems', 'quantity': 15, 'tier': 2, 'count': 9},
    {'name': 'r_bond_ticket', 'quantity': 2, 'tier': 2, 'count': 3},
    {'name': 'r_boost_module', 'quantity': 10, 'tier': 2, 'count': 9},

    {'name': 'gems', 'quantity': 20, 'tier': 3, 'count': 7},
    {'name': 'credits_hour', 'quantity': 2, 'tier': 3, 'count': 7},
    {'name': 'core_dust_hour', 'quantity': 2, 'tier': 3, 'count': 4},
    {'name': 'r_bond_ticket', 'quantity': 3, 'tier': 3, 'count': 3},
    {'name': 'r_boost_module', 'quantity': 15, 'tier': 3, 'count': 12},
    {'name': 'purple_mold', 'quantity': 1, 'tier': 3, 'count': 2},

    {'name': 'gems', 'quantity': 25, 'tier': 4, 'count': 7},
    {'name': 'credits_hour', 'quantity': 2, 'tier': 4, 'count': 7},
    {'name': 'core_dust_hour', 'quantity': 2, 'tier': 4, 'count': 4},
    {'name': 'sr_bond_ticket', 'quantity': 2, 'tier': 4, 'count': 3},
    {'name': 'sr_boost_module', 'quantity': 2, 'tier': 4, 'count': 12},
    {'name': 'purple_mold', 'quantity': 2, 'tier': 4, 'count': 2},

    {'name': 'gems', 'quantity': 30, 'tier': 5, 'count': 7},
    {'name': 'credits_hour', 'quantity': 3, 'tier': 5, 'count': 7},
    {'name': 'core_dust_hour', 'quantity': 3, 'tier': 5, 'count': 4},
    {'name': 'sr_bond_ticket', 'quantity': 3, 'tier': 5, 'count': 3},
    {'name': 'sr_boost_module', 'quantity': 3, 'tier': 5, 'count': 12},
    {'name': 'purple_mold', 'quantity': 2, 'tier': 5, 'count': 1},
    {'name': 'gold_mold', 'quantity': 1, 'tier': 5, 'count': 1},
]
# The total probability comes out to 1.00013 for some reason
for material_item in material_gacha_choices:
    material_item['probability'] = dispatch_p[material_item['tier'] - 2] * material_item['count']
material_prob = np.array([x['probability'] for x in material_gacha_choices])
material_prob /= np.sum(material_prob)
cum_mat_prob = convert_cum_prob(material_prob)

# print(f'{np.sum([x["probability"] for x in material_gacha_choices])}')
# print(f'{np.sum([x["probability"] for x in doll_gacha_choices])}')
# print(f'{np.sum([x["count"] for x in material_gacha_choices])}')

def get_empty_inventory() -> dict:
    """Returns an empty inventory from scratch."""
    return {
        'gems': 0,
        'core_dust_hour': 0,
        'credits_hour': 0,
        'gold_box': 0,
        'purple_box': 0,
        'gold_kit': 0,
        'purple_kit': 0,
        'blue_kit': 0,
        'doll_box': 0,
        'r_bond_ticket': 0,
        'sr_bond_ticket': 0,
        'r_boost_module': 0,
        'sr_boost_module': 0,
        'purple_mold': 0,
        'gold_mold': 0,
        'sr_doll': 0,
        'r_doll': 0
    }

def doll_gacha(count: int=1):
    """Rolls the doll gacha for the specified number of iterations."""
    selected_indices = random.choices(range(len(cum_doll_prob)), k=count, cum_weights=cum_doll_prob)
    return [
        [
            doll_gacha_choices[idx]['name'],
            doll_gacha_choices[idx]['quantity'],
        ]
    for idx in selected_indices]

def material_gacha(count: int=1):
    """Rolls the material gacha for the specified number of iterations."""
    selected_indices = random.choices(range(len(cum_mat_prob)), k=count, cum_weights=cum_mat_prob)
    return [
        [
            material_gacha_choices[idx]['name'],
            material_gacha_choices[idx]['quantity'],
        ]
    for idx in selected_indices]

def open_all_mileage_boxes(inventory: dict):
    """Converts doll RNG boxes into average expected SR/R dolls instead."""
    items = [["sr_doll", 1], ["r_doll", 1]]
    probabilities = [0.2, 0.8]
    samples = int(inventory["doll_box"] / 200)
    inventory["doll_box"] %= 200

    for selected_item, p_val in zip(items, probabilities):
        inventory[selected_item[0]] += selected_item[1] * p_val * samples

def convert_all_blue_dolls(inventory: dict):
    """Converts given blue dolls into average expected maintenance kits instead."""
    items = [["sr_doll", 1], ["purple_kit", 20], ["gold_kit", 10]]
    probabilities = [0.15, 0.55, 0.3]
    samples = int(inventory["r_doll"] / 5)
    inventory["r_doll"] %= 5

    for selected_item, p_val in zip(items, probabilities):
        inventory[selected_item[0]] += selected_item[1] * p_val * samples

def convert_purple_box(inventory: dict):
    """Converts all SR doll RNG boxes into the average expected maintenance kits."""
    items = [["purple_kit", 1], ["blue_kit", 3]]
    probabilities = [0.2, 0.8]
    samples = inventory["purple_box"]
    inventory["purple_box"] = 0

    for selected_item, p_val in zip(items, probabilities):
        inventory[selected_item[0]] += selected_item[1] * p_val * samples

def convert_gold_box(inventory: dict):
    """Converts all SSR doll RNG boxes into the average expected maintenance kits."""
    items = [["gold_kit", 2], ["purple_kit", 2], ["blue_kit", 5]]
    probabilities = [0.1, 0.2, 0.7]
    samples = inventory["gold_box"]
    inventory["gold_box"] = 0

    for selected_item, p_val in zip(items, probabilities):
        inventory[selected_item[0]] += selected_item[1] * p_val * samples


def transfer_claimed_to_inventory(inventory: dict, claimed_materials: list[tuple]):
    """Add a list of remaining dispatches to the given inventory."""
    for item_type, quantity in claimed_materials:
        inventory[item_type] += quantity


def new_dispatch(inventory: dict, method: str, threshold: int=6, doll_unclaimed: int=4, material_unclaimed: int=10, trash_only_scenario: bool=False):
    """Runs the dispatch simulation, adding the results to inventory and returning
    the number of times dispatch was reset.
    """
    
    num_resets = 0

    # Initial dispatches (if trash_only_scenario is True, then insert it with garbage)
    if (trash_only_scenario):
        doll_dispatch = ['blue_kit', 2] * doll_unclaimed
        mat_dispatch = ['r_boost_module', 10] * material_unclaimed
    else:
        doll_dispatch = doll_gacha(doll_unclaimed)
        mat_dispatch = material_gacha(material_unclaimed)

    # Map of method to break, reset, doll claim, and material claim conditons
    method_func_map = {
        'kisenix': [
            None,
            lambda: doll_unclaimed + material_unclaimed >= threshold,
            lambda item: item in please_doll_claim,
            lambda item: item in please_material_claim,
        ],
        'kisenix_cheaper': [
            None,
            lambda: (material_unclaimed >= 6 or
               (material_unclaimed == 5 and doll_unclaimed >= 1) or
               (material_unclaimed == 4 and doll_unclaimed >= 3) or
               (material_unclaimed == 3 and doll_unclaimed == 4)),
            lambda item: item in please_doll_claim,
            lambda item: item in please_material_claim,
        ],
        'kisenix_more_expensive': [
            None,
            lambda: (material_unclaimed >= 5 or
               (material_unclaimed == 4 and doll_unclaimed >= 3) or
               (material_unclaimed == 3 and doll_unclaimed == 4)),
            lambda item: item in please_doll_claim,
            lambda item: item in please_material_claim,
        ],
        'akusetsu': [
            lambda: any(item[0] == 'gems' for item in mat_dispatch),
            lambda: True,
            lambda item: item in please_doll_claim,
            lambda item: False,
        ],
        'gems_only': [
            None,
            lambda: doll_unclaimed + material_unclaimed >= threshold,
            lambda item: item in please_doll_claim,
            lambda item: item[0] == 'gems',
        ],
        'most_economic_but_gems_only': [
            None,
            lambda: material_unclaimed >= 6,
            lambda item: item in please_doll_claim,
            lambda item: item[0] == 'gems',
        ],
        'most_economic_route': [
            None,
            lambda: material_unclaimed >= threshold,
            lambda item: item in please_doll_claim,
            lambda item: item in please_material_claim,
        ],
        'kira': [
            None,
            lambda: doll_unclaimed > 0,
            lambda item: item in kira_doll_claim or \
                (doll_unclaimed <= threshold and item in kira_settle_claim),
            lambda item: item in kira_mat_claim,
        ],
        'no_reset': [
            None,
            lambda: False,
            lambda item: True,
            lambda item: False,
        ],
    }
    # Takes no arguments, determines if should settle for the existing dispatch
    should_break = method_func_map[method][0]
    # Takes no arguments, determines if we should reset dispatch
    should_reset = method_func_map[method][1]
    # Takes a doll tuple result as an argument
    should_claim_doll = method_func_map[method][2]
    # Takes a material tuple result as an argument
    should_claim_mat = method_func_map[method][3]

    # Iterate over the dispatches unless we should take the dispatch as is
    while should_break is None or not should_break():
        # Claim doll mats based on the doll dispatch condition
        for index, doll_item in enumerate(doll_dispatch):
            if not should_claim_doll(doll_item):
                continue
            inventory[doll_item[0]] += doll_item[1]
            doll_dispatch[index][1] = 0
            doll_unclaimed -= 1

        # Claim normal materials based on the normal mateerial dispatch condition
        for index, mat_item in enumerate(mat_dispatch):
            if not should_claim_mat(mat_item):
                continue
            inventory[mat_item[0]] += mat_item[1]
            mat_dispatch[index][1] = 0
            material_unclaimed -= 1

        # Decide whether or not to reset dispatch
        if not should_reset() or doll_unclaimed + material_unclaimed <= 0:
            break

        # Reset available dispatch
        if doll_unclaimed > 0:
            doll_dispatch = doll_gacha(doll_unclaimed)
        if material_unclaimed > 0:
            mat_dispatch = material_gacha(material_unclaimed)
        num_resets += 1

    # Add the remaining dispatches to inventory
    transfer_claimed_to_inventory(inventory, doll_dispatch)
    transfer_claimed_to_inventory(inventory, mat_dispatch)

    return num_resets


def main():
    """Main function."""

    # ONLY CHANGE THIS
    method = 'kisenix'
    threshold = 6 #only for some algorithms
    doll_unclaimed = 4
    material_unclaimed = 10
    trash_only_scenario = False

    convert_boxes_to_kits = True
    open_mileage_and_convert_blue_dolls_to_kits = True
    add_solo_raid_rewards = False

    total_days = 1
    num_sims = 10000


    # DO NOT TOUCH
    print("Method used: " + method + f"_{threshold}")
    print(get_method_description(method, threshold), "\n")

    print("Parameters:")
    if trash_only_scenario:
        print(f"• Starting list of {doll_unclaimed} doll and {material_unclaimed} material dispatches containing trash only.")
    else:
        print(f"• Starting list of {doll_unclaimed} doll and {material_unclaimed} material dispatches.")
    if convert_boxes_to_kits:
        print("• Boxes are converted into kits.")
    else:
        print("• Boxes are not converted into kits.")

    if open_mileage_and_convert_blue_dolls_to_kits:
        print("• Mileage boxes are opened and dolls are converted.")
    else:
        print("• Mileage boxes are unopened and dolls are not converted.")

    if add_solo_raid_rewards:
        print("• Solo Raid rewards are added on top.")
    else:
        print("• Solo Raid rewards are not included.")

    print()

    start_t = time.time()

    num_reset_samples = np.zeros(num_sims)
    inventory_samples = {
        key: np.zeros(num_sims) for key in get_empty_inventory().keys()
    }
    for sim_idx in range(num_sims):
        inventory = get_empty_inventory()
        for _ in range(total_days):
            num_reset_samples[sim_idx] += new_dispatch(inventory, method, threshold, doll_unclaimed, material_unclaimed, trash_only_scenario)
        if add_solo_raid_rewards:
            transfer_claimed_to_inventory(inventory, SOLO_RAID_DROPS)
        if convert_boxes_to_kits:
            convert_purple_box(inventory)
            convert_gold_box(inventory)
        if open_mileage_and_convert_blue_dolls_to_kits:
            open_all_mileage_boxes(inventory)
            convert_all_blue_dolls(inventory)
        for key, value in inventory.items():
            inventory_samples[key][sim_idx] = value

    avg_data = {key: np.mean(val) for key, val in inventory_samples.items()}
    gems_spent_avg = np.mean(num_reset_samples) * 50
    net_gems_avg = avg_data.get('gems') - gems_spent_avg
    end_t = time.time()

    print(f"Gems spent over {total_days} days (averaged over {num_sims}x simulated runs):",
          gems_spent_avg)
    print(f"Items obtained over {total_days} days (averaged over {num_sims}x simulated runs):")

    for key, value in avg_data.items():
        print(f"- {key.replace('_', ' ').title()} = {value:.2f}")

    print(f'Net gems earning: {net_gems_avg:.2f}')

    # solo raid rewards not cached yet
    if not add_solo_raid_rewards:
        if not (method == "most_economic_route" and threshold == 6):
            print("\nADDITIONAL COMPARISON VS MOST ECONOMIC ROUTE 6\n")
            keys_to_show = ["core_dust_hour", "credits_hour", "gold_kit", "purple_kit", "blue_kit"]
            comparison = {key: avg_data[key] - cached_most_economic_route_result[key] for key in keys_to_show
                          if key in avg_data and key in cached_most_economic_route_result}
            for key, value in comparison.items():
                print(f"- {key.replace('_', ' ').title()} = {value:+.2f}")
            print("Net gems earning:", net_gems_avg - cached_most_economic_route_result["gems"])

        if method != "no_reset":
            print("\nADDITIONAL COMPARISON VS NO RESET\n")
            keys_to_show = ["core_dust_hour", "credits_hour", "gold_kit", "purple_kit", "blue_kit"]
            comparison = {key: avg_data[key] - cached_no_reset_result[key] for key in keys_to_show
                          if key in avg_data and key in cached_no_reset_result}
            for key, value in comparison.items():
                print(f"- {key.replace('_', ' ').title()} = {value:+.2f}")
            print(f'Net gems earning: {net_gems_avg - cached_no_reset_result["gems"]:.2f}')

    print(f'Execution Time: {end_t - start_t:,.2f} sec')


if __name__ == "__main__":
    main()
