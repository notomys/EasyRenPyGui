
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    tag menu

    add "#21212db2" # The background; can be whatever

    use game_menu(_("About"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Version [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 36


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Help"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "help"
        spacing 23

        hbox:

            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button:
    xmargin 12

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    xalign 1.0
    textalign 1.0


## Info screen #################################################################
##
## Standalone informational screen intended to be opened from in-game controls.

## Skills tab defaults.
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

## Personality tab defaults.
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

screen info_screen():

    tag menu

    default info_tab = "overview"

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Info"))

    viewport:
        style_prefix "game_menu"
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        spacing 18

        hbox:
            spacing 18

            textbutton _("Overview"):
                selected info_tab == "overview"
                action SetScreenVariable("info_tab", "overview")

            textbutton _("Skills"):
                selected info_tab == "skills"
                action SetScreenVariable("info_tab", "skills")

            textbutton _("Personality"):
                selected info_tab == "personality"
                action SetScreenVariable("info_tab", "personality")

        if info_tab == "skills":
            use info_skills_tab
        elif info_tab == "personality":
            use info_personality_tab
        else:
            label _("Information")
            text _("This is a placeholder info screen.")
            text _("You can replace this content in a later template slice.")


screen info_skills_tab():

    vbox:
        spacing 16

        label _("Skills")

        for skill in info_skills:
            $ current_value = getattr(store, skill["current_var"])
            $ max_value = getattr(store, skill["max_var"])
            $ clamped_max = max(1, max_value)

            vbox:
                spacing 6

                hbox:
                    xfill True

                    text "[skill['label']]"
                    text "[current_value]/[max_value]" xalign 1.0

                bar value AnimatedValue(value=current_value, range=clamped_max, delay=0.0):
                    xfill True


screen info_personality_tab():

    vbox:
        spacing 18

        label _("Personality")

        for scale in info_personality_scales:
            $ scale_value = getattr(store, scale["value_var"])
            $ clamped_value = max(0, min(100, scale_value))

            vbox:
                spacing 6

                hbox:
                    xfill True
                    text "[scale['left_label']]"
                    text "[scale['right_label']]" xalign 1.0

                hbox:
                    spacing 12
                    xfill True

                    #text "[scale['left_label']]"

                    bar value AnimatedValue(value=clamped_value, range=100, delay=0.0):
                        xfill True

                    text "[scale['right_label']]"
