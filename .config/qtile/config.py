# =============================================== #
#                                                 #
#                                                 #
#              qtile 0.17.0 config                #
#                                                 #
# =============================================== #

import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from os.path import expanduser as eu

# Mod key
mod = "mod4"

# Terminal
terminal = "alacritty"

# Browser
browser = "firefox"

# ============ Basic Behavior ============
keys = [
    # Close window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Restart qtile
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),

    # Exit qtile
    KeyChord([mod, "shift"], "e", [
        Key([], "l", lazy.shutdown(), desc="Log off"),
        Key([], "r", lazy.spawn("systemctl reboot"), desc="Reboot PC"),
        Key([], "p", lazy.spawn("systemctl poweroff"), desc="Shutdown")
    ], mode="exit: [l]ogout, [r]eboot, [p]oweroff"),

    # Search for app. Customized to use dracula theme.
    # Tested with dmenu 5.0
    Key([mod], "d", lazy.spawn('dmenu_run'), desc="Spawn dmenu"),

    # Select monitor layout
    Key([mod, "shift"], "a", lazy.spawn(eu("~/.bin/select-monitor.sh")),
        desc="Select monitor layout using script"),
]

# ============ Media Controls ============
keys += [
    # Volume control
    # Tested with pamixer 1.4.5
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5"),
        desc="Increase volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5"),
        desc="Decrease volume"),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc="Toggle mute."),

    # Brightness control
    # Tested with light 1.2
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10"),
        desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10"),
        desc="Decrease brightness"),

    # Media player controls
    # Used with https://bit.ly/3hAVW5x
    Key([], "XF86AudioPlay", lazy.spawn("spotifyctl playpause"),
        desc="Play or pause spotify"),
    Key([], "XF86AudioNext", lazy.spawn("spotifyctl next"),
        desc="Next song spotify"),
    Key([], "XF86AudioPrev", lazy.spawn("spotifyctl previous"),
        desc="Previous song spotify")
]

# ========== Window movement ========== #
keys += [
    # Change focus between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),

    # Move window
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Orientation of workspace
    Key([mod], "v", lazy.layout.flip(), desc="Flip layout"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='Fullscreen'),

    # Floating mode
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle floating"),

    # Movement between screens
    Key([mod], "w", lazy.to_screen(0), desc="Switch to screen 0."),
    Key([mod], "e", lazy.to_screen(1), desc="Switch to screen 1."),
]

# ========== Workspace configuration ==========
# Workspaces names, keybinds and default layouts
workspaces = [["1", {"label": "",  "layout": "stack"}],
              ["2", {"label": "",  "layout": "monadtall"}],
              ["3", {"label": "",  "layout": "stack"}],
              ["4", {"label": "",  "layout": "monadtall"}],
              ["5", {"label": "",  "layout": "stack"}],
              ["6", {"label": "",  "layout": "stack"}],
              ["7", {"label": "",  "layout": "stack"}],
              ["8", {"label": "",  "layout": "stack"}],
              ["9", {"label": "",  "layout": "stack"}],
              ["0", {"label": "",  "layout": "stack"}],
              ["p", {"label": "",  "layout": "monadtall"}]]

# Apps default workspace
ws = lambda index: workspaces[index - 1][0]
matches = {
    # Browser
    ws(1): [Match(wm_class="firefox")],

    # Terminal and text editors
    ws(2): [Match(wm_class="Emacs"),
            Match(wm_class="st-256color"),
            Match(wm_class="kitty"),
            Match(wm_class="Alacritty")],

    # Viewers and media editors
    ws(3): [Match(wm_class="Inkscape"),
            Match(title="LibreOffice"),
            Match(wm_class="libreoffice-calc"),
            Match(wm_class="libreoffice-writer$"),
            Match(wm_class="Soffice"),
            Match(wm_class="okular"),
            Match(wm_class="Zathura"),
            Match(wm_class="Gimp"),
            Match(wm_class="Gephi 0.9.2"),
            Match(title="Starting Gephi 0.9.2")],

    # IDEs
    ws(4): [Match(wm_class="jetbrains-pycharm-ce"),
            Match(wm_class="java-lang-Thread"),
            Match(wm_class="Java"),
            Match(wm_class="Eclipse")],

    # Social
    ws(5): [Match(wm_class="discord"),
            Match(wm_class="Microsoft Teams - Preview"),
            Match(wm_class="Slack"),
            Match(wm_class="zoom"),
            Match(wm_class="whatsapp-nativefier-d40211"),
            Match(wm_class="TelegramDesktop"),
            Match(wm_class="Chromium")],

    # Media
    ws(6): [Match(wm_class="Popcorn-Time"),
            Match(wm_class="Stremio"),
            Match(wm_class="vlc"),
            Match(wm_class="qBittorrent")],

    # Configuration apps
    ws(7): [Match(wm_class="Arandr"),
            Match(wm_class="Pavucontrol"),
            Match(wm_class="Lxappearance"),
            Match(wm_class="Lightdm-settings"),
            Match(wm_class="Font-manager"),
            Match(wm_class="Nvidia-settings"),
            Match(wm_class="Bitwarden"),
            Match(wm_class="qt5ct")],

    # Production apps
    ws(8): [Match(wm_class="Audacity"),
            Match(wm_class="kdenlive")],

    # Miscellaneous apps
    ws(9): [Match(wm_class="VirtualBox Manager"),
            Match(wm_class="^Steam$")],

    # Background apps
    ws(10): [Match(wm_class="Spotify"),
             Match(wm_class="youtube-music-desktop-app")]
}

# _____ Force a match _____ #
force_match = [
    matches[ws(3)][8],
    matches[ws(3)][9],
    matches[ws(9)][1],
    matches[ws(10)][0]
]

# _____ Add matches to groups _____ #
for index in range(len(workspaces)):
    if ws(index + 1) in matches:
        workspaces[index][1]['matches'] = matches[ws(index + 1)]

# _____ Create groups _____ #
groups = [Group(name, **kwargs) for name, kwargs in workspaces]

for g in groups:
    keys += [
        # Keybinds for wokspace
        Key([mod], g.name, lazy.group[g.name].toscreen(toggle=False),
            desc="Switch to group {}".format(g.label)),

        # Move windows to workspace
        Key([mod, "control"], g.name, lazy.window.togroup(g.name),
            desc="Move focused window to group {}".format(g.name)),

        # Move windows to workspace
        Key([mod, "shift"], g.name,
            lazy.window.togroup(g.name, switch_group=True),
            desc="Switch to and move focused window to group {}".format(g.name))
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
    Key([mod, "shift"], "s", lazy.spawn("ytmdesktop"),
        desc="Launch youtube desktop"),
    Key([mod], "i", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "u", lazy.spawn(eu("~/.bin/launchers/launchchrome.sh")),
        desc="Launch chromium with copied link"),

    Key([mod, "shift"], kp0, lazy.spawn("teams"), desc="Launch teams"),
    Key([mod, "shift"], kp1, lazy.spawn("slack"), desc="Launch slack"),
    Key([mod, "shift"], kp2, lazy.spawn("arandr"), desc="Launch arandr"),
    Key([mod, "shift"], kp3, lazy.spawn("pavucontrol"),
        desc="Launch pavucontrol"),
    Key([mod, "shift"], kp4, lazy.spawn("bitwarden"), desc="Launch bitwarden"),
    Key([mod, "shift"], kp5, lazy.spawn("whatsapp"), desc="Launch whatsapp"),
    Key([mod, "shift"], kp6, lazy.spawn(eu("~/.bin/launchers/launch-telegram.sh")),
        desc="Launch telegram"),
    Key([mod, "shift"], kp7, lazy.spawn(eu("~/.bin/launchers/settings-nvidia.sh")),
        desc="Launch nvidia settings"),
    Key([mod, "shift"], kp8, lazy.spawn("popcorntime"),
        desc="Launch Popcorn time"),
    Key([mod, "shift"], kp9, lazy.spawn("stremio"), desc="Launch stremio")
]

# Screenshots manager
# Tested with flameshot v0.9.0
keys += [
    Key([], "Print", lazy.spawn(eu("~/.bin/screenshot.sh")),
        desc="Take screenshot of focused monitor"),
    Key([mod], "Print",
        lazy.spawn("flameshot gui -p " + eu("~/pictures/screenshots")),
        desc="Take screenshot with flameshot's GUI"),
    Key(["control"], "Print",
        lazy.spawn("flameshot full -c -p " + eu("~/pictures/screenshots")),
        desc="Take screenshot of all screens")
]

# ========== Aesthetics ========= #
# Dracula theme for windows
border_focused = "#6272A4"
border_unfocused = "#282A36"

# Dracula theme for bar
colors = {'background':      '#282A36',
          'background-alt1': '#44475A',
          'foreground':      '#F8F8F2',
          'foreground-alt':  '#BFBFBF',
          'foreground-alt1': '#6272A4',
          'red':             '#FF5555',
          'green':           '#50FA7B',
          'yellow':          '#F1FA8C',
          'blue':            '#BD93D9',
          'magenta':         '#FF79C6',
          'cyan':            '#8BE9FD',
          'orange':          '#FFB86C'}

# Widget settings
fonts = {'Normal': {'font': 'JetBrainsMono Nerd Font', 'fontsize': 14},
         'Icons':  {'font': 'FontAwesome',             'fontsize': 18},
         'Icons2': {'font': 'JetBrainsMono Nerd Font', 'fontsize': 18}}

# Bar sizes
heights = {'bar1': 30, 'bar2': 30}

# Padding
padding_left = {'bar1': 0, 'bar2': 0}
padding_right = {'bar1': 15, 'bar2': 15}

### Widgets
# Widget for displaying groups
config = dict(**fonts['Icons'],

              # Base configuration
              background = colors['background'],
              foreground = colors['foreground'],

              # Mouse behavior
              disable_drag    = True,
              use_mouse_wheel = False,

              # Foreground colors
              active      = colors['foreground'],
              inactive    = colors['foreground-alt1'],
              urgent_text = colors['foreground'],

              # Spacing
              margin_y  = 2,
              spacing   = 0,
              padding_x = 10,
              borderwidth = 2,

              # Highlight colors
              highlight_method           = 'line',
              urgent_alert_method        = 'line',
              highlight_color            = colors['background-alt1'],
              this_current_screen_border = colors['green'],
              other_screen_border        = colors['blue'],
              urgent_border              = colors['red'])
widget_groups = widget.GroupBox(**config)


# Widget for layout
config = dict(custom_icon_paths = [eu("~/.config/qtile/icons")],
              scale             = 0.5,
              padding           = -5)
widget_layout = widget.CurrentLayoutIcon(**config)

# Widget for number of windows
config = dict(**fonts['Normal'],
              show_zero = True)
widget_nw = widget.WindowCount(**config)


# Widget for displaying time
widget_clock = widget.Clock(**fonts['Normal'],
                            format = '%a, %d %b   %H:%M')
w_clock_icon = widget.TextBox(**fonts['Icons2'],
                              text    = '',
                              padding = 6)


# Widget for system tray
widget_systray = widget.Systray(background = colors['background-alt1'],
                                icon_size  = 16,
                                padding    = 15)


# Widget for icon battery
config = dict(**fonts['Icons2'],

              # Formatting options
              format          = '{char}',
              show_short_text = False,
              padding         = 4,

              # Icons for each state
              charge_char    = '',
              full_char      = '',
              empty_char     = '',
              discharge_char = '',
              unknown_char   = '',

              # Other options
              update_interval = 1,
              low_percentage  = 0.15,
              low_foreground  = colors['red'],
              foreground      = colors['foreground'],
              background      = colors['background'])
w_battery_icon = widget.Battery(**config)

# Widget for the percentage of the battery
config = dict(**fonts['Normal'],

              # Formatting options
              format          = '{percent:2.0%} ',
              show_short_text = False,
              padding         = 0,

              # Other options
              update_interval = config['update_interval'],
              low_percentage  = config['low_percentage'],
              low_foreground  = config['foreground'],
              foreground      = config['foreground'],
              background      = config['background'])
w_battery_text = widget.Battery(**config)


# Widget for key chords
widget_chord = widget.Chord(**fonts['Normal'],

                            # Formatting
                            background     = colors['background-alt1'],
                            foreground     = colors['foreground'],
                            padding        = 3,
                            name_transform = lambda name: f' {name} ')

# Check updates text and icon
w_update_icon = widget.TextBox(**fonts['Icons2'],
                               text    = 'ﮮ',
                               padding = 8)
w_update_text = widget.CheckUpdates(**fonts['Normal'],

                                    # Config
                                    distro              = 'Arch',
                                    colour_have_updates = colors['foreground'],
                                    colour_no_updates   = colors['foreground'],
                                    no_update_string    = '0',
                                    display_format      = '{updates}',
                                    padding             = 0)

# Mpris widget for spotify
widget_spotify = widget.Mpris2(**fonts['Normal'],
                               name='spotify',
                               objname="org.mpris.MediaPlayer2.spotify",
                               display_metadata=['xesam:artist', 'xesam:title'],
                               scroll_chars=15,
                               stop_pause_text='IDLE')

# _____ Method for creating widgets with padding _____ #
def create_widgets(widgets_left, widgets_center, widgets_right, screen):
    # Padding for bar
    paddingl = padding_left[f'bar{screen}']
    paddingr = padding_right[f'bar{screen}']

    widgets = []

    # Add left
    if len(widgets_left) > 0:
        background = widgets_left[0].background
        space = widget.Spacer(length=paddingl, background=background)
        widgets += [space] + widgets_left

    # Add center
    if len(widgets_center) > 0:
        widgets += [widget.Spacer()] + widgets_center + [widget.Spacer()]

    # Add right
    if len(widgets_right) > 0:
        if len(widgets_center) == 0:
            widgets += [widget.Spacer()]

        background = widgets_right[-1].background
        space = widget.Spacer(length=paddingr, background=background)
        widgets += widgets_right + [space]
    elif len(widgets_center) > 0:
        widgets += [widget.TextBox()]

    return widgets

# Bar for my first screen
def my_bar1():
    # Separate between systray end everything else
    config = dict(text = '',
                foreground = colors['background-alt1'],
                background = colors['background'],
                padding = -9,
                fontsize = 55,
                font = fonts['Normal']['font'])
    widget_sep = widget.TextBox(**config)

    # Separate modules
    w_sep = widget.Spacer(length = 10)
    w_sep1 = widget.Spacer(length = 4)

    # Other widgets
    widgets_left = [widget_groups, widget_chord]
    widgets_center = [w_clock_icon, widget_clock]
    widgets_right = [widget_layout, widget_nw, w_sep1, w_update_icon,
                     w_update_text, w_sep, w_battery_icon, w_battery_text,
                     widget_sep, widget_systray]
    widgets = create_widgets(widgets_left, widgets_center, widgets_right, 1)

    # Height of bar
    size = heights['bar1']

    # Background
    background = colors['background']

    return {'widgets': widgets, 'size': size, 'background': background}

# Bar for my second screen
def my_bar2():
    widgets_left = [widget_groups, widget_layout]
    widgets_center = [w_clock_icon, widget_clock]
    widgets_right = []
    widgets = create_widgets(widgets_left, widgets_center, widgets_right, 2)

    # Height of bar
    size = heights['bar2']

    # Background
    background = colors['background']

    return {'widgets': widgets, 'size': size, 'background': background}

# _____ Spawn each bar _____ #
screens = [Screen(top=bar.Bar(**my_bar1())),
           Screen(top=bar.Bar(**my_bar2()))]

# ========== Mouse Behavior ========== #
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
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
layout_theme_tall  = {'margin': gaps,
                      'border_focus': border_focused,
                      'border_normal': border_unfocused,
                      'border_width': border,
                      'align': layout.MonadTall._right,
                      'single_border_width': 0}
layout_theme_stack = {'margin': gaps,
                      'num_stacks': 1,
                      'border_width': 0}
layout_theme_float = {'border_focus': border_focused,
                      'border_normal': border_unfocused,
                      'border_width': border}

# Available layouts
layouts = [layout.MonadTall(**layout_theme_tall),
           layout.Stack(**layout_theme_stack)]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **layout_theme_float)

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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
