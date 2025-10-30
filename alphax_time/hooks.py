
app_name = "alphax_time"
app_title = "AlphaX Time"
app_publisher = "Neotec Integrated Solutions"
app_description = "Multi-country flextime & attendance engine for ERPNext HRMS"
app_email = "support@neotec.example"
app_version = "0.1.0"
app_license = "MIT"

# Include in Desk
app_include_js = []
app_include_css = []

# Fixtures: workspace (basic)
fixtures = [
    # remove the Workspace fixture to avoid duplicate/ordering issues for now
    # {"dt": "Workspace", "filters": [["label", "=", "AlphaX Time"]]}
]



# DocType Events / Scheduler
scheduler_events = {
    "hourly": [
        "alphax_time.utils.scheduler.hourly_process"
    ]
}

after_install = "alphax_time.utils.install.after_install"
