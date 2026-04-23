## Info screen #################################################################
##
## Standalone informational screen intended to be opened from in-game controls.

screen info_labeled_progress_row(label, value, max_value):

    $ clamped_max = max(1, max_value)
    $ clamped_value = max(0, min(value, clamped_max))

    vbox:
        spacing 6

        hbox:
            xfill True
            text "[label]"
            text "[clamped_value]/[clamped_max]" xalign 1.0

        bar value AnimatedValue(value=clamped_value, range=clamped_max, delay=0.0):
            xfill True


screen info_axis_bar_row(left_label, right_label, value):

    $ clamped_value = max(0, min(100, value))

    vbox:
        spacing 6

        hbox:
            xfill True
            text "[left_label]"
            text "[right_label]" xalign 1.0

        hbox:
            spacing 12
            xfill True

            bar value AnimatedValue(value=clamped_value, range=100, delay=0.0):
                xfill True


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

            textbutton _("Route"):
                selected info_tab == "route"
                action SetScreenVariable("info_tab", "route")

        if info_tab == "overview":
            label _("Information")
            text _("This is a placeholder info screen.")
            text _("You can replace this content in a later template slice.")
        elif info_tab == "skills":
            use info_skills_tab
        elif info_tab == "personality":
            use info_personality_tab
        elif info_tab == "route":
            use info_route_tab


screen info_skills_tab():

    vbox:
        spacing 16
        label _("Skills")

        for skill in info_skills:
            $ current_value = getattr(store, skill["current_var"])
            $ max_value = getattr(store, skill["max_var"])
            use info_labeled_progress_row(skill["label"], current_value, max_value)


screen info_personality_tab():

    vbox:
        spacing 18
        label _("Personality")

        for scale in info_personality_scales:
            $ scale_value = getattr(store, scale["value_var"])
            use info_axis_bar_row(scale["left_label"], scale["right_label"], scale_value)


screen info_route_tab():

    vbox:
        spacing 16
        label _("Route")

        for route in info_routes:
            textbutton "[route['label']]":
                action Show("route_popup", route=route)


screen route_popup(route):

    modal True
    zorder 210
    style_prefix "confirm"

    $ friendship_value = getattr(store, route["friendship_var"])
    $ romance_value = getattr(store, route["romance_var"])

    add "#0008"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 640

        has vbox
        spacing 20

        label "[route['title']]"

        hbox:
            spacing 20
            xfill True

            frame:
                xsize 180
                ysize 180
                background Solid("#4c4c58")
                text _("Image") xalign 0.5 yalign 0.5

            text "[route['quote']]":
                xfill True
                yalign 0.5

        use info_axis_bar_row(_("Friendship"), _("Rivalry"), friendship_value)
        use info_labeled_progress_row(_("Romance"), romance_value, 100)

        textbutton _("Close"):
            xalign 0.5
            action Hide("route_popup")
