
import frappe

def after_install():
    # Create a basic Workspace if not already imported via fixtures
    try:
        if not frappe.db.exists("Workspace", {"label": "AlphaX Time"}):
            ws = frappe.new_doc("Workspace")
            ws.label = "AlphaX Time"
            ws.public = 1
            ws.is_hidden = 0
            ws.insert(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "AlphaX Time after_install")
