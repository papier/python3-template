"""Canary unit test."""
import unittest


class TestCanaray(unittest.TestCase):
    """Canary test class."""

    def test_canary(self) -> None:
        """Canary."""
        # pylint: disable=W1503
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
