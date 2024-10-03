"""
Streamlit-App designed to be a companion for Bloons Tower Defense 6.

App created on 2024-10-03 by Codinghawk27.
"""

import streamlit as st
import numpy as np

PRIMARY_TOWERS = [
    "Dart Monkey",
    "Boomerang Monkey",
    "Bomb Shooter",
    "Tack Shooter",
    "Ice Monkey",
    "Glue Gunner",
]
MILITARY_TOWERS = [
    "Sniper Monkey",
    "Monkey Sub",
    "Monkey Buccaneer",
    "Monkey Ace",
    "Heli Pilot",
    "Mortar Monkey",
    "Dartling Gunner",
]
MAGIC_TOWERS = [
    "Wizard Monkey",
    "Super Monkey",
    "Ninja Monkey",
    "Alchemist",
    "Druid",
    "Mermonkey",
]
SUPPORT_TOWERS = [
    "Banana Farm",
    "Spike Factory",
    "Monkey Village",
    "Engineer Monkey",
    "Beast Handler",
]
TOWERS = {
    "Primary": PRIMARY_TOWERS,
    "Military": MILITARY_TOWERS,
    "Magic": MAGIC_TOWERS,
    "Support": SUPPORT_TOWERS,
}

MONKEY_IMAGES = {
    "Dart Monkey": "images/dart_monkey.png",
    "Boomerang Monkey": "images/boomerang_monkey.png",
    "Bomb Shooter": "images/bomb_shooter.png",
    "Tack Shooter": "images/tack_shooter.png",
    "Ice Monkey": "images/ice_monkey.png",
    "Glue Gunner": "images/glue_gunner.png",
    "Sniper Monkey": "images/sniper_monkey.png",
    "Monkey Sub": "images/monkey_sub.png",
    "Monkey Buccaneer": "images/monkey_buccaneer.png",
    "Monkey Ace": "images/monkey_ace.png",
    "Heli Pilot": "images/heli_pilot.png",
    "Mortar Monkey": "images/mortar_monkey.png",
    "Dartling Gunner": "images/dartling_gunner.png",
    "Wizard Monkey": "images/wizard_monkey.png",
    "Super Monkey": "images/super_monkey.png",
    "Ninja Monkey": "images/ninja_monkey.png",
    "Alchemist": "images/alchemist.png",
    "Druid": "images/druid.png",
    "Mermonkey": "images/mermonkey.png",
    "Banana Farm": "images/banana_farm.png",
    "Spike Factory": "images/spike_factory.png",
    "Monkey Village": "images/monkey_village.png",
    "Engineer Monkey": "images/engineer_monkey.png",
    "Beast Handler": "images/beast_handler.png",
}


def main() -> None:
    """Run the app."""
    initialize_session()

    st.title("BTD 6 Companion")

    monkey_team_tab, _ = st.tabs(["Monkey Team Generator", "Challenge Generator"])

    with monkey_team_tab:
        st.header("Monkey Team Generator")
        st.write("Generate a random monkey team")

        st.multiselect(
            "Filter towers by category",
            options=TOWERS.keys(),
            default=st.session_state["selected_tower_categories"],
            key="tower_category_multiselect",
            on_change=callback_tower_category_multiselection,
        )

        st.multiselect(
            "Filter individual monkeys",
            options=st.session_state["available_towers"],
            default=st.session_state["available_towers"],
            key="tower_multiselect",
            on_change=callback_tower_multiselection,
        )

        team_size = st.number_input(
            "Size of monkey team",
            min_value=1,
            max_value=len(st.session_state["selected_towers"]) - 1,
            step=1,
            value=3,
        )

        left, right = st.columns(2)
        if left.button("Generate random monkey team", use_container_width=True):
            # Generate a random monkey team
            monkey_team = np.random.choice(
                st.session_state["selected_towers"], team_size, replace=False
            )

            # Format output
            for monkey in monkey_team:
                image_display, name_display = st.columns(2)
                image_display.image(MONKEY_IMAGES[monkey])
                name_display.write(monkey)

        if right.button(
            "Reset selections", use_container_width=True, on_click=reset_selections
        ):
            st.write("Selections resetted.")


def initialize_session():
    if "selected_tower_categories" not in st.session_state:
        st.session_state["selected_tower_categories"] = TOWERS.keys()
    if "available_towers" not in st.session_state:
        available_towers = []
        for category in st.session_state["selected_tower_categories"]:
            available_towers.extend(TOWERS[category])
        st.session_state["available_towers"] = available_towers
    if "selected_towers" not in st.session_state:
        st.session_state["selected_towers"] = st.session_state["available_towers"]


def reset_selections():
    # Reset selections
    st.session_state["selected_tower_categories"] = TOWERS.keys()
    available_towers = []
    for category in st.session_state["selected_tower_categories"]:
        available_towers.extend(TOWERS[category])
    st.session_state["available_towers"] = available_towers
    st.session_state["selected_towers"] = st.session_state["available_towers"]

    # Reset selected tower categories
    del st.session_state["tower_category_multiselect"]
    st.session_state["tower_category_multiselect"] = [str(key) for key in TOWERS.keys()]

    # Reset selected towers
    del st.session_state["tower_multiselect"]
    st.session_state["tower_multiselect"] = available_towers


def callback_tower_category_multiselection():
    st.session_state["selected_tower_categories"] = st.session_state[
        "tower_category_multiselect"
    ]

    available_towers = []
    for category in st.session_state["selected_tower_categories"]:
        available_towers.extend(TOWERS[category])
    st.session_state["available_towers"] = available_towers
    st.session_state["selected_towers"] = available_towers


def callback_tower_multiselection():
    st.session_state["selected_towers"] = st.session_state["tower_multiselect"]


if __name__ == "__main__":
    main()
