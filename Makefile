.PHONY:
all: clean resources/icons.py

# build resource files:
resources/%.py: resources/%.qrc
	pyrcc5 -o $@ $<

.PHONY:
clean:
	find . -d -name __pycache__ | xargs rm -rf
	rm resources/*.py

