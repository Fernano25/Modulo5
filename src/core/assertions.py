import jsonschema
from jsonschema import validate

class Assertions:
    @staticmethod
    def assert_status_code(response, expected_code):
        """Assert that response status code matches expected code"""
        assert response.status_code == expected_code, \
            f"Expected status code {expected_code}, but got {response.status_code}"
    
    @staticmethod
    def assert_response_time(response, max_time=1000):
        """Assert that response time is within acceptable limits"""
        response_time = response.elapsed.total_seconds() * 1000  # Convert to milliseconds
        assert response_time <= max_time, \
            f"Response time {response_time}ms exceeds maximum allowed {max_time}ms"
    
    @staticmethod
    def assert_json_schema(response, schema):
        """Assert that response matches expected JSON schema"""
        try:
            validate(instance=response.json(), schema=schema)
        except jsonschema.ValidationError as e:
            raise AssertionError(f"JSON schema validation failed: {e.message}")
    
    @staticmethod
    def assert_key_in_response(response, key):
        """Assert that specific key exists in response"""
        response_json = response.json()
        assert key in response_json, f"Key '{key}' not found in response"
    
    @staticmethod
    def assert_value_equals(response, key, expected_value):
        """Assert that specific key has expected value"""
        response_json = response.json()
        actual_value = response_json.get(key)
        assert actual_value == expected_value, \
            f"Expected {key} to be '{expected_value}', but got '{actual_value}'"
    
    @staticmethod
    def assert_list_length(response, expected_length):
        """Assert that response list has expected length"""
        response_json = response.json()
        assert isinstance(response_json, list), "Response is not a list"
        actual_length = len(response_json)
        assert actual_length == expected_length, \
            f"Expected list length {expected_length}, but got {actual_length}"