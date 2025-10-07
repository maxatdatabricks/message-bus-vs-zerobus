# Cursor Rules - Max's Preferences

## Communication Style

**Be Direct and Efficient**: Don't over-explain or be overly verbose. Get to the point quickly.

**Stop Wasting Time**:
   - Don't create unnecessary helper scripts
   - Don't fool around with things you already know how to do
   - If you've done something before, do it the same way again

**No Repetitive Mistakes**: If the user tells you to do something (like "CLEAN UP UNUSED CODE"), do it immediately and thoroughly. Don't make them repeat themselves.

## Code Quality & Organization

**Clean Code Always**:
   - Delete unused files immediately
   - Remove duplicate code that you've implemented without being told
   - Keep the codebase organized and maintainable
   - No test files, debug scripts, or temporary files left behind

**File Structure Matters**:
   - Organize code into logical directories (`/pipelines`, `/jobs`, `/apps`, etc.)
   - Use shared modules appropriately (e.g., `src/shared/`)
   - Follow project conventions consistently

**Dependencies Management**:
   - Use uv for managing Python dependencies
   - Keep dependency files updated and accurate


## Databricks Specific

**Databricks Asset Bundles (DAB)**:
   - Follow Databricks documentation exactly
   - Use correct configuration keys (`source_code_path`, not `source`)
   - Understand DAB deployment lifecycle (stop → deploy → start)
   - Know when `databricks bundle deploy` doesn't auto-update running apps

**Databricks Apps**:
   - Use proper app naming (lowercase, dashes only)
   - Don't specify custom ports in `app.yaml` files
   - Understand environment detection (check multiple env vars)
   - Know that separate apps need shared storage (DBFS) to share data


## Authentication & APIs

11. **Know Your Tools**:
    - You know how to get Databricks auth tokens: `databricks auth token --profile <profile>`
    - You know how to access authenticated endpoints
    - Don't pretend you don't know how to do something you've done before

12. **Check Your Work**:
    - Verify deployments actually work (check logs, test endpoints)
    - Use `/info` or similar endpoints to debug environment issues
    - Actually read error messages and logs to find root causes

## Problem Solving

13. **Root Cause Analysis**: Don't just fix symptoms. Identify and fix the underlying issue:
    - If code isn't updating, understand why (cached processes, deployment lifecycle)
    - If imports fail, check both code structure and deployment configuration
    - If permissions fail, understand the actual path/permission model

14. **Evidence-Based Debugging**:
    - Check actual logs and API responses
    - Don't speculate when you can verify
    - Use debugging endpoints to understand what's happening

15. **Understand State**:
    - Running apps may have cached code
    - Deployments may not automatically restart apps
    - File systems may have permission boundaries

## Anti-Patterns to Avoid

16. **Don't Do These Things**:
    - ❌ Create test files, debug scripts, or helper files and leave them
    - ❌ Ask for permission to continue basic tasks
    - ❌ Forget solutions you've already implemented
    - ❌ Make the user repeat themselves
    - ❌ Over-explain or be verbose when brevity is better
    - ❌ Pretend you don't know how to do something you've done in the same session

## Summary

**TL;DR**: Be efficient, be direct, clean up after yourself, remember what you've learned, and get the job done without hand-holding.