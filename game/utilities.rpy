## Backend utilities ###########################################################
##
## Calendar progression helpers used by gameplay/story code.
## Shared bound/clamp primitives are also used by calendar_menu for UI-only index state.
## These helpers do not write to calendar_cycle_index / calendar_period_index.

init python:

    
    ## Call from script/gameplay flow to advance story time by cycle (week).
    ## Example use: `$ increment_calendar_cycle()` inside labels/events.
    def increment_calendar_cycle(step=1):
        u = get_calendar_cycle_upper_index()
        if u < 0:
            store.calendar_cycle = 0
            return store.calendar_cycle

        store.calendar_cycle = (store.calendar_cycle + int(step)) % (u + 1)
        return store.calendar_cycle

    ## Call from script/gameplay flow to advance story time by period (day).
    ## When period wraps from last index back to 0, this also advances cycle.
    ## Example use: `$ increment_calendar_period()` inside labels/events.
    def increment_calendar_period(step=1):
        u = get_calendar_period_upper_index()
        if u < 0:
            store.calendar_period = 0
            return store.calendar_period

        next_period = store.calendar_period + int(step)
        if next_period > u:
            store.calendar_period = 0
            increment_calendar_cycle()
            return store.calendar_period

        store.calendar_period = next_period
        return store.calendar_period

    ## UI helper: highest valid index for calendar_cycles.
    def get_calendar_cycle_upper_index():
        return len(store.calendar_cycles) - 1

    ## UI helper: highest valid index for calendar_periods.
    def get_calendar_period_upper_index():
        return len(store.calendar_periods) - 1

    ## UI helper: clamps any cycle index to a valid range for display/navigation.
    def clamp_calendar_cycle_index(value):
        u = get_calendar_cycle_upper_index()
        return max(0, min(int(value), u)) if u >= 0 else 0

    ## UI helper: clamps any period index to a valid range for display/navigation.
    def clamp_calendar_period_index(value):
        u = get_calendar_period_upper_index()
        return max(0, min(int(value), u)) if u >= 0 else 0

    ## UI helper: safe cycle index from store state, suitable for label lookup.
    def get_safe_calendar_cycle_index():
        return clamp_calendar_cycle_index(store.calendar_cycle)

    ## UI helper: safe period index from store state, suitable for label lookup.
    def get_safe_calendar_period_index():
        return clamp_calendar_period_index(store.calendar_period)

    ## UI helper: returns a valid cycle label (or fallback) so overlays never error.
    def get_safe_calendar_cycle_label(fallback=None):
        if fallback is None:
            fallback = _("No Cycle")

        if get_calendar_cycle_upper_index() < 0:
            return fallback

        return store.calendar_cycles[get_safe_calendar_cycle_index()]["label"]

    ## UI helper: returns a valid period label (or fallback) so overlays never error.
    def get_safe_calendar_period_label(fallback=None):
        if fallback is None:
            fallback = _("No Period")

        if get_calendar_period_upper_index() < 0:
            return fallback

        return store.calendar_periods[get_safe_calendar_period_index()]["label"]
