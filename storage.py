import pandas as pd
from models import DndClass, Race
try:
    df_classes = pd.read_excel("game_data.xlsx", sheet_name = "CLASS" )
except Exception as e:
    print("Something went wrong:", e)
    raise

ALL_CLASS = []
for _, row in df_classes.iterrows():
    prior = []
    for x in row["abilities_prior"].split(","):
        prior.append(x.strip())
    ALL_CLASS.append(DndClass(key = row["key"],
                        display_name = row["display_name"],
                        description = row["description"],
                        role = row["role"],
                        difficulty = row["difficulty"],
                        abilities_prior = prior,
                        hit_die = row["hit_die"]
                        ))

def parse_ability_bonus(text):
    result = {}
    parts = str(text).split(",")
    for part in parts:
        key,value = part.split(":")
        result[key.strip()] = int(value.strip())
    return result
      
ALL_RACES = []

try:
    df_races = pd.read_excel("game_data.xlsx", sheet_name = "RACE" )
except Exception as e:
    print("Something went wrong:", e)
    raise

for _, row in df_races.iterrows(): #man nereikalingas _ - index 
    ALL_RACES.append(Race(key = row["key"],
                          display_name = row["display_name"],
                          description = row["description"],
                          ability_bonus = parse_ability_bonus(row["ability_bonus"])))

def save_hero(hero):
    data = [{
        "name" : hero.name,
        "display_name_race" : hero.race.display_name,
        "display_name_class" : hero.dnd_class.display_name,
        "lvl" : hero.lvl,
        "hp_max" : hero.hp_max,
        "current_hp" : hero.current_hp,
        "ac" : hero.ac,
        "proficiency_bonus" : hero.proficiency_bonus,
        "STR" : hero.ability_scores.scores["STR"],
        "DEX" : hero.ability_scores.scores["DEX"],
        "CON" : hero.ability_scores.scores["CON"],
        "INT" : hero.ability_scores.scores["INT"],
        "WIS" : hero.ability_scores.scores["WIS"],
        "CHA" : hero.ability_scores.scores["CHA"],
        "history" : hero.history,
    }]
    df_hero = pd.DataFrame(data)
    with pd.ExcelWriter("game_data.xlsx", 
                        engine= "openpyxl", mode = "a", 
                        if_sheet_exists="replace") as writer: df_hero.to_excel(writer, 
                                                                               sheet_name = "HERO", 
                                                                               index = False)