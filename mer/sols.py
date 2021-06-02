import datetime
from mer.constants import date_of_start_of_mars_year_0, seconds_per_sol
from mer._validators import DatetimeValidator


def sols_after_mars_year_0(dt: datetime.datetime) -> float:
    """Compute the number of sols between a datetime and the start of Mars year
    0.

    Parameters
    ----------
    dt
        Any date.

    Raises
    ------
    TypeError
        Raised if :code:`date` is not a datetime.datetime.

    Examples
    --------
    Find the number of sols after Mars year 0 that MAVEN arrived at Mars.

    >>> import datetime, mer
    >>> dt = datetime.datetime(2014, 9, 2, 2, 24, 0)
    >>> sols = mer.sols_after_mars_year_0(dt)
    >>> sols
    21781.872772174716

    """
    return sols_between_datetimes(date_of_start_of_mars_year_0, dt)


def sols_between_datetimes(early_date: datetime.datetime,
                           later_date: datetime.datetime) -> float:
    """Compute the number of sols between two datetimes.

    Parameters
    ----------
    early_date
        The earlier of the two dates.
    later_date
        The latter of the two dates.

    Raises
    ------
    TypeError
        Raised if either :code:`early_date` or :code:`later_date` are not a
        datetime.datetime.

    Examples
    --------
    Compute the number of sols Opportunity was active. I don't know the hour,
    minute, or second of the start or end of the mission so I set them to 0.

    >>> import datetime, mer
    >>> opportunity_start = datetime.datetime(2004, 1, 25, 0, 0, 0)
    >>> opportunity_end = datetime.datetime(2018, 6, 10, 0, 0, 0)
    >>> mer.sols_between_datetimes(opportunity_start, opportunity_end)
    5109.551211085292

    """
    try:
        elapsed_seconds = (later_date - early_date).total_seconds()
        return elapsed_seconds / seconds_per_sol
    except TypeError as type_error:
        message = 'At least one of the inputs is not a datetime.datetime.'
        raise TypeError(message) from type_error


def sols_since_datetime(date: datetime.datetime) -> float:
    """Compute the number of sols between an input datetime and today.

    Parameters
    ----------
    date
        Any date.

    Raises
    ------
    TypeError
        Raised if :code:`date` is not a datetime.datetime.

    """
    return sols_between_datetimes(date, datetime.datetime.utcnow())
