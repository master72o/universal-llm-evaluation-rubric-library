import json, os

class RubricRegistry:
    def __init__(self, rubrics_dir=None):
        if rubrics_dir is None:
            rubrics_dir = os.path.join(os.path.dirname(__file__), '../rubrics')
        self.rubrics_dir = rubrics_dir
        self.rubrics = {}
        self.load_rubrics()

    def load_rubrics(self):
        for fname in os.listdir(self.rubrics_dir):
            if fname.endswith('.json'):
                fpath = os.path.join(self.rubrics_dir, fname)
                with open(fpath) as f:
                    data = json.load(f)
                    self.rubrics[data['id']] = data

    def list_rubrics(self):
        return sorted(list(self.rubrics.keys()))

    def get_rubric(self, rubric_id):
        return self.rubrics.get(rubric_id)

    def evaluate_simple(self, rubric_id, prompt, response):
        rubric = self.get_rubric(rubric_id)
        if not rubric:
            raise ValueError(f"Rubric {rubric_id} not found")

        # Basic heuristic score simulation
        score = 5
        feedback = []

        if "not" in response.lower() and "cannot" in response.lower() and "refuse" in response.lower():
            if rubric_id in ["helpfulness_intent_alignment", "math_step_by_step_reasoning"]:
                score -= 2
                feedback.append("Model refused benign prompt")

        if len(response.strip()) == 0:
            score = 1
            feedback.append("Empty response")

        return {
            "rubric_id": rubric_id,
            "rubric_name": rubric['name'],
            "score": max(1, score),
            "max_score": 5,
            "feedback": feedback if feedback else ["Response satisfies rubric criteria"]
        }
