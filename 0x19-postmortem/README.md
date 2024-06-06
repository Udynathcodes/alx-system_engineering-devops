**Issue Summary**

**Duration of the outage:**  
- Start time: June 1, 2024, 14:30 UTC  
- End time: June 1, 2024, 17:00 UTC  

**Impact:**  
- Service Affected: User Authentication Service  
- User Experience: Users were unable to log in to the platform, resulting in total access denial for both web and mobile applications.  
- Percentage of Users Affected: Approximately 85% of active users  

**Root Cause:**  
- A misconfigured database connection string during a routine deployment caused the authentication service to fail in establishing a connection to the primary database.

---

**Timeline**

- **14:30 UTC** - Issue detected by monitoring alerts indicating a spike in authentication failures.
- **14:32 UTC** - On-call engineer notified through pager duty.
- **14:35 UTC** - Initial investigation started; logs indicated database connection errors.
- **14:45 UTC** - Assumption: Possible database server issue. Database team alerted.
- **15:00 UTC** - Database team confirmed database servers were operational. Focus shifted to application configuration.
- **15:15 UTC** - Misleading path: Suspected network issues between the application server and database.
- **15:30 UTC** - Network team involved; no anomalies found in network connectivity.
- **16:00 UTC** - Cross-functional team review of the latest deployment changes initiated.
- **16:15 UTC** - Configuration file with database connection string reviewed; misconfiguration identified.
- **16:30 UTC** - Correct configuration applied and deployed.
- **16:45 UTC** - Authentication service gradually restored; continuous monitoring to ensure stability.
- **17:00 UTC** - Full service restoration confirmed; incident officially closed.

---

**Root Cause and Resolution**

**Root Cause:**  
The root cause of the outage was a misconfigured database connection string in the authentication service configuration file. During a routine deployment, the connection string included an incorrect database host address, preventing the authentication service from connecting to the primary database.

**Resolution:**  
The issue was resolved by:
1. Identifying the incorrect database connection string in the service configuration file.
2. Correcting the database host address in the configuration.
3. Redeploying the authentication service with the correct configuration.
4. Monitoring the service to ensure successful connections and user logins.

---

**Corrective and Preventative Measures**

**Improvements/Fixes:**
1. Implement a deployment checklist that includes verification of configuration files.
2. Enhance monitoring to include configuration validation checks.
3. Introduce automated testing to simulate deployment environments and catch misconfigurations.
4. Conduct regular training sessions for engineers on deployment best practices.

**Task List:**
1. **Patch Deployment Process:** Update the deployment pipeline to include automated configuration validation scripts.
2. **Add Monitoring:** Implement monitoring for configuration changes and database connection failures.
3. **Automated Testing:** Develop and integrate automated tests to validate configuration settings before deployment.
4. **Engineer Training:** Schedule and conduct training workshops for engineers focused on deployment and configuration management.

5. **Documentation:** Update internal documentation to reflect the new deployment and monitoring processes.

By addressing these tasks, we aim to mitigate the risk of similar incidents in the future and ensure a more robust deployment process.
