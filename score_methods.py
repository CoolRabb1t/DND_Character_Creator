class ScoreGenerationMethod:
    def generate(self, scores, chosen_class):
        raise NotImplementedError("This method must be overridden")

class StandardArrayMethod(ScoreGenerationMethod):
    def generate(self, scores, chosen_class):
        array = [15, 14, 13, 12, 10, 8]
        return array
    
class DiceRollMethod(ScoreGenerationMethod):
    def generate(self, scores, chosen_class):
        array = [scores.dice_roll() for i in range(0,6)]
        return array
    
class AutoByClassMethod(ScoreGenerationMethod):
    def generate(self, scores, chosen_class):
        scores.auto_by_class(chosen_class)
        return None
    
def create_score_method(type_of_method):
    if type_of_method == "Standard Array":
        return StandardArrayMethod()
    elif type_of_method == "Dice Roll":
        return DiceRollMethod()
    elif type_of_method == "Auto By Class":
        return AutoByClassMethod()
    else:
        return None
    
