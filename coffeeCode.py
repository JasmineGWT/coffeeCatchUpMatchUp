import random
import sys

BIZGROUPS = ["CP", "BT", "SS", "CORP", "LI", "POI", "PR"]

# 8 July
COFFEE_DRINKERS = {
    "Matthew Wightman": "CORP",
    "Peter King": "LI",
    "Deborah Frost": "CORP",
    "Emory Beck": "CORP",
    "Karl Baker": "CORP",
    "Geoff O'Malley": "PR",
    "Shane Thompstone": "POI",
    "James Ford": "CP",
    "Ian Harrison": "SS",
    "Greg Byrom": "PR",
    "Gareth Hodkinson": "LI",
    "Rob Deakin": "CP",
    "Dionne Hansen": "POI",
    "Wendy Sneddon": "PR",
    "Ben P. Jones": "SS",
    "Rebecca McAtamney": "POI",
    "Dave Collett": "BT",
    "Chris Crook": "CORP",
    "James E. O'Brien": "BT",
    "Kasey Oomen": "LI",
    "Sharmla David": "POI",
    "Paula Gentle": "BT",
    "Graeme Blick": "BT",
    "Bill M. Nelson": "POI",
    "Jasmine Wallis-Tearne": "CP",
    "Shannon Steven": "PR"
}

MATCH_WITHIN_GROUPS = False


def even_num_coffee_drinkers(COFFEE_DRINKERS):
    num_drinkers = len(COFFEE_DRINKERS)
    print(f"Number of coffee drinkers = {num_drinkers}")
    if num_drinkers % 2 != 0:
        print("ERROR:  There is an odd number of coffee drinkers")
        sys.exit()


def is_valid_team(COFFEE_DRINKERS):
    for i in COFFEE_DRINKERS.values():
        bizgroup = i
        if bizgroup not in BIZGROUPS:
            print(f"ERROR: team value of: '{team}' is not recognised")
            sys.exit()


def validate_coffee_drinkers(COFFEE_DRINKERS):
    even_num_coffee_drinkers(COFFEE_DRINKERS)
    is_valid_team(COFFEE_DRINKERS)


def main():
    coffee_drinkers = list(COFFEE_DRINKERS.keys())
    not_matched = list(COFFEE_DRINKERS.keys())
    validate_coffee_drinkers(COFFEE_DRINKERS)
    matched_in_same_group = {}
    pairs = {}

    for coffee_drinker in coffee_drinkers:
        if not_matched is None:
            break
        if coffee_drinker not in not_matched:
            continue
        not_matched.remove(coffee_drinker)
        team = COFFEE_DRINKERS[coffee_drinker]
        if MATCH_WITHIN_GROUPS:
            coffee_drinker_match = random.choice(not_matched)
        else:
            # First try match those not in the same team.
            try:
                coffee_drinker_match = random.choice(
                    [i for i in not_matched if COFFEE_DRINKERS[i] != team]
                )
            except:
                coffee_drinker_match = random.choice(not_matched)
                matched_in_same_group[coffee_drinker] = coffee_drinker_match

        # The Match
        pairs[coffee_drinker] = coffee_drinker_match
        not_matched.remove(coffee_drinker_match)

    print(pairs)
    if matched_in_same_group:
        print("!!! MATCHED IN SAME GROUP !!!")
        print(matched_in_same_group)
    if not_matched:
        print("!!! NOT MATCHED !!!")
        print(not_matched)

    print("MATCHED")
    for k, v in pairs.items():
        print(f"{k} > {v}")


if __name__ == "__main__":
    main()
