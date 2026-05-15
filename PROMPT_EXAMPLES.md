# Real-World Prompt Examples 🎓

Copy-paste ready examples for common daily scenarios.

---

## EXAMPLE 1: Bug Fix in Production

**Scenario:** User reported bug, need quick fix

```
PROBLEM STATEMENT

ISSUE:
Login button not responding on mobile devices after latest update

SYMPTOMS:
- Click event fires but page doesn't navigate
- Console shows no errors
- Only happens on iOS Safari (version 16+)
- Works fine on desktop and Android

EXPECTED BEHAVIOR:
User clicks login button → taken to /login page

CURRENT BEHAVIOR:
User clicks login button → nothing happens, stays on same page

ENVIRONMENT:
- React 18.2.0, Next.js 13.4
- iOS Safari 16.5
- Mobile viewport

WHEN IT OCCURS:
1. Visit site on iPhone
2. Tap login button
3. Notice no navigation

ATTEMPTED FIXES:
- Added e.preventDefault() - didn't help
- Tried onClick vs onTouchEnd - no difference
- Checked network requests - never fires

CURRENT CODE:
<button onClick={() => router.push('/login')}>
  Login
</button>

WHAT I'VE CHECKED:
- [x] JavaScript enabled
- [x] Mobile viewport meta tags present
- [x] No console errors
- [x] Button is not disabled
- [x] z-index isn't blocking click

ERROR LOGS:
[No errors in console]

DESIRED SOLUTION:
Root cause analysis - why doesn't iOS Safari trigger the click handler?
```

---

## EXAMPLE 2: Code Review Request

**Scenario:** Team member wants feedback on authentication module

```
CODE REVIEW REQUEST

REPO/FILE: 
https://github.com/myorg/app/blob/main/src/lib/auth.ts

CONTEXT:
This is a new authentication module replacing our old system. 
It handles user login, token refresh, and session management.
Using JWT tokens stored in httpOnly cookies.

REVIEW FOCUS AREAS:
- [x] Security (vulnerabilities, auth best practices)
- [x] Performance (database queries, caching)
- [x] Code quality (clarity, maintainability)
- [x] Error handling
- [x] Testing completeness

SPECIFIC QUESTIONS:
1. Is storing refresh token in httpOnly cookie the right approach?
2. Should we add rate limiting to login endpoint?
3. Are there race conditions with concurrent token refreshes?
4. Is the error logging secure (not exposing sensitive info)?

EXPECTED OUTPUT:
Line-by-line comments with suggestions, security review, and summary assessment.
```

---

## EXAMPLE 3: Feature Development

**Scenario:** Building new user dashboard feature

```
FEATURE DEVELOPMENT REQUEST

FEATURE NAME: 
User Analytics Dashboard

USER STORY:
As a user
I want to see my activity metrics and engagement stats
So that I can track my progress and understand my usage patterns

REQUIREMENTS:
- [ ] Display total logins, page views, features used
- [ ] Show 7-day, 30-day, 90-day views
- [ ] Calculate daily active time (hh:mm)
- [ ] Export data as CSV
- [ ] Mobile responsive design
- [ ] Load in under 2 seconds

ACCEPTANCE CRITERIA:
- [ ] User can select different time periods from dropdown
- [ ] Charts update when period changes
- [ ] CSV export includes all visible data
- [ ] Mobile view is readable on 375px width
- [ ] Respects user privacy settings (don't show restricted data)

TECHNICAL APPROACH:
- Frontend: React with Recharts for charts
- Backend: New /api/analytics endpoint
- Database: Add analytics table, aggregate queries
- Cache: Redis for 1-hour cache
- Auth: Require user login

DEPENDENCIES:
- Recharts library (already in project)
- New database migration
- Analytics event tracking system (already exists)

TIMELINE/PRIORITY:
Needed by end of sprint (5 working days)

ADDITIONAL CONTEXT:
- Design mockups: [Figma link]
- Analytics schema: [Doc link]
- Similar feature in Competitor X: [reference]
```

---

## EXAMPLE 4: Debugging Performance Issue

**Scenario:** Page loads slowly, need to optimize

```
PROBLEM STATEMENT

ISSUE:
Home page load time increased from 1.2s to 4.5s after recent deploy

SYMPTOMS:
- Lighthouse score dropped from 85 to 42
- Network tab shows unnecessary requests
- Large bundle size detected
- Users complaining about slowness

EXPECTED BEHAVIOR:
Page loads in under 2 seconds on 3G connection

CURRENT BEHAVIOR:
Page loads in 4.5s+ on 3G connection (first contentful paint at 3.2s)

ENVIRONMENT:
- Node.js 18.16
- Next.js 13.4 with SSR
- Deployed on Vercel
- Testing on 3G throttle

WHEN IT OCCURS:
Every page load consistently shows 4.5s+ timing

ATTEMPTED FIXES:
- Cleared Vercel cache - still slow
- Checked build size - 245KB (seems reasonable)
- Removed new npm package - still slow
- Reverted to previous deploy - fast again (isolated to latest code)

CURRENT CODE:
What changed in latest deploy:
- Added new analytics component
- Updated image optimization
- New data fetching pattern

WHAT I'VE CHECKED:
- [x] Network request waterfall
- [x] JavaScript parsing time
- [x] CSS parsing time
- [x] Image optimization status
- [x] Bundle analysis
- [x] API response times

ERROR LOGS:
[Performance logs from Vercel - see attached]

DESIRED SOLUTION:
- What's causing the 3.3s increase?
- Which component/resource is the bottleneck?
- Step-by-step optimization plan
```

---

## EXAMPLE 5: Documentation Request

**Scenario:** Need to document API endpoints

```
DOCUMENTATION REQUEST

TOPIC: 
REST API Authentication & Authorization

PURPOSE:
New developers on the team need to understand how to build against our API

AUDIENCE:
- Backend developers (moderate experience)
- Frontend developers integrating our API
- API consumers/partners

SECTIONS TO INCLUDE:
- [ ] Authentication overview (JWT + API keys)
- [ ] Getting started (creating API key)
- [ ] Endpoint authorization levels
- [ ] Error codes and handling
- [ ] Rate limiting
- [ ] Security best practices
- [ ] Code examples (cURL, Node, Python)
- [ ] Common issues & troubleshooting
- [ ] FAQ

TONE/STYLE:
Technical but beginner-friendly, with lots of practical examples

INCLUDE:
- [x] Code examples (at least 3 languages)
- [x] Real request/response examples
- [x] Sequence diagram for OAuth flow
- [x] Links to sandbox environment
- [x] Table of contents

FORMAT/LENGTH:
- Format: Markdown
- Length: ~3000 words
- Structure: Progressive (easy → advanced)

REFERENCES:
- Current API docs: [link]
- OpenAPI spec: [link]
- Similar API docs style: [example]

DELIVERABLE:
Ready-to-publish document for developer portal
```

---

## EXAMPLE 6: Learning Request

**Scenario:** Need to understand a new technology

```
LEARNING REQUEST

TOPIC:
React Server Components (RSC)

CONTEXT:
Our team is considering using Next.js 13+ with App Router which uses RSCs heavily.
Need to understand pros/cons and implementation patterns.

CURRENT KNOWLEDGE:
- 5 years React experience (class + hooks)
- Familiar with SSR and SSG
- Know basics of Next.js Pages Router

DESIRED OUTCOME:
Be able to:
1. Explain what Server Components are and how they differ from client components
2. Know when to use Server vs Client components
3. Implement basic Server Component patterns
4. Understand state management implications

DEPTH:
Detailed guide (not just overview) with code examples

TIME:
30-60 minutes to read and understand

EXAMPLES:
- How to structure a full-page Server Component with dynamic data
- Client component interaction patterns
- When NOT to use Server Components
- Common gotchas and mistakes
```

---

## EXAMPLE 7: Quick Morning Standup

**Scenario:** Plan your day in 5 minutes

```
DAILY PLAN - 2026-05-15

TODAY'S PRIORITY TASKS:
1. Fix login bug on iOS (from yesterday) - Est: 2 hours
2. Code review for team PR - Est: 1 hour
3. Write analytics dashboard API spec - Est: 1.5 hours

BLOCKERS/RISKS:
- Need clarification from Product on dashboard requirements
- iOS bug might need debugging tools assistance

CONTEXT FROM YESTERDAY:
- Dashboard project approved for sprint
- iOS login bug confirmed as high priority
- New team member joined, onboarding next week

MEETINGS:
- 9:30 AM - Daily standup
- 2:00 PM - Product discussion
- 3:30 PM - 1-on-1 with manager

SUCCESS METRICS:
At end of day, I will have:
- [ ] iOS login bug fixed and tested
- [ ] Code review submitted with feedback
- [ ] Dashboard spec drafted and shared with team
- [ ] Onboarding doc reviewed for new hire

STRETCH GOALS:
- Start implementing analytics backend if time permits
- Update API documentation
```

---

## EXAMPLE 8: Architecture Decision

**Scenario:** Choosing between two approaches

```
ARCHITECTURE QUESTION

CHALLENGE:
Need to handle real-time notifications for 100k+ concurrent users.
Current solution uses polling and is becoming expensive.

OPTIONS UNDER CONSIDERATION:
1. WebSocket (Socket.io) - bidirectional real-time
2. Server-Sent Events (SSE) - unidirectional from server
3. Long polling with optimization - stay with current approach
4. AWS SNS + Lambda + API Gateway - serverless approach

CONSTRAINTS:
- Budget: $2000/month max
- Team: 2 backend engineers
- Latency requirement: <500ms for 95th percentile
- Current: AWS infrastructure (would prefer to stay)
- Scaling: Need to support 2x growth in 6 months

TRADE-OFFS TO CONSIDER:
- Cost vs. Complexity vs. Latency vs. Dev effort
- Which scales best?
- Which is easiest for our team to maintain?

CONTEXT:
- Current system: Node.js + Express
- 100k daily active users
- 50k peak concurrent
- Current polling: every 2 seconds
- Monthly cost: $3500

WHAT WOULD HELP:
Recommendation with justification, comparing:
- Implementation effort
- Monthly cost estimate
- Latency impact
- Team learning curve
- Long-term maintenance
```

---

## EXAMPLE 9: PR Feedback (Providing)

**Scenario:** Reviewing a teammate's code

```
CODE REVIEW FEEDBACK

CODE:
https://github.com/myorg/app/pull/1234/files#diff-abc123

POSITIVE OBSERVATIONS:
- Excellent error handling with specific error messages
- Good use of TypeScript strict mode
- Test coverage is comprehensive (95%+)
- Clear variable naming and function documentation
- Follows existing code style perfectly

IMPROVEMENTS NEEDED:
1. Lines 45-50: N+1 query problem
   - Current: Loop fetches user for each post
   - Suggested: Batch fetch all users then join in-memory
   - Reason: Performance degrades with 1000+ posts
   - Impact: Queries drop from 1000 to 2, ~50x faster

2. Line 78: Missing null check
   - Current: `user.profile.bio.length`
   - Suggested: `user?.profile?.bio?.length ?? 0`
   - Reason: Could crash if profile/bio undefined
   - Impact: Better error resistance

3. Line 120: Cache headers missing
   - Current: No cache-control header on GET endpoint
   - Suggested: Add `Cache-Control: max-age=300`
   - Reason: High-traffic endpoint, responses rarely change
   - Impact: Reduce server load by 40%

QUESTIONS:
- Why did you choose Option A over Option B for the state management?
- Have you tested this with large datasets (10k+ records)?
- Should we add rate limiting to this endpoint?

OVERALL:
Great PR! Code is clean and well-tested. Just a couple performance optimizations needed before merge. Once those are fixed, this is good to go.
```

---

## EXAMPLE 10: Optimization Task

**Scenario:** Speed up slow database query

```
OPTIMIZATION REQUEST

CURRENT STATE:
User profile page load takes 8+ seconds
Primary bottleneck: getUserProfile database query

METRICS:
- Current response: 8.2 seconds
- Query execution: 7.8 seconds (of 8.2)
- Users affected: ~40k profiles load daily
- User complaints: Rising

TARGET:
- Target response: <1 second
- Query execution: <200ms
- 99th percentile latency: <500ms

CONSTRAINTS:
- Cannot change database schema (affects other systems)
- No additional servers available
- Must maintain data consistency
- Budget: $500/month additional cost max

CONTEXT:
- Database: PostgreSQL 14
- 50 million user records
- Table size: 15GB
- Current indexes: id, email, created_at
- Join: users → posts → comments (3 levels deep)

CURRENT QUERY:
```sql
SELECT u.*, p.*, c.*
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
LEFT JOIN comments c ON p.id = c.post_id
WHERE u.id = $1
ORDER BY p.created_at DESC
```

WHAT WOULD HELP:
- Query optimization (better indexes, query rewrite)
- Caching strategy recommendations
- Database tuning suggestions
- Schema adjustments if absolutely necessary
- Step-by-step implementation plan
```

---

## QUICK COPY-PASTE SHORTCUTS

### Debugging Unknown Issue
```
I'm seeing [SYMPTOM] when I try [ACTION].
It should [EXPECTED] but instead [ACTUAL].

Environment: [Details]
Code: [snippet]
Attempted: [What I've tried]

What could be causing this?
```

### Stuck on Feature
```
I'm building [FEATURE] and got stuck on [SPECIFIC PROBLEM].

Current approach: [What I'm doing]
Problem: [What's wrong]
Code: [relevant snippet]

What would be the best way to [GOAL]?
```

### Need Second Opinion
```
I have two ways to solve [PROBLEM]:

Option A: [Description] - Pros: [List] Cons: [List]
Option B: [Description] - Pros: [List] Cons: [List]

Which is better and why?
```

### Learning New Topic
```
Explain [TOPIC] to someone who knows [PRIOR KNOWLEDGE].

I need to understand:
1. [Concept 1]
2. [Concept 2]
3. [Concept 3]

With examples of [SPECIFIC USE CASE].
```

---

**Last Updated:** 2026-05-15

**💡 Tip:** Find an example similar to your situation, copy it, and customize with your details!
