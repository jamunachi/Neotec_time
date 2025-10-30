import frappe

def after_install():
    # consider any of these as "exists" to be safe across versions
    exists = (
        frappe.db.exists("Workspace", {"name": "AlphaX Time"})
        or frappe.db.exists("Workspace", {"label": "AlphaX Time"})
        or frappe.db.exists("Workspace", {"title": "AlphaX Time"})
    )
    if exists:
        return

    # Set ALL three: name, label, title
    doc = frappe.get_doc({
        "doctype": "Workspace",
        "name": "AlphaX Time",      # bypasses autoname
        "label": "AlphaX Time",     # required because autoname is field:label
        "title": "AlphaX Time",     # shown in UI
        "public": 1,
        "is_hidden": 0,
        "sequence_id": 0,
        "content": "[]",            # JSON string, not a list
        # optional: "module": "HR"
    })
    doc.insert(ignore_permissions=True)
