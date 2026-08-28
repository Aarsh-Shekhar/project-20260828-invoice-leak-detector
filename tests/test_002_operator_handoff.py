import unittest

from invoice_leak_detector.models import Record
from invoice_leak_detector.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="invoice-002", exposure=37920, signal=0.645, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
