def one(p):

    nonlethal = [
        f"{p[0]} went fishing. They weren't very successful.",
        f"{p[0]} went fishing. They caught a lot of fish!",
        f"{p[0]} watched the stars.",
        f"{p[0]} farted.",
        f"{p[0]} ate some berries. They were delicious!",
        f"{p[0]} picked some flowers.",
        f"{p[0]} went on a joyride.",
        f"{p[0]} went shopping.",
        f"{p[0]} hit the griddy.",
        f"{p[0]} widdawy hit the gwiddy.",
        ]
    
    lethal1 = [
        f"{p[0]} fell off a cliff and splattered.",
        f"{p[0]} ate some berries. They had a stomach ache and died.",
        f"{p[0]} tried to pet a bear. It tore them to shreds.",
        f"{p[0]} tried to make an improvised explosive. It exploded.",
        ]

    return (nonlethal, lethal1)

def two(p):

    nonlethal = [
        f"{p[0]} and {p[1]} went fishing together. They weren't very successful.",
        f"{p[0]} and {p[1]} went fishing together. They caught a lot of fish!",
        f"{p[0]} and {p[1]} watched the stars together.",
        f"{p[0]} farted. {p[1]} was grossed out.",
        f"{p[0]} farted. {p[1]} liked it?",
        f"{p[0]} stalked {p[1]}.",
        f"{p[0]} and {p[1]} went on a date. It went well!",
        f"{p[0]} and {p[1]} went on a date. It didn't go very well...",
        f"{p[0]} and {p[1]} hugged.",
        f"{p[0]} and {p[1]} went on a joyride.",
        f"{p[0]} and {p[1]} picked flowers together.",
        f"{p[0]} gaslit {p[1]}.",
        f"{p[0]} and {p[1]} hit the griddy.",
        ]

    lethal1 = [
        f"{p[0]} shoved {p[1]} off a cliff.",
        f"{p[0]} sniped {p[1]}.",
        f"{p[0]} lured {p[1]} into a trap.",
        f"{p[0]} didn't see {p[1]} and ran them over.",
        f"{p[0]} saw {p[1]} and ran them over.",
        f"{p[0]} threw a molotov at {p[1]}. They forgot to stop, drop, and roll.",
        f"{p[0]} snuck up on {p[1]} and stabbed them.",
        f"{p[0]} and {p[1]} had a suicide pact. But {p[0]} didn't follow through.",
        f"{p[0]} and {p[1]} went on a date. It REALLY didn't go well!",
        f"{p[0]} blew up {p[1]}.",
        f"{p[0]} killed {p[1]} and hit the griddy on their corpse.",
        ]

    lethal2 = [
        f"{p[0]} and {p[1]} had a suicide pact and killed themselves together.",
        f"{p[0]} blew up {p[1]} and themselves.",
        f"{p[0]} and {p[1]} tried to hunt a boar. They both got gored.",
        f"{p[0]} and {p[1]} went on a joyride. It was lots of fun! Until {p[0]} drove them off a cliff.",
        f"{p[0]} killed {p[1]}. But they couldn't take the guilt.",
        ]

    return (nonlethal, lethal1, lethal2)

def three(p):

    nonlethal = [
        f"{p[0]}, {p[1]}, and {p[2]} went fishing together. They weren't very successful.",
        f"{p[0]}, {p[1]}, and {p[2]} went fishing together. They caught a lot of fish!",
        f"{p[0]}, {p[1]}, and {p[2]} watched the stars together.",
        f"{p[0]} farted. {p[1]} and {p[2]} were grossed out.",
        f"{p[0]} farted. {p[1]} laughed. {p[2]} liked it?",
        f"{p[0]} and {p[1]} went on a date. {p[2]} third-wheeled.",
        f"{p[0]}, {p[1]}, and {p[2]} went shopping.",
        f"{p[0]}, {p[1]} and {p[2]} hit the griddy.",
        ]

    lethal1 = [
        f"{p[0]} and {p[1]} ran {p[2]} off a cliff.",
        f"{p[0]} and {p[1]} convinced {p[2]} to kickflip over a ravine. It didn't go well.",
        f"{p[0]} and {p[1]} lured {p[2]} into a trap.",
        f"{p[0]}, {p[1]}, and {p[2]} had a suicide pact. But only {p[2]} followed through.",
        f"{p[0]} and {p[1]} tried to play a prank on {p[2]}. It went terribly wrong.",
        f"{p[0]} and {p[1]} killed {p[2]} and hit the griddy on their corpse.",
        ]

    lethal2 = [
        f"{p[0]} snuck up on {p[1]} and {p[2]} as they discussed the political and economic state of the world. {p[0]} threw a bomb at them.",
        f"{p[0]} and {p[1]} tried to kill {p[2]}, but {p[0]} accidentally shot {p[1]} along with {p[2]}.",
        ]

    lethal3 = [
        f"{p[0]}, {p[1]}, and {p[2]} had a suicide pact and killed themselves together.",
        f"{p[0]}, {p[1]}, and {p[2]} tried to defuse a bomb without a guide.",
        f"{p[0]}, {p[1]}, and {p[2]} tried to tame a bear. It maimed all three of them.",
        ]

    return (nonlethal, lethal1, lethal2, lethal3)

def four(p):

    nonlethal = [
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} went fishing together. Against all odds, none of the four caught anything.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} went fishing together. They destroyed the local ecosystem with how much fish they caught!",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} watched the stars together.",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} picked flowers together.",
        f"{p[0]} farted. {p[1]}, {p[2]}, and {p[3]} were grossed out.",
        f"{p[0]} farted. {p[1]} laughed. {p[2]} was grossed out. {p[3]} liked it?",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} went on a double date. It was fun!",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} went on a double date. It didn't go very well...",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} went shopping!",
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} hit the griddy.",
        ]

    lethal1 = [
        f"{p[0]}, {p[1]}, and {p[2]} chased and cornered {p[3]}, killing them.",
        f"{p[0]} and {p[1]} chased {p[2]} and {p[3]}. They managed to kill {p[3]}, but {p[2]} got away.",
        f"{p[0]}, {p[1]}, and {p[2]} lured {p[3]} into a trap.",
        ]

    lethal2 = [
        f"{p[0]} and {p[1]} had a shootout with {p[2]} and {p[3]}. {p[0]} and {p[1]} were victorious!",
        f"{p[2]} and {p[3]} had a shootout with {p[0]} and {p[1]}. {p[0]} and {p[1]} were victorious!",
        f"{p[0]} and {p[2]} tried to ambush {p[1]} and {p[3]}. {p[3]} died, but {p[1]} killed {p[2]} and managed to escape.",
        ]

    lethal3 = [
        f"{p[0]} snuck up on {p[1]}, {p[2]}, and {p[3]} as they discussed the political and economic state of the world. {p[0]} threw a bomb at them.",
        f"{p[1]}, {p[2]}, and {p[3]} attacked {p[0]}, but the three of them got cocky. {p[0]} was barely able to kill the group.",
        ]

    lethal4 = [
        f"{p[0]}, {p[1]}, {p[2]}, and {p[3]} made a suicide pact and killed themselves together.",
        ]

    return (nonlethal, lethal1, lethal2, lethal3, lethal4)

def winner_comment(p):

    comment = [
        "They hit the griddy on the podium.",
        '"Suck it!"',
        "They bow graciously.",
        '"Can I go home now?"',
        '"I couldn\'t have done it on my own. I\'ll never forget those who helped me get here."',
        "They stand there awkwardly.",
        ]

    return comment

def no_winner_comment():

    comment = [
        'The wind blows.',
        'Birds fly overhead.',
        'What happened?',
        'Trees rustle.',
        'Leaves blow in the wind.',
        'Grass waves.',
        ]

    return comment
    

    
