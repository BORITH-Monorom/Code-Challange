# Copyright (c) 2025, Monorom and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class ModelVariants(Document):
	def autoname(self):
		model_variants = self.model_variants_name.strip().replace(" ", "-")
		self.name = make_autoname(f"VB-.###.-{model_variants}")

	pass
