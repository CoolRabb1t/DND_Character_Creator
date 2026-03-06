import random
class Character:

    def __init__(self, name, race, dnd_class, ability_scores):
        self.name = name
        self.race = race
        self.dnd_class = dnd_class
        self.ability_scores = ability_scores
        self._lvl = 1

    @property
    def name(self):
       return self._name
   
    @name.setter
    def name(self,value):
       value = str(value).strip()
       if not value:
          raise ValueError("Name can not be empty")
       self._name = value.title()

    @property
    def lvl(self):
       return self._lvl
   
    @lvl.setter
    def lvl(self,value):
       if not isinstance(value, int):
          raise TypeError("LVL must be number")
       if not  1 <= value <= 20:
          raise ValueError("Lvl must be between 1 and 20")
       self._lvl = value
   
    def lvl_up(self):
       if self._lvl < 20:
          self._lvl = self._lvl + 1
       else: 
          raise ValueError("LVL is already 20")
      
    @property
    def proficiency_bonus(self):
       return 2 + (self._lvl - 1) // 4
      

class AbilityScores:

     def __init__(self):
       self._scores = {
         "STR": 0,
         "DEX": 0,
         "CON": 0,
         "INT": 0,
         "WIS": 0,
         "CHA": 0
       }
       self._mod = {
         "STR": 0,
         "DEX": 0,
         "CON": 0,
         "INT": 0,
         "WIS": 0,
         "CHA": 0
       } 
    
     def standard_array(self):
        array = [15, 14, 13, 12, 10, 8]
        abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for i in array:
            print("Available:", abilities)
            while True:
               value = input(f"For what characteristic {i}").upper()
               if value in abilities:
                  self._scores[value] = i
                  abilities.remove(value)
                  break
               else:
                  print("MUST BE FROM AVAILABLE!")

     def dice_roll(self):
        dices = []
        for i in range(4):
           dice = random.randint(1,6)
           dices.append(dice)
        dices.remove(min(dices))
        return sum(dices)
     
     def dice_roll_method(self):
        dice_rolls = []
        for i in range(6):
           dice_rolls.append(self.dice_roll())
        abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for i in dice_rolls:
            print("Available:", abilities)
            while True:
               value = input(f"For what characteristic {i}").upper()
               if value in abilities:
                  self._scores[value] = i
                  abilities.remove(value)
                  break
               else:
                  print("MUST BE FROM AVAILABLE!")

     def auto_by_class(self,chosen_class):
        array = [15, 14, 13, 12, 10, 8]
        for i in range(6):
           self._scores[chosen_class.abilities_prior[i]] = array[i]
     def race_bonus(self,chosen_race):
        for i in chosen_race.ability_bonus:
           self._scores[i] += chosen_race.ability_bonus[i]
           
     def modifier(self):
        for i in self._mod:
           self._mod[i] = (self._scores[i] - 10) // 2
     
     def choose_score_generation_method(self,chosen_class):
        while True:
            try:
                value = int(input("What way do you want to choose?\n"
            "1 - Standard Array\n"
            "2 - Dice Roll\n"
            "3 - Auto\n"))
            except ValueError:
               print("Must be a number")
               continue
            if value not in [1,2,3]:
               print("Choose one way from available")
            elif value == 1:
               self.standard_array()
               break
            elif value == 2:
               self.dice_roll_method()
               break
            elif value == 3:
               self.auto_by_class(chosen_class)
               break

            
class DndClass():
   
     def __init__ (self, key, display_name, description, role, difficulty,abilities_prior):
       self._key = key
       self._display_name = display_name
       self._description = description
       self._role = role
       self._difficulty = difficulty
       self._abilities_prior = abilities_prior
     

FIGHTER = DndClass(
    key="fighter",
    display_name="Fighter (Воин)",
    description="Универсальный боец. Хорошо носит броню, устойчив и стабилен.",
    role="Frontline / Damage / Tank",
    difficulty="Easy",
    abilities_prior = ["STR", "CON", "DEX", "WIS", "CHA", "INT"]

)

ROGUE = DndClass(
    key="rogue",
    display_name="Rogue (Плут)",
    description="Ловкий, скрытный и хитрый. Силен в навыках и внезапных атаках.",
    role="Damage / Skill Expert",
    difficulty="Medium",
    abilities_prior = ["DEX", "CON", "WIS", "INT", "CHA", "STR"]
)

WIZARD = DndClass(
    key="wizard",
    display_name="Wizard (Волшебник)",
    description="Мастер магии с огромным выбором заклинаний.",
    role="Control / Utility / Damage",
    difficulty="Hard",
    abilities_prior = ["INT", "CON", "DEX", "WIS", "CHA", "STR"]
)

CLERIC = DndClass(
    key="cleric",
    display_name="Cleric (Жрец)",
    description="Божественный заклинатель. Может лечить, защищать и наносить урон.",
    role="Support / Healer / Tank",
    difficulty="Medium",
    abilities_prior = ["WIS", "CON", "STR", "DEX", "CHA", "INT"]
)

DRUID = DndClass(
    key="druid",
    display_name="Druid (Друид)",
    description="Повелитель природы. Может превращаться в животных.",
    role="Control / Support / Utility",
    difficulty="Medium",
    abilities_prior = ["WIS", "CON", "DEX", "INT", "CHA", "STR"]
)

BARD = DndClass(
    key="bard",
    display_name="Bard (Бард)",
    description="Музыкант и вдохновитель. Универсален и харизматичен.",
    role="Support / Control / Social",
    difficulty="Medium",
    abilities_prior = ["CHA", "DEX", "CON", "WIS", "INT", "STR"]
)

WARLOCK = DndClass(
    key="warlock",
    display_name="Warlock (Колдун)",
    description="Заключил договор с могущественным существом.",
    role="Damage / Utility",
    difficulty="Medium",
    abilities_prior = ["CHA", "CON", "DEX", "WIS", "INT", "STR"] 
)

PALADIN = DndClass(
    key="paladin",
    display_name="Paladin (Паладин)",
    description="Святой воин. Сочетает броню, урон и поддержку.",
    role="Tank / Damage / Support",
    difficulty="Easy",
    abilities_prior = ["STR", "CHA", "CON", "WIS", "DEX", "INT"]
)

SORCERER = DndClass(
    key="sorcerer",
    display_name="Sorcerer (Чародей)",
    description="Магия течёт в его крови. Гибкость заклинаний через метамагию.",
    role="Damage / Control",
    difficulty="Hard",
    abilities_prior = ["CHA", "CON", "DEX", "WIS", "INT", "STR"]
)

RANGER = DndClass(
    key="ranger",
    display_name="Ranger (Следопыт)",
    description="Охотник и мастер выживания.",
    role="Damage / Utility",
    difficulty="Medium",
    abilities_prior = ["DEX", "WIS", "CON", "STR", "INT", "CHA"]
)

BARBARIAN = DndClass(
    key="barbarian",
    display_name="Barbarian (Варвар)",
    description="Яростный воин с огромной живучестью.",
    role="Tank / Damage",
    difficulty="Easy",
    abilities_prior = ["STR", "CON", "DEX", "WIS", "CHA", "INT"]
)

MONK = DndClass(
    key="monk",
    display_name="Monk (Монах)",
    description="Боец без брони. Быстр, мобильный и техничный.",
    role="Mobile Damage",
    difficulty="Hard",
    abilities_prior = ["DEX", "WIS", "CON", "STR", "INT", "CHA"]
)

ALL_CLASS = [FIGHTER, MONK, BARBARIAN, BARD, PALADIN, ROGUE, RANGER, SORCERER, WARLOCK, DRUID, CLERIC, WIZARD]


class Race:
   def __init__(self, key, display_name, description, ability_bonus):
       self._key = key
       self._display_name = display_name
       self._description = description
       self._ability_bonus = ability_bonus  # dict {"STR":2, "CON":1}
        

HUMAN = Race(
    key="human",
    display_name="Human (Человек)",
    description="Универсальная и гибкая раса. Подходит для любого класса и стиля игры. Хороший выбор для новичков.",
    ability_bonus={"STR":1, "DEX":1, "CON":1, "INT":1, "WIS":1, "CHA":1}
)

ELF = Race(
    key="elf",
    display_name="Elf (Эльф)",
    description="Ловкие и внимательные. Отличный выбор для лучников, магов и скрытных персонажей.",
    ability_bonus={"DEX":2}
)

DWARF = Race(
    key="dwarf",
    display_name="Dwarf (Дварф)",
    description="Крепкие и выносливые. Хорошо подходят для ближнего боя и роли стойкого защитника.",
    ability_bonus={"CON":2}
)

HALFLING = Race(
    key="halfling",
    display_name="Halfling (Халфлинг)",
    description="Маленькие, быстрые и удачливые. Отличный выбор для скрытных и ловких персонажей.",
    ability_bonus={"DEX":2}
)

TIEFLING = Race(
    key="tiefling",
    display_name="Tiefling (Тифлинг)",
    description="Харизматичные и склонные к магии. Часто выбираются для заклинателей и социально активных персонажей.",
    ability_bonus={"CHA":2, "INT":1}
)

HALF_ORC = Race(
    key="half_orc",
    display_name="Half-Orc (Полуорк)",
    description="Сильные и живучие. Подходят для варваров и воинов, ориентированных на урон.",
    ability_bonus={"STR":2, "CON":1}
)

GNOME = Race(
    key="gnome",
    display_name="Gnome (Гном)",
    description="Любознательные и сообразительные. Хорошо подходят для магов и изобретателей.",
    ability_bonus={"INT":2}
)

DRAGONBORN = Race(
    key="dragonborn",
    display_name="Dragonborn (Драконорожденный)",
    description="Гордые воины с драконьей силой. Хороший выбор для харизматичных бойцов.",
    ability_bonus={"STR":2, "CHA":1}
)

HALF_ELF = Race(
    key="half_elf",
    display_name="Half-Elf (Полуэльф)",
    description="Гибкие и социально одарённые. Универсальный выбор для персонажей с высоким влиянием.",
    ability_bonus={"CHA":2}
)


ALL_RACES = [ HUMAN, ELF, DWARF, HALFLING, TIEFLING, HALF_ORC, GNOME, DRAGONBORN, HALF_ELF ]

def choose_from_list(options, title):
   i=1
   print (f"All {title}:")
   for variants in options:
      print(f"{i}. {variants._display_name}")
      i += 1
   while True:
       try:
          value = int(input(f"Choose your options: "))
       except ValueError:
          print("Must be a number")
          continue
       if 1 <= value <= len(options):
          return options[value-1]
       else:
          print(f"Must be one of the options")
def character_creator():
   name = input("Enter character name:")
   chosen_class = choose_from_list(ALL_CLASS, "classes")
   scores = AbilityScores()
   chosen_race = choose_from_list(ALL_RACES, "races")
   scores.choose_score_generation_method()
   scores.race_bonus(chosen_race)
   hero = Character(name, chosen_race, chosen_class, scores)

      