from django.db import models


class FlavourChoices(models.TextChoices):
    VANILLA = ("vanilla", "Vanilla")
    CHOCOLATE = ("chocolate", "Chocolate")
    STRAWBERRY = ("strawberry", "Strawberry")
    CHERRY = ("cherry", "Cherry")
    COFFEE = ("coffee", "Coffee")


class FrostingTypeChoices(models.TextChoices):
    BUTTERCREAM = ("buttercream", "Buttercream")
    CREAM_CHEESE = ("cream_cheese", "Cream cheese")
    FONDANT = ("fondant", "Fondant")


class Cake(models.Model):
    name = models.CharField(max_length=200)
    sponge_flavour = models.CharField(choices=FlavourChoices.choices, max_length=20)
    frosting_flavour = models.CharField(choices=FlavourChoices.choices, max_length=20)
    frosting_type = models.CharField(choices=FrostingTypeChoices.choices, max_length=20)
