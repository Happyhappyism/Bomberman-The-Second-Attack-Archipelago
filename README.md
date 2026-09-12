# Bomberman 64 The Second Attack Archipelago

### 10/7/25
Archipelago v0.6.4 compatibility

## Setup Guide
### What you need
- [Bizhawk 2.9.1](https://tasvideos.org/Bizhawk/ReleaseHistory#Bizhawk291) (Use 2.9.1, version 2.10 does not work with AP)
- The latest bomberman_tsa.apworld provided in the latest release post


### Installation
Same as every other unsupported N64 apworld, 
- simply move bomberman_tsa.apworld into the custom_worlds directory in your Archipelago install server
(default path: C:\ProgramData\Archipelago\custom_worlds)
- or simply double click the apworld and it should install itself (Archipelago version 0.5.0 and later)

### Running
1. In the Archipelago launcher push the 'Generate Template Options' button to generate a yaml for your options
2. Like every other apworld, fill out your yaml options and have the host generate the multiworld, the produced zip file should contain a .apbomb64 patch file. Receive this .apbomb64 patch from the multiworld host.
3. Push the 'Open Patch' button in the launcher and it should ask for a 'Bomberman 64 (US)' legal ROM dump (MD5 Hash: aec1fdb0f1caad86c9f457989a4ce482), then select the generated  .apbomb64 patch file to produce a .z64 ROM which should auto launch in a bizhawk instance. You should be set otherwise from here just follow the same instructions as any other supported N64 apworld.

### Recomendations
- In Bizhawk change your graphics plugin (Config -> Core Setting -> For Consoles -> Mupen64Plus -> Video Plugins) to Rice


### Troubleshooting
- The windows 7 version of archipelago uses python 3.8 which will not work with this apworld.
- Make sure you are not using version 2.10 of Bizhawk

## What is Randomized

### Items
- Elemental Stones
- Stage Access
- Guardian Armor Pieces
- Pommy Transformations
- Stage Key Items

### Locations
- Boss Clears
- Generator Clears
- Custom Parts/Gurdian Armor
- Stage Key Items


## Features
- Shopsanity
- Powerupsanity (Bomb Kick, Power Gloves, Remote)
- Pommysanity (Each Pommy Transformation is a check)
- Deathlink
- Randomized Music/Sound Effects

## Known Issues
- Some custom part checks can be collected over and over (ex. Alcatraz)
- Shopsanity: Sandals, Sneakers, and Gold Boots can be bought over and over (by entering/exiting a world and returning to the shop)
- Shopsanity: Buying High Heels sends Neverland Guardian Armor check.
- Starting with Dark Stone can crash the game if you watch the tutorial long enough
- Effects shuffle can crash the game (but this is noted as unstable in the yaml so it's fine)
- Rom Adjuster: "Open Doors" despawns the Starlight elevator in the area with the limo, making that passage one-way

## Planned Features
- I'll get back to you on that

## Notes
### Big thanks to 
- SavageWizzrobe for their extensive testing and RAM Mapping, this likely would not have come together without their help
- Cedar from the [decomp server](<https://discord.gg/hpkAyZwF>) for their tireless work and documentation of the game
- Adeleine64DS for their initial logic document for the game
- Ikari for special art assets for the powerups (usable with the ROM adjuster)
- Usagi Tsuki for testing
- And of course Noa for their motivation, testing, ideas and overall hard work bringing this together with me. Also likely would not have come together without them.

a legal Bomberman 64 The Second Attack (US) legal dump is required to play this apworld
Hash: aec1fdb0f1caad86c9f457989a4ce482

### Links
- [Latest Apworld Release](<https://github.com/Happyhappyism/Archipelago/releases/tag/bombtsa_v0.1.1>)
