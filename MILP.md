# **MILP for Optimized Field Visits in Preventive Maintenance**

## **Objective Function**
Minimize the total cost of field visits while ensuring high-priority sites are serviced efficiently.

$$
\min \sum_{i \in S} \sum_{j \in T} c_{ij} x_{ij}


Where:
- \( S \) = Set of sites requiring maintenance.
- \( T \) = Set of available technicians.
- \( c_{ij} \) = Cost of assigning technician \( j \) to site \( i \) (including travel and operational costs).
- \( x_{ij} \) = Binary decision variable (1 if technician \( j \) is assigned to site \( i \), 0 otherwise).

---

## **Constraints**

### **1. Each site is visited by exactly one technician**
$$
\sum_{j \in T} x_{ij} = 1, \quad \forall i \in S
$$
Every site must be assigned to a single technician.

---

### **2. Technician workload capacity constraint**
$$
\sum_{i \in S} d_i x_{ij} \leq W_j, \quad \forall j \in T
$$
Where:
- \( d_i \) is the service duration at site \( i \).
- \( W_j \) is the available work hours for technician \( j \).

---

### **3. Travel time constraint**
$$
\sum_{i \in S} \sum_{j \in T} t_{ij} x_{ij} \leq T_j, \quad \forall j \in T
$$
Where:
- \( t_{ij} \) is the travel time from technician \( j \) to site \( i \).
- \( T_j \) is the technician's total available travel time.

---

### **4. Binary Decision Variable Constraint**
$$
x_{ij} \in \{0,1\}, \quad \forall i \in S, j \in T
$$

Where \( x_{ij} = 1 \) if technician \( j \) is assigned to site \( i \), otherwise \( x_{ij} = 0 \).

---

## **Final Formulation**
$$
\min \sum_{i \in S} \sum_{j \in T} c_{ij} x_{ij}
$$
Subject to:
$$
\sum_{j \in T} x_{ij} = 1, \quad \forall i \in S
$$
$$
\sum_{i \in S} d_i x_{ij} \leq W_j, \quad \forall j \in T
$$
$$
\sum_{i \in S} \sum_{j \in T} t_{ij} x_{ij} \leq T_j, \quad \forall j \in T
$$
$$
x_{ij} \in \{0,1\}, \quad \forall i \in S, j \in T
$$
