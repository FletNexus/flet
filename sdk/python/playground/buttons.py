import logging
from datetime import datetime
from time import sleep

import flet
from flet import (
    Column,
    ElevatedButton,
    FilledButton,
    FilledTonalButton,
    FloatingActionButton,
    Icon,
    IconButton,
    OutlinedButton,
    Page,
    Row,
    Text,
    TextButton,
    colors,
    icons,
    theme,
)

logging.basicConfig(level=logging.DEBUG)


def main(page: Page):
    page.title = "Buttons Example"
    page.theme_mode = "light"
    # page.theme = theme.Theme(color_scheme_seed="green", use_material3=True)
    page.padding = 50
    page.floating_action_button = FloatingActionButton(icon=icons.ADD)

    page.add(
        Column(
            expand=1,
            scroll=True,
            controls=[
                Text("Elevated button", style="headlineMedium"),
                ElevatedButton("Normal button"),
                ElevatedButton("Disabled button", disabled=True),
                ElevatedButton(
                    "Button with icon and tooltip",
                    icon="chair_outlined",
                    tooltip="Hey, click me!",
                ),
                ElevatedButton(
                    "Button with colorful icon",
                    icon="park_rounded",
                    icon_color="green400",
                ),
                ElevatedButton(
                    width=150,
                    content=Row(
                        [
                            Icon(name="favorite", color="pink"),
                            Icon(name="audiotrack", color="green"),
                            Icon(name="beach_access", color="blue"),
                        ],
                        alignment="spaceAround",
                    ),
                ),
                Row(
                    [
                        ElevatedButton(
                            "Red button",
                            color=colors.WHITE,
                            bgcolor=colors.RED,
                            icon=icons.PALETTE,
                        ),
                        ElevatedButton(
                            "Green button",
                            color=colors.WHITE,
                            bgcolor=colors.GREEN,
                            icon=icons.PALETTE,
                        ),
                        ElevatedButton(
                            "Yellow button",
                            color=colors.BLACK,
                            bgcolor=colors.YELLOW,
                            icon=icons.PALETTE,
                        ),
                    ]
                ),
                #
                #
                #
                Text("Filled button", style="headlineMedium"),
                FilledButton("Filled button"),
                FilledButton("Disabled button", disabled=True),
                FilledButton("Filled with icon", icon=icons.ADD),
                #
                #
                #
                Text("Filled tonal button", style="headlineMedium"),
                FilledTonalButton("Filled tonal button"),
                FilledTonalButton("Disabled button", disabled=True),
                FilledTonalButton("Filled tonal with icon", icon=icons.ADD),
                #
                #
                #
                Text("Outlined button", style="headlineMedium"),
                OutlinedButton("Normal button"),
                OutlinedButton("Disabled button", disabled=True),
                OutlinedButton("Button with icon", icon="chair_outlined"),
                OutlinedButton(
                    "Button with colorful icon",
                    icon="park_rounded",
                    icon_color="green400",
                ),
                OutlinedButton(
                    width=150,
                    content=Row(
                        [
                            Icon(name="favorite", color="pink"),
                            Icon(name="audiotrack", color="green"),
                            Icon(name="beach_access", color="blue"),
                        ],
                        alignment="spaceAround",
                    ),
                ),
                Text("Text button", style="headlineMedium"),
                TextButton("Normal button"),
                TextButton("Disabled button", disabled=True),
                TextButton("Button with icon", icon="chair_outlined"),
                TextButton(
                    "Button with colorful icon",
                    icon=icons.PARK_ROUNDED,
                    icon_color="green400",
                ),
                TextButton(
                    width=150,
                    content=Row(
                        [
                            Icon(name="favorite", color="pink"),
                            Icon(name="audiotrack", color="green"),
                            Icon(name="beach_access", color="blue"),
                        ],
                        alignment="spaceAround",
                    ),
                ),
                Text("Icon button", style="headlineMedium"),
                Row(
                    [
                        IconButton(
                            icon="pause_circle_filled_sharp",
                            icon_color="blue400",
                            tooltip="Pause record",
                        ),
                        IconButton(
                            icon="delete_forever_rounded",
                            icon_color="pink600",
                            tooltip="Delete record",
                        ),
                        IconButton(
                            icon=icons.ANDROID,
                            icon_color="white",
                            bgcolor="blue",
                            tooltip="Beep... Beep... Beep...",
                        ),
                        IconButton(
                            icon=icons.SEND_ROUNDED, icon_color="white", bgcolor="green"
                        ),
                    ]
                ),
            ],
        )
    )


flet.app(name="test1", port=8550, target=main, view=flet.FLET_APP)
