## Calendar menu ###############################################################
##
## Full game menu shell (same pattern as info_screen). Open from the Calendar overlay;
## leave with Return or Close.
##
## Store-backed tuples and defaults: game/game_variables.rpy.
## Backend progression and shared bound/clamp helpers live in game/utilities.rpy.
##
## Index sync/clamp (init python below): keeps *_index variables in range, copies from
## calendar_cycle / calendar_period on screen show, and never assigns to those store fields.

init python:

    def calendar_cycle_index_reset_from_store():
        store.calendar_cycle_index = clamp_calendar_cycle_index(store.calendar_cycle)

    def calendar_period_index_reset_from_store():
        store.calendar_period_index = clamp_calendar_period_index(store.calendar_period)

    def calendar_menu_reset_from_store():
        calendar_cycle_index_reset_from_store()
        calendar_period_index_reset_from_store()

    def calendar_cycle_index_clamp():
        store.calendar_cycle_index = clamp_calendar_cycle_index(store.calendar_cycle_index)

    def calendar_period_index_clamp():
        store.calendar_period_index = clamp_calendar_period_index(store.calendar_period_index)


screen calendar_menu():

    tag menu

    on "show" action Function(calendar_menu_reset_from_store)

    add HBox(Transform("#292835", xsize=350), "#21212db2")

    use game_menu(_("Calendar"))

    viewport:
        style_prefix "game_menu"
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        spacing 18

        $ calendar_cycle_index_clamp()
        $ calendar_period_index_clamp()
        $ _cyc = calendar_cycles[calendar_cycle_index]
        label "[_cyc['label']]"

        hbox:
            spacing 12

            if calendar_cycle_index > 0:
                textbutton _("Previous"):
                    action [
                        SetVariable("calendar_cycle_index", calendar_cycle_index - 1),
                        Function(calendar_cycle_index_clamp),
                    ]

            if calendar_cycle_index < get_calendar_cycle_upper_index():
                textbutton _("Next"):
                    action [
                        SetVariable("calendar_cycle_index", calendar_cycle_index + 1),
                        Function(calendar_cycle_index_clamp),
                    ]

        hbox:
            spacing 24
            xfill True

            vbox:
                spacing 8

                for i, period in enumerate(calendar_periods):
                    textbutton "[period['label']]":
                        selected calendar_period_index == i
                        action [
                            SetVariable("calendar_period_index", i),
                            Function(calendar_period_index_clamp),
                        ]

            vbox:
                spacing 12
                xfill True

                $ _sel = calendar_periods[calendar_period_index]
                text _("Selected:")
                text "[_sel['label']]"
                text _("Placeholder content for this period.")

        textbutton _("Close"):
            action Return()
