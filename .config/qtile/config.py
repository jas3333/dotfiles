import os
import subprocess
from libqtile import qtile
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import colors


mod = "mod4"
terminal = guess_terminal()
myTerm = "kitty"
myBrowser = 'brave'

CITY_ID = os.environ.get('CITYID')
CITY_LINK = os.environ.get('CITY_LINK')

home = os.path.expanduser("~")


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

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

    # App Launchers
    Key([mod], "x", lazy.spawn("kitty")),
    Key([mod], "b", lazy.spawn("brave")),
    Key([mod], "r", lazy.spawn("rofi -combii -show drun")),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    Key([mod], "o", lazy.spawn("/usr/bin/octopi")),
    Key([mod], "c", lazy.spawn("calc")),
    Key([mod], "n", lazy.spawn("my-notepad")),
    Key([mod], "z", lazy.spawn("filezila")),

    # Change Wallpaper
    Key([mod], "w", lazy.spawn("wal --saturate 0.8 -qst -i " + home + "/.wallpapers/wallpaper")),
    # Picom toggle on/off
    Key([mod], "p", lazy.spawn("picom-toggle")),
    # Toggle sound sources
    Key([mod], "s", lazy.spawn("sound-change")),

    # Media Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("sound-up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("sound-down")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),

    # Toggle Layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Kill Focused Window
    Key([mod], "q", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),

    # Logout of Qtile
    Key([mod, "control"], "q", lazy.shutdown()),
]

# group_names = [
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'}),
#    ("", {'layout': 'columns'})]

# group_names = [
#    ("I", {'layout': 'monadwide'}),
#    ("II", {'layout': 'columns'}),
#    ("III", {'layout': 'columns'}),
#    ("IV", {'layout': 'columns'}),
#    ("V", {'layout': 'columns'}),
#    ("VI", {'layout': 'columns'}),
#    ("VII", {'layout': 'columns'}),
#    ("VIII", {'layout': 'columns'}),
#    ("IX", {'layout': 'columns'})]

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
    keys.append(Key([mod], str(i), lazy.group[name].toscreen(toggle=True)))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

groups.append(ScratchPad('scratchpad', [
    DropDown('myTerm', myTerm, width=0.6, height=0.6, x=0.2, y=0.2, opacity=0.8)
    ]))

keys.extend([
    Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle('myTerm')),
    ])

color, bar_color = colors.new_color()

layouts = [
    layout.Columns(border_focus=color[5], margin=15, border_normal=color[1]),
    layout.Max(),
    layout.Tile(margin=20,),
    layout.MonadTall(margin=20,),
    layout.Floating(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(margin=15, border_focus=color[5], border_normal=color[1]),
    # layout.Matrix(),
    layout.MonadWide(
        border_focus=color[5], margin=25, border_normal=color[1], ratio=0.18),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font='Operator Mono Lig Book Italic',
    fontsize=26,
    padding=0,
    background=bar_color,
    foreground=color[2])


extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(linewidth=1, foreground=bar_color, padding=10),
                widget.GroupBox(
                    highlight_method='line',
                    center_aligned=True,
                    borderwidth=2,
                    background=bar_color,
                    highlight_color=bar_color,
                    inactive=color[1],
                    padding=8,
                    this_current_screen_border=color[2],
                    other_screen_border=color[3],
                    this_screen_border=color[3]),

                widget.TextBox(font="sans", text="◤", fontsize=100, background=color[2], foreground=bar_color, padding=-1),
                widget.CurrentLayout(background=color[2], foreground=bar_color),
                widget.TextBox(font="sans", text="◢", fontsize=100, background=color[2], foreground=bar_color, padding=-1),

                widget.TaskList(
                    icon_size=45,
                    highlight_method='block',
                    margin=3,
                    padding_y=7,
                    padding_x=7,
                    border=bar_color,
                    background=bar_color,
                    foreground=color[2],
                    unfocused_border=bar_color,
                ),

                widget.Spacer(length=50, background=bar_color),
                widget.Mpris2(
                    max_chars=50,
                    scroll=True,
                    scroll_repeat=True,
                    width=350,
                    display_metadata=['xesam:artist', 'xesam:title'],
                ),

                widget.Spacer(length=700, background=bar_color),

                # widget.CheckUpdates(
                #     colour_have_updates=color[0],
                #     background=color[1],
                #     distro="Arch_checkupdates",
                #     display_format="Updates: {updates}",
                #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},),

                widget.TextBox(font="sans", text="◢", fontsize=100, background=bar_color, foreground=color[10], padding=-1),
                widget.TextBox(font="sans", text=" ", fontsize=28, background=color[10], foreground=color[4]),
                widget.Memory(background=color[10], foreground=color[4]),

                widget.Sep(background=color[10], foreground=color[4], linewidth=1, padding=20),
                widget.CPU(background=color[10], foreground=color[6] ,format='CPU: {load_percent}%'),

                widget.Sep(background=color[10], foreground=color[4], linewidth=1, padding=20),
                widget.TextBox(text="CPU Temp: ", background=color[10], foreground=color[3]),
                widget.ThermalSensor(foreground=color[3], background=color[10], tag_sensor='Tctl'),
                widget.Sep(background=color[10], foreground=color[4], linewidth=1, padding=20),
                
                widget.OpenWeather(
                    metric=False,
                    cityid=CITY_ID,
                    background=color[10],
                    foreground=color[9],
                    format='{icon} {weather} {temp:3.0f}{units_temperature}',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(CITY_LINK)},),

                widget.Sep(background=color[10], foreground=color[4], linewidth=1, padding=20),

                widget.WidgetBox(widgets=[
                    widget.Sep(foreground=color[4], linewidth=1, padding=20, background=color[10]),
                    widget.Systray(icon_size=40, padding=7, background=color[10])], 
                    background=color[10]),

                widget.Sep(background=color[10], foreground=color[4], linewidth=1, padding=20),
                widget.Clock(format='%b %d %a %H:%M',background=color[10], foreground=color[5]),
                widget.Sep(background=color[10], foreground=color[4], linewidth=0, padding=20),

            ],
            55,
            opacity=.7,
            margin=[5, 26, 0, 26],
            #border_width=[3, 3, 3, 3],
            #border_color="#A7A7A7",
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
floating_layout = layout.Floating(border_focus=color[5], border_normal=color[1], float_rules=[
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
