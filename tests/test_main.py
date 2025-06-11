import os
import pytest
from app.main import analyze_log

@pytest.fixture
def sample_log(tmp_path):
    file = tmp_path / "app.log"
    file.write_text("""INFO Starting the server...
WARNING Disk space is low
ERROR Failed to connect to database""")
    return str(file)

import pytest
from app.main import analyze_log
from app.utils.email_alerts import send_email

def test_analyze_log(tmp_path):
    test_file = tmp_path / "test.log"
    test_file.write_text("INFO Hello\nWARNING Be careful\nERROR Crash!")
    errors, warnings = analyze_log(str(test_file))
    assert "WARNING Be careful" in warnings
    assert "ERROR Crash!" in errors

def test_send_email_mock(monkeypatch):
    class MockSMTP:
        def __init__(self, smtp_server, port): pass
        def starttls(self): pass
        def login(self, user, pwd): pass
        def send_message(self, msg): pass
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_val, exc_tb): pass

    monkeypatch.setattr("smtplib.SMTP", MockSMTP)

    from app.utils.email_alerts import send_email
    send_email("Test", "Body", "to@example.com", "from@example.com", "dummy-pass")
