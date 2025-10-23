
# AlphaX Time (alphax_time)

Multi-country flextime & attendance engine for ERPNext HRMS.

## Install (Frappe/ERPNext v15)

```bash
# From your bench folder
bench get-app https://example.com/alphax_time.git
bench --site your.site install-app alphax_time
```

## Verify

```python
# In bench console
frappe.get_all("Workspace", filters={"label":"AlphaX Time"})
```

## Notes
- Minimal skeleton with core DocTypes to start. Extend fields/rules per your policy packs.
- Scheduler heartbeat is wired. See: `alphax_time/utils/scheduler.py`.
