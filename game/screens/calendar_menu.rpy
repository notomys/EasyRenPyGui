## Calendar menu ###############################################################
##
## Full game menu shell (same pattern as info_screen). Open from the Calendar overlay;
## leave with Return or Close.
##
## Store-backed tuples and defaults: game/game_variables.rpy.
##
## Index sync/clamp (init python below): keeps *_index variables in range, copies from
## calendar_cycle / calendar_period on screen show, and never assigns to those store fields.

init python:

    def _calendar_cycle_index_upper():
        # Author cap (max_cycles) and tuple length; both are inclusive high indices.
        return min(store.max_cycles, len(store.calendar_cycles) - 1)

    def _calendar_period_index_upper():
        return len(store.calendar_periods) - 1

    def calendar_cycle_index_reset_from_store():
        u = _calendar_cycle_index_upper()
        store.calendar_cycle_index = max(0, min(store.calendar_cycle, u))

    def calendar_period_index_reset_from_store():
        u = _calendar_period_index_upper()
        store.calendar_period_index = max(0, min(store.calendar_period, u))

    def calendar_menu_reset_from_store():
        calendar_cycle_index_reset_from_store()
        calendar_period_index_reset_from_store()

    def calendar_cycle_index_clamp():
        u = _calendar_cycle_index_upper()
        store.calendar_cycle_index = max(0, min(store.calendar_cycle_index, u))

    def calendar_period_index_clamp():
        u = _calendar_period_index_upper()
        store.calendar_period_index = max(0, min(store.calendar_period_index, u))


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

            if calendar_cycle_index < max_cycles:
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
