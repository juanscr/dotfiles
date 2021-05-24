from libqtile import widget

class MyWidgets:
    def __init__(self, colors, fonts):
        self.fonts = fonts
        self.colors = colors

    def get_groups(self):
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
