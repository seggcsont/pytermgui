from pytermgui import str_to_color, IndexedColor, RGBColor, HEXColor


def test_fg_simple():
    color = str_to_color("4")

    assert isinstance(color, IndexedColor)
    assert color.name == "4"
    assert color.sequence == "\x1b[34m"


def test_bg_simple():
    color = str_to_color("@2")

    assert isinstance(color, IndexedColor)
    assert color.name == "@2"
    assert color.sequence == "\x1b[42m"


def test_fg_named():
    color = str_to_color("green")

    assert isinstance(color, IndexedColor)
    assert color.name == "2"
    assert color.sequence == "\x1b[32m"


def test_bg_named():
    color = str_to_color("@bright-blue")

    assert isinstance(color, IndexedColor)
    assert color.name == "@12"
    assert color.sequence == "\x1b[104m"


def test_fg_indexed():
    color = str_to_color("121")

    assert isinstance(color, IndexedColor)
    assert color.name == "121"
    assert color.sequence == "\x1b[38;5;121m"
    assert color.sequence == "\x1b[38;5;121m"


def test_bg_indexed():
    color = str_to_color("@96")

    assert isinstance(color, IndexedColor)
    assert color.name == "@96"
    assert color.sequence == "\x1b[48;5;96m"


def test_fg_rgb():
    color = str_to_color("45;123;36")

    assert isinstance(color, RGBColor)
    assert color.name == "45;123;36"
    assert color.sequence == "\x1b[38;2;45;123;36m"


def test_bg_rgb():
    color = str_to_color("@123;23;45")

    assert isinstance(color, RGBColor)
    assert color.name == "@123;23;45"
    assert color.sequence == "\x1b[48;2;123;23;45m"


def test_fg_hex():
    color = str_to_color("#123456")

    assert isinstance(color, HEXColor)
    assert color.name == "#123456"
    assert color.sequence == "\x1b[38;2;18;52;86m"
    assert color.sequence == "\x1b[38;2;18;52;86m"


def test_bg_hex():
    color = str_to_color("#abcdef")

    assert isinstance(color, HEXColor)
    assert color.name == "#abcdef"
    assert color.sequence == "\x1b[38;2;171;205;239m"
    assert color.sequence == "\x1b[38;2;171;205;239m"