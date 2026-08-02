"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
import TDFunctions as TDF

class StateExt:
    """
    STATE is the temporal memory of the artwork.

    AUDIO describes what is happening now.

    STATE describes what continues to exist after the sound has passed.
    It does not process signals.

    It accumulates experience.
    """

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        self._state = {}

    def Publish(self, key: str, value: str, source=None) -> None:
        """
        key: state name
        value: state value
        source: Caller Component
        """
        self._state[key] = {
            "value": value,
            "source": source
        }
        # print(f"StateExt.Set(): {key}: {value} - source component: {source}")
        op.LOG.Log(f"StateExt.Set(): {key}: {value} - source component: {source}")
        # print("StateExt.Set(): calling RefreshDashboard()")
        op.LOG.Log("StateExt.Set(): calling RefreshDashboard()")
        self.RefreshDashboard()

    def Get(self, key, default=None):
        return self._state.get(key, default)

    def Remove(self, key):
        # print(f"StateExt.Remove(): attempting to remove key '{key}'")
        op.LOG.Log(f"StateExt.Remove(): attempting to remove key '{key}'")
        self._state.pop(key, None)
        self.RefreshDashboard()


    def RefreshDashboard(self):
        table = op.UI.op("state_table")

        table.clear()

        # print("StateExt.RefreshDashboard(): clearing table...")
        op.LOG.Log("StateExt.RefreshDashboard(): clearing table...")
        table.appendRow(["Feature", "Value", "Source"])

        for key, entry in self._state.items():
            # print(f"StateExt.RefreshDashboard(): adding {key}: {entry['value']} " 
                  # f"for source component {entry['source']}")
            op.LOG.Log(f"StateExt.RefreshDashboard(): adding {key}: {entry['value']} " 
                       f"for source component {entry['source']}")
            table.appendRow([
                key, 
                entry["value"], 
                entry["source"]
            ])