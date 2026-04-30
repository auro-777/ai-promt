Absolutely. Here’s a precise AI prompt that focuses on notification without automated blocking:

---

As an AI architecture agent, design a GitHub Actions workflow that periodically (e.g., every 2–3 hours) pulls vulnerability data from multiple external feeds (e.g., NVD, CERT, MITRE). After gathering the data, the workflow should compare the newly published vulnerabilities against the existing JFrog X-Ray curation rules (via JFrog REST APIs) to identify any new vulnerable packages not yet blocked.

The workflow should:

1. Pull and parse multiple vulnerability feeds.
2. Consolidate results and compare them to JFrog X-Ray curated policies.
3. If any newly published vulnerable package is detected (i.e., not blocked in JFrog), send a detailed email notification to the security team. The email should contain the package name, CVE, severity, and source feed.
4. Ensure no automatic blocking occurs—no curation overrides; the team must manually validate and act.
5. Provide a modular design so new feeds can be added or adjusted.
6. Include a high-level architecture diagram (e.g., in Mermaid) showing the flow from external feeds to comparison with JFrog, and email notification to the team.
7. Draft a README that explains how to configure the workflow, add feeds, and customize email recipients.

Focus on a human-in-the-loop approach: the workflow should empower the team with timely notifications so they can validate the risk and decide if a manual block is necessary.

---

This prompt ensures the AI focuses on a notification-driven workflow, keeping the manual validation step intact, while still automating the detection and reporting side of things. Let me know if that covers it!
