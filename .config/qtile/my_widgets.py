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
