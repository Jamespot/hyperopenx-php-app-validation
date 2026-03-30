from slapos.grid.promise.generic import GenericPromise
import socket


class RunPromise(GenericPromise):
    def sense(self):
        host = self.getConfig('host')
        port = int(self.getConfig('port'))
        try:
            with socket.create_connection((host, port), timeout=5):
                self.logger.info(f"PHP app running on {host}:{port}.")
        except Exception as e:
            self.logger.error(f"Error connecting to PHP app: {e}")

    def anomaly(self):
        return self._anomaly(result_count=3, failure_amount=3)
