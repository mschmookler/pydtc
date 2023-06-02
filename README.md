# pydtc
Python 3 datetime constructor to simplify object creation from a variety of formats.

    # Suppose your team works in London
    from pydtc inport PYDTC
    lon_dt = PYDTC("Europe/London")
    
    # strptime for naive ISO-8601
    dt = lon_dt("2023-01-01 12:34:56")
    dt == datetime(2023, 1, 1, 12, 34, 56, tzinfo=TZ_LON)
    # True

    # Convert from another timezone
    dt_ny = datetime(2023, 1, 1, 7, 34, 56, tzinfo=TZ_NY)
    dt == dt_chi
    # True

    