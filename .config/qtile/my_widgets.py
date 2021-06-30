from __future__ import annotations
import functools

from libqtile.widget.base import _Widget
from libqtile.widget.battery import Battery
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.chord import Chord
from libqtile.widget.clock import Clock
from libqtile.widget.currentlayout import CurrentLayoutIcon
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.mpris2widget import Mpris2
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.textbox import TextBox
from libqtile.widget.window_count import WindowCount
from os.path import expanduser as eu
from typing import Any, Callable

def add_mirror(
        func: Callable[..., list[_Widget]]
) -> Callable[..., list[_Widget]]:
    """It adds the mirror parameter to the function.

    Parameters
    ----------
    func: Callable[..., list[_Widget]]
        The function that creates the widgets.

    Returns
    -------
    Callable[..., list[_Widget]]
        The new function that stores the result in the object.
    """

    @functools.wraps(func)
    def wrapper(self: MyWidgets, *args: Any, **kwargs: Any) -> list[_Widget]:
        """It stores the result of the function or returns the stored value.

        Parameters
        ----------
        self: MyWidgets
            The object to store the result.
        args: Any
            The positional arguments of the function.
        kwargs: Any
            The named arguments of the function.

        Returns
        -------
        list[libqtile.base._Widget]
            The list of the widgets.
        """

        name_func = func.__name__
        mirror = kwargs.pop('mirror', True)
        if name_func in self.store and mirror:
            return self.store[name_func]

        result = func(self, *args, **kwargs)
        self.store[name_func] = result
        return result

    return wrapper


class MyWidgets:
    """Class to store all my favorite configuration for my used widgets for the
    qtile bar.

    Attributes
    ----------
    colors: dict[str, str]
        A mapping between the color name and the color in hex. The colors
        currently used right now are background, background-alt1, foreground,
        foreground-alt1, green, orange, yellow and blue.
    fonts: dict[str, dict[str, Any]]
        The name for the font and their configuration. Currently, the Icons,
        Icons2 and Normal font are being used.
    padding_left: dict[str, int]
        A map between the screen ('bar_X') to their padding. This is the space
        between the start of the bar and the first widget.
    padding_right: dict[str, int]
        A map between the screen ('bar_X') to their padding. This is the space
        between the end of the bar and the last widget.
    store: dict[str, list[_Widget]]
        The already created widgets.
    """

    def __init__(
            self,
            colors: dict[str, str],
            fonts: dict[str, dict[str, Any]],
            padding_left: dict[str, int],
            padding_right: dict[str, int]
    ) -> None:

        self.fonts: dict[str, dict[str, Any]] = fonts
        self.colors: dict[str, str] = colors
        self.padding_left: dict[str, int] = padding_left
        self.padding_right: dict[str, int] = padding_right
        self.store: dict[str, list[_Widget]] = {}

    @add_mirror
    def widget_groups(self) -> list[_Widget]:
        """Widget for displaying groups.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        config = dict(
            **self.fonts['Icons'],

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
            block_highlight_text_color = self.colors['green']
        )

        return [GroupBox(**config)]

    @add_mirror
    def widget_layout(
            self,
            add_sep: bool = True,
            add_pipe: bool = True
    ) -> list[_Widget]:
        """Module for showing layout and number of windows.

        Parameters
        ----------
        add_sep: bool, optional
            Add a space to the right. Default: True.
        add_pipe: bool, optional
            Add a pipe separator to the left. Default: True.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        # Widget for layout
        config = dict(custom_icon_paths = [eu("~/.config/qtile/icons")],
                      scale             = 0.5,
                      padding           = -5,
                      foreground        = self.colors['green'])
        widget_layout = CurrentLayoutIcon(**config)

        # Widget for number of windows
        config = dict(**self.fonts['Normal'],
                      foreground = self.colors['green'],
                      show_zero  = True)
        widget_nw = WindowCount(**config)

        widgets = [widget_layout, widget_nw]

        if add_sep:
            widgets += [Spacer(length=5)]
        if add_pipe:
            pipe = TextBox(**self.fonts['Normal'],
                           text       = '|',
                           foreground = self.colors['green'])
            widgets = [pipe, Spacer(length = 5)] + widgets

        return widgets

    @add_mirror
    def widget_update(
            self,
            add_sep: bool = True,
            add_pipe: bool = True
    ) -> list[_Widget]:
        """Module for displaying updates.

        Requirements
        ------------
        - pacman-contrib

        Parameters
        ----------
        add_sep: bool, optional
            Add a space to the right. Default: True.
        add_pipe: bool, optional
            Add a pipe separator to the left. Default: True.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        # Icon
        w_update_icon = TextBox(**self.fonts['Icons2'],
                                text    = 'ﮮ',
                                foreground = self.colors['yellow'],
                                padding    = 8)

        # Text
        config = dict(**self.fonts['Normal'],
                      distro              = 'Arch_checkupdates',
                      colour_have_updates = self.colors['yellow'],
                      colour_no_updates   = self.colors['yellow'],
                      no_update_string    = '0',
                      display_format      = '{updates}',
                      padding             = 0,
                      update_interval     = 60)
        w_update_text = CheckUpdates(**config)

        widgets = [w_update_icon, w_update_text]

        if add_sep:
            widgets += [Spacer(length=8)]
        if add_pipe:
            pipe = TextBox(**self.fonts['Normal'],
                           text       = '|',
                           foreground = self.colors['yellow'])
            widgets = [pipe] + widgets

        return widgets

    @add_mirror
    def widget_time(self) -> list[_Widget]:
        """Widget for displaying the time.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        # Icon
        w_clock_icon = TextBox(**self.fonts['Icons2'],
                               text    = ' ',
                               padding = 6)

        # Text
        widget_clock = Clock(**self.fonts['Normal'],
                             format = '%a, %d %b   %H:%M')

        return [w_clock_icon, widget_clock]

    @add_mirror
    def widget_battery(
            self,
            add_sep: bool = True,
            add_pipe: bool = True
    ) -> list[_Widget]:
        """Widget for displaying battery usage.

        Parameters
        ----------
        add_sep: bool, optional
            Add a space to the right. Default: True.
        add_pipe: bool, optional
            Add a pipe separator to the left. Default: True.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

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
        w_battery_icon = Battery(**config)

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
        w_battery_text = Battery(**config)

        widgets = [w_battery_icon, w_battery_text]
        if add_sep:
            widgets += [Spacer(length=5)]
        if add_pipe:
            pipe = TextBox(**self.fonts['Normal'],
                           text       = '|',
                           foreground = self.colors['orange'])
            widgets = [pipe, Spacer(length = 5)] + widgets

        return widgets

    def widget_tray(self, add_pipe: bool = True) -> list[_Widget]:
        """Widget for displaying system tray.

        Parameters
        ----------
        add_pipe: bool, optional
            Add a pipe separator to the left. Default: True.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        config = dict(background = self.colors['background'],
                      icon_size = 16,
                      padding = 15)
        widget_systray = Systray(**config)
        widgets = [widget_systray]

        if add_pipe:
            pipe = TextBox(**self.fonts['Normal'],
                           text       = '|',
                           foreground = self.colors['foreground'],
                           padding    = -2)
            widgets = [pipe] + widgets

        return widgets

    @add_mirror
    def widget_chord(self) -> list[_Widget]:
        """Widget for showing key chords.

        Parameters
        ----------
        add_sep: bool, optional
            Add a space to the right. Default: True.
        add_pipe: bool, optional
            Add a pipe separator to the left. Default: True.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        config = dict(**self.fonts['Normal'],

                      # Formatting
                      background     = self.colors['background-alt1'],
                      foreground     = self.colors['foreground'],
                      padding        = 3,
                      name_transform = lambda name: f' {name} ')
        widget_chord = Chord(**config)

        return [widget_chord]

    @add_mirror
    def widget_spotify(
            self,
            add_sep: bool = True
    ) -> list[_Widget]:
        """Widget for showing spotify.

        Parameters
        ----------
        add_sep: bool, optional
            Add a space to the right. Default: True.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        config = dict(**self.fonts['Normal'],
                      name             = 'spotify',
                      objname          = "org.mpris.MediaPlayer2.spotify",
                      display_metadata = ['xesam:artist', 'xesam:title'],
                      scroll_chars     = 15,
                      stop_pause_text  = 'IDLE')
        widget_spotify = Mpris2(**config)

        widgets = [widget_spotify]
        if add_sep:
            return widgets + [Spacer(length=10)]

        return widgets

    def create_widgets(
            self,
            widgets_left: list[_Widget],
            widgets_center: list[_Widget],
            widgets_right: list[_Widget],
            screen: int
    ) -> list[_Widget]:
        """It creates the widgets list by section.

        Parameters
        ----------
        widgets_left: list[_Widget]
            The list of widgets to the left of the bar.
        widgets_center: list[_Widget]
            The list of widgets to the center of the bar.
        widgets_right: list[_Widget]
            The list of widgets to the right of the bar.
        screen: int
            The screen the bar is going to be displayed at.

        Returns
        -------
        list[_Widget]
            The widgets to add to the bar.
        """

        # Padding for bar
        paddingl = self.padding_left[f'bar{screen}']
        paddingr = self.padding_right[f'bar{screen}']

        widgets = []

        # Add left
        if len(widgets_left) > 0:
            background = widgets_left[0].background
            space = Spacer(length=paddingl, background=background)
            widgets += [space] + widgets_left

        # Add center
        if len(widgets_center) > 0:
            widgets += [Spacer()] + widgets_center + [Spacer()]

        # Add right
        if len(widgets_right) > 0:
            if len(widgets_center) == 0:
                widgets += [Spacer()]

            background = widgets_right[-1].background
            space = Spacer(length=paddingr, background=background)
            widgets += widgets_right + [space]
        elif len(widgets_center) > 0:
            widgets += [TextBox()]

        return widgets
