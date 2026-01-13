import pykx as kx
import os
import sys
import argparse

def parse_cli():
    parser = argparse.ArgumentParser(description="My script with named args")
    parser.add_argument("--host", type=str, default=None, help="Host")
    parser.add_argument("--port", type=int, default=None, help="Port number")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    print("Port:", args.port)
    print("Host:", args.host)
    print("Debug:", args.debug)
    return args

class KdbClient:
    def __init__(self, host=None, port=None, args=None):
        cli_host = args.host if args else None
        cli_port = args.port if args else None
        self.host = cli_host or host or os.getenv('KDBX_HOST', 'localhost')
        self.port = cli_port or port or int(os.getenv('KDBX_DB_PORT', 5050))
        self.q = kx.QConnection(self.host, int(self.port))
    
    def query(self, query_str):
        try:
            result = self.q(query_str)
            return result
        except Exception as e:
            return f"❌ Query failed: {e}"

    def sample_query(self):
        return self.query("count select from trade")

    def close(self):
        self.q.close()

if __name__ == "__main__":
   args = parse_cli()
   kdb_client = KdbClient("localhost", 5896, args)
