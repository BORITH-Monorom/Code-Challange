// Copyright (c) 2025, Monorom and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicles", {
    vehicle_type: function(frm) {
            // Filter brands by selected vehicle type
            frm.set_query('brand', function() {
                return {
                    filters: { type: frm.doc.vehicle_type },
                };
            });
        }
});
