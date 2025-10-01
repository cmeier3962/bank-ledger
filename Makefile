.PHONY: smoke clean

smoke:
	@PYTHONPATH=src python scripts/smoke_test.py

clean:
	@rm -rf __pycache__ .pytest_cache .coverage coverage.xml