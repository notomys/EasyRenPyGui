## Game variables ##############################################################
##
## Developer customization entrypoint for the Info screen.
## Edit this file to add/remove rows and tweak starting values.


## Skills ######################################################################
##
## Add/remove entries here to change which skills are shown by default.

define info_skills = (
    {
        "label": _("Strength"),
        "current_var": "strength_current",
        "max_var": "strength_max",
    },
    {
        "label": _("Agility"),
        "current_var": "agility_current",
        "max_var": "agility_max",
    },
    {
        "label": _("Intellect"),
        "current_var": "intellect_current",
        "max_var": "intellect_max",
    },
    {
        "label": _("Charisma"),
        "current_var": "charisma_current",
        "max_var": "charisma_max",
    },
    {
        "label": _("Endurance"),
        "current_var": "endurance_current",
        "max_var": "endurance_max",
    },
    {
        "label": _("Luck"),
        "current_var": "luck_current",
        "max_var": "luck_max",
    },
)

## These values are expected to change during gameplay.
default strength_current = 35
default strength_max = 100
default agility_current = 48
default agility_max = 100
default intellect_current = 62
default intellect_max = 100
default charisma_current = 51
default charisma_max = 100
default endurance_current = 42
default endurance_max = 100
default luck_current = 27
default luck_max = 100


## Personality #################################################################
##
## Add/remove entries here to change which personality scales are shown.

define info_personality_scales = (
    {
        "left_label": _("Introverted"),
        "right_label": _("Extroverted"),
        "value_var": "intro_extro_value",
    },
    {
        "left_label": _("Logical"),
        "right_label": _("Emotional"),
        "value_var": "logical_emotional_value",
    },
    {
        "left_label": _("Objective"),
        "right_label": _("Intuitive"),
        "value_var": "objective_intuitive_value",
    },
    {
        "left_label": _("Modest"),
        "right_label": _("Ambitious"),
        "value_var": "modest_ambitious_value",
    },
)

## 0 = left-side label, 100 = right-side label.
default intro_extro_value = 40
default logical_emotional_value = 55
default objective_intuitive_value = 65
default modest_ambitious_value = 35


## Route #######################################################################
##
## Add/remove entries here to change which routes are shown in the Route tab.

define info_routes = (
    {
        "label": _("red"),
        "title": _("Red Route"),
        "quote": _("a quote about the red route"),
        "friendship_var": "red_friendship_rivalry",
        "romance_var": "red_romance",
    },
    {
        "label": _("blue"),
        "title": _("Blue Route"),
        "quote": _("a quote about the blue route"),
        "friendship_var": "blue_friendship_rivalry",
        "romance_var": "blue_romance",
    },
    {
        "label": _("yellow"),
        "title": _("Yellow Route"),
        "quote": _("a quote about the yellow route"),
        "friendship_var": "yellow_friendship_rivalry",
        "romance_var": "yellow_romance",
    },
)

## Per-route relationship defaults.
## 0 = Friendship end, 100 = Rivalry end.
default red_friendship_rivalry = 50
default blue_friendship_rivalry = 50
default yellow_friendship_rivalry = 50

## Romance defaults use the same 0-100 range as other bars.
default red_romance = 0
default blue_romance = 0
default yellow_romance = 0
