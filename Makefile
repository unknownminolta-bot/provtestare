# Casio formula bank: test, then EactMaker export (requires network for --convert).
PYTHON ?= python3
CASIO := casio

.PHONY: all build test casio-eam help

# Default: full build (audit tests + g2e + g1e binaries).
all: build

build: test
	$(PYTHON) $(CASIO)/generate_eam_g2e.py --convert --formats both

test:
	$(PYTHON) $(CASIO)/test_formula_audit.py

# .eam only (no HTTP); use when offline or iterating on SECTIONS text.
casio-eam:
	$(PYTHON) $(CASIO)/generate_eam_g2e.py

help:
	@echo "make / make build  — test + generate g2e + g1e (EactMaker, needs network)"
	@echo "make test          — run casio/test_formula_audit.py only"
	@echo "make casio-eam     — write .eam files only (no converter)"
