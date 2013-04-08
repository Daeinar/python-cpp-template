main:
	python setup.py build_ext --inplace

clean:
	rm -rf build/ interface.{c,cpp} testlib.so
