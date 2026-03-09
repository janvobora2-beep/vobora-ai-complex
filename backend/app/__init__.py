from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


def create_app():
    app = Flask(__name__)

    # Initialize Prometheus metrics
    metrics = PrometheusMetrics(app)

    return app
