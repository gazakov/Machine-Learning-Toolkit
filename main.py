import unittest
import logging
import os

# Set up logging configuration
logging.basicConfig(filename='tests.log', level=logging.INFO, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

def run_tests():
    logger.info("Starting tests execution")

    # Discover and load tests
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner().run(tests)

    # Check if tests were successful
    if result.wasSuccessful():
        logger.info("All tests passed successfully")
    else:
        logger.error("Detected test errors or failures")
        for failed_test in result.failures + result.errors:
            logger.error('Test error: %s. Reason: %s', failed_test[0], failed_test[1])

    logger.info("Testing finished")

if __name__ == '__main__':
    run_tests()
