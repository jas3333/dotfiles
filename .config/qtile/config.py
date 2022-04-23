import os
import subprocess
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile


mod = "mod4"
terminal = guess_terminal()
myTerm = "kitty"


# with open("/home/jas/.cache/wal/colors", "r") as file:
#    color_list = file.read().splitlines()
#
#color = []
# for index, col in enumerate(color_list):
#    if index < len(color_list) - 1:
#        color.append([col, color_list[index + 1]])

color = [
    # Top color       Bottom
        ["#d9d1a5", "#d9d1a5"],  # Fonts
        ["#252a31", "#414954"],  # Background for Bar Ends
        ["#343b40", "#4a5256"],  # Changes Center Bar
        ["#ababab", "#4e473f"],  # Changes Other screen markers
        ["#777777", "#c6c6c6"],  # Changes something
        ["#ababab", "#313131"],  # Changes something
        ["#ababab", "#313131"],  # Changes something
        ["#ababab", "#313131"],  # Changes something
        ["#ababab", "#313131"],  # Changes something
        ["#ababab", "#313131"],  # Changes something

]


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # Switch focus to next/prev screen.
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # Move Windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize Windows
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    # Flip Windows
    Key([mod], "space", lazy.layout.flip()),

    # Reset Window Size
    Key([mod], "n", lazy.layout.normalize()),

    # App Launchers
    Key([mod], "x", lazy.spawn("kitty")),
    Key([mod], "b", lazy.spawn("brave")),
    Key([mod], "r", lazy.spawn("rofi -combii -show drun")),
    Key([mod], "w", lazy.spawn(
        "wal -qst -i /home/jas/.wallpapers/wallpaper/ --iterative")),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    Key([mod], "c", lazy.spawn("calc")),
    Key([mod], "t", lazy.spawn("krita")),

    # Enable/Disabale Picom
    Key([mod], "p", lazy.spawn("picom-toggle")),

    # Media Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("sound-up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("sound-down")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),

    # Toggle Layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Kill Focused Window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # System Hotkeys
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
]


# group_names = [
#    ("I", {'layout': 'columns'}),
#    ("II", {'layout': 'columns'}),
#    ("III", {'layout': 'columns'}),
#    ("IV", {'layout': 'columns'}),
#    ("V", {'layout': 'columns'}),
#    ("VI", {'layout': 'columns'}),
#    ("VII", {'layout': 'columns'}),
#    ("VIII", {'layout': 'columns'}),
#    ("IX", {'layout': 'columns'})
# ]
#
#
# group_names = [
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'})
# ]

group_names = [
    ("1", {'layout': 'columns'}),
    ("2", {'layout': 'columns'}),
    ("3", {'layout': 'columns'}),
    ("4", {'layout': 'columns'}),
    ("5", {'layout': 'columns'}),
    ("6", {'layout': 'columns'}),
    ("7", {'layout': 'columns'}),
    ("8", {'layout': 'columns'}),
    ("9", {'layout': 'columns'}),
]


groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layouts = [

    layout.Columns(
        border_focus=color[6],
        border_normal=color[1],
        margin=10,
        border_width=2,
        border_on_single=True),

    layout.Max(),
    layout.Tile(margin=40,),
    layout.MonadTall(margin=20,),
    layout.Stack(num_stacks=2),
    layout.Floating(),
    layout.Matrix(),

    layout.Bsp(
        border_focus=color[6],
        border_normal=color[1],
        margin=10,
        border_width=2),

    layout.MonadWide(
        border_focus=color[6],
        border_normal=color[1],
        margin=15,
        ratio=0.16,),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Operator Mono Lig Book Italic',
    fontsize=16,
    padding=0,
    background=color[1],
    foreground=color[0],

)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=1,
                    background=color[1],
                    foreground=color[1],
                    padding=10),

                widget.CurrentLayout(),

                widget.Sep(
                    linewidth=1,
                    background=color[1],
                    foreground=color[4],
                    padding=10),

                widget.GroupBox(
                    highlight_method='line',
                    center_aligned=True,
                    borderwidth=2,
                    background=color[1],
                    highlight_color=color[1],
                    inactive=color[0],
                    padding=8,
                    this_current_screen_border=color[0],
                    other_screen_border=color[3],
                    this_screen_border=color[3]),

                widget.Sep(
                    linewidth=1,
                    background=color[1],
                    foreground=color[4],
                    padding=10),

                widget.Sep(
                    linewidth=1,
                    background=color[1],
                    foreground=color[1],
                    padding=10),

                widget.Spacer(background=color[2], length=5),

                widget.TaskList(
                    icon_size=15,
                    highlight_method='block',
                    margin=0,
                    padding_y=6,
                    padding_x=5,
                    border=color[1],
                    background=color[2],
                    unfocused_border=color[2],
                ),

                widget.TextBox(
                    foreground=color[1],
                    background=color[2],
                    text="◢",
                    fontsize=90,
                    padding=-15),

                widget.CheckUpdates(
                    background=color[1],
                    distro="Arch_checkupdates",
                    display_format="Updates: {updates}",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.TextBox(
                    font="sans",
                    text=" ",
                    fontsize=18,
                    background=color[1]),

                widget.Memory(background=color[1]),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.CPU(
                    background=color[1],
                    format='CPU: {load_percent}%'),
                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.TextBox(
                    text="CPU Temp: ",
                    background=color[1]),

                widget.ThermalSensor(
                    background=color[1],
                    tag_sensor='Tctl'),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                # widget.OpenWeather(
                #     metric=False,
                #     cityid=,
                #     background=color[1],
                #     format='{icon} {weather} {temp:3.0f}{units_temperature}',
                #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("brave https://www.accuweather.com/en/us/yourcity/cityzip/daily-weather-forecast/city_id")},),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.Systray(
                    icon_size=20,
                    padding=7,
                    background=color[1]),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.Clock(
                    format='%b %d %a %H:%M',
                    background=color[1],),
                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=0,
                    padding=20),

            ],
            35, opacity=.8, margin=[5, 16, 0, 16]
        ),
    ),
    # 2nd Monitor
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=1,
                    background=color[1],
                    foreground=color[1],
                    padding=10),

                widget.CurrentLayout(
                    background=color[1],
                    foreground=color[0]),

                widget.Sep(
                    linewidth=1,
                    background=color[1],
                    foreground=color[4],
                    padding=10),

                widget.GroupBox(
                    highlight_method='line',
                    center_aligned=True,
                    borderwidth=2,
                    background=color[1],
                    font="Operator Mono Lig Book Italic",
                    fontsize=18,
                    highlight_color=color[1],
                    inactive=color[3],
                    padding=8,
                    this_current_screen_border=color[0],
                    other_current_screen_border=color[3],
                    other_screen_border=color[3],
                    this_screen_border=color[3]),

                widget.Sep(
                    linewidth=1,
                    background=color[1],
                    foreground=color[4],
                    padding=10),

                widget.Sep(
                    linewidth=1,
                    background=color[2],
                    foreground=color[2],
                    padding=10),

                widget.Spacer(
                    background=color[2],
                    length=5),

                widget.TaskList(
                    highlight_method='block',
                    background=color[2],
                    margin=0,
                    padding_y=6,
                    padding_x=5,
                    border=color[1],
                    unfocused_border=color[2],
                    icon_size=15),

                widget.TextBox(
                    foreground=color[1],
                    background=color[2],
                    text="◢",
                    fontsize=90,
                    padding=-15),

                widget.TextBox(
                    font="sans",
                    text="  ",
                    fontsize=18,
                    background=color[1]),

                widget.Memory(background=color[1]),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.CPU(
                    background=color[1],
                    foreground=color[0],
                    format='CPU: {load_percent}%'),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.TextBox(
                    text="CPU Temp: ",
                    background=color[1]),

                widget.ThermalSensor(
                    background=color[1],
                    foregroune=color[2],
                    tag_sensor='Tctl'),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=1,
                    padding=20),

                widget.Clock(
                    format='%b %d %a %H:%M',
                    background=color[1],),

                widget.Sep(
                    background=color[1],
                    foreground=color[4],
                    linewidth=0,
                    padding=20),
            ],
            35, opacity=.8, margin=[5, 16, 0, 16]
        ),

    ),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#828282",
    float_rules=[

        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
