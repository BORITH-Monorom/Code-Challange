# Copyright (c) 2025, Monorom and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt

class VehicleActivityLog(Document):
	def validate(self):
		if flt(self.odometer) < flt(self.last_odometer_value):
			frappe.throw(
				_("Current Odometer Value should be greater than Last Odometer Value {0}").format(self.last_odometer_value)
			)
	def on_submit(self):
		frappe.db.set_value("Vehicles", self.license_plate, "last_odometer", self.odometer)

