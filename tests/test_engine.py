import unittest
import sys
import os

# Aggiunge la directory principale al path per importare main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

class TestBrainLogicEngine(unittest.TestCase):

    def setUp(self):
        """Inizializzazione delle variabili di test prima di ogni suite."""
        self.test_depth = 4
        self.mock_state = main.generate_mock_puzzle_state(self.test_depth)

    def test_puzzle_state_generation(self):
        """Verifica che la generazione dello stato del puzzle sia strutturata correttamente."""
        self.assertIn("puzzle_id", self.mock_state)
        self.assertIn("difficulty_index", self.mock_state)
        self.assertIn("nodes", self.mock_state)
        self.assertEqual(len(self.mock_state["nodes"]), self.test_depth)

    def test_puzzle_difficulty_bounds(self):
        """Verifica che l'indice di difficoltà generato rientri nei limiti logici."""
        difficulty = self.mock_state["difficulty_index"]
        self.assertTrue(1.5 <= difficulty <= 5.0)

    def test_heuristic_solver_mutation(self):
        """Verifica che il motore di risoluzione modifichi correttamente gli stati dei nodi."""
        # Forza un nodo nello stato 'locked' per testare la mutazione
        self.mock_state["nodes"][0]["state"] = "locked"
        
        resolved_state = main.solve_heuristic_step(self.mock_state)
        
        # Verifica che dopo l'esecuzione il nodo sia passato a 'resolved'
        self.assertEqual(resolved_state["nodes"][0]["state"], "resolved")

if __name__ == "__main__":
    unittest.main()
