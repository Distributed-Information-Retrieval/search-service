import rpyc

class SearchService(rpyc.Service):
    exposed_version = "1.0.0"

    def on_connect(self, conn):
        print(f"Connection from {conn}")
        return super().on_connect(conn)

    def on_disconnect(self, conn):
        print(f"Connection closed from {conn}")
        return super().on_disconnect(conn)

    def exposed_query(self, query):
        return f"Welcome {query}"

    def exposed_doc(self):
        return """
            add (self, a: float, b: float)
            sub (self, a: float, b: float)
            mul (self, a: float, b: float)
            div (self, a: float, b: float)
            pow (self, a: float, b: float)
            pow (self, a: float, b: float, mod: float)
            iam (self, name: string)
        """


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(SearchService, hostname="0.0.0.0", port=8001)
    print("RPC server on 0.0.0.0:8001")
    server.start()
