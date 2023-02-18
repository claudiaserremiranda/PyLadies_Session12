class BoardGame():
    def __init__(self, name, play_time, min_players, max_players, from_age):
        self.name = name
        self.play_time = play_time
        self.min_players = min_players
        self.max_players = max_players
        self.from_age = from_age
        self.num_times_played = 0

    def __str__(self):
        return """
        The Board Game is called '{}' and has an avegare duration of {} minutes.
        It can be played with {} to {} players.
        Minimum age advised is {} years old.
        """.format(self.name, self.play_time, self.min_players, self.max_players, self.from_age)

    def play(self, num_people, duration, min_age):
        
        if num_people >= self.min_players and num_people <= self.max_players and min_age >= self.from_age and duration >= (self.play_time - 10) and duration <= (self.play_time + 10):
            self.num_times_played += 1
            print("The '{}' is perfect for you. You will have lots of fun! This is the {} time you have played this game.". format(self.name, self.num_times_played))
            return True

        if num_people < self.min_players:
            print("You can't play this game. You need at least {} players".format(self.min_players))
            return False
        elif num_people > self.max_players:
            print("You can't all play this game at the same time. Max {} players allowed".format(self.max_players))
            return False

        if duration < (self.play_time - 10):
            print("This game might be to short for your expectations! Average duration is {} minutes. Try a different one!".format(self.play_time))
            return False
        elif duration > (self.play_time + 10):
            print("This game might take longer than you expect! Average duration is {} minutes. If you have time, go for it!".format(self.play_time))
            return False

        if min_age < self.from_age:
            print("This game is not adequate for your age. You should be older than {} years old.".format(self.from_age))
            return False
        

class Wargame(BoardGame):
    def __init__(self, name, play_time, min_players, max_players, from_age, violence):
        super().__init__(name, play_time, min_players, max_players, from_age)
        self.violence = violence
        

    def play(self, num_people, duration, min_age):
        if super().play(num_people, duration, min_age):
            if self.violence == "low":
                print("This Wargame is really chilled!")
            elif self.violence == "medium":
                print("This Wargame is neither violent nor not ideal for sensible souls!")
            if self.violence == "high":
                print("This game is extremelly violente! Not the cup of tee of everyone!")


class EuroGame(BoardGame):
    def __init__(self, name, play_time, min_players, max_players, from_age, figures_material):
        super().__init__(name, play_time, min_players, max_players, from_age)
        self.figures_material = figures_material
        

    def campfire_allowed(self):
        materials = ["cardboard", "wood", "plastic", "metal"]

        if self.figures_material not in materials:
            raise ValueError("Please enter a valid figures material: cardboard, wood, plastic or metal")
        elif self.figures_material == "metal":
            print ("You can safely play this board game next to a campfire.")
        else:
            print ("This board game should not be played next to a campfire.")  