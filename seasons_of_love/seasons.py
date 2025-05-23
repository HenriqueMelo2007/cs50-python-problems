import datetime
import re
import num2words


class TimeInfo:
    def __init__(self, birthday_date):
        self._birthday_date = datetime.date(
            int(birthday_date[0]), int(birthday_date[1]), int(birthday_date[2])
        )
        self._current_date = datetime.date.today()
        self._difference_minutes = (
            abs((self._current_date - self._birthday_date).days) * 24 * 60
        )

    def __str__(self):
        return f"{num2words.num2words(self._difference_minutes, lang='en').replace(' and', '').replace(',', '')} ({self._difference_minutes}) minutes"

    @classmethod
    def get(cls):
        regex = r"^(\d{4})-(\d{2})-(\d{2})$"
        while True:
            birthday = input("Date of birth (YYYY-MM-DD): ").strip()
            match = re.search(regex, birthday)
            if match:
                return cls(match.groups())

    @property
    def birthday_date(self):
        return self._birthday_date

    @property
    def current_date(self):
        return self._current_date

    @property
    def difference_minutes(self):
        return self._difference_minutes


def main():
    user_time = TimeInfo.get()
    print(user_time)


if __name__ == "__main__":
    main()
