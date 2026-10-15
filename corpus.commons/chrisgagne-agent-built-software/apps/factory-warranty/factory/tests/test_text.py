"""Model text reaching a person is inert: no controls, no invisible characters, nothing that renders or fetches."""
from factory.text import inert, invisible_chars


def test_inert_strips_controls_and_invisible_characters():
    sneaky = "ok\x1b[2J‮gnp.​\U000e0041hidden️"
    assert inert(sneaky) == "ok[2Jgnp.hidden"
    assert invisible_chars(sneaky) == ["U+001B", "U+200B", "U+202E", "U+E0041", "U+FE0F"]


def test_inert_defuses_images_and_html_but_keeps_the_words():
    text = "See ![x](https://evil.example/p.png) and <img src=x> but 3 < 4 stays.\nTab\tkept."
    out = inert(text)
    assert "![" not in out and "!\\[x](https://evil.example/p.png)" in out
    assert "<img" not in out and "&lt;img src=x>" in out and "3 < 4" in out and "\t" in out and "\n" in out
