# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = source/_build

CONDA_ENV_NAME=sphinx
PWD=$(shell pwd)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	rm -rf docs/*
	cp -R $(BUILDDIR)/html/* docs

serve:
	conda run -n ${CONDA_ENV_NAME} --cwd=$(PWD)  --live-stream sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html"

commit: html
	git add --all
	git commit -m "自动"
	git push