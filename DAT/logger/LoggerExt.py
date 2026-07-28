from TDStoreTools import StorageManager
import TDFunctions as TDF


import datetime
import os

class LoggerExt:
    """
    LoggerExt writes timestamped messages to a per-run log file
    in the LOG/ directory. Each run gets its own file named
    app_<YYYYMMDD-HHMMSS>.log.
    """

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        os.makedirs("LOG", exist_ok=True)
        run_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        self.log_file = os.path.join("LOG", f"app_{run_id}.log")

    def Log(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        with open(self.log_file, "a", encoding="utf-8") as log_file:
            log_file.write(entry + "\n")
