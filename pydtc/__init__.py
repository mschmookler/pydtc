from datetime import datetime, tzinfo
from dateutil.parser.isoparser import _takes_ascii, isoparser
from dateutil.tz import gettz


class nosep_isoparser(isoparser):
    """Subclass isoparser and overwrite isoparse method."""
    @_takes_ascii
    def isoparse(self, dt_str):
        """Check if there is a digit where we expect a separator and handle it."""
        _, pos = self._parse_isodate(dt_str)
        
        if len(dt_str) > pos:
            if dt_str[pos] in b"0123456789" and self._sep is None:
                return super().isoparse(dt_str[:pos] + b"T" + dt_str[pos:])
        return super().isoparse(dt_str)

class DTC:
    """Datetime constructor metaclass that accepts multiple formats.
    
    Accepts ISO 8601 datetime strings with or without the date/time
    separator and coerces them into an aware datetime according to
    the passed in timezone.
    """
    def __init__(self, tz_info: tzinfo):
        if isinstance(tz_info, str):
            self.tzinfo = gettz(tz_info)
        elif isinstance(tz_info, tzinfo):
            self.tzinfo = tz_info
        else:
            raise TypeError("tzinfo must be a datetime.tzinfo or a string representing a timezone")

    def __call__(self, dt):
        if isinstance(dt, str):
            _dt = nosep_isoparser().isoparse(dt)
        elif isinstance(dt, datetime):
            _dt = dt
        else:
            raise TypeError("Input must be a datetime.datetime or an ISO 8601 string")
        
        if _dt.tzinfo is None:
            return _dt.replace(tzinfo=self.tzinfo)
        else:
            return _dt.astimezone(self.tzinfo)
    
    def now(self):