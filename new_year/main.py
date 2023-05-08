"""
This module calculates the current Gregorian and Jalali dates along with the number of days remaining until the new year.
"""

import datetime
import jdatetime


def until_new_year() -> str:
    """
    This function calculates the number of days left until the new year.
    :return: Number of days left.
    """
    m_date = datetime.datetime.now()
    j_date = jdatetime.datetime.now()

    m_new_year = datetime.date(m_date.year + 1, 1, 1) if m_date.month == 12 and m_date.day > 25 \
        else datetime.date(m_date.year + 1, 1, 1)

    j_new_year = jdatetime.date(j_date.year + 1, 1, 1) if j_date.month == 10 and j_date.day > 2 \
        else jdatetime.date(j_date.year, 1, 1) + jdatetime.timedelta(days=365)

    if j_new_year.year > j_date.year + 1:
        j_new_year -= datetime.timedelta(days=1)

    m_days_to_new_year = (m_new_year - m_date.date()).days
    j_days_to_new_year = (j_new_year - j_date.date()).days

    return f'Until the new year: {m_days_to_new_year} days.\n' \
           f'Until the Jalali new year: {j_days_to_new_year} days.\n'


def date_time_now() -> str:
    """
    This function returns the current date and time.
    :return: Current date and time.
    """

    m_date = datetime.datetime.now()
    j_date = jdatetime.datetime.now()

    return f'Today is: {m_date.year}-{m_date.month}-{m_date.day}\n' \
           f'Today in Iran is: {j_date.year}/{j_date.month}/{j_date.day}\n'


def main():
    """
    This function is written to execute and use this module`s functions in itself.
    """

    return date_time_now()


if __name__ == "__main__":
    print(main())
    print(until_new_year())
