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
from typing import Any, Callable, Optional

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

def add_separation(
        space: int
) -> Callable[[Callable[..., list[_Widget]]], Callable[..., list[_Widget]]]:
    """It adds parameters to add a spacer to the right of the widgets.

    Parameters
    ----------
    space: int
        The number of pixels to add to the right.

    Returns
    -------
    Callable[[Callable[..., list[_Widget]]], Callable[..., list[_Widget]]]
        The decorator for the function that adds the parameter.
    """

    def decorator(
            func: Callable[..., list[_Widget]]
    ) -> Callable[..., list[_Widget]]:
        """The decorator to add the add_sep  parameter.

        Parameters
        ----------
        func: Callable[..., list[_Widget]]
            The function that gives the list of widgets.

        Returns
        -------
        Callable[..., list[_Widget]]
            The function with the add_sep parameter.
        """

        @functools.wraps(func)
        def wrapper(self: MyWidgets, *args: Any, **kwargs: Any) -> list[_Widget]:
            """It adds a space to the right of the widgets.

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
                The list of the widgets with the spacer.
            """

            add_sep = kwargs.pop('add_sep', True)
            widgets = func(self, *args, **kwargs)
            if add_sep:
                widgets += [Spacer(length = space)]

            return widgets

        return wrapper

    return decorator

def add_pipe(
        color: str,
        space: Optional[int] = None,
        padding: int = 0
) -> Callable[[Callable[..., list[_Widget]]], Callable[..., list[_Widget]]]:
    """It adds parameters to add a pipe to the left of the widgets.

    Parameters
    ----------
    pipe: str
        The color for the pipe.
    space: int, optional
        The number of pixels to add between the pipe and the widgets.
        Default: None.

    Returns
    -------
    Callable[[Callable[..., list[_Widget]]], Callable[..., list[_Widget]]]
        The decorator for the function that adds the parameter.
    """

    def decorator(
            func: Callable[..., list[_Widget]]
    ) -> Callable[..., list[_Widget]]:
        """The decorator to add the add_pipe parameter.

        Parameters
        ----------
        func: Callable[..., list[_Widget]]
            The function that gives the list of widgets.

        Returns
        -------
        Callable[..., list[_Widget]]
            The function with the add_sep parameter.
        """

        @functools.wraps(func)
        def wrapper(self: MyWidgets, *args: Any, **kwargs: Any) -> list[_Widget]:
            """It adds a separator and a pipe in the respective places.

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
                The list of the widgets with the spacer and the pipe.
            """

            add_pipe = kwargs.pop('add_pipe', True)
            widgets = func(self, *args, **kwargs)

            # Add space
            if space is not None:
                widgets.insert(0, Spacer(length = space))

            # Add pipe
            if add_pipe:
                widgets.insert(0, TextBox(
                    **self.fonts['Normal'],
                    text       = '|',
                    foreground = self.colors[color],
                    padding = padding
                ))

            return widgets

        return wrapper

    return decorator

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
    @add_separation(space = 5)
    @add_pipe(color = 'green', space = 5)
    def widget_layout(self) -> list[_Widget]:
        """Module for showing layout and number of windows.

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
        return widgets

    @add_mirror
    @add_separation(space = 8)
    @add_pipe(color = 'yellow')
    def widget_update(self) -> list[_Widget]:
        """Module for displaying updates.

        Requirements
        ------------
        - pacman-contrib

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
    @add_separation(space = 5)
    @add_pipe(color = 'orange', space = 5)
    def widget_battery(self) -> list[_Widget]:
        """Widget for displaying battery usage.

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

        widgets: list[_Widget] = [w_battery_icon, w_battery_text]
        return widgets

    @add_pipe(color = 'foreground', padding = -2)
    def widget_tray(self) -> list[_Widget]:
        """Widget for displaying system tray.

        Returns
        -------
        list[libqtile.widget.base._Widget]
            The list of widgets to add to the bar.
        """

        config = dict(background = self.colors['background'],
                      icon_size = 16,
                      padding = 15)
        widget_systray = Systray(**config)

        widgets: list[_Widget] = [widget_systray]
        return widgets

    @add_mirror
    def widget_chord(self) -> list[_Widget]:
        """Widget for showing key chords.

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
    @add_separation(space = 10)
    def widget_spotify(self) -> list[_Widget]:
        """Widget for showing spotify.

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

        widgets: list[_Widget] = [widget_spotify]
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
            widgets += widgets_left
            widgets.insert(0, space)

        # Add center
        if len(widgets_center) > 0:
            widgets.append(Spacer())
            widgets += widgets_center
            widgets.append(Spacer())

        # Add right
        if len(widgets_right) > 0:
            if len(widgets_center) == 0:
                widgets.append(Spacer())

            background = widgets_right[-1].background
            space = Spacer(length=paddingr, background=background)
            widgets += widgets_right
            widgets.append(space)

        elif len(widgets_center) > 0:
            widgets.append(TextBox())

        return widgets
