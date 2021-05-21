# 3 sides : footsteps, shotgun, brain
# red has has more shoutgun than yellow, which has more shoutgun that green
# 3 reds 4 yellow 5 green
# red = 3 shotgun, yellow = 2, green = 1
# 3 footsteps = reroll them again
# 2 footsteps = take 1 more and roll them again
# 1 turn means taking 3 dice and rolling them
# separate brains and shotgun
# footprints mean roll footstep + 2 more dice
# shotgun means you lose all brains, and turn goes to next player
# you can stop your turn any time you want, and score all brains, then next player goes. the game finishes next round after someone gets 13 brains (everyone has 1 round to try and tie)
# tie = the tying players roll untill some1 loses

import random
import zombiedice


class RandomContinueBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        rollAgain = random.randint(0, 1)
        while diceRollResults is not None and rollAgain:
            diceRollResults = zombiedice.roll()
            rollAgain = random.randint(0, 1)


class StopAfterTwoBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults["brains"]

            if brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll()


class StopAfterTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults["brains"]

            if brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll()


class RollFourButMaybeStop:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        numberOfRolls = 0
        shotguns = 0
        while diceRollResults is not None and numberOfRolls < 5:
            shotguns += diceRollResults["shotgun"]

            if shotguns == 2:
                break
            else:
                numberOfRolls += 1
                diceRollResults = zombiedice.roll()


class StopAfterRollingMoreShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults["brains"]
            shotguns += diceRollResults["shotgun"]
            if brains < shotguns:
                break
            else:
                diceRollResults = zombiedice.roll()


zombies = (
    # zombiedice.examples.RandomCoinFlipZombie(name="Random"),
    # zombiedice.examples.RollsUntilInTheLeadZombie(name="Until Leading"),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(
    #     name="Until 2 Shotguns", minShotguns=2
    # ),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(
    #     name="Until 1 Shotgun", minShotguns=1
    # ),
    RandomContinueBot(name="Random Continue Bot"),
    StopAfterTwoBrains(name="Untill 2 brains"),
    StopAfterTwoShotguns(name="Untill 2 Shotguns"),
    RollFourButMaybeStop(name="Roll four but stop if 2 Shotguns"),
    StopAfterRollingMoreShotguns(
        name="Rolls untill there are more shotguns than brains"
    ),
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
