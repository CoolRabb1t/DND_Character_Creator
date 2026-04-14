import unittest

from models import Character, AbilityScores, Item, Ability
from score_methods import (
    create_score_method,
    StandardArrayMethod,
    DiceRollMethod,
    AutoByClassMethod,
)
from storage import ALL_CLASS, ALL_RACES


def make_scores():
    scores = AbilityScores()
    scores.assign_score("STR", 15)
    scores.assign_score("DEX", 14)
    scores.assign_score("CON", 13)
    scores.assign_score("INT", 12)
    scores.assign_score("WIS", 10)
    scores.assign_score("CHA", 8)
    scores.modifier()
    return scores


def make_inventory():
    return [Item("Backpack"), Item("Potion")]


def make_abilities():
    return [Ability("Attack"), Ability("Dodge")]


def make_hero():
    return Character(
        name="cool",
        race=ALL_RACES[0],
        dnd_class=ALL_CLASS[0],
        lvl=1,
        ability_scores=make_scores(),
        current_hp=None,
        hp_max=None,
        history="test history",
        inventory=make_inventory(),
        abilities=make_abilities()
    )


class TestCharacter(unittest.TestCase):

    # Checks that a character is created correctly with valid input data
    def test_character_creation(self):
        hero = make_hero()
        self.assertEqual(hero.name, "Cool")
        self.assertEqual(hero.lvl, 1)
        self.assertEqual(hero.history, "test history")
        self.assertEqual(len(hero.inventory), 2)
        self.assertEqual(len(hero.abilities), 2)

    # Checks that creating a character with an empty name raises ValueError
    def test_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            Character(
                name="",
                race=ALL_RACES[0],
                dnd_class=ALL_CLASS[0],
                lvl=1,
                ability_scores=make_scores(),
                current_hp=None,
                hp_max=None,
                history="",
                inventory=make_inventory(),
                abilities=make_abilities()
            )

    # Checks that an invalid level raises ValueError
    def test_invalid_level_raises_error(self):
        with self.assertRaises(ValueError):
            Character(
                name="Hero",
                race=ALL_RACES[0],
                dnd_class=ALL_CLASS[0],
                lvl=0,
                ability_scores=make_scores(),
                current_hp=None,
                hp_max=None,
                history="",
                inventory=make_inventory(),
                abilities=make_abilities()
            )

    # Checks that None history is converted into an empty string
    def test_history_none_becomes_empty_string(self):
        hero = Character(
            name="Hero",
            race=ALL_RACES[0],
            dnd_class=ALL_CLASS[0],
            lvl=1,
            ability_scores=make_scores(),
            current_hp=None,
            hp_max=None,
            history=None,
            inventory=make_inventory(),
            abilities=make_abilities()
        )
        self.assertEqual(hero.history, "")

    # Checks that None inventory becomes an empty list
    def test_inventory_none_becomes_empty_list(self):
        hero = Character(
            name="Hero",
            race=ALL_RACES[0],
            dnd_class=ALL_CLASS[0],
            lvl=1,
            ability_scores=make_scores(),
            current_hp=None,
            hp_max=None,
            history="test",
            inventory=None,
            abilities=make_abilities()
        )
        self.assertEqual(hero.inventory, [])

    # Checks that None abilities becomes an empty list
    def test_abilities_none_becomes_empty_list(self):
        hero = Character(
            name="Hero",
            race=ALL_RACES[0],
            dnd_class=ALL_CLASS[0],
            lvl=1,
            ability_scores=make_scores(),
            current_hp=None,
            hp_max=None,
            history="test",
            inventory=make_inventory(),
            abilities=None
        )
        self.assertEqual(hero.abilities, [])

    # Checks that healing correctly increases current HP
    def test_heal(self):
        hero = make_hero()
        old_hp = hero.current_hp
        hero.take_damage(2)
        hero.heal(1)
        self.assertEqual(hero.current_hp, old_hp - 1)

    # Checks that taking damage correctly decreases current HP
    def test_take_damage(self):
        hero = make_hero()
        old_hp = hero.current_hp
        hero.take_damage(1)
        self.assertEqual(hero.current_hp, old_hp - 1)

    # Checks that negative healing raises ValueError
    def test_negative_heal_raises_error(self):
        hero = make_hero()
        with self.assertRaises(ValueError):
            hero.heal(-1)

    # Checks that negative damage raises ValueError
    def test_negative_damage_raises_error(self):
        hero = make_hero()
        with self.assertRaises(ValueError):
            hero.take_damage(-1)

    # Checks that proficiency bonus is correct for level 1
    def test_proficiency_bonus(self):
        hero = make_hero()
        self.assertEqual(hero.proficiency_bonus, 2)

    # Checks that level up increases level and does not decrease HP
    def test_level_up(self):
        hero = make_hero()
        old_lvl = hero.lvl
        old_hp = hero.current_hp
        hero.lvl_up()
        self.assertEqual(hero.lvl, old_lvl + 1)
        self.assertGreaterEqual(hero.current_hp, old_hp)

    # Checks that add_item adds a valid Item object
    def test_add_item(self):
        hero = make_hero()
        hero.add_item(Item("Rope"))
        self.assertEqual(hero.inventory[-1].name, "Rope")

    # Checks that add_ability adds a valid Ability object
    def test_add_ability(self):
        hero = make_hero()
        hero.add_ability(Ability("Stealth"))
        self.assertEqual(hero.abilities[-1].name, "Stealth")


class TestAbilityScores(unittest.TestCase):

    # Checks that a valid score is assigned correctly
    def test_assign_score_valid(self):
        scores = AbilityScores()
        scores.assign_score("STR", 15)
        self.assertEqual(scores.scores["STR"], 15)

    # Checks that an invalid ability name raises ValueError
    def test_assign_score_invalid_name(self):
        scores = AbilityScores()
        with self.assertRaises(ValueError):
            scores.assign_score("POWER", 15)

    # Checks that a non-integer score raises TypeError
    def test_assign_score_invalid_type(self):
        scores = AbilityScores()
        with self.assertRaises(TypeError):
            scores.assign_score("STR", "15")

    # Checks that the modifier is calculated correctly
    def test_modifier(self):
        scores = AbilityScores()
        scores.assign_score("STR", 15)
        scores.modifier()
        self.assertEqual(scores.mod["STR"], 2)

    # Checks that dice roll result is always between 3 and 18
    def test_dice_roll_range(self):
        scores = AbilityScores()
        result = scores.dice_roll()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 18)

    # Checks that racial bonuses are applied correctly
    def test_race_bonus(self):
        scores = AbilityScores()
        scores.assign_score("STR", 10)
        race = ALL_RACES[0]
        original = scores.scores.copy()

        scores.race_bonus(race)

        changed = False
        for ability, bonus in race.ability_bonus.items():
            self.assertEqual(scores.scores[ability], original[ability] + bonus)
            changed = True

        self.assertTrue(changed)


class TestScoreMethods(unittest.TestCase):

    # Checks that the factory returns StandardArrayMethod
    def test_create_standard_array_method(self):
        method = create_score_method("Standard Array")
        self.assertIsInstance(method, StandardArrayMethod)

    # Checks that the factory returns DiceRollMethod
    def test_create_dice_roll_method(self):
        method = create_score_method("Dice Roll")
        self.assertIsInstance(method, DiceRollMethod)

    # Checks that the factory returns AutoByClassMethod
    def test_create_auto_by_class_method(self):
        method = create_score_method("Auto By Class")
        self.assertIsInstance(method, AutoByClassMethod)

    # Checks that an invalid method name returns None
    def test_create_invalid_method(self):
        method = create_score_method("Wrong Method")
        self.assertIsNone(method)

    # Checks that StandardArrayMethod returns the correct fixed array
    def test_standard_array_generate(self):
        scores = AbilityScores()
        method = StandardArrayMethod()
        array = method.generate(scores, ALL_CLASS[0])
        self.assertEqual(array, [15, 14, 13, 12, 10, 8])

    # Checks that DiceRollMethod returns 6 values in the valid range
    def test_dice_roll_generate(self):
        scores = AbilityScores()
        method = DiceRollMethod()
        array = method.generate(scores, ALL_CLASS[0])
        self.assertEqual(len(array), 6)
        for value in array:
            self.assertGreaterEqual(value, 3)
            self.assertLessEqual(value, 18)

    # Checks that AutoByClassMethod assigns scores by class priority
    def test_auto_by_class_generate(self):
        scores = AbilityScores()
        method = AutoByClassMethod()
        chosen_class = ALL_CLASS[0]
        result = method.generate(scores, chosen_class)

        self.assertIsNone(result)
        self.assertEqual(scores.scores[chosen_class.abilities_prior[0]], 15)
        self.assertEqual(scores.scores[chosen_class.abilities_prior[1]], 14)


if __name__ == "__main__":
    unittest.main()