import json
import uuid
from datetime import datetime

class StructuredLogger:
    LEVELS = {'DEBUG': 10, 'INFO': 20, 'WARN': 30, 'ERROR': 40}

    def __init__(self, service_name='app', min_level='INFO'):
        self.service_name = service_name
        self.min_level = min_level
        self.correlation_id = None
        self.logs = []

    def set_correlation_id(self, correlation_id=None):
        pass

    def _format_entry(self, level, message, extra=None):
        # timestamp (ISO format), level, message, service, correlation_id, extra
        pass

    def _should_log(self, level):
        pass

    def debug(self, message, **extra):
        pass

    def info(self, message, **extra):
        pass

    def warn(self, message, **extra):
        pass

    def error(self, message, **extra):
        pass

    def get_logs(self):
        return list(self.logs)
