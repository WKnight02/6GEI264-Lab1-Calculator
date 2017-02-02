import unittest as test

from bin.calcCore import *

class TestCore(test.TestCase):

    def setUp(this):
        this.core = Core()

    def test_press(this):
        """ Tests if the press method works properly
        It should not allow every characters
        """
        core = this.core

        # Test every character in the core's input
        def test():
            for c in core.input:
                if c not in core.CHARACTERS:
                    return False
            return True

        # Press every character possible (almost)
        for i in range(65536):
            c = chr(i)
            core.press(c)

        # Assertions
        this.assertEqual(True, test(), "Some character passed thru")
        core.input += "&é"'-è_çà'
        this.assertEqual(False, test(), "Everything passed, should not")

    def test_clear(this):
        """Tests if we can clear the input/history
        """
        core = this.core

        text = "azertyuiop"
        core.input = text

        # Clear one char from the input
        core.clear()
        this.assertEqual(core.input, text[:-1])

        # Tries to over delete characters
        for _ in range(2 * len(core.input)):
            core.clear()
        this.assertEqual(core.input, "")

        # Put some text into the input
        this.input = "qsdfghjklm"

        # Clear the whole input
        core.clearAll()
        this.assertEqual(core.input, "")

    def test_evaluation(this):
        """Tests if the evaluation is rather correct
        """
        core = this.core

        expressions = {

            # Addition/Soustraction
            "1+1-1": 1,

            # Division
            "2*3/2": 3,

            # Puissance
            "2**8": 256,

            # Nombre négatif/priorité opératoire
            "2+-1*-1": 3,

            # Parenthèses
            "(2+-1)*-1": -1,

            # Virgule
            "1.201+1.01+0": 2.21,

            # Mauvaise syntaxe
            "1)+1": None,

            # Division par zéro
            "1/0": None,
        }

        for expression, expected in expressions.items():

            core.input = expression
            result = core.evalInput()

            this.assertEqual(result, expected, "Eval: " + expression)

    def test_history(this):
        """Tests if the history works as intended
        """
        core = this.core

        # Generate multiple histories
        count = 3
        for _ in range(count):
            core.input = "1+2"
            core.evalInput()

        # Every history entry that is not empty
        registered = [i for i in core.history if len(i) > 0]
        this.assertEqual(len(registered), count)

        # Tries to overflow the history
        for _ in range(core.HISTORY_LEN * 2):
            core.evalExpression("meh")
        this.assertEqual(len(core.history), core.HISTORY_LEN)

    def test_reset(this):
        """Tests if the calc reset works
        """
        core = this.core

        # Put some input and evaluate it
        core.input = "1+2"
        core.evalInput()
        core.reset()

        # Is everything cleaned ?
        this.assertEqual(len([0 for i in core.history if len(i) > 0]), 0)
        this.assertEqual(core.input, "")
