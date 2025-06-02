import random
import os
from enum import Enum
import il_supermarket_scarper.scrappers as all_scrappers
from il_supermarket_scarper.scraper_stability import ScraperStability


class ScraperFactory(Enum):
    """all scrapers avaliabe"""

    MEGA = all_scrappers.Mega  # קרפור \ מגה
    RAMI_LEVY = all_scrappers.RamiLevy  # רשת חנויות רמי לוי שיווק השקמה 2006 בע"מ
    SHUFERSAL = all_scrappers.Shufersal  # שופרסל בע"מ (כולל רשת BE)
    TIV_TAAM = all_scrappers.TivTaam  # טיב טעם רשתות בע"מ
    VICTORY = all_scrappers.Victory  # ויקטורי רשת סופרמרקטים בע"מ
    YOHANANOF = all_scrappers.Yohananof  # מ. יוחננוף ובניו (1988) בע"מ

    @classmethod
    def all_listed_scrappers(cls):
        """get all the scarpers and filter disabled scrapers"""
        return list(member.name for member in cls)

    @classmethod
    def all_active(cls, limit=None, files_types=None, when_date=None):
        """get all the scarpers and filter disabled scrapers"""
        return (
            member
            for member in cls
            if cls.is_scraper_enabled(
                member,
                limit=limit,
                files_types=files_types,
                when_date=when_date,
            )
        )

    @classmethod
    def sample(cls, n=1):
        """sample n from the scrappers"""
        return random.sample(cls.all_scrapers_name(), n)

    @classmethod
    def all_scrapers(cls, limit=None, files_types=None, when_date=None):
        """list all scrapers possible to use"""
        return [
            e.value
            for e in ScraperFactory.all_active(
                limit=limit, files_types=files_types, when_date=when_date
            )
        ]

    @classmethod
    def all_scrapers_name(cls, limit=None, files_types=None, when_date=None):
        """get the class name of all listed scrapers"""
        return [
            e.name
            for e in ScraperFactory.all_active(
                limit=limit, files_types=files_types, when_date=when_date
            )
        ]

    @classmethod
    def get(cls, class_name, limit=None, files_types=None, when_date=None):
        """get a scraper by class name"""

        enum = None
        if isinstance(class_name, ScraperFactory):
            enum = class_name
        elif class_name in cls.all_scrapers_name():
            enum = getattr(ScraperFactory, class_name)

        if enum is None:
            raise ValueError(f"class_names {class_name} not found")

        if not cls.is_scraper_enabled(
            enum, limit=limit, files_types=files_types, when_date=when_date
        ):
            return None
        return enum.value

    @classmethod
    def is_scraper_enabled(cls, enum, limit=None, files_types=None, when_date=None):
        """get scraper value base on the enum value, if it disabled, return None"""
        env_var_value = os.environ.get("DISABLED_SCRAPPERS")
        if env_var_value is not None:
            disabled_scrappers = list(map(str.strip, env_var_value.split(",")))
            if enum.name in disabled_scrappers:
                return False
        #
        if ScraperStability.is_validate_scraper_found_no_files(
            enum.name,
            limit=limit,
            files_types=files_types,
            when_date=when_date,
            utilize_date_param=getattr(enum.value, 'utilize_date_param', False),
        ):
            return False
        return True
