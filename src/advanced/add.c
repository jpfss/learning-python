#include <Python.h>

int add_one(int a){
    return a + 1;      
}

static PyObject * py_add_one(PyObject *self, PyObject *args){
    int num;
    if (!PyArg_ParseTuple(args, "i", &num)) return NULL;
    return PyLong_FromLong(add_one(num));
}

static PyMethodDef Methods[] = {
    {"add_one", py_add_one, METH_VARARGS}, 
    {NULL, NULL}
};

static struct PyModuleDef cModule = {
    PyModuleDef_HEAD_INIT,
    "Test", /*module name*/
    "", /* module documentation, may be NULL */
    -1, /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    Methods
};

PyMODINIT_FUNC PyInit_Test(void){ return PyModule_Create(&cModule);}