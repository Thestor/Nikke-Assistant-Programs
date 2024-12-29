# -*- coding: utf-8 -*-

def get_method_description(method_name, threshold = 0):
    
    if (method_name == "kisenix"):
        method_description = f"""• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• If sum of unclaimed doll dispatches + material dispatches is {threshold} or above, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif (method_name == "kisenix_cheaper"):
        method_description = """• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• If sum of unclaimed doll dispatches + material dispatches is 7 or above (or 6 if 1 doll), then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif (method_name == "akusetsu"):
        method_description = """• Take all doll dispatches that are at least B or above.
• If there is at least 1 gem dispatch, take all."""

    elif (method_name == "gems_only"):
        method_description = f"""• Take all doll dispatches that are at least B or above.
• Take all gems dispatches.
• If sum of unclaimed doll dispatches + material dispatches is {threshold}, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif (method_name == "most_economic_but_gems_only"):
        method_description = """• Take all doll dispatches that are at least B or above.
• Take all gems dispatches.
• If sum of unclaimed material dispatches is 6 or above, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif (method_name == "most_economic_route_6"):
        method_description = """• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• If sum of unclaimed material dispatches is 6 or above, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif (method_name == "most_economic_route_5"):
        method_description = """• Take all doll dispatches that are at least B or above.
• Take all gems, core dust, and credit dispatches.
• If sum of unclaimed material dispatches is 5 or above, then reroll immediately.
• Repeat until condition is not satisfied, then claim all."""

    elif (method_name == "kira"):
        method_description = """• Take all doll dispatches that are at least B or above.
• Take all gems dispatches.
• Only after no doll dispatches remain then you claim all."""

    elif (method_name == "no_reset"):
        method_description = "No reset is done at all."

    return method_description