// Copyright (c) 2025, Monorom and contributors
// For license information, please see license.txt

frappe.ui.form.on("task", {
        is_completed: function(frm){
            if(frm.doc.is_completed){

                frm.set_value('status', 'Done')
            }else{
                frm.set_value('status', 'To Do')
            }
        },

        status: function(frm){
            if(frm.doc.status === "Done"){
                frm.set_value("is_completed", true)
            }else{
                frm.set_value("is_completed", false)
            }
        }
});
