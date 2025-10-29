import frappe

def after_install():
    if not frappe.db.exists("Workspace", {"label": "AlphaX Time"}):
        frappe.get_doc({
            "doctype": "Workspace",
            "name": "AlphaX Time",
            "label": "AlphaX Time",
            "public": 1,
            "is_hidden": 0,
            "sequence_id": 0,
            "content": []
        }).insert(ignore_permissions=True)
