from dataclasses import dataclass


@dataclass
class EventLogMultipleEntries:
    # The page to return (1-based numbering)
    pageNumber: int = 1
    # The number of events to return per page
    eventsPerPage: int = 25
    # Only events created on or after this date/time (UTC ISO-8601) will be returned
    earliestDate: str = "2000-01-01T00:00:00.000000Z"
    # Only events created on or before this date/time (UTC ISO-8601) will be returned
    latestDate: str = "2050-01-01T00:00:00.000000Z"
    # (Optional) This string will be ANDed into the SQL WHERE clause when querying the event log database
    sqlWhereClause: str = ""


@dataclass
class EventLogSingleEntry:
    # The ID of the event to return
    id: int = 1
