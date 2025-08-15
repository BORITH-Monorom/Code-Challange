# Copyright (c) 2025, Monorom and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class BrandType(Document):
	def autoname(self):
		brand = self.brand_name.strip().replace(" ", "-")
		self.name = make_autoname(f"VB-.###.-{brand}")

	pass