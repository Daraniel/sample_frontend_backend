class AppException(Exception):
    """Base exception class for our all of our app's errors."""
    pass


class DataSourceException(AppException):
    """Base exception class for data source errors."""
    pass


class DataNotFoundException(DataSourceException):
    """Raised when data is not found in the specified table."""
    pass


class MetadataNotFoundException(DataSourceException):
    """Raised when metadata is not found in the specified table."""
    pass
