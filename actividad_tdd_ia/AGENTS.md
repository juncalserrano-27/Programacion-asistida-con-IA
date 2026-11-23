## Definition of done
- Before saying a task is finished, run `python -m pytest` and show me the output.
- Never edit anything in tests/ unless I explicitly ask.
- Never use @pytest.mark.skip, @pytest.mark.xfail, `# noqa`, `# type: ignore`,
  or wrap code in try/except to hide a failure: fix it or ask me.
- Implement only what a test requires. No extra features.
