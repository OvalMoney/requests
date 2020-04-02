# -*- encoding: utf-8

import os
import pytest
from requests.compat import json as complexjson

@pytest.mark.skipif(os.getenv("RAPIDJSON", default="False")=="False", reason="requires python3.5 or higher")
def test_rapidjson_lib():
    import rapidjson
    assert complexjson == rapidjson
