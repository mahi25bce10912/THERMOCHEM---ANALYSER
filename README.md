# THERMOCHEM---ANALYSER
Thermochem Analyzer is a scientific instrument used to study the thermal and chemical behavior of materials by measuring heat flow, temperature changes, and reaction properties. It helps in analyzing composition, stability, phase transitions, and energy changes in substances for research and industrial applications.


ThermoChem Analyzer Pro is a **Python-based GUI application** built using **Tkinter** that allows users to explore and calculate important concepts in **Thermodynamics and Chemistry** interactively.

It is designed for students, educators, and anyone interested in visualizing chemical concepts through calculations and graphs.

---

## 🚀 Features

### 🔥 Thermodynamics Modules

#### 1. Calorimetry
- Calculates heat energy using:
  q = mcΔT

- Also computes final temperature

#### 2. Gibbs Free Energy
- Uses formula:

ΔG = ΔH - TΔS

- Determines whether a process is **spontaneous or non-spontaneous**
- Includes **ΔG vs Temperature graph**

#### 3. Enthalpy (Hess's Law)
- Computes enthalpy change:

ΔH = H(products) - H(reactants)

- Calculates total enthalpy based on moles

#### 4. Phase Change Energy
- Calculates energy required during phase transitions:

q = mL


#### 5. Heat Engine Efficiency
- Calculates **Carnot efficiency**:

η = 1 - Tc/Th


---

### 📊 Visualization Features

- 📈 Gibbs Free Energy Graph
- 📉 Entropy Trend Graph (Solid → Liquid → Gas)

---

### 🧬 Chemistry Modules

#### Molecular Shape Predictor
- Predicts geometry based on electron pairs
- Supported shapes:
- Linear
- Trigonal Planar
- Tetrahedral
- Includes **2D structure visualization using Canvas**

#### Bond Polarity Analyzer
- Calculates electronegativity difference
- Classifies bonds as:
- Nonpolar Covalent
- Polar Covalent

---

## 🖥️ User Interface

- Clean and modern GUI
- Dark-themed sidebar navigation
- Clearly labeled input fields
- Real-time result display
- Interactive buttons and graphs

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- NumPy (numerical calculations)
- Matplotlib (graph plotting)

---

## 📦 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/thermochem-analyzer.git
cd thermochem-analyzer
Step 2: Install Dependencies
pip install numpy matplotlib
Step 3: Run the Application
python main.py
