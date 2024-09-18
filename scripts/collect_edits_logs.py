import sys, json
from pychunkedgraph.graph import ChunkedGraph
from pychunkedgraph.graph.attributes import OperationLogs


def extract_logs(graph_id):
    cg = ChunkedGraph(graph_id=graph_id)

    logs = cg.client.read_log_entries(operation_ids=list(range(cg.client.get_max_operation_id())))
    parsed_logs = []
    keyerror_logs = []
    for i, log in logs.items():
        print(log)
        exc = log[OperationLogs.OperationException]
        if "Index" in exc:
            continue
        _log = {"id": int(i)}
        try:
            _log["added_edges"] = log[OperationLogs.AddedEdge].tolist()
            _log["sink_coords"] = log[OperationLogs.SinkCoordinate].tolist()
            _log["source_coords"] = log[OperationLogs.SourceCoordinate].tolist()
            parsed_logs.append(_log)
        except KeyError:
            keyerror_logs.append(_log)
            # print(log)

    # with open(f"{cg.graph_id}_logs.json", "w") as f:
    #     json.dump(parsed_logs, f)
    
    # with open(f"{cg.graph_id}_error_logs.json", "w") as f:
    #     json.dump(keyerror_logs, f)


def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <graph_id>")
        sys.exit(1)

    # Get the arguments
    graph_id = sys.argv[1]

    # Use the arguments
    print(f"Graph_id: {graph_id}")
    extract_logs(graph_id)

if __name__ == "__main__":
    main()