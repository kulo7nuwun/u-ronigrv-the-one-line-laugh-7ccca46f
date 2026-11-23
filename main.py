"""The One-Line Laugh - entry.

Writes one original funny line to /output/entry.txt.
"""

LINE = "My houseplants died of neglect while my screen time flourished like I'd been watering it daily."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
