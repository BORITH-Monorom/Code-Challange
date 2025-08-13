// Copyright (c) 2025, Monorom and contributors
// For license information, please see license.txt

frappe.ui.form.on("Parent Doc", {
    // onload: function(frm){
    //     frappe.msgprint("Here is the Parent")
    // }
    age: function(frm){
        if(frm.doc.age < 18){
            frappe.msgprint(`You are teenager`, "allow only 18+")
        }else{
            frappe.msgprint("You are a man")
        }
    }

});
 