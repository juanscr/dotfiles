from libqtile import widget
from os.path import expanduser as eu

class MyWidgets:
    def __init__(self, colors, fonts, padding_left, padding_right):
        self.fonts = fonts
        self.colors = colors
        self.padding_left = padding_left
        self.padding_right = padding_right
        self.store = {}

    def widget_groups(self, mirror=True):
        """Widget for displaying groups."""
        if 'widget_groups' in self.store and mirror:
            return self.store['widget_groups']

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
                      urgent_border              = self.colors['red'],
                      block_highlight_text_color = self.colors['green'])

        self.store['widget_groups'] = [widget.GroupBox(**config)]
        return self.store['widget_groups']

    def widget_layout(self, add_sep=True, add_pipe=True, mirror=True):
        """Module for showing layout and number of windows."""
        if 'widget_layout' in self.store and mirror:
            return self.store['widget_layout']

        # Widget for layout
        config = dict(custom_icon_paths = [eu("~/.config/qtile/icons")],
                      scale             = 0.5,
                      padding           = -5,
                      foreground        = self.colors['green'])
        widget_layout = widget.CurrentLayoutIcon(**config)

        # Widget for number of windows
        config = dict(**self.fonts['Normal'],
                      foreground = self.colors['green'],
                      show_zero  = True)
        widget_nw = widget.WindowCount(**config)

        widgets = [widget_layout, widget_nw]

        if add_sep:
            widgets += [widget.Spacer(length=5)]
        if add_pipe:
            pipe = widget.TextBox(**self.fonts['Normal'],
                                  text       = '|',
                                  foreground = self.colors['green'])
            widgets = [pipe, widget.Spacer(length = 5)] + widgets

        self.store['widget_layout'] = widgets
        return widgets

    def widget_update(self, add_sep=True, add_pipe=True, mirror=True):
        """Module for displaying updates."""
        if 'widget_update' in self.store and mirror:
            return self.store['widget_update']

        # Icon
        w_update_icon = widget.TextBox(**self.fonts['Icons2'],
                                       text    = 'ﮮ',
                                       foreground = self.colors['yellow'],
                                       padding = 8)

        # Text
        config = dict(**self.fonts['Normal'],
                      distro              = 'Arch',
                      colour_have_updates = self.colors['yellow'],
                      colour_no_updates   = self.colors['yellow'],
                      no_update_string    = '0',
                      display_format      = '{updates}',
                      padding             = 0,
                      update_interval     = 1800)
        w_update_text = widget.CheckUpdates(**config)

        widgets = [w_update_icon, w_update_text]

        if add_sep:
            widgets += [widget.Spacer(length=8)]
        if add_pipe:
            pipe = widget.TextBox(**self.fonts['Normal'],
                                  text       = '|',
                                  foreground = self.colors['yellow'])
            widgets = [pipe] + widgets

        self.store['widget_update'] = widgets
        return widgets

    def widget_time(self, mirror=True):
        """Widget for displaying the time."""
        if 'widget_time' in self.store and mirror:
            return self.store['widget_time']

        # Icon
        w_clock_icon = widget.TextBox(**self.fonts['Icons2'],
                                      text    = ' ',
                                      padding = 6)

        # Text
        widget_clock = widget.Clock(**self.fonts['Normal'],
                                    format = '%a, %d %b   %H:%M')

        return [w_clock_icon, widget_clock]

    def widget_battery(self, add_sep=True, add_pipe=True):
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
                    low_foreground  = self.colors['orange'],
                    foreground      = self.colors['orange'],
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
            widgets += [widget.Spacer(length=5)]
        if add_pipe:
            pipe = widget.TextBox(**self.fonts['Normal'],
                                  text       = '|',
                                  foreground = self.colors['orange'])
            widgets = [pipe, widget.Spacer(length = 5)] + widgets

        self.store['widget_time'] = widgets
        return widgets

    def widget_tray(self, add_pipe=True):
        """Widget for displaying system tray."""
        config = dict(background = self.colors['background'],
                      icon_size = 16,
                      padding = 15)
        widget_systray = widget.Systray(**config)
        widgets = [widget_systray]

        if add_pipe:
            pipe = widget.TextBox(**self.fonts['Normal'],
                                  text       = '|',
                                  foreground = self.colors['foreground'],
                                  padding    = -2)
            widgets = [pipe] + widgets

        return widgets

    def widget_chord(self, mirror=True):
        """Widget for showing key chords."""
        if 'widget_chord' in self.store and mirror:
            return self.store['widget_chord']

        config = dict(**self.fonts['Normal'],

                      # Formatting
                      background     = self.colors['background-alt1'],
                      foreground     = self.colors['foreground'],
                      padding        = 3,
                      name_transform = lambda name: f' {name} ')
        widget_chord = widget.Chord(**config)

        self.store['widget_chord'] = [widget_chord]
        return self.store['widget_chord']

    def widget_spotify(self, add_sep=True, mirror=True):
        """Widget for showing spotify."""
        if 'widget_spotify' in self.store and mirror:
            return self.store['widget_spotify']

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

        self.store['widget_spotify'] = widgets
        return widgets

    def create_widgets(self, widgets_left, widgets_center, widgets_right,
                       screen):
        """It creates the widgets list by section"""

        # Padding for bar
        paddingl = self.padding_left[f'bar{screen}']
        paddingr = self.padding_right[f'bar{screen}']

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
