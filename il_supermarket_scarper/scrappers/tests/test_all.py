from il_supermarket_scarper.scrappers_factory import ScraperFactory
from .test_cases import make_test_case

class MegaTestCase(make_test_case(ScraperFactory.MEGA, 37)):
    """Test case for ScraperFactory.MEGA."""


class RamiLevyTestCase(make_test_case(ScraperFactory.RAMI_LEVY, 1)):
    """Test case for ScraperFactory.RAMI_LEVY."""


class ShufersalTestCase(make_test_case(ScraperFactory.SHUFERSAL, 176)):
    """Test case for ScraperFactory.SHUFERSAL."""


class TivTaamTestCase(make_test_case(ScraperFactory.TIV_TAAM, 3)):
    """Test case for ScraperFactory.TIV_TAAM."""


class VictoryTestCase(make_test_case(ScraperFactory.VICTORY, 1)):
    """Test case for ScraperFactory.VICTORY."""


class YohananofTestCase(make_test_case(ScraperFactory.YOHANANOF, 1)):
    """Test case for ScraperFactory.YOHANANOF."""
