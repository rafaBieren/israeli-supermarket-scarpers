from il_supermarket_scarper import ScraperStability, ScraperFactory, datetime_in_tlv
from il_supermarket_scarper.utils import _is_saturday_in_israel


def test_stable_scraper():
    """test sample stable scarper"""
    assert not ScraperStability.is_validate_scraper_found_no_files(
        ScraperFactory.VICTORY.name
    )


def test_not_active():
    """test grap between active and not"""
    all_listed = ScraperFactory.all_listed_scrappers()
    all_active = ScraperFactory.all_scrapers_name(
        when_date=datetime_in_tlv(2024, 12, 12, 0, 0, 0)
    )

    # No chains should be disabled by default in the reduced set
    expected_to_fail = 0
    assert len(set(all_listed) - set(all_active)) == expected_to_fail
