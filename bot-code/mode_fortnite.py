import random

def one(p):

    nonlethal = [
        f"{p[0]} went fishing. They weren't very successful.",
        f"{p[0]} went fishing. They caught a flopper!",
        f"{p[0]} watched the sky.",
        f"{p[0]} farted.",
        f"{p[0]} ate some slap berries. They were delicious!",
        f"{p[0]} picked some mushrooms.",
        f"{p[0]} went on a joyride.",
        f"{p[0]} claimed a capture point.",
        f"{p[0]} hit the griddy.",
        f"{p[0]} widdawy hit the gwiddy.",
        f"{p[0]} tamed a dinosaur.",
        f"{p[0]} found a pizza!",
        f"{p[0]} found a legendary weapon!",
        f"{p[0]} blew up a gas station.",
        f"{p[0]} jumped into a rift.",
        f"{p[0]} rode a boar.",
        f"{p[0]} rode a wolf.",
        f"{p[0]} drove across the map.",
        f"{p[0]} killed some bots.",
        f"{p[0]} pulled off a heist!",
        f"{p[0]} barely escaped the storm!",
        f"{p[0]} hid in a bush.",
        f"{p[0]} ran around with a chicken.",
        f"{p[0]} sniped a chicken.",
        f"{p[0]} howled.",
        ]
    
    lethal1 = [
        f"{p[0]} fell off a cliff and splattered.",
        f"{p[0]} got killed by a bot.",
        f"{p[0]} got lost in the storm.",
        f"{p[0]} blew up a gas station, along with themselves.",
        f"{p[0]} got pecked to death by a chicken.",
        f"{p[0]} blew themselves up with their own rocket launcher.",
        f"{p[0]} fell out of a tree.",
        ]

    return (nonlethal, lethal1)

def two(p):

    nonlethal = [
        f"{p[0]} and {p[1]} went fishing together. They weren't very successful.",
        f"{p[0]} and {p[1]} went fishing together. They caught a lot of fish and weapons!",
        f"{p[0]} and {p[1]} watched the sky together.",
        f"{p[0]} farted. {p[1]} was grossed out.",
        f"{p[0]} farted. {p[1]} liked it?",
        f"{p[0]} stalked {p[1]} from the trees.",
        f"{p[0]} and {p[1]} hugged.",
        f"{p[0]} and {p[1]} went on a joyride.",
        f"{p[0]} and {p[1]} picked mushrooms together.",
        f"{p[0]} and {p[1]} pulled off a heist!",
        f"{p[0]} and {p[1]} hit the griddy.",
        f"{p[0]} and {p[1]} killed a boss.",
        f"{p[0]} survived a bounty from {p[1]}.",
        f"{p[0]} and {p[1]} hunted some animals.",
        f"{p[0]} got knocked, but {p[1]} revived them.",
        f"{p[0]} and {p[1]} hid in a bush together.",
        f"{p[0]} and {p[1]} jumped into a dumpster.",
        f"{p[0]} chased {p[1]} across the map.",
        f"{p[0]} and {p[1]} claimed a capture point.",
        f"{p[0]} and {p[1]} shared a pizza.",
        f"{p[0]} gave some heals to {p[1]}.",
        f"{p[0]} shared their ammo with {p[1]}.",
        f"{p[0]} knocked {p[1]} off a zipline.",
        f"{p[0]} begged {p[1]} for V-Bucks.",
        f"{p[0]} and {p[1]} howled together.",
        f"{p[0]} howled. {p[1]} gave them a weird a look.",
        ]

    lethal1 = [
        f"{p[0]} impulsed {p[1]} off a cliff.",
        f"{p[0]} sniped {p[1]}.",
        f"{p[0]} sniped {p[1]} from a bush.",
        f"{p[1]} ran into {p[0]}'s spike trap.",
        f"{p[1]} was surprised by {p[0]}'s dart trap.",
        f"{p[0]} didn't see {p[1]} and ran them over.",
        f"{p[0]} saw {p[1]} and ran them over.",
        f"{p[0]} threw a firefly jar at {p[1]}. They forgot to stop, drop, and roll.",
        f"Both {p[0]} and {p[1]} ran out of ammo, so {p[0]} managed to bludgeon {p[1]} to death with their harvester.",
        f"{p[0]} shotgunned {p[1]}.",
        f"{p[0]} blew up {p[1]}.",
        f"{p[0]} killed {p[1]} and hit the griddy on their corpse.",
        f"{p[0]} threw a junk rift at {p[1]} and buried them.",
        f"{p[0]} took a bounty on {p[1]} and killed them.",
        ]

    lethal2 = [
        f"{p[0]} blew up {p[1]} and themselves.",
        f"{p[0]} and {p[1]} tried to hunt a boar. They both got gored.",
        f"{p[0]} and {p[1]} went on a joyride. It was lots of fun! Until {p[0]} drove them into a gas station.",
        f"{p[0]} got into a fight with {p[1]}. They won! But they got pecked by a chicken before they could heal.",
        f"{p[0]} and {p[1]} got killed by bots.",
        f"{p[0]} and {p[1]} have a brutal fight. Both at low health, they somehow shoot at the exact same time, killing each other.",
        f"{p[0]} set {p[1]} and themself on fire.",
        f"{p[0]} killed {p[1]} but couldn't outrun the storm.",
        f"{p[0]} shockwaved {p[1]} into the storm, but {p[1]} managed to shoot and kill them before their own death.",
        ]

    return (nonlethal, lethal1, lethal2)

def three(p):

    nonlethal = [
        f"{p[0]}, {p[1]}, and {p[2]} went fishing together. They weren't very successful.",
        f"{p[0]}, {p[1]}, and {p[2]} went fishing together. They caught lots of floppers, shield fish, and weapons!",
        f"{p[0]}, {p[1]}, and {p[2]} watched the sky together.",
        f"{p[0]} farted. {p[1]} and {p[2]} were grossed out.",
        f"{p[0]} farted. {p[1]} laughed. {p[2]} liked it?",
        f"{p[0]}, {p[1]} and {p[2]} hit the griddy.",
        f"{p[0]}, {p[1]} and {p[2]} ate some pizza!",
        f"{p[0]}, {p[1]} and {p[2]} hid in a bush.",
        f"{p[0]}, {p[1]} and {p[2]} claimed a capture point.",
        f"{p[0]} and {p[1]} chased {p[2]} across the map.",
        f"{p[0]}, {p[1]} and {p[2]} split the loot from a cache.",
        f"{p[0]}, {p[1]} and {p[2]} howled together.",
        f"{p[0]} howled. {p[1]} and {p[2]} shared confused glances.",
        ]

    lethal1 = [
        f"{p[0]} and {p[1]} ran {p[2]} off a cliff.",
        f"{p[0]} and {p[1]} convinced {p[2]} to do a trickshot off of the highest building in Tilted. It didn't go well.",
        f"{p[0]} and {p[1]} lured {p[2]} into a trap.",
        f"{p[0]} and {p[1]} tried to play a prank on {p[2]}. It went terribly wrong.",
        f"{p[0]} and {p[1]} killed {p[2]} and hit the griddy on their corpse.",
        ]

    lethal2 = [
        f"{p[0]} snuck up on {p[1]} and {p[2]} as they danced together. {p[0]} shot a barrage of grenades at them.",
        f"{p[0]} and {p[1]} tried to kill {p[2]}, but {p[0]} accidentally shot {p[1]} along with {p[2]}.",
        f"{p[0]} third-partied {p[1]} and {p[2]}.",
        f"{p[1]} and {p[2]} chased {p[0]}. They were caught off guard by {p[0]}'s trap.",
        ]

    lethal3 = [
        f"{p[0]}, {p[1]}, and {p[2]} were having fun flying a plane around the map, until {p[0]} crashed it into a mountain. Who let them be the pilot?",
        f"{p[0]} and {p[1]} weren't paying attention and ran off a cliff. Trying to revive them, {p[2]} also fell off the cliff.",
        f"{p[0]} managed to kill both {p[1]} and {p[2]}, but the storm finished them off.",
        f"{p[0]}, {p[1]}, and {p[2]} got killed by a bot squad.",
        f"{p[0]}, {p[1]}, and {p[2]} tried to pull off the greatest heist and got killed by turrets.",
        
        ]

    return (nonlethal, lethal1, lethal2, lethal3)

def four(p):

    nonlethal = [
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} went fishing together. Against all odds, none of the four caught anything.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} went fishing together. They depleted every fishing spot!",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} watched the sky together.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} picked mushrooms together.",
        f"{p[0]} farted. {p[1]}, {p[2]}, and {p[3]} were grossed out.",
        f"{p[0]} farted. {p[1]} laughed. {p[2]} was grossed out. {p[3]} liked it?",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} hit the griddy.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} drove around the map on a battle bus.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} hid in a bush. It was a tight fit.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} flew through a slipstream.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} jumped into a rift.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} claimed a capture point.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} danced for a few minutes before going their separate ways.",
        f"{p[0]} and {p[1]} chased {p[2]} and {p[3]} across the map.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} howled together.",
        f"{p[0]} tried to start a group howl. {p[1]}, {p[2]}, and {p[3]} ignored them.",
        ]

    lethal1 = [
        f"{p[0]}, {p[1]}, and {p[2]} chased and cornered {p[3]}, killing them.",
        f"{p[0]} and {p[1]} chased {p[2]} and {p[3]}. They managed to kill {p[3]}, but {p[2]} got away.",
        f"{p[0]}, {p[1]}, and {p[2]} tricked {p[3]} into a trap.",
        f"{p[0]}, {p[1]}, and {p[2]} dared {p[3]} to fight a chicken. Somehow, the chicken won.",
        f"{p[0]}, {p[1]}, {p[2]} and {p[3]} lost track of time and got caught in the storm. {p[3]} didn't make it out.",
        ]

    lethal2 = [
        f"{p[0]} and {p[1]} had a shootout with {p[2]} and {p[3]}. {p[0]} and {p[1]} were victorious!",
        f"{p[2]} and {p[3]} had a shootout with {p[0]} and {p[1]}. {p[0]} and {p[1]} were victorious!",
        f"{p[0]} and {p[2]} tried to ambush {p[1]} and {p[3]}. {p[3]} died, but {p[1]} killed {p[2]} and managed to escape.",
        f"{p[0]}, {p[1]}, {p[2]} and {p[3]} weren't paying attention and got surprised by the storm. {p[2]} and {p[3]} couldn't run fast enough.",
        ]

    lethal3 = [
        f"{p[0]} snuck up on {p[1]}, {p[2]}, and {p[3]} as they emoted together. {p[0]} shot a rocket at them.",
        f"{p[1]}, {p[2]}, and {p[3]} were showing off their dance moves to one another. Unfortunately, they didn't notice {p[0]} until it was too late.",
        f"{p[1]}, {p[2]}, and {p[3]} attacked {p[0]}, but the three of them got cocky. {p[0]} was barely able to clutch and kill the group.",
        f"{p[0]} hid in a bush and watched {p[1]}, {p[2]}, and {p[3]} fight it out. Just as {random.choice([p[1],p[2],p[3]])} fired the last shot and stopped to catch their breath, {p[0]} sniped them.",
        f"{p[0]} fourth-partied {p[1]}, {p[2]}, and {p[3]}.",
        ]

    lethal4 = [
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} got into a huge fight. {random.choice([p[0],p[1],p[2],p[3]])} came out on top, but they died in the storm.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} got killed by bots.",
        f"{p[0]} and {p[1]} got into a fight with {p[2]} and {p[3]}. None of them survived.",
        ]

    return (nonlethal, lethal1, lethal2, lethal3, lethal4)

def winner_comment(p):

    comment = [
        "They hit the griddy.",
        '"Suck it!"',
        "They bow graciously.",
        '"Can I go home now?"',
        '"I couldn\'t have done it on my own. I\'ll never forget those who helped me get here."',
        "They stand there awkwardly.",
        '"I\'m getting out of the loop!"',
        '"Easy."',
        '"EASY!"',
        ]

    return comment

def no_winner_comment():

    comment = [
        "Crows fly overhead.",
        "The grass waves.",
        "The wind blows.",
        "The loop resets.",
        "The bus driver gets ready for their next trip.",
        "What happened?",
        "Where did everyone go?",
        "Maybe next time.",
        "Trees rustle in the wind.",
        ]

    return comment
    

    
