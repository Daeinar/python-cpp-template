#include "testlib.h"

std::vector<int> c_multiply(std::vector<int> &v, int c) {
  std::vector<int> w;
  for (int i = 0; i < v.size(); i++) {
    w.push_back(v[i]*c);
  }
  return w;
}

