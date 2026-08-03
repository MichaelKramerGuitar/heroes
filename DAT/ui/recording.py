"""
Panel Execute DAT

me - this DAT

panelValue - the PanelValue object that changed
prev - the previous value of the PanelValue object that changed

Make sure the corresponding toggle is enabled in the Panel Execute DAT.
"""

from typing import Any

def onOffToOn(panelValue: PanelValue):
	"""
	Called when a panel value changes from 0 to non-zero.
	"""
	recording = op.STATE.Toggle(
		"recording",
		source="UI"
	)

	op.RECORD.op("RECORD_visual").par.record = recording
	
	return

def whileOn(panelValue: PanelValue):
	"""
	Called every frame while a panel value is non-zero.
	"""
	return

def onOnToOff(panelValue: PanelValue):
	"""
	Called when a panel value changes from non-zero to 0.
	"""
	# op.LOG.Log(f"[start_recording] ON TO OFF: Panel value changed to {panelValue.val}")
	# op.RECORD.op("RECORD_visual").par.record = False
	return

def whileOff(panelValue: PanelValue):
	"""
	Called every frame while a panel value is 0.
	"""
	return

def onValueChange(panelValue: PanelValue, prev: Any):
	"""
	Called when a panel value changes.
	
	Args:
		panelValue: The PanelValue object that changed
		prev: The previous value of the PanelValue object
	"""
	# if panelValue.val:
	# 	op.STATE.Activate("recording", source="UI")
	# 	op.AUDIO.op("audiodevin1").par.active = True
	# 	op.LOG.Log(f"[recording]: Panel value changed from {prev} to {panelValue.val}")
	# else:
	# 	op.STATE.Deactivate("recording")
	# 	op.AUDIO.op("audiodevin1").par.active = False
	# 	op.LOG.Log(f"[recording]: Panel value changed from {prev} to {panelValue.val}")