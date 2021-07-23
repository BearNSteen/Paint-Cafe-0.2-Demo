import time


def dialog(data, name, days):
    if name == "Dane":
        dane_dialog = [
            ["Hello there!",
             "Have we met before?",
             "Oh, your name is " + data["playername"] + "? A pleasure to meet you!",
             "I hope you speak with me again. This has been pleasant."
             ],
            ["Hello again, " + data["playername"] + "!",
             "Did I tell you what I do for a job?",
             "I'm actually a royal bodyguard. I protect a princess for a living.",
             "Because of that, I'm always really thankful for this cafe.",
             "Thanks for serving great coffee."
             ]
        ]
        try:
            for line in dane_dialog[days]:
                print(line)
                time.sleep(2)
        except IndexError:
            print("Dane nods silently at you and continues sipping his coffee.")