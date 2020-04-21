#include</home/evgeny/ENS_DISKR_OPTIM/3_sat/minisat/core/Solver.h>

#include <iostream>
using Minisat::mkLit;
using Minisat::lbool;
using Minisat::Solver;
int main() {
   

    Solver solver();
    // Create variables
    auto A = solver.newVar();
    // auto B = solver.newVar();
    // auto C = solver.newVar();
    
    // // Create the clauses
    // solver.addClause( mkLit(A),  mkLit(B),  mkLit(C));
    // solver.addClause(~mkLit(A),  mkLit(B),  mkLit(C));
    // solver.addClause( mkLit(A), ~mkLit(B),  mkLit(C));
    // solver.addClause( mkLit(A),  mkLit(B), ~mkLit(C));
    
    // // Check for solution and retrieve model if found
    // auto sat = solver.solve();
    // if (sat) {
    //     std::clog << "SAT\n"
    //               << "Model found:\n";
    //     std::clog << "A := " << (solver.modelValue(A) == l_True) << '\n';
    //     std::clog << "B := " << (solver.modelValue(B) == l_True) << '\n';
    //     std::clog << "C := " << (solver.modelValue(C) == l_True) << '\n';
    // } else {
    //     std::clog << "UNSAT\n";
    //     return 1;
    // }
}