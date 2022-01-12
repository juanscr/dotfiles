# =============================================== #
#                                                 #
#                                                 #
#              qtile 0.17.0 config                #
#                                                 #
# =============================================== #

import subprocess
from os.path import expanduser as eu

from libqtile import bar, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.layout.floating import Floating
from libqtile.layout.stack import Stack
from libqtile.layout.xmonad import MonadTall
from libqtile.lazy import lazy

from my_widgets import MyWidgets

# Mod key
mod = "mod4"

# Browser
browser = "brave"

# Terminal
terminal = eu("~/.bin/launchers/launch-terminal.sh")

# ============ Basic Behavior ============
keys = [
    # Close window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Restart qtile
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    # Lock screen
    Key(
        [mod, "shift"], "x", lazy.spawn("betterlockscreen -l blur"), desc="Lock screen."
    ),
    # Exit qtile
    KeyChord(
        [mod, "shift"],
        "e",
        [
            Key([], "l", lazy.shutdown(), desc="Log off"),
            Key([], "r", lazy.spawn("systemctl reboot"), desc="Reboot PC"),
            Key([], "p", lazy.spawn("systemctl poweroff"), desc="Shutdown"),
        ],
        mode="exit: [l]ogout, [r]eboot, [p]oweroff",
    ),
    # Search for app. Customized to use dracula theme.
    # Tested with dmenu 5.0
    Key([mod], "d", lazy.spawn("dmenu_run"), desc="Spawn dmenu"),
    # Select monitor layout
    Key(
        [mod, "shift"],
        "a",
        lazy.spawn(eu("~/.bin/select-monitor.sh")),
        desc="Select monitor layout using script",
    ),
]

# ============ Media Controls ============
playerctl = "playerctl -p spotify,%any"
keys += [
    # Volume control
    # Tested with pamixer 1.4.5
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5"), desc="Increase volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5"), desc="Decrease volume"),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc="Toggle mute."),
    # Brightness control
    # Tested with light 1.2
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("xbacklight -inc 10"),
        desc="Increase brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("xbacklight -dec 10"),
        desc="Decrease brightness",
    ),
    # Media player controls
    # Used with https://bit.ly/3hAVW5x
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn(f"{playerctl} play-pause"),
        desc="Play or pause spotify",
    ),
    Key([], "XF86AudioNext", lazy.spawn(f"{playerctl} next"), desc="Next song spotify"),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn(f"{playerctl} previous"),
        desc="Previous song spotify",
    ),
]

# ========== Window movement ========== #
keys += [
    # Change focus between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    # Move window
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    # Resize windows
    Key([mod, "control"], "j", lazy.layout.shrink(), desc="Decrease window size"),
    Key([mod, "control"], "k", lazy.layout.grow(), desc="Increase window size"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Orientation of workspace
    Key([mod], "v", lazy.layout.flip(), desc="Flip layout"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen"),
    # Floating mode
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle floating"),
    # Movement between screens
    Key([mod], "w", lazy.to_screen(0), desc="Switch to screen 0."),
    Key([mod], "e", lazy.to_screen(1), desc="Switch to screen 1."),
]

# ========== Workspace configuration ==========
# Workspaces names, keybinds and default layouts
workspaces = [
    ["1", {"label": "", "layout": "stack"}],
    ["2", {"label": "", "layout": "monadtall"}],
    ["3", {"label": "", "layout": "stack"}],
    ["4", {"label": "", "layout": "monadtall"}],
    ["5", {"label": "", "layout": "stack"}],
    ["6", {"label": "", "layout": "stack"}],
    ["7", {"label": "", "layout": "stack"}],
    ["8", {"label": "", "layout": "stack"}],
]

# Apps default workspace
ws = lambda index: workspaces[index - 1][0]
OPENFORTIVPN = "OpenfortiVPN"
matches = {
    # Browser
    ws(1): [Match(wm_class="firefox"), Match(wm_class="Brave-browser")],
    # Terminal and text editors
    ws(2): [
        Match(wm_class="Emacs"),
        Match(wm_class="st-256color"),
        Match(wm_class="kitty"),
        Match(wm_class="Alacritty"),
    ],
    # Viewers and media editors
    ws(3): [
        Match(wm_class="Inkscape"),
        Match(title="LibreOffice"),
        Match(wm_class="libreoffice-calc"),
        Match(wm_class="libreoffice-writer$"),
        Match(wm_class="Soffice"),
        Match(wm_class="okular"),
        Match(wm_class="Zathura"),
        Match(wm_class="Gimp"),
        Match(wm_class="Gephi 0.9.2"),
        Match(title="Starting Gephi 0.9.2"),
        Match(wm_class="Pcmanfm"),
    ],
    # IDEs
    ws(4): [
        Match(wm_class="jetbrains-pycharm-ce"),
        Match(wm_class="jetbrains-idea-ce"),
        Match(wm_class="java-lang-Thread"),
        Match(wm_class="Eclipse"),
        Match(title="win0", wm_class="jetbrains-idea-ce"),
    ],
    # Social
    ws(5): [
        Match(wm_class="discord"),
        Match(wm_class="Microsoft Teams - Preview"),
        Match(wm_class="Slack"),
        Match(wm_class="zoom"),
        Match(wm_class="whatsapp-nativefier-d40211"),
        Match(wm_class="TelegramDesktop"),
        Match(wm_class="Chromium"),
    ],
    # Media
    ws(6): [
        Match(wm_class="Popcorn-Time"),
        Match(wm_class="Stremio"),
        Match(wm_class="vlc"),
        Match(wm_class="qBittorrent"),
    ],
    # Configuration apps
    ws(7): [
        Match(wm_class="Arandr"),
        Match(wm_class="Pavucontrol"),
        Match(wm_class="Lxappearance"),
        Match(wm_class="Lightdm-settings"),
        Match(wm_class="Font-manager"),
        Match(wm_class="Nvidia-settings"),
        Match(wm_class="Bitwarden"),
        Match(wm_class="qt5ct"),
        Match(wm_class="v4l2ucp"),
        Match(wm_class="DBeaver"),
        Match(wm_class=OPENFORTIVPN),
        Match(wm_class="org.remmina.Remmina"),
    ],
    # Background apps
    ws(8): [Match(wm_class="Spotify"), Match(wm_class="youtube-music-desktop-app")],
}

# _____ Force a match _____ #
force_match = [
    matches[ws(3)][8],
    matches[ws(3)][9],
    matches[ws(8)][0],
]

# _____ Add matches to groups _____ #
for index in range(len(workspaces)):
    if ws(index + 1) in matches:
        workspaces[index][1]["matches"] = matches[ws(index + 1)]

# _____ Create groups _____ #
groups = [Group(name, **kwargs) for name, kwargs in workspaces]

for g in groups:
    keys += [
        # Keybinds for wokspace
        Key(
            [mod],
            g.name,
            lazy.group[g.name].toscreen(toggle=False),
            desc="Switch to group {}".format(g.label),
        ),
        # Move windows to workspace
        Key(
            [mod, "control"],
            g.name,
            lazy.window.togroup(g.name),
            desc="Move focused window to group {}".format(g.name),
        ),
        # Move windows to workspace
        Key(
            [mod, "shift"],
            g.name,
            lazy.window.togroup(g.name, switch_group=True),
            desc="Switch to and move focused window to group {}".format(g.name),
        ),
    ]

# ========== Gaps configuration ========== #
# Borders size
border = 2

# Gaps
gaps = 10

# ========== Application behavior ========== #
# _____ Add keybinds for keypads _____ #
kp0 = "KP_Insert"
kp1 = "KP_End"
kp2 = "KP_Down"
kp3 = "KP_Next"
kp4 = "KP_Left"
kp5 = "KP_Begin"
kp6 = "KP_Right"
kp7 = "KP_Home"
kp8 = "KP_Up"
kp9 = "KP_Prior"

keys += [
    # Keybinds
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch spotify"),
    Key([mod], "i", lazy.spawn(browser), desc="Launch browser"),
    Key(
        [mod],
        "u",
        lazy.spawn(eu("~/.bin/launchers/launchchrome.sh")),
        desc="Launch chromium with copied link",
    ),
    Key(
        [mod, "shift"],
        kp0,
        lazy.spawn(
            f"{terminal} --class {OPENFORTIVPN},{OPENFORTIVPN} "
            + "-e sudo openfortivpn -c /etc/openfortivpn/config"
        ),
        desc="Launch teams",
    ),
    Key([mod, "shift"], kp1, lazy.spawn("slack"), desc="Launch slack"),
    Key([mod, "shift"], kp2, lazy.spawn("arandr"), desc="Launch arandr"),
    Key([mod, "shift"], kp3, lazy.spawn("pavucontrol"), desc="Launch pavucontrol"),
    Key([mod, "shift"], kp4, lazy.spawn("bitwarden-desktop"), desc="Launch bitwarden"),
    Key([mod, "shift"], kp5, lazy.spawn("discord"), desc="Launch discord"),
    Key([mod, "shift"], kp6, lazy.spawn("telegram-desktop"), desc="Launch telegram"),
    Key(
        [mod, "shift"],
        kp7,
        lazy.spawn(eu("~/.bin/launchers/settings-nvidia.sh")),
        desc="Launch nvidia settings",
    ),
    Key([mod, "shift"], kp8, lazy.spawn("popcorntime"), desc="Launch Popcorn time"),
    Key([mod, "shift"], kp9, lazy.spawn("stremio"), desc="Launch stremio"),
]

# Screenshots manager
# Tested with flameshot v0.9.0
keys += [
    Key(
        [],
        "Print",
        lazy.spawn(eu("~/.bin/screenshot.sh")),
        desc="Take screenshot of focused monitor",
    ),
    Key(
        [mod],
        "Print",
        lazy.spawn("flameshot gui -p " + eu("~/pictures/screenshots")),
        desc="Take screenshot with flameshot's GUI",
    ),
    Key(
        ["control"],
        "Print",
        lazy.spawn("flameshot full -c -p " + eu("~/pictures/screenshots")),
        desc="Take screenshot of all screens",
    ),
]

# ========== Aesthetics ========= #
# _____ Function for obtaining the number of monitors _____ #
def get_number_of_monitors() -> int:
    """It gets the number of monitors.

    Returns
    -------
    int
        The number of active non-mirrored monitors.
    """

    try:
        output = subprocess.check_output(
            eu("~/.config/qtile/check_number_of_monitors.sh"), shell=True
        ).decode()[:-1]
    except subprocess.SubprocessError:
        return 0

    return int(output)


n_monitor = get_number_of_monitors()

# Dracula theme for windows
border_focused = "#6272A4"
border_unfocused = "#282A36"

# Dracula theme for bar
colors = {
    "background": "#282A36",
    "background-alt1": "#44475A",
    "foreground": "#F8F8F2",
    "foreground-alt": "#BFBFBF",
    "foreground-alt1": "#6272A4",
    "red": "#FF5555",
    "green": "#50FA7B",
    "yellow": "#F1FA8C",
    "blue": "#BD93D9",
    "magenta": "#FF79C6",
    "cyan": "#8BE9FD",
    "orange": "#FFB86C",
}

# Widget settings
fonts = {
    "Normal": {"font": "JetBrains Mono", "fontsize": 12},
    "Icons": {"font": "FontAwesome", "fontsize": 16},
    "Icons2": {"font": "JetBrainsMono Nerd Font", "fontsize": 16},
}

# Bar sizes
heights = {"bar1": 30, "bar2": 30}

# Padding
padding_left = {"bar1": 0, "bar2": 0}
padding_right = {"bar1": 15, "bar2": 15}

# Widgets class
mw = MyWidgets(colors, fonts, padding_left, padding_right)

# Bar for my first screen
def my_bar1():
    widgets_left = [*mw.widget_groups(), *mw.widget_chord()]
    widgets_center = [*mw.widget_time(add_pipe=False)]
    widgets_right = [
        *mw.widget_spotify(),
        *mw.widget_volume(),
        *mw.widget_layout(),
        *mw.widget_update(),
        *mw.widget_battery(),
        *mw.widget_tray(),
    ]
    widgets = mw.create_widgets(widgets_left, widgets_center, widgets_right, 1)

    # Height of bar
    size = heights["bar1"]

    # Background
    background = colors["background"]

    return {"widgets": widgets, "size": size, "background": background}


# Bar for my second screen
def my_bar2():
    widgets_left = [*mw.widget_groups(mirror=False), *mw.widget_chord()]
    widgets_center = [*mw.widget_time(add_pipe=False)]
    widgets_right = [*mw.widget_cpu(), *mw.widget_ram(), *mw.widget_brightness()]
    widgets = mw.create_widgets(widgets_left, widgets_center, widgets_right, 2)

    # Height of bar
    size = heights["bar2"]

    # Background
    background = colors["background"]

    return {"widgets": widgets, "size": size, "background": background}


# Bar for my only screen
def my_bar_full():
    system_info = [
        *mw.widget_cpu(background="background-alt1"),
        *mw.widget_ram(background="background-alt1"),
        *mw.widget_brightness(background="background-alt1"),
    ]
    widgets_left = [*mw.widget_groups(), *mw.widget_chord()]
    widgets_center = []
    widgets_right = [
        *mw.widget_spotify(max_length=20),
        *mw.widget_volume(),
        *mw.widget_layout(),
        *mw.widget_update(),
        *mw.widget_battery(),
        *mw.widget_group(system_info),
        *mw.widget_time(compact=True),
        *mw.widget_tray(),
    ]
    widgets = mw.create_widgets(widgets_left, widgets_center, widgets_right, 1)

    # Height of bar
    size = heights["bar1"]

    # Background
    background = colors["background"]

    return {"widgets": widgets, "size": size, "background": background}


# _____ Spawn each bar _____ #
if n_monitor == 2:
    screens = [Screen(top=bar.Bar(**my_bar1())), Screen(top=bar.Bar(**my_bar2()))]
else:
    screens = [Screen(top=bar.Bar(**my_bar_full()))]

# ========== Mouse Behavior ========== #
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Change focus with mouse
follow_mouse_focus = True

# Focus window
focus_on_window_activation = "smart"

# Other
bring_front_click = False
cursor_warp = False
auto_fullscreen = True


# ========== Layouts ========== #
# _____ Configuring themes based on previous variables _____ #
layout_theme_tall = {
    "margin": gaps,
    "border_focus": border_focused,
    "border_normal": border_unfocused,
    "border_width": border,
    "align": MonadTall._right,
    "single_border_width": 0,
}
layout_theme_stack = {"margin": gaps, "num_stacks": 1, "border_width": 0}
layout_theme_float = {
    "border_focus": border_focused,
    "border_normal": border_unfocused,
    "border_width": border,
}

# Available layouts
layouts = [MonadTall(**layout_theme_tall), Stack(**layout_theme_stack)]
zoom_rules = [
    Match(wm_class="zoom", title="Settings"),
    Match(wm_class="zoom", title="Choose ONE of the audio conference options"),
    Match(wm_class="zoom", title=None),
]
middle_float = [
    Match(wm_type="dialog"),
    Match(title="win0", wm_class="jetbrains-idea-ce"),
]
dbeaver_items = {
    "class": Match(wm_class="DBeaver"),
    "title": Match(title="DBeaver 21.3.2 "),
    "not_resize": [Match(title="Connection changed "), Match(title="Exit DBeaver ")],
}
floating_layout = Floating(
    float_rules=[
        Match(wm_type="confirm"),
        Match(wm_type="download"),
        Match(wm_type="error"),
        Match(wm_type="file_progress"),
        Match(wm_type="notification"),
        Match(wm_type="splash"),
        Match(wm_type="toolbar"),
        Match(wm_type="confirmreset"),
        Match(wm_type="makebranch"),
        Match(wm_type="maketag"),
        Match(wm_type="notification"),
        Match(wm_type="utility"),
        Match(wm_type="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="meet.google.com is sharing your screen."),
        Match(wm_class="Pinentry-gtk-2"),
        Match(wm_class="Matplotlib"),
        Match(wm_class="flameshot", title="Configuration"),
        Match(wm_class="Inkscape", title="Preferences"),
        Match(wm_class="mpv"),
        Match(wm_class="Sxiv"),
        Match(wm_class="Options Editor"),
        Match(title="Close Firefox"),
        *zoom_rules,
        *middle_float,
    ],
    **layout_theme_float,
)

# ========== Hooks ========== #
# Automatic workspace for apps
@hook.subscribe.client_new
def default_workspaces(window):
    for group in groups:
        if any(match.compare(window) for match in group.matches):
            window.togroup(group.name)
            break


# Startup all apps
@hook.subscribe.startup_once
def autostart():
    script = eu("~/.config/qtile/autostart.sh")
    subprocess.call([script])


# Force a workspace match
@hook.subscribe.client_managed
def force_match_default_workspace(window):
    if any(match.compare(window) for match in force_match):
        default_workspaces(window)


# Change size of floating windows
@hook.subscribe.client_new
def resize_floating_windows(window):

    go_to_middle = False
    if window.window.get_wm_type() == "dialog":
        window.cmd_enable_floating()
        window.cmd_set_size_floating(900, 700)
    elif any(rule.compare(window) for rule in zoom_rules):
        window.cmd_enable_floating()
        if zoom_rules[0].compare(window):
            window.cmd_set_size_floating(900, 700)
    elif (
        dbeaver_items["class"].compare(window)
        and not dbeaver_items["title"].compare(window)
        and not any(rule.compare(window) for rule in dbeaver_items["not_resize"])
    ):
        window.cmd_enable_floating()
        window.cmd_set_size_floating(900, 700)
        go_to_middle = True

    # Move to middle of screen
    go_to_middle |= any(rule.compare(window) for rule in middle_float)
    if go_to_middle:
        screen = window.qtile.current_screen
        size = window.cmd_get_size()
        x, y = screen.x, screen.y
        window.cmd_set_position_floating(
            x + int((screen.width - size[0]) / 2),
            y + int((screen.height - size[1]) / 2),
        )


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
