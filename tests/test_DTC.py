from datetime import datetime, tzinfo
from dateutil.tz import gettz

import pytest

import pydtc.DTC

TZ_CHI = gettz("America/Chicago")


class TestDTC:
    
    def __init__(self):
        self.constructor = pydtc.DTC("America/Chicago")

    @pytest.mark.parametrize("dt_str,expected_dt", [
        "2022", datetime(2022, tzinfo=TZ_CHI),
    ])
    def test_constructor(self, dt, expected_dt):
        assert self.constructor(dt_str) == dt