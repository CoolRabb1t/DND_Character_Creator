import random
class Character:

    def __init__(self, name, race, dnd_class, lvl, 
                 ability_scores, history = None, current_hp = None, hp_max = None, inventory = None, abilities = None):
        self.name = name
        self.race = race
        self.dnd_class = dnd_class
        self.ability_scores = ability_scores
        self.lvl = lvl
        self.history = history
        self.inventory = inventory
        self.abilities = abilities
        if hp_max is None:
            self._hp_max = dnd_class.hit_die + ability_scores.mod['CON']
        else:
            self.hp_max = hp_max
        if current_hp is None:
            self.current_hp = self.hp_max
        else:
            self.current_hp = current_hp

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        if value is None:
            self._inventory = []
            return
        if not isinstance(value, list):
            raise TypeError("Inventory must be a list")
        for item in value:
            if not isinstance(item, Item):
                raise TypeError("All inventory elements must be Item objects")
        self._inventory = value
        
    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, value):
        if value is None:
            self._abilities = []
            return
        if not isinstance(value, list):
            raise TypeError("Abilities must be a list")
        for ability in value:
            if not isinstance(ability, Ability):
                raise TypeError("All abilities elements must be Ability objects")
        self._abilities = value
        
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
            gain = self.roll_hp_gain()
            gain = gain + self.ability_scores.mod["CON"]
            self.hp_max = self.hp_max + gain
            self.current_hp = self.current_hp + gain
        else: 
            raise ValueError("LVL is already 20")
      
    @property
    def proficiency_bonus(self):
        return 2 + (self._lvl - 1) // 4
    
    @property
    def hp_max(self):
        return self._hp_max
    
    @hp_max.setter
    def hp_max(self, value):
        if not isinstance(value, int):
            raise TypeError("HP must be a number")
        if value <= 0:
            raise ValueError("HP max must be greater than 0")
        self._hp_max = value
        
    @property
    def ac(self):
        return 10 + self.ability_scores.mod['DEX']
    
    @property
    def current_hp(self):
        return self._current_hp
    
    @property
    def history(self):
        return self._history
    
    @history.setter
    def history(self, story):
        if story is None:
            self._history = ""
        else: 
            self._history = str(story).strip()


    @current_hp.setter
    def current_hp(self, value):
        if not isinstance(value, int):
            raise TypeError("HP must be a number")
        elif value > self._hp_max:
            raise ValueError("Curent HP can not be more than HP max")
        elif value < 0:
            raise ValueError("Curent HP can not be negative")
        self._current_hp = value
    
    def roll_hp_gain(self):
        return random.randint(1, self.dnd_class.hit_die)
    
    def take_damage(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer")
        if amount < 0:
            raise ValueError("Can not be negative")
        self.current_hp -= amount
 
    def heal(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer")
        if amount < 0:
            raise ValueError("Can not be negative")
        self.current_hp += amount
    
    def add_item(self, item):
        if not isinstance(item, Item):
            raise TypeError("Inventory object must be Item")
        self.inventory.append(item)

    def add_ability(self, ability):
        if not isinstance(ability, Ability):
            raise TypeError("Ability object must be Ability")
        self.abilities.append(ability)

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
    
    @property
    def scores(self):
        return self._scores
    
    @property
    def mod(self):
        return self._mod
    
    def assign_score(self, ability, score):
        allowed = {"STR", "DEX", "CON", "INT", "WIS", "CHA"}
        if ability not in allowed:
            raise ValueError("Invalid ability name")
        if not isinstance(score, int):
            raise TypeError("Score must be an integer")
        if score < 0:
            raise ValueError("Score can not be negative")
        self._scores[ability] = score 
    
    def dice_roll(self):
        dices = []
        for i in range(4):
            dice = random.randint(1,6)
            dices.append(dice)
        dices.remove(min(dices))
        return sum(dices)
     
    def auto_by_class(self,chosen_class):
        array = [15, 14, 13, 12, 10, 8]
        for i in range(6):
            self.scores[chosen_class.abilities_prior[i]] = array[i]
    def race_bonus(self,chosen_race):
        for i in chosen_race.ability_bonus:
            self.scores[i] += chosen_race.ability_bonus[i]
     
    def modifier(self):
        abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for i in abilities:
            self.mod[i] = (self.scores[i] - 10) // 2


class DndClass:
   
    def __init__ (self, key, display_name, description, role, difficulty, abilities_prior, hit_die):
        self._key = key
        self._display_name = display_name
        self._description = description
        self._role = role
        self._difficulty = difficulty
        self._abilities_prior = abilities_prior
        self._hit_die = hit_die

    @property
    def abilities_prior(self):
        return self._abilities_prior
    
    @property
    def display_name(self):
        return self._display_name
    
    @property
    def hit_die(self):
        return self._hit_die
        
    @property
    def description(self):
        return self._description
    
    @property
    def role(self):
        return self._role
    
    @property
    def difficulty(self):
        return self._difficulty
    
class Race:
    def __init__(self, key, display_name, description, ability_bonus):
        self._key = key
        self._display_name = display_name
        self._description = description
        self._ability_bonus = ability_bonus  # dict {"STR":2, "CON":1}

    @property
    def ability_bonus(self):
        return self._ability_bonus
    
    @property
    def display_name(self): 
        return self._display_name
    
    @property
    def description(self):
        return self._description
    
class Item:
    def __init__(self, name, description=""):
        self.name = str(name).strip()
        self.description = str(description).strip()
        if not self.name:
            raise ValueError("Item name can not be empty")
        
class Ability:
    def __init__(self, name, description=""):
        self.name = str(name).strip()
        self.description = str(description).strip()
        if not self.name:
            raise ValueError("Ability name can not be empty")
