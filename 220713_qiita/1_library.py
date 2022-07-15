import jellyfish


def main():
    jellyfish.levenshtein_distance(u"jellyfish", u"smellyfish")


if __name__ == "__main__":
    for _ in range(10000):
        main()
