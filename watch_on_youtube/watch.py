import re


def main():
    user_html: str = input("HTML: ").strip()
    shorter_url_equivalent: str = parse(user_html)
    print(shorter_url_equivalent)


def parse(user_html) -> str | None:
    try:
        regex = (
            r"(?:http)?(?:s)?(?:\://)?(?:www\.)?(?:youtube.com){1}(?:/embed/){1}(\w+)"
        )
        search = re.search(regex, user_html)
        url: tuple = search.groups()
        base = "https://youtu.be/"
        return base + url[0]
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
