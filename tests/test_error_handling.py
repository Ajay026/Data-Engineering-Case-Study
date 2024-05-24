import pytest
from error_handling.error_monitoring import log_error

def test_log_error(mocker):
    mocker.patch('logging.error')
    log_error("Test error message")
    assert logging.error.called
