# apps/alphax_time/alphax_time/utils/install.py
import frappe

def after_install():
    # Some versions key Workspaces by label; be safe and check both fields
    exists = frappe.db.exists("Workspace", {"label": "AlphaX Time"}) or \
             frappe.db.exists("Workspace", {"title": "AlphaX Time"})
    if not exists:
        frappe.get_doc({
            "doctype": "Workspace",
            # IMPORTANT for autoname
            "label": "AlphaX Time",
            # Good to also set title for UI
            "title": "AlphaX Time",
            "public": 1,
            "is_hidden": 0,
            "sequence_id": 0,
            # Workspace expects JSON string for content
            "content": "[]"
            # Optional niceties:
            # "module": "HR"  # or a module you prefer
        }).insert(ignore_permissions=True)
