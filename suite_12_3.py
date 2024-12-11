import tests_12_3
import unittest

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)