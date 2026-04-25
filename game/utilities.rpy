## Backend utilities ###########################################################
##
## Calendar progression helpers used by gameplay/story code.
## Shared bound/clamp primitives are also used by calendar_menu for UI-only index state.
## These helpers do not write to calendar_cycle_index / calendar_period_index.

init python:

    def get_calendar_cycle_upper_index():
        return len(store.calendar_cycles) - 1

    def get_calendar_period_upper_index():
        return len(store.calendar_periods) - 1

    def clamp_calendar_cycle_index(value):
        u = get_calendar_cycle_upper_index()
        return max(0, min(int(value), u)) if u >= 0 else 0

    def clamp_calendar_period_index(value):
        u = get_calendar_period_upper_index()
        return max(0, min(int(value), u)) if u >= 0 else 0

    def increment_calendar_cycle(step=1):
        u = get_calendar_cycle_upper_index()
        if u < 0:
            store.calendar_cycle = 0
            return store.calendar_cycle

        store.calendar_cycle = (store.calendar_cycle + int(step)) % (u + 1)
        return store.calendar_cycle

    def increment_calendar_period(step=1):
        u = get_calendar_period_upper_index()
        if u < 0:
            store.calendar_period = 0
            return store.calendar_period

        store.calendar_period = (store.calendar_period + int(step)) % (u + 1)
        return store.calendar_period

    def get_safe_calendar_cycle_index():
        return clamp_calendar_cycle_index(store.calendar_cycle)

    def get_safe_calendar_period_index():
        return clamp_calendar_period_index(store.calendar_period)

    def get_safe_calendar_cycle_label(fallback=None):
        if fallback is None:
            fallback = _("No Cycle")

        if get_calendar_cycle_upper_index() < 0:
            return fallback

        return store.calendar_cycles[get_safe_calendar_cycle_index()]["label"]

    def get_safe_calendar_period_label(fallback=None):
        if fallback is None:
            fallback = _("No Period")

        if get_calendar_period_upper_index() < 0:
            return fallback

        return store.calendar_periods[get_safe_calendar_period_index()]["label"]
