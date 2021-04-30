# ===============================================
#
#              qtile 0.17.0 config
#
# ===============================================

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.dgroups import simple_key_binder
from libqtile.lazy import lazy

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
        Key([], "r", lazy.spwan("systemctl reboot"), desc="Reboot PC"),
        Key([], "p", lazy.spwan("systemctl poweroff"), desc="Shutdown")
    ], mode="exit: [l]ogout, [r]eboot, [p]oweroff"),

    # Search for app. Customized to use dracula theme.
    # Tested with dmenu 5.0
    Key([mod], "d", lazy.spawn('dmenu_run'), desc="Spawn dmenu"),

    # Select monitor layout
    Key([mod, "shift"], "a", lazy.spwan("$HOME/.bin/select-monitor.sh"),
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
]

[
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

]

# ========== Workspace configuration ==========
# Configuration for workspaces (label, key)
group_names = [("1", "1"),
               ("2", "2"),
               ("3", "3"),
               ("4", "4"),
               ("5", "5"),
               ("6", "6"),
               ("7", "7"),
               ("8", "8"),
               ("9", "9"),
               ("10", "0"),
               ("11", "p")]

# Apps default workspace
matches = {
    # Browser
    groups[0][0]: [Match(wm_class=["Brave-browser",
                                   "firefox"])],

    # Terminal and text editors
    groups[1][0]: [Match(wm_class=["Emacs",
                                   "Gedit",
                                   "st-256color",
                                   "kitty",
                                   "Alacritty"])],

    # Viewers and media editors
    groups[2][0]: [Match(title=["LibreOffice"],
                         wm_class=["Evince",
                                   "Inkscape",
                                   "libreoffice-calc",
                                   "libreoffice-writer$",
                                   "Soffice",
                                   "okular",
                                   "Zathura",
                                   "Gimp",
                                   "Gephi 0.9.2"])],

    # IDEs
    groups[3][0]: [Match(wm_class=["jetbrains-pycharm-ce",
                                   "java-lang-Thread",
                                   "Java",
                                   "Eclipse"])],

    # Social
    groups[4][0]: [Match(wm_class=["discord",
                                   "Microsoft Teams - Preview",
                                   "Slack",
                                   "zoom",
                                   "whatsapp-nativefier-d40211",
                                   "TelegramDesktop",
                                   "Chromium"])],

    # Media
    groups[5][0]: [Match(wm_class=["ffplay",
                                   "Popcorn-Time",
                                   "Stremio",
                                   "vlc",
                                   "qBittorrent"])],

    # Configuration apps
    groups[6][0]: [Match(wm_class=["Arandr",
                                   "Pavucontrol",
                                   "Lxappearance",
                                   "Lightdm-settings",
                                   "Font-manager",
                                   "Nvidia-settings",
                                   "Bitwarden"])],

    # Production apps
    groups[7][0]: [Match(wm_class=["Audacity",
                                   "kdenlive",
                                   "Ntcardvt"])],

    # Miscellaneous apps
    groups[8][0]: [Match(wm_class=["VirtualBox Manager",
                                   "^Steam$"])],

    # Background apps
    groups[9][0]: [Match(wm_class=["Spotify",
                                   "youtube-music-desktop-app"])],
}

# Add matches to groups
kwargs = {}
for x in group_names:
    kwargs[x[0]] = {}
    if x[0] in matches:
        kwargs[x[0]]['matches'] = matches[x[0]]

# Create workspaces
groups = list(map(lambda x: Group(x[0], **kwargs[x[0]]), group_names))

# Create keybinds
keys = list(map(lambda x: x[1], group_names))
dgroups_key_binder = simple_key_binder(mod, keynames=keys)

for i in groups:
    keys.extend([

        # Keybinds for each wokspace
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.label)),

        # Move windows to workspace
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.MonadTall(),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
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
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# ========== Hooks ==========
# Automatic workspace for apps
@hook.subscribe.client_new
def default_workspaces(window):
    for group in groups:
        if any(match.compare(window) for match in group.matches):
            window.togroup(group.label)
            break

# Spotify assignment
@hook.subscribe.client_managed
def assign_spotify(window):
    if window.window.get_wm_class() == "Spotify":
        window.togroup(groups[-1].label)

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
