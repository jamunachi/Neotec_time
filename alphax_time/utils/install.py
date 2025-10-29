# apps/alphax_time/alphax_time/utils/install.py
import frappe

def after_install():
    # Prefer checking by title (current field used in Workspace UI)
    exists = frappe.db.exists("Workspace", {"title": "AlphaX Time"})
    if not exists:
        frappe.get_doc({
            "doctype": "Workspace",
            "title": "AlphaX Time",   # REQUIRED
            "public": 1,
            "is_hidden": 0,
            "sequence_id": 0,
            "content": "[]",          # store JSON as string, e.g., "[]"
            # Optional but harmless (helps organization in the Desk):
            # "module": "HR",  # or any module name you prefer
        }).insert(ignore_permissions=True)
