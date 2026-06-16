import sqlite3, json
from datetime import datetime

class ExperimentTracker:
    def __init__(self, name, db="experiments.db"):
        self.name = name
        self.run_id = name + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        self.db = sqlite3.connect(db)
        self.db.execute("CREATE TABLE IF NOT EXISTS runs (run_id TEXT PRIMARY KEY, name TEXT, params TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        self.db.execute("CREATE TABLE IF NOT EXISTS metrics (id INTEGER PRIMARY KEY, run_id TEXT, metric TEXT, value REAL, step INTEGER)")
        self.db.commit()
        self.metrics = []

    def log_params(self, params):
        self.db.execute("INSERT OR REPLACE INTO runs (run_id, name, params) VALUES (?, ?, ?)", (self.run_id, self.name, json.dumps(params)))
        self.db.commit()

    def log_metric(self, name, value, step=0):
        self.metrics.append((name, value, step))
        self.db.execute("INSERT INTO metrics (run_id, metric, value, step) VALUES (?, ?, ?, ?)", (self.run_id, name, value, step))
        self.db.commit()

    def get_runs(self):
        return self.db.execute("SELECT * FROM runs").fetchall()

def demo():
    t = ExperimentTracker("demo")
    t.log_params({"lr": 1e-4, "batch_size": 32, "model": "resnet50"})
    import random
    for i in range(10):
        t.log_metric("loss", 1.0/(i+1) + random.random()*0.1, step=i)
    print(f"Run: {t.run_id}, Metrics: {len(t.metrics)}")

if __name__ == "__main__":
    demo()
