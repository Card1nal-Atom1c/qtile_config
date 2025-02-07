from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.widget import Spacer, GenPollText
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

mod = "mod1"
keys = [
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod,"shift"], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod,"shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating1(), desc="Toggle floating on the focused window"),
    Key([mod], "q", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod,"shift"], "p", lazy.spawn("rofi -show run"), desc="Launch terminal"),
]

__groups={
    1:Group("Term"),
    2:Group("Web"),
    3:Group("Code"),
    4:Group("Apps"),
    9:Group("VPN"),
}
groups=[__groups[i] for i in __groups]
def get_gropus_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                str(get_gropus_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                str(get_gropus_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),

        ]
    )

layouts = [
    layout.Bsp(border_focus_stack=["#616161", "#616161"], border_width=4,single_border_witdth=0,margin=4)
]

widget_defaults = dict(
    font="HackNerdFont",
    fontsize=12,
    padding=1
)
extension_defaults = widget_defaults.copy()
def IP():
    try:
        salida=subprocess.check_output('$HOME/.config/qtile/scripts/IP.sh',shell=True)
        salida_decode=salida.decode('utf-8').strip()
        print(f"salida del script:{salida_decode}")
        return salida_decode
    except subprocess.CalledProcessError as e:
        print(f"error:{e.returncode}")
        return f"Error: {e.returncode}"
def HTB():
    try:
        salida=subprocess.check_output('$HOME/.config/qtile/scripts/HTB.sh',shell=True)
        salida_decode=salida.decode('utf-8').strip()
        print(f"salida del script:{salida_decode}")
        return salida_decode
    except subprocess.CalledProcessError as e:
        print(f"error:{e.returncode}")
        return f"Error: {e.returncode}"
def Target():
    try:
        salida=subprocess.check_output('$HOME/.config/qtile/scripts/Target.sh',shell=True)
        salida_decode=salida.decode('utf-8').strip()
        print(f"salida del script:{salida_decode}")
        return salida_decode
    except subprocess.CalledProcessError as e:
        print(f"error:{e.returncode}")
        return f"Error: {e.returncode}"

screens = [
    Screen(
        bottom=bar.Bar(
            [   

                widget.GroupBox(background="#4d4c4c",foreground="#ffffff"),
                widget.Prompt(),
                widget.TextBox(
                    text="",
                    background="#616161",
                    foreground="#4d4c4c",
                    fontsize=35
                ),
                widget.WindowName(background="#616161"),
                widget.TextBox(
                    text="",
                    foreground="#616161",
                    fontsize=35
                ),
                widget.Systray(),
                Spacer(length=bar.STRETCH),
                
            ],
            40,
            background="#00000000"
        ),
        top=bar.Bar([
                Spacer(length=bar.STRETCH),
                widget.TextBox(
                    text="",
                    foreground="#616161",
                    fontsize=35
                ),
                GenPollText(
                func=Target,
                update_interval=10,
                background="#616161"),
                widget.TextBox(
                    text="",
                    foreground="#4d4c4c",
                    background="#616161",
                    fontsize=35
                ),
                GenPollText(
                func=HTB,
                update_interval=10,
                background="#4d4c4c"),
                widget.TextBox(
                    text="",
                    foreground="#383737",
                    background="#4d4c4c",
                    fontsize=35
                ),
                GenPollText(
                func=IP,
                update_interval=10,
                background="#383737"),
                widget.TextBox(
                    text="",
                    foreground="#242323",
                    background="#383737",
                    fontsize=35
                ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",background="#242323"),
                widget.TextBox(
                    text="",
                    foreground="#000000",
                    background="#242323",
                    fontsize=35
                ),
                widget.QuickExit(background="#000000"),

            ],
            40,
            background="#00000000"

        ),

    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home=os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)
