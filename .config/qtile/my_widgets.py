from libqtile import widget
from os.path import expanduser as eu

class MyWidgets:
    def __init__(self, colors, fonts):
        self.fonts = fonts
        self.colors = colors

    def widget_groups(self):
        """Widget for displaying groups."""
        config = dict(**self.fonts['Icons'],

                      # Base configuration
                      background = self.colors['background'],
                      foreground = self.colors['foreground'],

                      # Mouse behavior
                      disable_drag    = True,
                      use_mouse_wheel = False,

                      # Foreground colors
                      active      = self.colors['foreground'],
                      inactive    = self.colors['foreground-alt1'],
                      urgent_text = self.colors['foreground'],

                      # Spacing
                      margin_y  = 2,
                      spacing   = 0,
                      padding_x = 10,
                      borderwidth = 2,

                      # Highlight colors
                      highlight_method           = 'line',
                      urgent_alert_method        = 'line',
                      highlight_color            = self.colors['background-alt1'],
                      this_current_screen_border = self.colors['green'],
                      other_screen_border        = self.colors['blue'],
                      urgent_border              = self.colors['red'])

        return [widget.GroupBox(**config)]

    def widget_layout(self, add_sep=True):
        """Module for showing layout and number of windows."""

        # Widget for layout
        config = dict(custom_icon_paths = [eu("~/.config/qtile/icons")],
                      scale             = 0.5,
                      padding           = -5)
        widget_layout = widget.CurrentLayoutIcon(**config)

        # Widget for number of windows
        config = dict(**self.fonts['Normal'],
                      show_zero = True)
        widget_nw = widget.WindowCount(**config)

        widgets = [widget_layout, widget_nw]

        if add_sep:
            return widgets + [widget.Spacer(length=4)]

        return widgets

    def widget_update(self, add_sep=True):
        """Module for displaying updates."""

        # Icon
        w_update_icon = widget.TextBox(**self.fonts['Icons2'],
                                       text    = 'ﮮ',
                                       padding = 8)

        # Text
        config = dict(**self.fonts['Normal'],
                      distro              = 'Arch',
                      colour_have_updates = self.colors['foreground'],
                      colour_no_updates   = self.colors['foreground'],
                      no_update_string    = '0',
                      display_format      = '{updates}',
                      padding             = 0)
        w_update_text = widget.CheckUpdates(**config)

        widgets = [w_update_icon, w_update_text]

        if add_sep:
            return widgets + [widget.Spacer(length=10)]

        return widgets

    def widget_time(self):
        """Widget for displaying the time."""

        # Icon
        w_clock_icon = widget.TextBox(**self.fonts['Icons2'],
                                      text    = '',
                                      padding = 6)

        # Text
        widget_clock = widget.Clock(**self.fonts['Normal'],
                                    format = '%a, %d %b   %H:%M')

        return [w_clock_icon, widget_clock]

    def widget_battery(self, add_sep=False):
        """Widget for displaying battery usage."""

        # Widget for icon battery
        config = dict(**self.fonts['Icons2'],

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
                    low_foreground  = self.colors['red'],
                    foreground      = self.colors['foreground'],
                    background      = self.colors['background'])
        w_battery_icon = widget.Battery(**config)

        # Widget for the percentage of the battery
        config = dict(**self.fonts['Normal'],

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

        widgets = [w_battery_icon, w_battery_text]
        if add_sep:
            return widgets + [widget.Spacer(length=10)]

        return widgets

    def widget_tray(self):
        """Widget for displaying system tray."""

        # Separate between systray end everything else
        config = dict(text = '',
                      foreground = self.colors['background-alt1'],
                      background = self.colors['background'],
                      padding = -9,
                      fontsize = 55,
                      font = self.fonts['Normal']['font'])
        widget_sep = widget.TextBox(**config)

        # Systay
        config = dict(background = self.colors['background-alt1'],
                      icon_size = 16,
                      padding = 15)
        widget_systray = widget.Systray(**config)

        return [widget_sep, widget_systray]

    def widget_chord(self):
        """Widget for showing key chords."""

        config = dict(**self.fonts['Normal'],

                      # Formatting
                      background     = self.colors['background-alt1'],
                      foreground     = self.colors['foreground'],
                      padding        = 3,
                      name_transform = lambda name: f' {name} ')
        widget_chord = widget.Chord(**config)

        return [widget_chord]

    def widget_spotify(self, add_sep=True):
        """Widget for showing spotify."""

        config = dict(**self.fonts['Normal'],
                      name             = 'spotify',
                      objname          = "org.mpris.MediaPlayer2.spotify",
                      display_metadata = ['xesam:artist', 'xesam:title'],
                      scroll_chars     = 15,
                      stop_pause_text  = 'IDLE')
        widget_spotify = widget.Mpris2(**config)

        widgets = [widget_spotify]
        if add_sep:
            return widgets + [widget.Spacer(length=10)]

        return widgets
