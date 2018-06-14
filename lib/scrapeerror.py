class ScrapeError(Exception):
    """An error happened while scraping."""
    pass

class FormatError(ScrapeError):
    """The whole page format is wrong, danger Will Robinson."""
    pass

class NoListingError(ScrapeError):
    """No listing data was found, it has probably been removed."""
    pass
