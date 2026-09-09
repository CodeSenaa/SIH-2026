from tc_auth.db import Base
from connect import engine

def init():
    from SAMPLE_MODULE.db import SampleTable
    Base.metadata.create_all(
        bind=engine,
    )


def destroy():
    from SAMPLE_MODULE.db import SampleTable

    Base.metadata.drop_all(
        bind=engine,
    )