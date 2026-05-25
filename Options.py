from dataclasses import dataclass
from Options import Choice, Range, Toggle, OptionGroup, DefaultOnToggle, Removed, PerGameCommonOptions, StartInventoryPool, DeathLink

class Goal(Choice):
    """
    Required Goal to complete the seed
    Noah - Clear the game by defeating the final boss, determined by the final boss option
    Generators - Clear the game by clearing a certain number of planets
    Stone Hunt - Clear the game by collecting all of the Elemental Stones.
    """
    #display_name = "Goal"
    option_noah = 0
    option_generators = 1
    option_stones = 2
    default = 0

class NoahAccess(Choice):
    """
    Requirement to access Warship Noah, the game's final dungeon
    Generators - Open up Noah by clearing a certain number of planets
    Warship Keys - Open Noah by collecting 3 Warship Keys from the item pool
    Coordinates -  Opens Noah by collecting the coordinates to Noah from the item pool
    """
    option_generators = 0
    option_keys = 1
    option_coord = 2
    default = 0

class BossGoal(Choice):
    """Determines which final boss should be fought at Noah to complete the game"""
    option_sthertoth = 0
    option_lilith = 1
    option_angel = 2
    default = 0

class RequiredPlanets(Range):
    """Number of generators which need to be destroyed to access Noah or Clear the game depending on other options"""
    display_name = "Required Generators"
    range_start = 1
    range_end = 7
    default = 5
    
class StartingElement(Choice):
    """Determines your starting bomb element"""
    option_fire = 0
    option_ice = 1
    option_wind = 2
    option_earth = 3
    option_lightning = 4
    option_light = 5
    option_dark = 6
    option_random_element = 7
    default = 7

class StartingPlanets(Range):
    """Number of random planets you can visit from the start, you can always visit Alcatraz, Noah will not be included."""
    display_name = "Starting Planets"
    range_start = 1
    range_end = 7
    default = 2

class IncludeKeys(Toggle):
    """If enabled will add 3 Warship Key items into the item pool which each will autocomplete sections of Warship Noah
    but are not necessary to progress, this option will always be set if keys are set to open Warship Noah"""

class IncludeTraps(DefaultOnToggle):
    """If enabled will add negative traps to the item pool"""

class ReduceFood(Toggle):
    """Reduces how much food is required to get Pommy's evolution checks"""

class Shopsanity(Toggle):
    """Adds shop locations into the location pool. Shop hint items are not included"""

class Pommysanity(Toggle):
    """Adds pommy transformation locations into the location pool"""

class PommyShop(Toggle):
    """When Shopsanity is enabled, this will place Pommy Gene transformation items onto certain shop locations"""

class PowerupSanity(Toggle):
    """When enabled will include Power Glove and Bomb Kick items as checks"""

class RandomMusic(Toggle):
    """Randomizes the music table every time the client is loaded"""
class RandomSound(Toggle):
    """Randomizes the Sound Effect table every time the client is loaded"""

class RandomEffect(Toggle):
    """Randomizes the Animated Effects, likely pretty unstable for now"""

class IconShuffle(Toggle):
    """When enabled will shuffle powerup icons"""

class Character(Choice):
    """Determines the base character model"""
    option_bomberman = "17e.bin"
    option_lilith = "6b9.bin"
    option_baelfael = "560.bin"
    option_behemos = "561.bin"
    option_ashtarth = "562.bin"
    option_zhael = "563.bin"
    option_molok = "564.bin"
    option_zoniha = "589.bin"
    option_bulzeeb = "591.bin"
    option_monkey = "5eb.bin"
    option_platypus = "5ec.bin"
    option_fox = "5ed.bin"
    option_party_girl = "5ee.bin"
    option_humanoid_girl = "5ef.bin"
    option_panda = "5f0.bin"
    option_wolf = "5f1.bin"
    option_bunny = "5f2.bin"
    option_bull = "5f3.bin"
    option_sword_boy = "5f4.bin"
    option_young_maid = "5f5.bin"
    option_viking = "5f6.bin"
    option_reaper = "5f7.bin"
    option_witch = "5f8.bin"
    option_knight = "5f9.bin"
    option_red_king = "5fa.bin"
    option_green_king = "5fb.bin"
    option_mini_bomber = "542.bin"
    option_random = "Random"
    default = "17e.bin"

class GuardianHelmet(Choice):
    """Determine what model will be used to replace the guardian helmet"""
    option_guardian_helmet =  "3e7.bin"
    option_full_helmet = "3eb.bin"
    option_plate = "3ef.bin"
    option_helmet = "3f3.bin"
    option_pointed_hat =  "3f7.bin"
    option_robot_head =  "3fb.bin"
    option_cat_ears =  "3ff.bin"
    option_mohawk = "403.bin"
    option_cowboy_hat = "407.bin"
    option_topknot = "40b.bin"
    option_beret = "40f.bin"
    option_beard = "413.bin"
    option_headgear = "417.bin"
    option_gold_helmet = "41b.bin"
    option_ribbon = "41f.bin"
    option_bald_head = "423.bin"
    option_rabbit_ears = "427.bin"
    option_none = "None"
    option_random = "Random"
    default = "3e7.bin"

class GuardianVest(Choice):
    """Determine what model will be used to replace the guardian vest"""
    option_guardian_vest = "3e8.bin"
    option_warriors_armor = "3ec.bin"
    option_frog_suit = "3f0.bin"
    option_biker_suit = "3f4.bin"
    option_clown_suit = "3f8.bin"
    option_robot_suit = "3fc.bin"
    option_cat_suit = "400.bin"
    option_leather_jacket = "404.bin"
    option_cowboy_vest = "408.bin"
    option_kimono = "40c.bin"
    option_artists_smock = "410.bin"
    option_tank_body = "414.bin"
    option_elephant_suit = "418.bin"
    option_gold_suit = "41c.bin"
    option_pink_dress = "420.bin"
    option_apron = "424.bin"
    option_duck_suit = "428.bin"
    option_none = "None"
    option_random = "Random"
    default = "3e8.bin"

class GuardianArm(Choice):
    """Determine what model will be used to replace the guardian arms"""
    option_guardian_gloves =  "3e9.bin"
    option_gauntlet  =  "3ed.bin"
    option_webbed_gloves =  "3f1.bin"
    option_leather_gloves =  "3f5.bin"
    option_white_gloves =  "3f9.bin"
    option_robot_arm =  "3fd.bin"
    option_cat_gloves =  "401.bin"
    option_brass_knuckles = "405.bin"
    option_cowboy_gloves = "409.bin"
    option_sword = "40d.bin"
    option_paint_set = "411.bin"
    option_fan = "415.bin"
    option_gloves = "419.bin"
    option_gold_gloves = "41d.bin"
    option_slash_claws = "421.bin"
    option_hand_puppets = "425.bin"
    option_drill = "429.bin"
    option_none = "None"
    option_random = "Random"
    default = "3e9.bin"

class GuardianLeg(Choice):
    """Determine what model will be used to replace the guardian boots"""
    option_guardian_boots =  "3ea.bin"
    option_armored_boots =  "3ee.bin"
    option_frog_feet =  "3f2.bin"
    option_leather_boots =  "3f6.bin"
    option_clown_shoes =  "3fa.bin"
    option_robot_boots =  "3fe.bin"
    option_cat_slippers =  "402.bin"
    option_boots = "406.bin"
    option_cowboy_boots = "40a.bin"
    option_sandals = "40e.bin"
    option_slippers = "412.bin"
    option_bigfoot_shoes = "416.bin"
    option_kung_fu_shoes = "41a.bin"
    option_gold_boots = "41e.bin"
    option_high_heels = "422.bin"
    option_pommy_slippers = "426.bin"
    option_sneakers = "42a.bin"
    option_none = "None"
    option_random = "Random"
    default = "3ea.bin"

bomberman_tsa_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
        NoahAccess,
        RequiredPlanets,
        BossGoal,
        IncludeKeys,
    ]),
    OptionGroup("Gameplay Options", [
        StartingElement,
        StartingPlanets,
        ReduceFood,
        PowerupSanity,
        Shopsanity,
        Pommysanity,
        PommyShop,
        IncludeTraps,
        DeathLink,
    ]),
    OptionGroup("Randomization Options", [
        RandomMusic,
        RandomSound,
        RandomEffect,

    ]),
    OptionGroup("ROM Adjustments", [
        Character,
        GuardianHelmet,
        GuardianVest,
        GuardianArm,
        GuardianLeg,
    ]),
]

@dataclass
class BombTSAOptions(PerGameCommonOptions):
    game_goal: Goal
    noah_open : NoahAccess
    planet_required: RequiredPlanets
    noah_boss: BossGoal
    start_element: StartingElement
    start_planet: StartingPlanets
    death_link: DeathLink
    random_music: RandomMusic
    random_sound: RandomSound
    random_efx: RandomEffect
    reduce_food: ReduceFood
    pommysanity: Pommysanity
    shopsanity: Shopsanity
    powersanity: PowerupSanity
    pommyshop: PommyShop
    include_traps: IncludeTraps
    include_warkeys: IncludeKeys
    chara_model: Character
    guardian_helmet: GuardianHelmet
    guardian_vest: GuardianVest
    guardian_arms: GuardianArm
    guardian_legs: GuardianLeg