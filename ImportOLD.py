import sqlite3
import sys
import xml.etree.ElementTree as ET

# Incoming Pokemon MUST be in this format
#
# <pokemon pokedex="" classification="" generation="">
#     <name>...</name>
#     <hp>...</name>
#     <type>...</type>
#     <type>...</type>
#     <attack>...</attack>
#     <defense>...</defense>
#     <speed>...</speed>
#     <sp_attack>...</sp_attack>
#     <sp_defense>...</sp_defense>
#     <height><m>...</m></height>
#     <weight><kg>...</kg></weight>
#     <abilities>
#         <ability />
#     </abilities>
# </pokemon>

# connect to pokemon sqlite 
conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()

# Read pokemon XML file name from command-line
# (Currently this code does nothing; your job is to fix that!)
if len(sys.argv) < 2:
    print("You must pass at least one XML file name containing Pokemon to insert")

for i, arg in enumerate(sys.argv):
    # Skip if this is the Python filename (argv[0])
    if i == 0:
        continue

# parse XML file
tree = ET.parse(arg)
root = tree.getroot()

# iterate through each pokemon in XML file
for pokemon in root.findall('pokemon'):
    # extract relevant data from the pokemon
    name = pokemon.find('name').text
    pokedex = pokemon.attrib['pokedex']
    classification = pokemon.attrib['classification']
    generation = pokemon.attrib['generation']
    hp = pokemon.find('hp').text
    attack = pokemon.find('attack').text
    defense = pokemon.find('defense').text
    speed = pokemon.find('speed').text
    sp_attack = pokemon.find('sp_attack').text
    sp_defense = pokemon.find('sp_defense').text
    height = pokemon.find('height/m').text
    weight = pokemon.find('weight/kg').text

    # Insert the Pokemon into the database
    c.execute("INSERT INTO pokemon VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (name, pokedex, classification, generation, hp, attack, defense, speed, sp_attack, sp_defense, height, weight))

# commit changes and close database connection
conn.commit()
conn.close()
