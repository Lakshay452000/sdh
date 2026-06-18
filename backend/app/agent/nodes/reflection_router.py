def reflection_router(
    state
):

    if state["needs_more_info"]:
        return "planner"

    return "responder"