# AI Prompt Templates for Daily Work 📋

Complete template collection for every common task. Copy, fill in, and use!

---

## 📑 Table of Contents

1. **Quick Templates** - For fast everyday tasks
2. **Detailed Templates** - For complex work
3. **Specialty Templates** - For specific scenarios
4. **Tips & Tricks** - Pro tips for better results

---

# QUICK TEMPLATES (2-3 Minutes)

## QUICK TASK TEMPLATE

Use for: Simple coding tasks, quick fixes, small features

```
QUICK TASK

WHAT: [One sentence what you need]
WHERE: [File or component]
WHY: [Brief reason]
DETAILS: [Code snippet or context]
OUTPUT: [What you want to receive]
```

**Example:**
```
QUICK TASK

WHAT: Add error handling to API call
WHERE: src/services/userService.ts, function fetchUser()
WHY: Currently crashes if API fails
DETAILS: 
  Current: const data = await api.get('/user')
WHY: Returns 500 error sometimes, needs fallback
OUTPUT: Function with try-catch and error fallback
```

---

## QUICK CODE REVIEW TEMPLATE

Use for: Fast review of specific code

```
QUICK REVIEW

CODE LOCATION: [URL or file path]
LINES: [Line numbers if specific]
FOCUS: [What to check]
CONTEXT: [What it does]
```

**Example:**
```
QUICK REVIEW

CODE LOCATION: src/auth.ts lines 45-60
FOCUS: Security issues and performance
CONTEXT: Validates JWT tokens from requests
```

---

# DETAILED TEMPLATES (5+ Minutes)

## DETAILED TASK-BASED TEMPLATE

Use for: Complex features, significant changes

```
─ TASK REQUEST ─

PROJECT: [Project name]
TASK: [What needs to be built]

╔═══════════════════════╗
║  OBJECTIVE            ║
╚═══════════════════════╝
[One clear sentence of what success looks like]

╔═══════════════════════╗
║  BACKGROUND          ║
╚═══════════════════════╝
[Context: Why is this needed? What's the business reason?]

╔═══════════════════════╗
║  REQUIREMENTS         ║
╚═══════════════════════╝
- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3
- [ ] Requirement 4

╔═══════════════════════╗
║  TECHNICAL DETAILS    ║
╚═══════════════════════╝
Language/Framework: [e.g., React, Node.js]
Database: [If applicable]
Third-party APIs: [If needed]
Performance: [Speed/response time needs]
Security: [Special concerns]

╔═══════════════════════╗
║  SUCCESS CRITERIA     ║
╚═══════════════════════╝
✓ [How to verify it's done correctly]
✓ [What should work]
✓ [What should NOT break]

╔═══════════════════════╗
║  CONSTRAINTS          ║
╚═══════════════════════╝
⚠ [Limitations/restrictions]
⚠ [Things to be careful about]
⚠ [Incompatibilities]

╔═══════════════════════╗
║  DELIVERABLE         ║
╚═══════════════════════╝
[Type of output needed - code, docs, etc.]
[Format expected]
[Quality level required]
```

---

## DETAILED CODE REVIEW TEMPLATE

Use for: Thorough review of major code changes

```
─ CODE REVIEW REQUEST ─

╔═══════════════════════╗
║  CODE LOCATION        ║
╚═══════════════════════╝
URL: [GitHub link]
Branch: [Branch name]
PR: [PR number if applicable]

╔═══════════════════════╗
║  WHAT THIS DOES       ║
╚═══════════════════════╝
[Paragraph explaining the code's purpose]

╔═══════════════════════╗
║  FOCUS AREAS          ║
╚═══════════════════════╝
- [x] Security (vulnerabilities, auth)
- [x] Performance (queries, caching)
- [x] Code quality (readability, patterns)
- [x] Testing (coverage, edge cases)
- [x] Documentation (clarity, comments)

╔═══════════════════════╗
║  SPECIFIC QUESTIONS   ║
╚═══════════════════════╝
Q1: [First question]
Q2: [Second question]
Q3: [Third question]

╔═══════════════════════╗
║  CONTEXT              ║
╚═══════════════════════╝
[Team standards and patterns to follow]
[Related documentation]
[Similar implementations to reference]

╔═══════════════════════╗
║  EXPECTED OUTPUT      ║
╚═══════════════════════╝
[Type of feedback wanted]
[Format of response]
[Priority issues vs. nice-to-haves]
```

---

## DETAILED PROBLEM-SOLVING TEMPLATE

Use for: Debugging bugs, troubleshooting

```
─ PROBLEM STATEMENT ─

╔═══════════════════════╗
║  THE ISSUE            ║
╚═══════════════════════╝
[One line description of what's wrong]

╔═══════════════════════╗
║  HOW IT FAILS         ║
╚═══════════════════════╝
Steps to reproduce:
1. [Step 1]
2. [Step 2]
3. [Step 3]

╔═══════════════════════╗
║  WHAT SHOULD HAPPEN   ║
╚═══════════════════════╝
[Expected behavior]

╔═══════════════════════╗
║  WHAT ACTUALLY HAPPENS║
╚═══════════════════════╝
[Actual behavior]

╔═══════════════════════╗
║  ERROR MESSAGES       ║
╚═══════════════════════╝
[Errors or logs]
[Stack trace if available]

╔═══════════════════════╗
║  ENVIRONMENT          ║
╚═══════════════════════╝
OS: [Windows/Mac/Linux]
Browser: [Version]
Node: [Version]
Frameworks: [Names and versions]
Database: [If applicable]

╔═══════════════════════╗
║  WHAT I'VE TRIED      ║
╚═══════════════════════╝
- [x] Attempt 1 - Result
- [x] Attempt 2 - Result
- [x] Attempt 3 - Result

╔═══════════════════════╗
║  CURRENT CODE         ║
╚═══════════════════════╝
[Relevant code snippet]

╔═══════════════════════╗
║  WHAT CHANGED         ║
╚═══════════════════════╝
[Recent changes that might be related]

╔═══════════════════════╗
║  IMPACT               ║
╚═══════════════════════╝
Severity: [Critical/High/Medium/Low]
Users affected: [How many/who]
Urgency: [Timeline needed]
```

---

## DETAILED FEATURE DEVELOPMENT TEMPLATE

Use for: Building major features

```
─ FEATURE DEVELOPMENT ─

╔═══════════════════════╗
║  FEATURE NAME         ║
╚═══════════════════════╝
[Official name of feature]

╔═══════════════════════╗
║  USER STORY           ║
╚═══════════════════════╝
As a [user type]
I want to [action]
So that [benefit]

╔═══════════════════════╗
║  BUSINESS CONTEXT     ║
╚═══════════════════════╝
[Why this feature matters]
[What problem it solves]
[Expected impact]

╔═══════════════════════╗
║  REQUIREMENTS         ║
╚═══════════════════════╝
FUNCTIONAL:
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

TECHNICAL:
- [ ] [Tech requirement 1]
- [ ] [Tech requirement 2]

NON-FUNCTIONAL:
- [ ] Performance: [Target]
- [ ] Scalability: [Requirements]
- [ ] Security: [Concerns]

╔═══════════════════════╗
║  ACCEPTANCE CRITERIA  ║
╚═══════════════════════╝
Given [context]
When [action]
Then [outcome]

[Repeat for multiple scenarios]

╔═══════════════════════╗
║  DESIGN APPROACH      ║
╚═══════════════════════╝
Frontend: [Technology, components]
Backend: [Technology, endpoints]
Database: [Schema changes]
Third-party: [Services needed]

╔═══════════════════════╗
║  DEPENDENCIES         ║
╚═══════════════════════╝
- [x] Dependency 1 (due date)
- [x] Dependency 2 (status)
- [x] Blocking task (priority)

╔═══════════════════════╗
║  TIMELINE             ║
╚═══════════════════════╝
Priority: [P0/P1/P2]
Needed by: [Date]
Estimated effort: [Hours/days]

╔═══════════════════════╗
║  DELIVERABLES         ║
╚═══════════════════════╝
- [ ] Working feature
- [ ] Unit tests (>90% coverage)
- [ ] Documentation
- [ ] Demo/PR ready
```

---

## DETAILED DOCUMENTATION TEMPLATE

Use for: Writing comprehensive guides

```
─ DOCUMENTATION REQUEST ─

╔═══════════════════════╗
║  TOPIC                ║
╚═══════════════════════╝
[What to document]

╔═══════════════════════╗
║  INTENDED AUDIENCE    ║
╚═══════════════════════╝
Primary: [Skill level, role]
Secondary: [Other users who might read]

╔═══════════════════════╗
║  PURPOSE              ║
╚═══════════════════════╝
[Why this documentation is needed]
[What problem it solves]

╔═══════════════════════╗
║  REQUIRED SECTIONS    ║
╚═══════════════════════╝
1. [Section title]
2. [Section title]
3. [Section title]
4. [Section title]
5. [Section title]

╔═══════════════════════╗
║  STYLE PREFERENCES    ║
╚═══════════════════════╝
Tone: [Technical/Casual/Formal]
Depth: [Overview/Detailed/Expert]
Verbosity: [Concise/Balanced/Comprehensive]

╔═══════════════════════╗
║  REQUIRED ELEMENTS    ║
╚═══════════════════════╝
- [x] Code examples (languages: [])
- [x] Diagrams/flowcharts
- [x] Real request/response examples
- [x] FAQ section
- [x] Troubleshooting
- [x] Links to related docs

╔═══════════════════════╗
║  FORMAT & LENGTH      ║
╚═══════════════════════╝
Format: [Markdown/HTML/PDF]
Length: [Word count or page count]
Structure: [Linear/Hierarchical]
TOC: [Yes/No]

╔═══════════════════════╗
║  REFERENCES           ║
╚═══════════════════════╝
[Link to similar docs]
[Link to source material]
[Link to specifications]

╔═══════════════════════╗
║  DELIVERABLE         ║
╚═══════════════════════╝
[Ready to publish format]
[Quality expectations]
[Approval process]
```

---

# SPECIALTY TEMPLATES

## LEARNING REQUEST TEMPLATE

Use when: Learning new technology/concept

```
LEARNING OBJECTIVE

TOPIC: [What to learn]

CURRENT KNOWLEDGE:
[What I already know - be specific]

TARGET KNOWLEDGE:
After learning, I should be able to:
1. [Skill 1]
2. [Skill 2]
3. [Skill 3]

DEPTH LEVEL:
[ ] Beginner overview
[ ] Intermediate understanding
[ ] Expert level
[ ] Hands-on practical

TIME BUDGET:
[How much time you can spend]

PRACTICAL APPLICATION:
[How you'll use this knowledge]

PRIOR STRUGGLES:
[What confused you before]

PREFERRED LEARNING STYLE:
[ ] Conceptual explanation
[ ] Step-by-step tutorial
[ ] Real-world examples
[ ] Interactive code walkthrough
```

---

## ARCHITECTURE DECISION TEMPLATE

Use when: Choosing between technical approaches

```
ARCHITECTURE DECISION

CHALLENGE: [Problem to solve]

OPTIONS UNDER CONSIDERATION:
1. Option A: [Description]
2. Option B: [Description]
3. Option C: [Description]

CONSTRAINTS:
- Budget: [Max cost]
- Team: [Size, skills]
- Performance: [Requirements]
- Timeline: [Deadline]
- Scaling: [Growth expectations]

EVALUATION CRITERIA:
[How to judge which is best]

TRADE-OFFS:
For each option, compare:
- Cost
- Complexity
- Performance
- Learning curve
- Maintenance effort

CURRENT STATE:
[What we're using now]
[Known issues]
[Limitations]

WHAT WOULD HELP:
Recommendation with:
- Pros and cons
- Cost comparison
- Implementation effort
- Long-term implications
```

---

## API DESIGN TEMPLATE

Use when: Designing REST/GraphQL endpoints

```
API ENDPOINT DESIGN

ENDPOINT: [Method and path]
PURPOSE: [What it does]

REQUEST:
- Method: [GET/POST/PUT/DELETE]
- Path: [/path/to/resource]
- Auth: [Required/Optional]
- Rate limit: [Requests per minute]

PARAMETERS:
- [param name]: [type, required/optional, description]

REQUEST BODY EXAMPLE:
[JSON example]

RESPONSES:
Success (200):
[Response example]

Error (400):
[Error response]

Error (401):
[Unauthorized response]

Error (500):
[Server error response]

EDGE CASES:
- [Case 1: How handled]
- [Case 2: How handled]

IMPLEMENTATION NOTES:
[Special considerations]
```

---

## PERFORMANCE OPTIMIZATION TEMPLATE

Use when: Improving speed/efficiency

```
OPTIMIZATION REQUEST

WHAT'S SLOW: [Component/Query/Feature]

CURRENT METRICS:
- Response time: [XYZ ms]
- CPU usage: [X%]
- Memory: [X MB]
- Database queries: [X]

TARGET METRICS:
- Response time: [Target ms]
- CPU usage: [Target %]
- Memory: [Target MB]

CONSTRAINTS:
- Can't change: [Unchangeable parts]
- Budget: [Cost limit]
- Availability: [Can't be down]

CURRENT APPROACH:
[How it currently works]

BOTTLENECK ANALYSIS:
[Where time is spent]
[Where resources are used]

ATTEMPTED FIXES:
[What you've tried]

DESIRED OUTCOME:
[Type of solution wanted]
```

---

## CODE EXPLANATION TEMPLATE

Use when: Understanding unfamiliar code

```
CODE EXPLANATION REQUEST

CODE LOCATION:
[File path and lines, or code snippet]

CONTEXT:
[Where it's used]
[Why it matters]

WHAT CONFUSES ME:
1. [Specific line/pattern]
2. [Specific behavior]
3. [Design choice]

WHAT I UNDERSTAND:
[What makes sense so far]

WHAT I WANT TO KNOW:
[Specific questions]

USAGE EXAMPLE:
[How it's called/used]
```

---

# PRO TIPS & TRICKS 🎯

## Tip 1: Be Specific
❌ Bad: "This is slow"
✅ Good: "Home page takes 4.5s to load, should be <1s on 3G"

## Tip 2: Show Your Work
❌ Bad: "This doesn't work"
✅ Good: "Steps to reproduce: 1) Login 2) Click button 3) Page crashes with 'Cannot read property X'"

## Tip 3: Provide Context
❌ Bad: "Fix this code"
✅ Good: "This code handles user authentication for mobile Safari - currently fails because..."

## Tip 4: Define Success
❌ Bad: "Make this better"
✅ Good: "Reduce response time from 5s to under 1s"

## Tip 5: Include Examples
❌ Bad: "Add validation"
✅ Good: "Email should match /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/"

## Tip 6: Iterate on Responses
If response isn't perfect:
1. Point out what was unclear
2. Ask for specific clarification
3. Refine your next prompt

## Tip 7: Use Formatting
- Use **bold** for emphasis
- Use `code` for specific terms
- Use lists for clarity
- Use spacing between sections

---

## Checklist Before Sending

Before you submit your prompt, check:

- [ ] One clear objective (not multiple questions)
- [ ] Context provided (background/why)
- [ ] Specific details included (not vague)
- [ ] Current code or attempt shown (if applicable)
- [ ] Error messages included (if applicable)
- [ ] Expected output defined (what you want back)
- [ ] Format/language specified
- [ ] Constraints mentioned (budget, time, etc.)

---

**Last Updated:** 2026-05-15

**Quick Start:** Pick the template that matches your task, copy it, fill in [brackets], and send!

