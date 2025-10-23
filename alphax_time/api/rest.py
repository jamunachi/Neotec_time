
import frappe
from frappe import _

@frappe.whitelist()
def ping():
    return {"status": "ok", "app": "alphax_time"}
