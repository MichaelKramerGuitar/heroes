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

    def Set(self, key, value):
        self._state[key] = value

    def Get(self, key, default=None):
        return self._state.get(key, default)