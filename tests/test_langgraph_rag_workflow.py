import unittest
from unittest.mock import patch
from lang_graph_engine import LangGraphWorkflowEngine, State

class TestLangGraphWorkflow(unittest.TestCase):
    def setUp(self):
        self.engine = LangGraphWorkflowEngine()
    
    def test_node_1(self):
        state = {"graph_state": "Initial"}
        result = self.engine.node_1(state)
        self.assertEqual(result["graph_state"], "Initial I am")
    
    def test_node_2(self):
        state = {"graph_state": "Initial"}
        result = self.engine.node_2(state)
        self.assertEqual(result["graph_state"], "Initial happy!")
    
    def test_node_3(self):
        state = {"graph_state": "Initial"}
        result = self.engine.node_3(state)
        self.assertEqual(result["graph_state"], "Initial sad!")
    
    @patch('random.random')
    def test_decide_mood_happy(self, mock_random):
        # Force the random choice to be "happy"
        mock_random.return_value = 0.25
        state = {"graph_state": "Initial"}
        result = self.engine.decide_mood(state)
        self.assertEqual(result, "node_2")
    
    @patch('random.random')
    def test_decide_mood_sad(self, mock_random):
        # Force the random choice to be "sad"
        mock_random.return_value = 0.75
        state = {"graph_state": "Initial"}
        result = self.engine.decide_mood(state)
        self.assertEqual(result, "node_3")
    
    def test_full_workflow(self):
        result = self.engine.run({"graph_state": "Test input."})
        self.assertIn("graph_state", result)
        # The exact result will depend on the random mood choice
        self.assertTrue(
            result["graph_state"].startswith("Test input. I am") and
            (result["graph_state"].endswith("happy!") or result["graph_state"].endswith("sad!"))
        )

if __name__ == "__main__":
    unittest.main()