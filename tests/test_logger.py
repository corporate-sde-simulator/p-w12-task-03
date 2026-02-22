import pytest, sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from structuredLogger import StructuredLogger

class TestStructuredLogger:
    def test_info_creates_log(self):
        logger = StructuredLogger()
        logger.info('User logged in', user_id=123)
        logs = logger.get_logs()
        assert len(logs) == 1
        assert logs[0]['level'] == 'INFO'
        assert logs[0]['message'] == 'User logged in'

    def test_json_format(self):
        logger = StructuredLogger()
        logger.info('test')
        entry = logger.get_logs()[0]
        json.dumps(entry)  # Should not raise

    def test_correlation_id(self):
        logger = StructuredLogger()
        logger.set_correlation_id('req-123')
        logger.info('step 1')
        logger.info('step 2')
        logs = logger.get_logs()
        assert all(l['correlation_id'] == 'req-123' for l in logs)

    def test_min_level_filters(self):
        logger = StructuredLogger(min_level='WARN')
        logger.debug('ignored')
        logger.info('ignored')
        logger.warn('kept')
        assert len(logger.get_logs()) == 1

    def test_has_timestamp(self):
        logger = StructuredLogger()
        logger.info('test')
        assert 'timestamp' in logger.get_logs()[0]
