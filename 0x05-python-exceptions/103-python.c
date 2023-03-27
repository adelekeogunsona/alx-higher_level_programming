#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
	int i;
	PyListObject *list;

	if (!PyList_Check(p)) {
		printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
    }

	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)PyList_GET_SIZE(p));
	printf("[*] Allocated = %d\n", (int)list->allocated);

	for (i = 0; i < PyList_GET_SIZE(p); i++) {
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
	fflush(stdout);
}

void print_python_bytes(PyObject *p)
{
	int i, size;
	char *bytes;

	if (!PyBytes_Check(p)) {
		printf("[*] Python bytes info\n  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
    }

	bytes = PyBytes_AsString(p);
	size = PyBytes_Size(p);

	printf("[*] Python bytes info\n");
	printf("  [.] bytes object info\n");
	printf("    - size: %d\n", size);
	printf("    - trying string: %s\n", bytes);

	printf("  [.] first %d bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 9; i++) {
		printf("%02hhx ", bytes[i]);
	}
	if (size >= 10) {
		printf("%02hhx", bytes[i]);
	}
	printf("\n");
	fflush(stdout);
}

void print_python_float(PyObject *p)
{
	char *float_str;

	if (!PyFloat_Check(p)) {
		printf("[*] Python float info\n  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	float_str = PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("[*] Python float info\n  value: %s\n", float_str);
	fflush(stdout);
}
