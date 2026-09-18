.PHONY: test check-release

# Run only synthetic standard-library tests; no research-data paths are accessed.
test:
	python3 -B -m unittest discover -s tests -v

# Inspect Git-tracked paths and text only; no local data is read.
check-release:
	python3 -B tools/check_release_boundary.py
