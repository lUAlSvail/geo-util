import unittest
import subprocess
import time

class TestGeoUtil(unittest.TestCase):

    def run_command(self, *args):
        """Helper to run the command-line utility and return output."""
        result = subprocess.run(
            ["python3", "geo_util.py"] + list(args),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()

    def test_valid_city(self):
        """Test valid city/state lookup."""
        output = self.run_command("Madison, WI")
        self.assertIn("Madison", output)
        self.assertIn("Lat:", output)
        self.assertIn("Lon:", output)

    def test_valid_zip(self):
        """Test valid ZIP code lookup."""
        output = self.run_command("10001")
        self.assertIn("Lat:", output)
        self.assertIn("Lon:", output)

    def test_valid_zip_with_leading_zero(self):
        """Test valid ZIP code that starts with a zero (common in Northeast US)."""
        output = self.run_command("02108")  # Boston, MA ZIP code
        self.assertIn("Lat:", output)
        self.assertIn("Lon:", output)

    def test_valid_city_with_spaces(self):
        """Test valid city with a space in the name."""
        output = self.run_command("San Francisco, CA")
        self.assertIn("San Francisco", output)
        self.assertIn("Lat:", output)
        self.assertIn("Lon:", output)

    def test_multiple_valid_locations(self):
        """Test multiple valid locations (city/state and ZIP mixed)."""
        output = self.run_command("Chicago, IL", "60601", "Los Angeles, CA", "90210")
        self.assertIn("Chicago", output)
        self.assertIn("Los Angeles", output)
        self.assertIn("Lat:", output)
        self.assertIn("Lon:", output)

    def test_invalid_city(self):
        """Test handling of an invalid city."""
        output = self.run_command("InvalidCity")
        self.assertIn("Error:", output)

    def test_invalid_zip(self):
        """Test handling of an invalid ZIP code."""
        output = self.run_command("99999")  # Likely non-existent ZIP
        self.assertIn("Error:", output)

    def test_mixed_valid_and_invalid_inputs(self):
        """Test mix of valid and invalid locations."""
        output = self.run_command("New York, NY", "99999", "FakeCity, ZZ")
        self.assertIn("New York", output)
        self.assertIn("Error:", output)

    def test_slow_response_handling(self):
        """Simulate slow API response and ensure program does not hang indefinitely."""
        start_time = time.time()
        output = self.run_command("New York, NY")
        end_time = time.time()
        self.assertIn("New York", output)
        self.assertLess(end_time - start_time, 10, "API call took too long")

    def test_empty_input(self):
        """Test empty input handling."""
        result = subprocess.run(
            ["python3", "geo_util.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertIn("usage:", result.stderr.lower())  # argparse should print usage message

if __name__ == "__main__":
    unittest.main()
