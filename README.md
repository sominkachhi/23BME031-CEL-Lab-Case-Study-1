# 23BME031-CEL-Lab-Case-Study-1
➤ Project Overview

This project focuses on determining the market equilibrium price of a commodity by modeling demand and supply curves as nonlinear functions and solving the resulting equation using numerical computation and graphical visualization in MATLAB.

The equilibrium price is the point where:

• The nonlinear demand relation • The nonlinear supply relation

are simultaneously satisfied.

The study demonstrates how computational techniques can be used to analyze and solve nonlinear economic models.

➤ Objective

The primary objectives of this project are:

• To understand the concept of market equilibrium • To model demand and supply as nonlinear functions of price • To formulate the equilibrium condition • To derive the nonlinear price equation • To compute the equilibrium price numerically • To visualize demand and supply curves using MATLAB

➤ Problem Description

A simplified market system is considered where:

• Demand varies nonlinearly with price • Supply varies nonlinearly with price

The goal is to determine the steady-state price at which the quantity demanded equals the quantity supplied.

➤ Mathematical Formulation

Nonlinear Demand Function

D(p) = 100 - 5p - 0.1p^2

Where:

• Constant term → Maximum potential demand • Linear term → Decrease of demand with price • Quadratic term → Nonlinear demand behavior

Nonlinear Supply Function

S(p) = 20 + 2p + 0.1p^2

Where:

• Constant term → Base production level • Linear term → Increase of supply with price • Quadratic term → Increasing marginal cost

➤ Equilibrium Condition

Market equilibrium occurs when:

D(p) = S(p)

Substituting the nonlinear models:

100 - 5p - 0.1p^2 = 20 + 2p + 0.1p^2

Rearranging:

0.2p^2 + 7p - 80 = 0

This nonlinear equation governs the equilibrium price.

➤ Numerical Solution Approach

Since the equilibrium equation is nonlinear, a numerical method is applied.

A price adjustment equation is defined:

\frac{dp}{dt} = -(0.2p^2 + 7p - 80)

Euler’s Method is used for iterative computation:

p_{new} = p - (0.2p^2 + 7p - 80)\Delta t

Iterations continue until convergence is achieved.

➤ Methodology

The equilibrium price is determined using the following computational procedure: 1. Assume an initial price 2. Compute supply–demand imbalance 3. Update price using Euler’s method 4. Repeat iterations until convergence 5. Generate a range of price values 6. Plot nonlinear demand and supply curves 7. Identify equilibrium from curve intersection

➤ MATLAB Implementation

The MATLAB script performs:

• Definition of nonlinear demand and supply models • Numerical iteration using Euler’s method • Convergence detection • Graphical plotting of demand and supply curves • Visualization of equilibrium behavior

➤ Results

The computational analysis yields:

• Equilibrium Price ≈ 9.08 units

This value represents the price at which nonlinear demand equals nonlinear supply.

➤ Graphical Interpretation

• Demand Curve → Downward sloping nonlinear curve • Supply Curve → Upward sloping nonlinear curve • Intersection → Market Equilibrium

➤ Key Concepts Demonstrated

This project illustrates the application of:

• Nonlinear mathematical modeling • Market equilibrium analysis • Numerical methods (Euler method) • MATLAB computational tools • Iterative convergence behavior

➤ Analytical Significance

Market equilibrium determination is important in:

• Economic system analysis • Engineering economics • Resource planning models • Computational modeling of nonlinear systems

This project highlights the effectiveness of numerical methods in solving nonlinear equations.

➤ How to Run the Project 1. Open MATLAB 2. Copy the provided .m script 3. Run the file

Observe:

• Convergence of price • Demand and supply curves • Equilibrium behavior

➤ Author

Somin Kachhi Mechanical Engineering Student Computational Engineering Laboratory Project

➤ Project Summary

This project successfully demonstrates how the equilibrium price of a nonlinear economic system can be determined using numerical computation and MATLAB visualization techniques, reinforcing the role of computational methods in engineering and analytical problem solving.
