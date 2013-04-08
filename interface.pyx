from libcpp.vector cimport vector

cdef extern from "testlib.c":
  vector[int] c_multiply(vector[int] v, int c)

cpdef multiply(vector[int] v, int c):
  return c_multiply(v,c)
