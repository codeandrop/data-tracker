class MetricsView():
    def metrics_list(self, metrics):
        response = []
        for metric in metrics:
            response.append(
                {
                    "id": metric[0],
                    "market": metric[1],
                    "base": metric[2],
                    "quote": metric[3],
                    "stdev": metric[4],
                    "rank": metric[5],
                }
            )
        return response

    def metric_item(self, metric):
        return {
            "id": metric[0],
            "market": metric[1],
            "base": metric[2],
            "quote": metric[3],
            "stdev": metric[4],
            "rank": metric[5],
        }
