
import frappe

def hourly_process():
    # Placeholder job to verify scheduler wiring.
    # Later: compute Daily Flextime Status for pending days.
    frappe.logger().info("AlphaX Time hourly scheduler heartbeat OK.")
