import os
import subprocess
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import random


mod = "mod4"
terminal = guess_terminal()
myTerm = "kitty"
myBrowser = 'brave'
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

    # Reset Window Size
    Key([mod], "n", lazy.layout.normalize()),

    # App Launchers
    Key([mod], "x", lazy.spawn("kitty")),
    Key([mod], "b", lazy.spawn("librewolf")),
    Key([mod], "r", lazy.spawn('rofi -combi-modi window,drun,ssh -theme DarkBlue -font "Operator Mono Lig 24" -show combi -icon-theme "candy-icons" -show-icons')),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    Key([mod], "o", lazy.spawn("octopi")),


    # Change Wallpaper
    Key([mod], "w", lazy.spawn("wal --saturate 0.8 -q -i " + home + "/.wallpapers/wallpaper")),
    # Picom toggle on/off
    Key([mod], "p", lazy.spawn("picom-toggle")),
    # Toggle sound sources
    Key([mod], "s", lazy.spawn("sound-change")),

    #Media Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("sound-up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("sound-down")),

    # Toggle Layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Kill Focused Window
    Key([mod], "q", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),

    # Logout of Qtile
    Key([mod, "control"], "q", lazy.shutdown()),
]

group_names = [("I", {'layout': 'monadwide'}), 
               ("II", {'layout': 'columns'}), 
               ("III", {'layout': 'columns'}),
               ("IV", {'layout': 'columns'}), 
               ("V", {'layout': 'columns'}), 
               ("VI", {'layout': 'columns'}), 
               ("VII", {'layout': 'columns'}), 
               ("VIII", {'layout': 'columns'}), 
               ("IX", {'layout': 'columns'})]  

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

#            Top      Bottom
color = [["#1b1b1c","#4c5570"], # inner bar             0
         ["#292f3d","#292f3d"], # outer bar             1
         ["#4c5570","#2b2b2b"], # Inactive Group Color  2
         ["#f9f7f8","#f9f7f8"], # Active Group Color    3
         ["#d75f5f","#d75f5f"], # Group Border Color    4
         ["#a9d0d8","#a9d0d8"], #Outer Bar              5
         ["#21051b","#21051b"], #Outer Bar              6
         ["#21051b","#21051b"], #Outer Bar              7
        ]

layouts = [
    layout.Columns(border_focus = color[5],margin = 15, border_normal=color[1]),
    layout.Max(),
    layout.Tile(margin = 20,),
    layout.MonadTall(margin = 20,),
    layout.Floating(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(margin = 15, border_focus = color[5], border_normal=color[1]),
    # layout.Matrix(),
    layout.MonadWide(border_focus = color[5],margin = 25, border_normal=color[1],ratio=0.18 ),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    fontsize=25,
    padding=0,
    background=color[0],)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(linewidth = 0, background = color[1], padding = 20),
                widget.GroupBox(highlight_method='line',
                    fontsize=30,
                    background=color[1],
                    highlight_color=color[1],
                    spacing=20,
                    this_current_screen_border='#fcfcf9',
                    block_highlight_text_color=None,
                    borderwidth=5,
                    center_aligned=True,
                    font='Operator Mono Book Italic',
                    margin_y = 8,),
                widget.TextBox(
                    font = 'sans',
                    foreground = color[1],
                    text = "◤",
                    fontsize = 90,
                    padding = -15),
                widget.CurrentLayout(),
                widget.CurrentLayoutIcon(padding = 5, scale = .6),
                widget.TaskList(
                    border = color[2],
                    borderwidth = 5,
                    highlight_method = 'block',
                    margin_y = 5,
                    padding = 6,),
                widget.Chord(
                    chords_colors={'launch': ("#ff0000", "#ffffff"),},
                    name_transform=lambda name: name.upper(),),
                widget.TextBox(
                    font = "sans",
                    foreground = color[1],
                    text = "◢",
                    fontsize = 90,
                    padding = -15),
                widget.CheckUpdates(
                    background = color[1],
                    distro = "Arch_checkupdates",
                    display_format = "Updates: {updates}",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},),
                widget.Sep(background = color[1], foreground = color[0], linewidth = 4, padding = 20),
                widget.TextBox(
                    font = "sans",
                    text = " ",
                    fontsize = 27,
                    background = color[1]),
                widget.Memory(
                    background = color[1],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},),
                widget.Sep(background = color[1], foreground = color[0], linewidth = 4, padding = 20),
                widget.CPU(background = color[1], format = 'CPU:{load_percent}%', max_chars = 11,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},),
                widget.Sep(background = color[1], foreground = color[0], linewidth = 4, padding = 20),
                widget.TextBox(text = "CPU Temp: ", background = color[1]),
                widget.ThermalSensor(background=color[1],  tag_sensor = 'Tctl'),
                widget.Sep(background = color[1], foreground = color[0], linewidth = 4, padding = 20),
               # widget.OpenWeather(
               #     metric = False,
               #     cityid = ########, 
               #     background = color[1],
               #     format = ' {weather}{temp:3.0f}{units_temperature}',
               # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("brave https://www.accuweather.com/enteryourowncity")},),
                widget.Sep(background = color[1], foreground = color[0], linewidth = 4, padding = 20),
                widget.Systray(icon_size = 40,background = color[1], padding = 10 ),
                widget.Sep(background = color[1], foreground = color[0], linewidth = 4, padding = 20),
                widget.Clock(format='%b %d %a %H:%M',background = color[1],),
                widget.Sep(background = color[1], foreground = color[0], linewidth = 0, padding = 20),
            ],
            45, opacity = 0.60, margin=[0, 28, 0, 28]
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
floating_layout = layout.Floating(border_focus=color[5],border_normal=color[1],float_rules=[
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
